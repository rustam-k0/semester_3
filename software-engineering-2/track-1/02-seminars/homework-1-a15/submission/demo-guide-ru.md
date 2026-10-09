# A1–A5 — Шпаргалка для показа

SWE II · Zug 1 · WiSe 2026/27

## Где показывать окна, а где ответы

На занятии по упражнениям показываешь преподавателю экран своего ноутбука. Окна программ и результаты команд показываются живьём. Ответы открывай в соседней вкладке VS Code: [validation-answers-en.md](validation-answers-en.md), либо распечатай. Отдельный PDF и скриншоты для загрузки не требуются. По сохранённым условиям Moodle сдача через Moodle/email не принимается; после показа нужно отметить принятие в списке. Дедлайн: 23 октября 2026, 23:59, Europe/Berlin; сам зачёт возможен только на занятии.

Здесь порядок показа рекомендован для удобства. Обязательные пункты взяты из Validation A1–A5; дополнительные демонстрации отдельно помечены.

## Подготовь окна

1. **Terminal.app** — для A1, A3, A4 и примеров A2. Открыть через Spotlight: Cmd+Space → Terminal. Запусти `/opt/homebrew/bin/bash -l`, затем `echo "$BASH_VERSION"`: должна появиться версия Bash.
2. **VS Code** — для A5 и файла английских ответов. Учебный проект: `/Users/damirahavaashova/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world`.
3. **Finder и браузер** — дополнительные примеры HOME и Javadoc, если преподаватель попросит.

Один раз выполни подготовку ниже. Первой строкой запускается Bash; следующие строки вводи уже внутри него. Это подключает Java 25, GNU sed и команду именно Microsoft VS Code. Все дальнейшие блоки выполняй в этой shell.

```bash
/opt/homebrew/bin/bash -l
source "$HOME/.config/a15/env.sh"
echo "$BASH_VERSION"
```

Команды и файлы перепроверены 9 октября 2026. Это подготовка к зачёту, а не подтверждение полученных баллов.

## A1 — Terminal: показать команды и понимать вывод

Вводи по очереди, чтобы успевать объяснять:

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

Скобки запускают последнюю часть в отдельной shell, поэтому текущая папка основного терминала не меняется. Последний блок использует учебный `hello.txt` в подготовленной папке `.config/a15`. `>` записывает файл заново. Для варианта `sed` из задания нужен настроенный GNU sed; стандартный macOS sed может иначе обработать `\n`.

| Команда / термин | Что объяснить |
| --- | --- |
| `uname -a`, `whoami` | Сведения о системе; имя пользователя |
| `HOME`, `cd`, `pwd` | Домашняя папка; переход; текущая папка |
| `ls -l`, `ls -la` | Подробный список; также скрытые записи |
| `realpath .` | Полный путь с разрешением символических ссылок; `.` — текущая папка |
| `PATH`, `tr` | Где искать программы; замена двоеточий переносами строк |
| `echo`, `>`, `cat` | Вывести текст; записать его в файл; прочитать файл |
| `pipe` / `\|` | Передать stdout одной команды в stdin следующей |
| `sed`, `wc` | Преобразовать текст; посчитать строки, слова и байты |

## A2 — ответы: открыть английский файл

Покажи раздел **A2**, 15 вопросов. Умей объяснить ответы своими словами; для личных вопросов покажи свой HOME и его содержимое.

Ключевые понятия: **terminal** — окно ввода/вывода; **shell** — интерпретатор внутри него; **process/PID** — запущенная программа/её номер; **stdin/stdout/stderr** — ввод/обычный вывод/ошибки; **environment variable** — переменная окружения; **dotfile** — скрытое имя с точкой; **UTF-8** — кодировка Unicode; **ANSI** — управление отображением; **PS1** — приглашение Bash.

Короткие дополнительные примеры, если попросят:

```bash
ps -p $$ -o comm=
echo "$HOME"
ls -la "$HOME"
command -v java
printf 'one\ntwo\n' | wc -l
printf 'Привет, €\n'
printf 'Hello \033[31;1mWorld\033[0m\n'
PS1='\u@\h \w \$ '
```

`$$` — PID текущей shell; `$SHELL` может показывать login shell, а не текущую. Pipe даст `2`; ANSI-пример должен окрасить World. PS1 в этом примере меняет приглашение только текущей shell.

Для цветного prompt в Bash:

```bash
PS1='\[\e[32m\]\u@\h \w\[\e[0m\] \$ '
```

