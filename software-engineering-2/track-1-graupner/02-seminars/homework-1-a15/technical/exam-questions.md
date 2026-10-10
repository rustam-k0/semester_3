# Exam questions and answers

Вопросы A2 и A4 из задания, ответы и команды для показа. Проверка окружения: 2026-10-07; объединение материалов: 2026-10-09.

# A2 — ответы и демонстрация

Проверено 2026-10-07 на macOS 26.5.2, arm64 (Apple Silicon). Материалы: README A2 и все пять разделов 21–25.

1. **Terminal** — приложение для текстового ввода и вывода, эмулирующее экран и клавиатуру аппаратного терминала. В macOS это Terminal.app; внутри работает отдельная shell. Терминал полезен для автоматизации, компиляции и работы с удалёнными системами.
2. **Shell** — интерпретатор команд: выполняет builtins, запускает программы, настраивает pipes и redirects. Исходная login shell этого пользователя — `/bin/zsh`. Для занятий настроен Homebrew Bash `/opt/homebrew/bin/bash`, версия 5.3.9, в Terminal.app и VS Code. `echo "$BASH_VERSION"; ps -p $$ -o comm=` показывает текущую shell; `$SHELL` может сохранять login shell и не доказывает текущую.
3. **Unix process** — экземпляр выполняемой программы с PID, памятью, окружением и файловыми дескрипторами (stdin, stdout, stderr). Родитель создаёт ребёнка; `fork()` возвращает 0 ребёнку, PID ребёнка родителю, -1 при ошибке. `exec` заменяет программу внутри процесса. Exported variables наследуются ребёнком; изменения не возвращаются родителю.
4. **`|`** соединяет stdout слева со stdin справа. `printf 'one\ntwo\n' | wc -l` выводит 2. stderr автоматически не включён в pipe.
5. **HOME** — домашний каталог пользователя, где находятся личные файлы и настройки. `cd` без аргументов переходит туда.
6. Фактический HOME: `/Users/damirahavaashova`. Показ: `echo "$HOME"; (cd; pwd; realpath .)`.
7. Пять существующих записей HOME: `Desktop`, `Documents`, `Downloads`, `Library`, `Pictures`. `ls -l "$HOME"` показывает обычные записи, `ls -la "$HOME"` также скрытые. В Finder: Go → Home, Cmd+Shift+. показывает dotfiles.
8. **PATH** — exported variable со списком каталогов через `:`. Shell ищет executable по порядку, если команда задана без пути. `command -v java` показывает выбранный executable; `printf '%s\n' "$PATH" | tr ':' '\n'` показывает каталоги по строкам. Не следует добавлять `.` в начало PATH.
9. PATH задаётся окружением родителя и startup-файлами shell. Для A15 добавлен `$HOME/.config/a15/env.sh`, подключённый из `.bash_profile`, `.bashrc`, `.zprofile`, `.zshrc`. Java начинается с `/opt/homebrew/Cellar/openjdk/25/libexec/openjdk.jdk/Contents/Home/bin`; далее VS Code, Sublime, GNU tools и Homebrew. Изменение для текущей shell: `export PATH="/some/tool/bin:$PATH"`; постоянное — в startup-файле. `source "$HOME/.config/a15/env.sh"` применяет настройки в текущем процессе.
10. **Dotfiles** — имена с начальной точкой; обычно скрыты в обычном листинге. Часто хранят конфигурацию, но точка сама по себе не задаёт формат или назначение.
11. Пять примеров: `.bash_profile` — startup login Bash; `.bashrc` — interactive Bash; `.zprofile` — login zsh; `.zshrc` — interactive zsh; `.gitconfig` — пользовательские Git-настройки. Здесь `.bashrc` была dangling symlink на `~/dotfiles/.bashrc`; файл-цель создан, ссылка сохранена. Дополнительно `.zsh_history` хранит историю, `.ssh` — каталог SSH-конфигурации/ключей (не показывайте секретные ключи).
12. **UTF-8** — кодировка Unicode длиной 1–4 байта на code point; первые 128 кодов совместимы с ASCII. ASCII — 7-битный набор 0–127, без кириллицы и €; «extended ASCII» не одна универсальная кодировка. `printf 'Привет, €\n'` показывает Unicode. `printf '€' | od -An -tx1` даёт `e2 82 ac`. CR = 13 = 0x0D, LF = 10 = 0x0A. UTF-16 использует также surrogate pairs, а не всегда один 16-битный элемент.
13. **ANSI escape sequence** — последовательность управляющих байтов, начиная с ESC (27/0x1B), для цвета, курсора и других функций терминала. `printf 'Hello \033[31;1mWorld\033[0m\n'` красит World и сбрасывает стиль; `printf` переносимее `echo -e`.
14. **Pretty prompt** задаётся `PS1` в Bash. Для демонстрации в отдельном Bash: `PS1='\[\e[32m\]\u@\h \w\[\e[0m\] \\$ '`. `\u` — пользователь, `\h` — host, `\w` — каталог; `\[...\]` ограждает непечатаемые управляющие байты. Постоянный prompt помещают в `.bashrc`; исходный zsh prompt сохранён.
15. **Ken Thompson** — один из создателей Unix в Bell Labs, создатель B, соавтор UTF-8 вместе с Rob Pike; участвовал в разработке Go. Dennis Ritchie создал C и участвовал в Unix; Brian Kernighan известен книгами и инструментами Unix; Stephen Bourne создал Bourne shell; Bill Joy — vi и C shell; Linus Torvalds — Linux и Git.

