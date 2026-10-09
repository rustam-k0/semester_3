<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
## A3: *Java* - Setup

*Java* comes in two major varieties:

- *Java JRE* - Java Runtime Environment only includes the 

    - `java` Virtual Machine and libraries needed during runtime to run
        compiled Java programs.

- *Java SDK* - Java Software Development Kit includes the full set of Java tools:

    - `javac` - the Java compiler to compile Java source code in `*.java` files
        to [*Portable Byte Code*](https://en.wikipedia.org/wiki/List_of_JVM_bytecode_instructions)
        in `*.class` files that can be loaded and executed by the JavaVM.

    - `javadoc` - the Java documentation compiler that generates HTML-documentation from
        comments in Java source code.

    - `jar` - the Java archiver that packages `*.class` files into `*.jar` (Java archive)
        files for distribution.

Other varieties include:

- *Java SE* standard edition, which is the free implementation distributed by
    *Oracle* and with *Open-JDK* that only includes the standard Java libraries.

- [*Jakarta EE*](https://en.wikipedia.org/wiki/Jakarta_EE) enterprise edition or
    *Java EE* (former name), which is a large framework for commercial Java
    software development.


Java is an open language specification, which means multiple implementations
exist, most prominently:

- [*Java from Oracle*](https://www.oracle.com/java) -
    [*Oracle*](https://en.wikipedia.org/wiki/Oracle_Corporation) is a dominat
    US data- and database company that aquired Java from *Sun Microsystems*
    in 2010 and owns Java.

- [*Open-JDK*](https://openjdk.org) is an open-source implementation of the
    Java Platform, Standard Edition (Java SE).

The [*Java Version history*](https://en.wikipedia.org/wiki/Java_version_history)
dates back to Jan 23, 1996 with *JDK 1.0*.

- *Java 26 SE* was released on March 17, 2026

- *LTS* (Long-term support) releases are *Java SE 25 (LTS)* and *Java SE 25 (LTS)*.

New *Java* releases often cause problems with existing code and libraries,
see example
[*"Unable to compile using java 25 \#3949"*](https://github.com/projectlombok/lombok/issues/3949)
for problems of *Java 25* with the [*lombok*](https://projectlombok.org/) library.

It is *adviced* to use the stable *Java 25* for the course. The more adventurous can
try the latest *Java*.


&nbsp;
---
### Install *Java* or use a *Dev-Container*

If you have no *Java* (25 LTS) installed, install or create a *Dev-Container*.

Installation:

**`->` Mac:** - follow steps in article
    [*"Install Java on macOS"*](https://www.baeldung.com/java-macos-installation#using-homebrew-package-manager)
    using *brew* (mind to choose Java not older than *Java 25*, which is preferred).

**`->` Windows:** - download
    [*x64 installer*](https://www.oracle.com/de/java/technologies/downloads/#jdk25-windows)
    and install *Java*.

**`->` Linux:** - follow steps in article
    [*"Java auf Linux installieren"*](https://docs.fabricmc.net/de_de/players/installing-java/linux)
    depending on your *Linux* distribution.


The optional container examples are available in the original repository linked in `../source-notes.md`. This laptop uses a native JDK.

### Test your Configuration


&nbsp;

Test: open a terminal and show that tools are installed with proper (same) versions:

```sh
java --version          --> java 25.0.2 2026-01-20 LTS

javac --version         --> javac 25

javadoc --version       --> javadoc 25

jar --version           --> jar 25
```

Verify the Java - installation path is set to the *JAVA_HOME* environment variable:

```sh
echo $JAVA_HOME         --> /c/Program Files/Java/jdk-25
```

Create file `HelloWorld.java` in a directory: `~/workspaces/hello-world`
(`~` refers to the *HOME*-directory):

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Compile and execute:

```sh
cd                                  # change to your HOME directory

mkdir -p ~/workspaces/hello-world   # make (mk) directories

cd workspaces/hello-world           # change into the 'hello-world' directory

# print the working directory
pwd                         --> /c/Sven1/svgr2/workspaces/hello-world

# create file '' in the directory - use an editor or IDE
...

cat HelloWorld.java         --> output the file content

# compile file 'HelloWorld.java'
javac HelloWorld.java       --> Java compiler creates file 'HelloWorld.class'

# run 'HelloWorld.class'
java HelloWorld             --> 'Hello, World!'
```


&nbsp;
---
### Validation

In order to collect points, show a terminal on your laptop with commands:

```sh
java --version          --> java 25.0.2 2026-01-20 LTS -- or similar

javac --version         --> javac 25

javadoc --version       --> javadoc 25

jar --version           --> jar 25

# compile and run the 'HelloWorld'-program
cat HelloWorld.java

javac HelloWorld.java

java HelloWorld
```

Output:

```
java 25.0.2 2026-01-20 LTS
javac 25.0.2
javadoc 25.0.2
jar 25.0.2

Hello, World!
```
