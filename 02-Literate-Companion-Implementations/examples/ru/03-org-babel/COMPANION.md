# Companion

Этот companion показывает Org Babel workflow вокруг одного канонического plain-text источника: `primes.org`.

## Модель источника и компактный конвейер

Org Babel-источник:

- `primes.org` (канонический Org/Org Babel literate-источник)

Машинная ветка:

- `primes.org -> emacs --batch / org-babel-tangle -> primes.cpp -> g++ -> primes -> output.txt`

`primes.cpp` генерируется через tangling в Org Babel. В отличие от `02-noweb-like`, здесь `primes.cpp` — локальный сгенерированный артефакт и обычно должен игнорироваться, если только репозиторий не коммитит его намеренно как демонстрацию. Компилятор видит только `primes.cpp`; маркеры Org он не видит.

## Что такое Emacs / Org-mode / Org Babel

Emacs — программируемый текстовый редактор и расширяемое текстовое/рабочее окружение. В этом companion Emacs используется не только как визуальный редактор, но и как движок обработки, который запускает Org Babel в batch-режиме.

Org-mode — режим структурированных plain-text документов в Emacs.

Org Babel — подсистема Org-mode для исходных блоков: именование, ссылки, tangling в исходники, выполнение и экспорт.

Компактная формула:

- Emacs: программируемый редактор / расширяемая текстовая среда
- Org-mode: структурированные plain-text документы
- Org Babel: кодовые блоки + tangling + выполнение + экспорт

## Команды машинной ветки (проверенный WSL-маршрут)

```bash
emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")'
g++ -std=c++17 -Wall -Wextra -pedantic primes.cpp -o primes
./primes > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

Успешный маркер tangling:

- `Tangled 1 code block from primes.org`

Ожидаемые маркеры вывода программы:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `      6571      6997      7499      7919`

## Опциональная читаемая/export-ветка

Org-mode умеет экспорт документов, а Org Babel может участвовать в executable/literate documentation workflows.

Читаемая ветка / экспорт:

- `primes.org -> Org export -> читаемые форматы документов`

Этот companion проверяет tangling/build-путь. Экспорт — часть более широкой Org-экосистемы, но для данного smoke-check не обязателен.

## Маркеры и синтаксис блоков (Org Babel)

- `* Heading` создаёт структуру документа.
- `#+name: constants` задаёт имя исходного блока.
- `#+begin_src cpp` начинает C++ исходный блок.
- `#+end_src` завершает исходный блок.
- `:tangle primes.cpp` задаёт файл для генерации.
- `:noweb yes` включает noweb-подобное разворачивание.
- `<<constants>>` ссылается на именованный блок.
- `org-babel-tangle-file` раскрывает ссылки и записывает результат tangling.

C++-компилятор получает только сгенерированный `primes.cpp`, а не `.org`-документ.

## Почему не просто комментарии?

Обычные комментарии:

- пояснение прикреплено к коду.
- исходник остаётся в основном ориентированным прежде всего на код.

Org Babel:

- кодовые блоки живут внутри структурированного объяснительного документа.
- именованные блоки можно вводить там, где это лучше для читателя.
- tangling извлекает машинно-ориентированный исходник.

Короткая формула:

- Обычные комментарии: пояснение прикреплено к коду.
- Org Babel: код организован внутри структурированного документа, а затем извлекается для машины.

## Место в наборе

`03-org-babel` показывает мощный современный literate workflow внутри Emacs/Org-mode. Он сильнее всего раскрывается, когда Emacs/Org-mode принят как рабочая среда, но это не самый лёгкий C++ маршрут. Полное сравнение всех companion-вариантов см. в корневом README.

## Установка (основной WSL/Linux маршрут)

```bash
sudo apt update
sudo apt install emacs-nox build-essential
```

Если нужен полный графический пакет:

```bash
sudo apt install emacs build-essential
```

Проверка:

```bash
command -v emacs
emacs --version
g++ --version
```

Проверенное окружение:

- WSL / Debian/Ubuntu-подобное окружение.
- Проверялся Emacs 29.3.
- `emacs --batch ...` успешно выдавал `Tangled 1 code block from primes.org`.

Практическая заметка: при установке на некоторых системах может появиться диалог конфигурации Postfix как побочный эффект зависимостей. Для этого companion почтовый сервер не нужен; если спрашивает, выбирайте `No configuration`.

## Заметки для Windows

Emacs можно установить нативно в Windows.

- Страница GNU Emacs download описывает installer/zip-варианты.
- Windows binaries доступны через GNU mirrors/FTP.
- Рекомендуемый прямой каталог для этого проекта: <https://ftp.gnu.org/gnu/emacs/windows/>.
- Для zip-установки можно использовать `bin\runemacs.exe`.

Если Emacs не в PATH, PowerShell не найдёт `emacs` автоматически.

```powershell
where.exe emacs
emacs --version
```

Если не найден:

- добавьте Emacs `bin` в PATH, или
- запускайте `emacs.exe` полным путём, например:

```powershell
& "C:\path\to\emacs\bin\emacs.exe" --batch primes.org -l org -l ob-tangle --eval "(org-babel-tangle-file \"primes.org\")"
```

Нативный tangling в Windows может работать, но нативная сборка также требует отдельный C++ toolchain (например, MSYS2/MinGW-w64 или Visual Studio Build Tools). Для этого companion основной воспроизводимый маршрут — WSL/Linux с полной проверкой цепочки.

## Заметка про редакторы / VS Code

`primes.org` можно открывать и редактировать в других редакторах, включая редакторы Windows и VS Code с расширениями для Org. Это вспомогательная поддержка редактирования.

Воспроизводимый workflow этого companion использует Emacs batch mode как процессор Org Babel. Если проект не хочет принимать Emacs/Org-mode как окружение, обычно практичнее `02-noweb-like`. Если нужна историческая полная tangle/weave-модель, лучше ориентироваться на `01-cweb`.

## Диагностика и частые сообщения

При первых batch-запусках Emacs может печатать:

```text
Could not read ‘org-id-locations’ from ~/.emacs.d/.org-id-locations, setting it to nil
```

Для этого companion это не ошибка сборки; это означает, что локальный Org ID cache-файл ещё не создан. Ключевой признак успеха:

- `Tangled 1 code block from primes.org`

Заметка про line endings при смешанном Windows/WSL редактировании: держите `.org` и сгенерированный `.cpp` в LF, если появляются CR-артефакты.

```bash
sed -i 's/\r$//' primes.org
emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")'
```

## Какие файлы появляются

- `COMPANION.md`  
  Документация для этого companion-примера. Коммитится.
- `primes.org`  
  Канонический Org Babel literate-источник. Коммитится.
- `primes.cpp`  
  Генерируется через tangling в Org Babel. Игнорируется, если только не коммитится намеренно для демонстрации.
- `primes`  
  Скомпилированный исполняемый файл. Игнорируется.
- `output.txt`  
  Локально сохранённый вывод для smoke-check. Игнорируется.

## Благодарности и ссылки

- Загрузка GNU Emacs: <https://www.gnu.org/software/emacs/download.html>
- Windows-каталог GNU Emacs на FTP: <https://ftp.gnu.org/gnu/emacs/windows/>
- Org manual: извлечение исходного кода: <https://orgmode.org/manual/Extracting-Source-Code.html>
- Сравнительный источник по CWEB: Дональд Э. Кнут и Сильвио Леви, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