## Дополнительные разделы: практическая демонстрация

```bash
# Выполнять в отдельном Bash, не менять существующие файлы HOME:
/opt/homebrew/bin/bash -l
cd "$HOME/.config/a15"
printf 'Hello World\n' > hello.txt
cat hello.txt | sed 's/./&\n/g' | wc
# GNU sed: 12 строк, 10 слов, 23 байта; пробел и исходный LF тоже учитываются.
ls -la "$HOME" | grep ' \.[a-z].*'
# Фильтрует строки dotfiles; шаблон учебный, не универсальный парсер имён.
A15_LOCAL=local
bash -c 'printf "local=<%s>\n" "$A15_LOCAL"'
# Пусто: переменная не exported.
export A15_LOCAL
bash -c 'printf "exported=<%s>\n" "$A15_LOCAL"'
# local: ребёнок унаследовал exported variable.
unset A15_LOCAL
alias a15ll='ls -la'
a15ll
# Alias подставляет команду в interactive shell.
a15_path() { local sep="$1"; shift; local result="" arg; for arg in "$@"; do result="${result:+$result$sep}$arg"; done; printf '%s\n' "$result"; }
a15_path ':' /bin /usr/bin '/Applications/Visual Studio Code.app'
# Функция принимает аргументы и сохраняет пробелы благодаря "$@".
history 5
# История текущей интерактивной shell; секретные команды не показывать.
```

Bash login: `/etc/profile`, затем первый существующий из `.bash_profile`, `.bash_login`, `.profile`; `.bashrc` подключён явно из `.bash_profile`. Interactive non-login Bash читает `.bashrc`. `.bash_logout` — при завершении login Bash. Zsh: `.zshenv`, для login `.zprofile`, для interactive `.zshrc`, затем для login `.zlogin`; при logout `.zlogout` (с соответствующими system-wide файлами). Не каждая shell читает все rc-файлы. `source` выполняет файл в текущей shell; обычный запуск скрипта работает в дочернем процессе. Alias не наследуется; функции Bash можно явно экспортировать через `export -f`, но это не требуется здесь. Функции имеют exit status, текстовый результат удобно получать через `$()`.

Filesystem связывает имена, метаданные и данные на накопителе. Абсолютный путь начинается с `/`, относительный — от working directory; `.` означает текущий каталог, `..` — родительский. Symlink хранит путь к другой записи, mount присоединяет filesystem к точке дерева. В macOS для просмотра mounts используется `mount`, а не отсутствующий `/etc/mtab`. Размер блока зависит от filesystem: числа в исходнике — примеры, не универсальные свойства SSD.


