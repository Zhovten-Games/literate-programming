# Companion

Этот companion показывает практический CWEB-процесс для одного literate-источника: `primes.w`.

## Двухветочный конвейер

CWEB-источник:

- `primes.w`

Машинная ветка:

- `primes.w -> ctangle -> primes.c -> cc/gcc -> primes -> output.txt`

Читаемая ветка:

- `primes.w -> cweave -> primes.tex -> pdftex -> primes.pdf`

## Машинная ветка (ориентация на компилятор)

```bash
ctangle primes.w
cc -Wall -Wextra -pedantic primes.c -o primes
./primes > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

`ctangle` раскрывает ссылочные секции CWEB и генерирует обычный C-код в `primes.c`. Далее компилятор работает только с plain C.

## Читаемая ветка (ориентация на чтение)

```bash
cweave primes.w
pdftex primes.tex
```

Эта ветка строит читаемый документ (`primes.pdf`) из того же исходника.

## Маркеры CWEB: роль и смысл

- `@` — управляющий префикс CWEB.
- `@*` начинает крупную секцию в woven-документе.
- `@c` начинает программный фрагмент, который использует `ctangle`.
- `@<Section name@>` — ссылка на именованный кодовый фрагмент.
- `@ @<Section name@>=` — определение именованного кодового фрагмента.
- `ctangle` подставляет определения вместо ссылок и генерирует нормальный C-код.
- Компилятор C никогда не видит маркеры CWEB; он видит только сгенерированный `primes.c`.

## Почему не просто комментарии?

Обычные комментарии:

- пояснение прикреплено к коду.
- человеческий текст добавляется к коду, но порядок в основном остаётся code-first.

CWEB:

- код организован внутри объяснительного источника, затем извлекается для машины.
- именованные фрагменты можно вводить в порядке, удобном для понимания человеком.
- затем `ctangle` собирает их в порядке, удобном для компилятора.

## Место в наборе

`01-cweb` — исторический маршрут для C-семейства, наиболее близкий к WEB-идее Кнута. Он показывает полный tangle/weave-раздел: генерацию машинного исходника и генерацию читаемой документации. Полное сравнение всех companion-вариантов см. в корневом README.

## Установка (проверенный маршрут для Debian/Ubuntu/WSL)

Этот процесс в первую очередь ориентирован на Unix-like окружение. На Windows практичный путь — WSL.

Установка базовых инструментов:

```bash
sudo apt update
sudo apt install texlive-binaries build-essential
```

Проверка:

```bash
command -v ctangle
command -v cweave
ctangle --version
```

Для PDF-ветки `pdftex primes.tex` может сначала завершиться ошибкой:

```text
I can't find file `cwebmac`.
```

Проверенное исправление для Debian/Ubuntu/WSL:

```bash
sudo apt install texlive-extra-utils texlive-formats-extra
kpsewhich cwebmac.tex
```

После этого:

```bash
cweave primes.w
pdftex primes.tex
```

Указанные имена пакетов — это проверенный Debian/Ubuntu/WSL-маршрут, но не универсальное правило для всех дистрибутивов.

## Какие файлы появляются после обеих веток

- `COMPANION.md`  
  Документация для этого companion-примера. Коммитится в репозиторий.
- `primes.w`  
  Канонический CWEB literate source. Коммитится в репозиторий.
- `primes.c`  
  Сгенерирован `ctangle primes.w`. Машинно-ориентированный C-исходник. Не редактировать вручную. Игнорируется.
- `primes`  
  Скомпилированный исполняемый файл. Игнорируется.
- `output.txt`  
  Локально сохранённый вывод программы для smoke-check. Игнорируется.
- `primes.tex`  
  Сгенерирован `cweave primes.w`. TeX source для читаемого документа. Игнорируется.
- `primes.pdf`  
  Сгенерирован `pdftex primes.tex`. Читаемый срендеренный документ. Игнорируется.
- `primes.idx`  
  Служебный индексный файл из weave/PDF-процесса. Игнорируется.
- `primes.scn`  
  Служебный файл секций из weave/PDF-процесса. Игнорируется.
- `primes.toc`  
  Служебный файл оглавления из weave/PDF-процесса. Игнорируется.
- `primes.log`  
  TeX build log. Игнорируется.

Сгенерированные файлы намеренно исключены через `.gitignore` этого каталога.

## Благодарности и ссылки

- Дональд Э. Кнут и Сильвио Леви — основные авторы CWEB.
- Современная разработка/сопровождение указана в выводе TeX Live `CTANGLE`: <https://github.com/ascherer/cweb>.

- Дональд Э. Кнут и Сильвио Леви, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
