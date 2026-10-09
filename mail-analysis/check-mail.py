#!/usr/bin/env python3
"""Check BHT IMAP access without modifying messages or saving credentials."""

import email
import getpass
import imaplib
import ssl
from email.header import decode_header, make_header


def header(message, name):
    return str(make_header(decode_header(message.get(name, ""))))


def main():
    username = input("BHT login [bjxj1484]: ").strip() or "bjxj1484"
    password = getpass.getpass("BHT password (hidden, not saved): ")
    connection = imaplib.IMAP4("imap.bht-berlin.de", 143, timeout=30)
    try:
        connection.starttls(ssl_context=ssl.create_default_context())
        connection.login(username, password)
        password = None
        status, count = connection.select("INBOX", readonly=True)
        if status != "OK":
            raise RuntimeError("Could not open INBOX read-only")
        print("Connected with STARTTLS. INBOX opened read-only.")
        print("Messages:", count[0].decode())
        status, result = connection.uid("search", None, "ALL")
        if status != "OK":
            raise RuntimeError("Could not list messages")
        for uid in result[0].split()[-10:]:
            status, parts = connection.uid(
                "fetch", uid,
                "(BODY.PEEK[HEADER.FIELDS (DATE FROM SUBJECT)])",
            )
            if status != "OK":
                raise RuntimeError("Could not read message headers")
            for part in parts:
                if isinstance(part, tuple):
                    message = email.message_from_bytes(part[1])
                    print("\nDate:", header(message, "Date"))
                    print("From:", header(message, "From"))
                    print("Subject:", header(message, "Subject"))
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
        raise SystemExit("Connection failed: " + str(error))
