# A1–A5 — Short validation answers

Software Engineering II · Zug 1 · WiSe 2026/27

Show these notes and the working setup on your laptop during the exercise class. A2 and A4 contain the written validation questions; A1, A3 and A5 require practical demonstrations. Paper or a text file is allowed. Acceptance must be recorded in the completion list; Moodle/email submission is not accepted.

## Before running commands

Open Terminal and run these lines once. The first line starts the course Bash; enter the remaining lines in that new shell. Run each demonstration block separately.

```bash
/opt/homebrew/bin/bash -l
source "$HOME/.config/a15/env.sh"
echo "$BASH_VERSION"
```

## A1 — Laptop setup

Demonstration: open Terminal and show the configuration-test commands from [A1](../technical/a1-laptop-setup/README.md). Explain the system, user, HOME, PATH, directory listings, output redirection and pipes.

```bash
uname -a
whoami
echo "$HOME"
cd
ls -l
ls -la
realpath .
echo "$PATH"
echo "$PATH" | tr ':' '\n'
echo 'Hello World'
(
  cd "$HOME/.config/a15" || exit
  echo 'Hello World' > hello.txt
  cat hello.txt
  cat hello.txt | sed 's/./&\n/g'
  cat hello.txt | sed 's/./&\n/g' | wc
)
```

The last command prints counts for lines, words and bytes (`12 10 23` with the configured GNU sed). The subshell keeps the file demonstration in the existing course scratch folder.

## A2 — Understanding the terminal: all 15 validation questions

1. **What is a terminal?** A program that provides text input and output, usually running a shell inside it.
2. **What is a shell?** A command interpreter that runs commands and programs. I use Bash for the course; macOS also has zsh.
3. **What is a Unix process?** A running instance of a program with a process ID (PID), memory and an environment.
4. **How does `|` work?** It sends the standard output of one command to the standard input of the next.
5. **What is the HOME directory?** The user's personal directory for files and configuration.
6. **What is the path to your HOME directory?** `/Users/damirahavaashova`; check with `echo "$HOME"`.
7. **What is in your HOME directory (five entries)?** `Desktop`, `Documents`, `Downloads`, `Library`, `Pictures`. Check with `ls "$HOME"`.
8. **What is PATH? What does it do?** An environment variable containing directories searched, in order, for executable commands.
9. **Where is PATH defined? How can it be changed?** It is inherited from the parent process and can be set in shell startup files such as `.bash_profile` or `.bashrc`. `export PATH="$JAVA_HOME/bin:$PATH"` changes it for the current shell and its children; edit a startup file for future sessions.
10. **What are dotfiles?** Files or directories whose names start with a dot; normally hidden in directory listings. Many store configuration.
11. **Name five dotfiles and briefly explain their purpose.** `.bash_profile`: login Bash setup; `.bashrc`: interactive Bash setup; `.zprofile`: login zsh setup; `.zshrc`: interactive zsh setup; `.gitconfig`: user Git configuration.
12. **What is UTF-8 and why is it not ASCII?** UTF-8 encodes Unicode characters using 1–4 bytes. ASCII represents 128 characters; UTF-8 also supports characters such as `€` and Cyrillic, while preserving ASCII byte values.
13. **What is an ANSI escape sequence and what is it used for?** A control sequence starting with ESC, used for terminal colours, cursor movement and other display controls.
14. **How can a pretty prompt be created?** In Bash, set `PS1` with username, directory and optional ANSI colours, usually in `.bashrc`. Example: `PS1='\u@\h \w \$ '`.
15. **Who is Ken Thompson?** A co-creator of Unix, creator of the B language and co-designer of UTF-8 with Rob Pike.

## A3 — Java setup

Demonstration: show `java --version`, `javac --version`, `javadoc --version` and `jar --version`. Show `HelloWorld.java`, compile it with `javac HelloWorld.java`, then run `java HelloWorld`. The course setup uses JDK 25.

```bash
cd "$HOME/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world" || exit
java --version
javac --version
javadoc --version
jar --version
cat HelloWorld.java
javac HelloWorld.java && java -cp . HelloWorld
```

Expected program output: `Hello, World (with Javadoc)!`. The earlier A3 example prints `Hello, World!`; this project includes the A4 Javadoc changes.

## A4 — Git setup: all 10 validation questions

Run inside the exercise project (not the semester workspace repository):

```bash
cd "$HOME/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world" || exit
cat ~/.gitconfig
git status
git log --oneline --decorate
```


1. **Where is a local Git repository stored?** In the hidden `.git` directory inside this project; it stores history and repository metadata.
2. **What is a commit?** A recorded project snapshot, with metadata, parent references and a unique hash.
3. **What is a branch?** A named reference to a commit that moves forward when new commits are made on that branch.
4. **Why was `HelloWorld.java` committed, but `HelloWorld.class` and `doc` were not?** The Java source is needed to reproduce the program. The class file and documentation are generated and excluded through `.gitignore`.
5. **What does a clean project state mean?** There are no pending changes or untracked, non-ignored files reported by `git status`.
6. **When is a project state dirty?** When it has uncommitted changes or untracked, non-ignored files.
7. **How can a dirty state be cleaned up?** Commit intended changes, stash unfinished work, or discard unwanted changes. Ignore generated files appropriately.
8. **Can commits be altered after being committed?** An existing commit object is immutable. Amending a commit or rebasing changed history creates replacement commits with new hashes.
9. **Can commits be altered after being pushed?** Replacement commits can be created locally, but replacing remote history requires a force push and coordination with collaborators.
10. **How can mistakenly pushed commits be corrected?** Usually create a correcting commit or use `git revert <commit>` to record an undo without rewriting shared history.

## A5 — VS Code setup

Open the exercise project and these answers:

```bash
cd "$HOME/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world" || exit
code .
code ../submission/validation-answers-en.md
```

In VS Code, open `HelloWorld.java`, click **Run** above `main`, and show the output in the integrated terminal. Show the installed **Extension Pack for Java**; **Code Runner** is recommended. Moodle settings: Auto Save `afterDelay`, line endings `LF`.

## Sources and scope

Questions: [A2 Validation](../technical/a2-understanding-the-terminal/README.md) and [A4 Validation](../technical/a4-git-setup/README.md). Practical requirements: A1, A3 and A5 README files. Acceptance rules: [source notes](../technical/source-notes.md). Commands, JDK 25, project output, clean Git state and installed VS Code extensions rechecked on 2026-10-09. The local [earlier checklist](../technical/validation-checklist.md) records setup history. GUI Run buttons and visual colour rendering were not rechecked in this revision. This document does not certify acceptance.
