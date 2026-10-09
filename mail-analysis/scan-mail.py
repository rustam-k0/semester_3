#!/usr/bin/env python3
"""Read BHT mail using a credential stored in the macOS login Keychain."""

import argparse
import ctypes
import email
import getpass
import imaplib
import json
import ssl
from email import policy
from html.parser import HTMLParser

SERVICE = b"bht-mail-analysis"
ACCOUNT = b"bjxj1484"


def keychain(password=None):
    security = ctypes.CDLL("/System/Library/Frameworks/Security.framework/Security")
    pointer = ctypes.c_void_p
    integer = ctypes.c_uint32
    find = security.SecKeychainFindGenericPassword
    find.argtypes = [pointer, integer, ctypes.c_char_p, integer,
                     ctypes.c_char_p, ctypes.POINTER(integer),
                     ctypes.POINTER(pointer), ctypes.POINTER(pointer)]
    find.restype = ctypes.c_int32
    free = security.SecKeychainItemFreeContent
    free.argtypes = [pointer, pointer]
    free.restype = ctypes.c_int32
    release = ctypes.CDLL(
        "/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation"
    ).CFRelease
    release.argtypes = [pointer]
    release.restype = None
    length, data, item = integer(), pointer(), pointer()
    status = find(None, len(SERVICE), SERVICE, len(ACCOUNT), ACCOUNT,
                  ctypes.byref(length), ctypes.byref(data), ctypes.byref(item))
    try:
        if password is None:
            if status != 0:
                raise RuntimeError("Keychain credential unavailable (code "
                                   + str(status) + "). Run with --setup first.")
            return ctypes.string_at(data, length.value).decode("utf-8")
        raw = password.encode("utf-8")
        if status == 0:
            modify = security.SecKeychainItemModifyAttributesAndData
            modify.argtypes = [pointer, pointer, integer, ctypes.c_char_p]
            modify.restype = ctypes.c_int32
            result = modify(item, None, len(raw), raw)
        elif status == -25300:
            add = security.SecKeychainAddGenericPassword
            add.argtypes = [pointer, integer, ctypes.c_char_p, integer,
                            ctypes.c_char_p, integer, ctypes.c_char_p, pointer]
            add.restype = ctypes.c_int32
            result = add(None, len(SERVICE), SERVICE, len(ACCOUNT), ACCOUNT,
                         len(raw), raw, None)
        else:
            raise RuntimeError("Keychain access failed (code " + str(status) + ")")
        if result != 0:
            raise RuntimeError("Could not save credential (code " + str(result) + ")")
    finally:
        if data:
            free(None, data)
        if item:
            release(item)


class HTMLText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1
        if tag in ("br", "p", "div", "li", "tr"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, value):
        if not self.hidden:
            self.parts.append(value)


def record(uid, message):
    body = message.get_body(preferencelist=("plain", "html"))
    text = ""
    if body is not None:
        text = body.get_content()
        if body.get_content_type() == "text/html":
            parser = HTMLText()
            parser.feed(text)
            text = "".join(parser.parts)
    return {
        "uid": int(uid), "date": str(message.get("Date", "")),
        "from": str(message.get("From", "")),
        "subject": str(message.get("Subject", "")),
        "text": text[:20000], "text_truncated": len(text) > 20000,
        "attachments": [part.get_filename() for part in message.iter_attachments()
                        if part.get_filename()],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--setup", action="store_true",
                        help="Verify and save a password entered locally")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--after-uid", type=int, default=0)
    args = parser.parse_args()
    if args.limit < 1 or args.after_uid < 0:
        parser.error("limit must be positive and after-uid nonnegative")
    password = (getpass.getpass("BHT password (hidden): ")
                if args.setup else keychain())
    connection = imaplib.IMAP4("imap.bht-berlin.de", 143, timeout=30)
    try:
        connection.starttls(ssl_context=ssl.create_default_context())
        connection.login(ACCOUNT.decode(), password)
        if args.setup:
            keychain(password)
            print("Connection verified. Password saved to macOS Keychain.")
            return
        password = None
        status, _ = connection.select("INBOX", readonly=True)
        if status != "OK":
            raise RuntimeError("Could not open INBOX read-only")
        status, data = connection.uid("search", None, "ALL")
        if status != "OK":
            raise RuntimeError("Could not list messages")
        pending = [uid for uid in data[0].split() if int(uid) > args.after_uid]
        # On incremental scans, process oldest pending UIDs first to avoid skips.
        selected = pending[:args.limit] if args.after_uid else pending[-args.limit:]
        messages = []
        for uid in selected:
            status, parts = connection.uid("fetch", uid, "(BODY.PEEK[])")
            if status != "OK":
                raise RuntimeError("Could not fetch UID " + uid.decode())
            raw = next((part[1] for part in parts if isinstance(part, tuple)), None)
            if raw is None:
                raise RuntimeError("Missing message content for UID " + uid.decode())
            messages.append(record(uid, email.message_from_bytes(raw, policy=policy.default)))
        print(json.dumps({
            "folder": "INBOX", "uid_validity": connection.response("UIDVALIDITY")[1],
            "pending_count": len(pending), "returned_count": len(messages),
            "messages": messages,
        }, ensure_ascii=False, indent=2, default=lambda value: value.decode("ascii")))
    finally:
        password = None
        try:
            connection.logout()
        except (OSError, imaplib.IMAP4.error):
            pass


if __name__ == "__main__":
    try:
        main()
    except (OSError, imaplib.IMAP4.error, RuntimeError) as error:
        raise SystemExit("Mail scan failed: " + str(error))
