# A15 — Validation checklist

Дата проверки: 2026-10-07 (Europe/Berlin). Software Engineering II, WiSe 2026/27, track 1. Прочитаны основной README, source-notes, A1–A5 (Java) и все пять дополнительных разделов A2; учтён соседний Moodle screenshot. Python пропущен. Оригинальные материалы не редактировались.

## A1 — компьютер и терминал

- [x] macOS 26.5.2 (25F84), Darwin, arm64 / Apple Silicon. HOME `/Users/damirahavaashova`.
- [x] Homebrew 6.0.2, Git 2.51.1, Homebrew Bash 5.3.9 уже имелись.
- [x] Установлены GNU coreutils 9.12, GNU sed 4.10 и Sublime Text build 4215. `subl --version` проходит.
- [x] Docker уже установлен: CLI и engine 29.4.0; `docker info` отвечает. Контейнеры не создавались и не перестраивались.
- [x] Для Terminal.app задан `/opt/homebrew/bin/bash`; для integrated terminal VS Code — профиль A15 Bash с `-l`. Login shell учётной записи пока `/bin/zsh`; Bash работает без изменения прав или `/etc/shells`.
- [x] Новый Bash login session читает JAVA_HOME и PATH. Команды Test your Configuration выполнены; фактический вывод — проверка от 2026-10-07 (временный журнал удалён).
- [x] `uname -a`, `whoami`, HOME, `cd`, `ls -l`, `ls -la`, `realpath .`, PATH, `tr`, `echo`, redirect, `cat`, `sed`, `wc` проверены. `hello.txt` создан в отдельном `~/.config/a15`, чтобы не перезаписывать личные файлы HOME. GNU sed даёт 12 строк, 10 слов, 23 байта.
- [ ] Самостоятельно открыть новое окно Terminal.app и подтвердить `echo "$BASH_VERSION"` → 5.3.9. Конфигурация проверена через defaults и отдельный Bash, запуск нового окна Terminal.app визуально не проверялся.

Показ преподавателю:

```bash
/opt/homebrew/bin/bash -l
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
cd "$HOME/.config/a15"
echo 'Hello World' > hello.txt
cat hello.txt
cat hello.txt | sed 's/./&\n/g'
cat hello.txt | sed 's/./&\n/g' | wc
```

Применимые требования Mac выполнены в пользовательском окружении. Администраторские права и sudoers не изменялись: `sudo visudo` из исходника не требуется для уже работающего Homebrew. Если преподаватель требует именно смену login shell учётной записи, лично выполнить `chsh -s /bin/bash` и ввести пароль только в Terminal; системный Bash уже в `/etc/shells`. Современный Homebrew Bash доступен как настроенная shell Terminal/VS Code. Для login shell именно `/opt/homebrew/bin/bash` может понадобиться администраторское добавление в `/etc/shells`; это отдельно не выполнялось. Tabby, Oh My Zsh, Jenv, дополнительные IDE, косметические настройки необязательны.

