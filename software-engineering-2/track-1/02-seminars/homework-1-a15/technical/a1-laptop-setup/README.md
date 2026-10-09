<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
## A1: *Laptop* - Setup

The terminal is remains a primary tool to interact with computers also in
modern software development.

- *Mac* or *Linux* laptops have proper terminal software pre-installed.

- *Windows* laptops require the separate setup of *Unix*-compatible terminal
    software. Several choices exist:

  - a light-weight *Unix*-Emulator such as
    [*cygwin*](https://www.cygwin.com) --
    (*GitBash* is not a complete equivalent [1], it only works for *git*).

  - a virtual machine running *Linux* using the
    [*Windows Subsystem for Linux (WSL)*](https://learn.microsoft.com/en-us/windows/wsl/install)
    or laternative virtual machine software such as *VirtualBox* or *VMWare*.

  - a *Docker Container*, see
    [*Install Docker Desktop on Windows*](https://docs.docker.com/desktop/setup/install/windows-install/),
    which installs and uses *WSL* on *Windows*.

  - a [*VSCode Dev-Container*](https://learn.microsoft.com/en-us/windows/dev-environment/docker/dev-containers)
    -- that opens a *Linux*-Terminal in *VSCode* and is also running on *WSL*.

Depending on your system, verify you have the software installed described in the
following section, install if necessary.


&nbsp;

### For *Mac*

Read article by *Thomas Auinger:*
    [*"Setting up my new MacBook Air M3 for Java Development"*](https://medium.com/@thomas.auinger/setting-up-my-new-macbook-air-m3-for-java-development-fc609af738cb).

- Install the [*brew*](https://brew.sh/) package manager, if not already installed:

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

- Give user sudo-permissions (in order to install software from the terminal):

    ```
    sudo visudo
    ```

    Make sure the `%admin` entry appears as shown and add, if not:

    ```
    # User privilege specification
    root    ALL=(ALL) ALL
    %admin  ALL=(ALL) ALL
    ```

- Follow steps, installing *git*, *sublime*, *VSC* and *Docker*. Install *Java*,
    depending on course.

- Install package [*coreutils*](https://formulae.brew.sh/formula/coreutils), which
    installs some needed *Unix* tools such as *realpath*.

- Switch to *bash*, see article
    [*How To Change Your Default Shell From Zsh To Bash on Mac*](https://medium.com/@alvyynm/how-to-change-your-default-shell-from-zsh-to-bash-on-mac-0bbd481b4a8d).

- Feel free to install other packages such as *"Tabby"* and *"Oh My Zsh"* for
    pretty prompts (not required).

- Depending on course, read article
    [*Setting up your Apple Silicon Mac for Python development with Visual Studio Code*](https://medium.com/@sorenlind/setting-up-your-apple-silicon-mac-for-python-development-with-visual-studio-code-2c6344a6e5b4)
    for additional information for *Python* development on a *Mac*.


&nbsp;

### For *Windows*

If you are not familiar with *WSL* or *Dev-Container*,
    [*Install Cygwin*](https://www.cygwin.com/install.html) using
    [*setup-x86_64.exe*](https://www.cygwin.com/setup-x86_64.exe).

Launch the *cygwin*-installer *setup-x86_64.exe* and, during installation, select
packages (you may later add/change packages by re-running the installer):
- *vim* - visual editor,
- *wget* - web downloader,
- *curl* - web downloader.


&nbsp;

After installation, open a *cygwin*-terminal and configure:

1. Switch from path prefix `/cygdrive/c` to `/c` and use Unix `rwx` file access
    over Windows ACL:

    - navigate to the *cygwin* installation directory under `C:\cygwin64` (default).

    - inside, edit file `/etc/fstab` (e.g. open with a text editor such as
        [*vim*](https://www.vim.org) (already installed with cygwin),
        [*nano*](https://www.nano-editor.org) or
        [*sublime*](https://www.sublimetext.com)) and replace line:
        ```
        none /cygdrive cygdrive binary,posix=0,user 0 0
            ^^^^^^^^^

        with:
        none / cygdrive binary,posix=0,user,noacl 0 0
            ^
        ```

1. Change the *cygwin* *HOME*-directory from the installation path
    `C:\cygwin64\home\<user-name>` to a path you prefer on your laptop [2]
    (optional).
    Otherwise, your *cygwin* *HOME*-directory will remain under that path, which
    is different from your *Windows* *HOME*-directory `C:\Users\<user-name>`.

    - Change the *cygwin* *HOME*-directory path, edit file `/etc/nsswitch.conf`
        and enter the `<path>` in line `db_home`:
        ```sh
        db_home: <path>     # e.g. db_home: /c/users/svgr
        ```
        Example:
        ```sh
        db_home: /c/home/svgr
        ```

References

  - [1] [*Differences between Cygwin and MinGW*](https://stackoverflow.com/questions/771756/what-is-the-difference-between-cygwin-and-mingw).

  - [2] [*Change Cygwin HOME directory after installation*](https://stackoverflow.com/questions/1494658/how-can-i-change-my-cygwin-home-folder-after-installation).


&nbsp;
---
### Test your Configuration

Applies to all laptops: *Mac*, *Windows* and *Linux*.

Open a new terminal, type and understand the following commands:

```sh
# show the system running for this terminal
uname -a

# show my user-id
whoami 

# show path of the 'HOME' directory on your laptop
echo $HOME      --> e.g. /c/Sven1/svgr2
                --> path on Windows start with the drive letter '/c'

# change to the 'HOME' directory
cd

# show content of the 'HOME' directory ('-l' long version)('-a' all file/directories)
ls -l

# show content of the 'HOME' directory ('-a' show all file/directories, also dotfiles)
ls -la

# show the actual path to the current ('.') directory resolving symbolic links
realpath .

# show content of the 'PATH' variable
echo $PATH

# pretty print 'PATH' using the character translation command 'tr'
echo ${PATH} | tr ':' '\n'

# output text 'Hello World'
echo "Hello World"

# redirect output to a new file 'hello.txt'
echo "Hello World" > hello.txt

# show content of the file 'hello.txt'
cat hello.txt

# split into lines for each character using the stream editor 'sed'
cat hello.txt | sed 's/./&\n/g'

# count lines using the word/line count command 'wc'
cat hello.txt | sed 's/./&\n/g' | wc

```


&nbsp;
---
### Validation

In order to collect points, show the terminal on your laptop with
the commands above.