# A4 — ответы Validation

Учебный проект: `/Users/damirahavaashova/Desktop/semester_3/software-engineering-2/track-1-graupner/02-seminars/homework-1-a15/hello-world`. Имя и email Git сохранены: Rustam Khavaiashkhov, rustam.khavaiashkhov@informatik.hs-fulda.de.

1. Локальный repository находится в скрытом каталоге `.git` внутри проекта. Он содержит objects, refs, HEAD, index и настройки; рабочие исходники находятся рядом.
2. Commit — неизменяемый объект с snapshot дерева файлов, ссылкой на родителя/родителей, author/committer, временем и сообщением. Commit ID вычисляется по всему объекту, не только по файлам. Для SHA-1 это 20 байт, отображаемых как 40 hex-символов, а не 40 байт.
3. Branch — именованный изменяемый указатель на commit. Историю можно проследить через parent links; она может образовывать граф. Здесь `main`; HEAD обычно символически указывает на эту branch.
4. `HelloWorld.java` — исходный код, его следует версионировать. `.class` и `doc/` генерируются из него, поэтому исключены через `.gitignore`; `bin/` также исключён для output VS Code. `.gitignore` не снимает tracking уже добавленного файла.
5. Clean state: нет изменений между working tree и index и между index и HEAD; нет неотслеживаемых неигнорируемых файлов. Проверка: `git status` → `nothing to commit, working tree clean`.
6. Dirty state: есть незакоммиченные изменения — staged, unstaged или untracked. После правки Java-кода это было продемонстрировано до staging.
7. Нужные изменения staged через `git add`, затем committed; при необходимости их временно сохраняют через stash. Ненужные изменения можно отменить через restore, но это удаляет незакоммиченные правки; такие команды не выполнялись над пользовательскими проектами. Игнорирование подходит для generated files.
8. Существующий commit не меняется на месте. `commit --amend` или rebase создают новые commits с новыми ID и перемещают refs. Старый объект некоторое время может оставаться доступен через reflog.
9. После push тоже возможно переписать локальную историю, но опубликованные commits уже могли быть использованы другими. Замена remote history потребует согласованного force push; это не нормальный способ исправления общей истории.
10. Ошибочный опубликованный commit обычно исправляют новым commit или `git revert <id>`, который записывает обратное изменение, сохраняя историю. Если опубликован secret, нужно отдельно отозвать secret и согласовать очистку истории. Push в этом задании не выполнялся.

## Показ преподавателю

```bash
cd "/Users/damirahavaashova/Desktop/semester_3/software-engineering-2/track-1-graupner/02-seminars/homework-1-a15/hello-world"
cat ~/.gitconfig
git status
git log --oneline --decorate
cat .gitignore
git check-ignore HelloWorld.class doc/index.html
git show --stat 9942da7
git diff 9942da7~1..9942da7 --name-status
git diff 9942da7~1..9942da7 -- .gitignore
javac HelloWorld.java
java HelloWorld
open doc/index.html
```

История: empty root commit с tag `root`, `add .gitignore`, `add HelloWorld.java`, `add Javadoc`, `configure VS Code for JDK 25`. Результат последней Java-версии: `Hello, World (with Javadoc)!`. Начальный `Hello, World!` успешно запускался до изменения по результатам проверки от 2026-10-07.

Исправление исходника: `git log --one-line` ошибочно, правильный флаг — `--oneline`. `.gitconfig` не обязательно создаётся при первом запуске Git; identity задаётся явно. Index после commit соответствует snapshot, а не буквально очищается. Настройки `core.ignorecase=true`, `core.autocrlf=false`, `core.filemode=false`, `core.eol=lf`, `init.defaultBranch=main` применены глобально; существующий `core.excludesfile` сохранён. В существующих repositories локальная конфигурация может перекрывать глобальную.