Прочитана [статья A1 о Mac Java development](https://medium.com/@thomas.auinger/setting-up-my-new-macbook-air-m3-for-java-development-fc609af738cb); использованы только относящиеся к заданию инструменты. Нативный JDK достаточен; Dev-Container не нужен.

## A2 — понимание терминала

- [x] `exam-questions.md`: все 15 вопросов Validation, фактические HOME/shell/пять записей HOME, demo commands, объяснения процессов, filesystem, dotfiles, startup, aliases/functions.
- [x] UTF-8 € → `e2 82 ac`; inheritance без export → пусто, после export → `local`; pipe и dotfile listing проверены.
- [ ] Лично объяснить ответы преподавателю, показать Unicode/ANSI цвет, alias/function и Finder HOME (Cmd+Shift+. для dotfiles). Цвет и Finder визуально не проверялись.

## A3 — Java

- [x] Использован имеющийся native arm64 OpenJDK 25; другой JDK 11 сохранён. Новая Java не устанавливалась.
- [x] JAVA_HOME `/opt/homebrew/Cellar/openjdk/25/libexec/openjdk.jdk/Contents/Home`, bin первым в PATH. Все четыре executable из одного JDK.
- [x] Новый Bash session: `java --version`, `javac --version`, `javadoc --version`, `jar --version` → 25; `os.arch = aarch64`.
- [x] Начальный HelloWorld compiled/run → `Hello, World!`; версия A4 → `Hello, World (with Javadoc)!`. Журналы: проверка от 2026-10-07 (временный журнал удалён), проверка от 2026-10-07 (временный журнал удалён).

```bash
cd "/Users/damirahavaashova/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world"
echo "$JAVA_HOME"
command -v java javac javadoc jar
java --version
javac --version
javadoc --version
jar --version
cat HelloWorld.java
javac HelloWorld.java
java HelloWorld
```

Установлен базовый build 25, соответствующий требованию major version 25; обновление до более нового patch release не выполнялось. Путь намеренно закреплён на имеющуюся версию, чтобы последующий upgrade формулы `openjdk` на новый major не изменил курс автоматически.

## A4 — Git

- [x] Существующие identity и `core.excludesfile` сохранены. Добавлены ровно настройки A4: ignorecase=true, autocrlf=false, filemode=false, eol=lf, defaultBranch=main.
- [x] Создан отдельный repository `/Users/damirahavaashova/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world`; существующие repositories не редактировались.
- [x] Empty root commit + tag `root`, отдельные commits `.gitignore`, Java source, Javadoc, VS Code configuration. Выполнены staging, status, diff и проверки истории; журнал — проверка от 2026-10-07 (временный журнал удалён).
- [x] Javadoc `doc/index.html` создан; `.class`, `doc/`, `bin/` игнорируются. Generated files не committed.
- [x] Финальный `git status`: `nothing to commit, working tree clean`. Remote не настроен, push не выполнялся.
- [x] `exam-questions.md`: все 10 вопросов Validation и команды показа.

```bash
cd "/Users/damirahavaashova/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world"
cat ~/.gitconfig
git status
git log --oneline --decorate
cat .gitignore
git check-ignore HelloWorld.class doc/index.html
git show --stat 9942da7
git diff 9942da7~1..9942da7 --name-status
open doc/index.html
```

- [ ] Лично открыть HTML Javadoc в браузере: существование/генерация проверены, отображение в браузере не проверялось.

## A5 — VS Code

- [x] Уже установлен Visual Studio Code 1.133.0 arm64. Попытка cask-install остановлена Homebrew из-за существующей app; app сохранена, переустановка не требовалась.
- [x] `code` в новых Bash/zsh sessions теперь выбирает VS Code через PATH; старая `/usr/local/bin/code` ссылка на Cursor сохранена. `code .` открыл именно VS Code с учебным проектом.
- [x] Extension Pack for Java 0.31.1 и Code Runner 0.12.2 уже установлены в VS Code; проверены также Red Hat Java, Java Debug/Test/Maven/Projects.
- [x] Existing user settings сохранены; добавлены Moodle `files.autoSave=afterDelay`, `files.eol="\n"`, Java language-server home, Bash terminal profile. JSONC проверен парсингом. Workspace settings задают JavaSE-25 default и Code Runner через JAVA_HOME.
- [x] Доверие предоставлено только созданной учебной папке. Java Run в редакторе выполнил JDK 25 и показал в integrated terminal `Hello, World (with Javadoc)!`.
- [x] Run Code / Code Runner также успешно compiled/run и показал тот же результат в integrated terminal. Выбор JDK подтверждён полным executable path в Java Run. CLI inventory — проверка от 2026-10-07 (временный журнал удалён).

Для показа: открыть новый Terminal → `cd ~/Desktop/semester_3/software-engineering-2/track-1/02-seminars/homework-1-a15/hello-world` → `code .` → открыть HelloWorld.java → нажать **Run** над main. Альтернатива: **Run Code** вверху редактора / Ctrl+Option+N. Если нужно показать JDK отдельно: Command Palette → **Java: Configure Java Runtime**. UTF-8/LF исходника сохранены; исходная настройка скрытой status bar пользователя сохранена.

## Исправления и ограничения

- `git log --one-line` заменён на `git log --oneline`.
- macOS BSD sed отличается от GNU sed для `\n` в replacement: установлен GNU sed и добавлен в course PATH, чтобы исходные команды работали.
- Windows `.exe`, `/c/...`, `mintty`, Explorer и `/etc/mtab` не применяются к macOS; использованы Bash, `/Users/...`, Finder и `mount`.
- В тексте источника исправлены в ответах неточности ASCII, CR, UTF-16, fork return value, commit hash size и index.
- Обнаружена несвязанная ошибка старого Homebrew cask `inkscape` при полном inventory; нужные formulae/casks установились. Её исправление вне A15 не выполнялось.
- Нет удаления пользовательских данных, правок sudoers/administrator permissions, push, публикации или отправки задания.

## Личные действия и зачёт

1. Открыть новое окно Terminal.app, проверить Bash; при необходимости выбрать Terminal → Settings → General → Shells open with → Command `/opt/homebrew/bin/bash`. Для занятия также всегда доступен `/opt/homebrew/bin/bash -l`.
2. Прочитать ответы A2/A4, потренироваться объяснять и показывать команды; открыть Finder HOME и HTML Javadoc.
3. На упражнении показать преподавателю A1–A5 и оформить подтверждение в списке. По Moodle дедлайн 2026-10-23, 23:59 Europe/Berlin; зачёт возможен только на занятии, Moodle/email submission не признаётся. Автоматическая настройка не означает получение 15 баллов.
