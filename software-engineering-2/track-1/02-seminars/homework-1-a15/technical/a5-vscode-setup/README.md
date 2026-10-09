<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
## A5: *VSCode* - Setup

[*Visual Studio Code (VSCode)*](https://code.visualstudio.com) by *Microsoft* is a modern,
popular *IDE* (Integrated Development Environment) with:

- Multiple programming languages support (*"polyglot"*).

- A large choice of extensions (e.g. *"Java extension pack"*, *"Code Runner"* extension).

- Ability to develop in remote environments (cloud, containers) over the network.

- Built-in *AI integration* (Microsoft's *Co-Pilot*) or through extensions, e.g. *Claude*
    and others.


For this course, following *VSCode* extensions need to be installed:

- [*Extension Pack for Java*](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack) -- required.

- [*Code Runner*](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) -- recommended.

`->` Make sure you can start *VSCode* from the terminal, e.g. by setting *PATH* in
`.bashrc`.

`->` *VSCode* opens each project separately (not multiple projects or entire
workspaces at once, which is in contrast to older *IDE* such as *eclipse*).

`->` Hence, *VSCode* must be started from within the project directory.

Navigate to the project directory and start *VSCode*:

```sh
cd ~/workspaces/hello-world         # cd to into the project directory

code .                              # start VSCode in this '.' (dot) current directory
```

*VSCode* will open and show project files.

Run the *HelloWorld* Program with:

- the internal *launcher* (see screenshot) or with

- *Code Runner* that is activated by (default): `<Ctrl> + <Alt> + N`

Output of the program should appear in the integrated Terminal panel (launcher) or
in the Output panel (Code Runner).

&nbsp;

<img src="../markup/img/vscode-1.png" width="800"/>


&nbsp;
---
### Validation

In order to collect points, show *VSCode* working on your laptop.