В Finder: **Go → Home**, затем **Cmd+Shift+.** для скрытых файлов. Если спросят про startup files: `.bash_profile` — login Bash; `.bashrc` — interactive Bash; `.zprofile` и `.zshrc` — аналогичные роли в zsh. **Alias** — сокращение команды; **function** — именованный блок команд; `export` передаёт переменную дочерним процессам.

## A3 — Terminal: Java и работающая программа

```bash
cd "$HOME/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world" || exit
java --version
javac --version
javadoc --version
jar --version
cat HelloWorld.java
javac HelloWorld.java && java -cp . HelloWorld
```

Покажи версии инструментов JDK 25, исходный код и успешный вывод. В текущей версии проекта ожидается `Hello, World (with Javadoc)!`; первоначальная версия задания выводит `Hello, World!`.

Понимать: **JDK** — комплект инструментов Java; **javac** компилирует `.java` в `.class`; **java/JVM** выполняет bytecode; **javadoc** создаёт HTML-документацию; **jar** упаковывает Java-архивы. `java -cp . HelloWorld` запускается без расширения `.class`; `-cp .` явно указывает искать класс в текущей папке. `&&` запускает программу только после успешной компиляции. Дополнительно: `echo "$JAVA_HOME"` показывает JDK, `command -v java javac javadoc jar` — выбранные программы.

## A4 — Terminal + английские ответы: Git

Все команды Git выполняй в учебном проекте:

```bash
cd "$HOME/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world" || exit
cat ~/.gitconfig
git status
git log --oneline --decorate
```

Покажи конфигурацию, `working tree clean` и историю выполненных шагов. В исходнике опечатка `--one-line`; правильно `--oneline`. Затем открой раздел **A4** английского файла — 10 вопросов.

Дополнительно можно показать:

```bash
cd "$HOME/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world" || exit
ls -ld .git
cat .gitignore
git check-ignore HelloWorld.class doc/index.html
open doc/index.html
```

Последняя команда открывает Javadoc в браузере. `.git` — локальная история; `.gitignore` — правила исключения; **working tree** — рабочие файлы; **staging area/index** — подготовленные изменения; **commit** — записанный снимок; **branch** — ссылка на коммит; **clean/dirty** — отсутствие/наличие незаписанных изменений.

Команды понимать, но для показа чистого проекта выполнять их не нужно: `git add` подготавливает изменения; `git commit` сохраняет снимок; `git diff` показывает различия; `git stash` откладывает работу; `git revert` добавляет отменяющий коммит; `git commit --amend` создаёт замену последнего коммита. Commit неизменяем: amend/rebase создают новые хеши. Учебный локальный проект не требует push.

## A5 — окно VS Code: запустить Java

В Terminal:

```bash
cd "$HOME/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world" || exit
code .
code ../submission/validation-answers-en.md
```

Вторая команда открывает ответы; учебный проект остаётся открытым в VS Code. Для русского файла можно также выполнить `code ../submission/demo-guide-ru.md` из папки проекта.

В VS Code:

1. В Explorer слева открой **HelloWorld.java**.
2. Нажми **Run** над методом `main` и покажи вывод в нижней панели **Terminal**. Если она скрыта: **View → Terminal**.
3. Открой **Extensions** (Cmd+Shift+X), покажи установленный **Extension Pack for Java**. **Code Runner** рекомендован; можно показать **Run Code**, в этой конфигурации вывод тоже идёт в Terminal.
4. В **Settings** (Cmd+,) найди `Files: Auto Save` → `afterDelay`; для `Files: Eol` должно быть `\n` (LF). Это настройки из Moodle.
5. Если спросят про JDK: Cmd+Shift+P → **Java: Configure Java Runtime**, покажи Java 25.

Понимать: **IDE** — среда разработки; **extension** — дополнение; **integrated terminal** — терминал внутри редактора; **UTF-8** — кодировка файла; **LF** — перевод строки; **auto save** — автоматическое сохранение. `code .` открывает текущую папку как проект.

## Перед уходом

Уточни, что приняты все пять частей A1–A5 (по 3 балла), и оформлено подтверждение в списке. Файл с ответами сам по себе не заменяет показ работающего окружения.

Источники: [основные инструкции](../technical/README.md), Validation в README A1–A5, [условия Moodle](../technical/source-notes.md), [проверка настройки 7 октября](../technical/validation-checklist.md). Команды перепроверены 9 октября 2026: Java 25, компиляция/запуск, Git, GNU sed, VS Code CLI и расширения. Кнопки Run и отображение цвета в окнах этой проверкой не подтверждались; проверь их лично до занятия. Настройки программ не менялись.
