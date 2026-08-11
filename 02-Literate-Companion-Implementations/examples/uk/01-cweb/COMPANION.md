# Companion

Цей companion показує практичний CWEB-процес для одного literate-джерела: `primes.w`.

## Двогілковий конвеєр

CWEB-джерело:

- `primes.w`

Машинна гілка:

- `primes.w -> ctangle -> primes.c -> cc/gcc -> primes -> output.txt`

Читабельна гілка:

- `primes.w -> cweave -> primes.tex -> pdftex -> primes.pdf`

## Машинна гілка (орієнтація на компілятор)

```bash
ctangle primes.w
cc -Wall -Wextra -pedantic primes.c -o primes
./primes > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

`ctangle` розгортає посилальні секції CWEB і генерує звичайний C-код у `primes.c`. Далі компілятор працює лише з plain C.

## Читабельна гілка (орієнтація на читання)

```bash
cweave primes.w
pdftex primes.tex
```

Ця гілка будує читабельний документ (`primes.pdf`) із того самого джерела.

## Маркери CWEB: роль і зміст

- `@` — керівний префікс CWEB.
- `@*` починає велику секцію у woven-документі.
- `@c` починає програмний фрагмент, який використовує `ctangle`.
- `@<Section name@>` — посилання на іменований кодовий фрагмент.
- `@ @<Section name@>=` — визначення іменованого кодового фрагмента.
- `ctangle` підставляє визначення замість посилань і генерує звичайний C-код.
- Компілятор C отримує лише згенерований `primes.c`, без маркерів CWEB.

## Чому самих коментарів недостатньо?

Звичайні коментарі:

- пояснення прикріплено до коду;
- текст для людини додається до коду, а порядок переважно залишається code-first.

CWEB:

- код організовано всередині пояснювального джерела, а потім видобуто для машини;
- іменовані фрагменти можна вводити у зручному для людського розуміння порядку;
- далі `ctangle` складає їх у порядку, зручному для компілятора.

## Місце у наборі

`01-cweb` — історичний маршрут для C-сімейства, найближчий до WEB-ідеї Кнута. Він показує повний tangle/weave-поділ: генерацію машинного вихідного тексту і читабельної документації. Повне порівняння всіх companion-варіантів наведено в кореневому README.

## Встановлення (перевірений маршрут для Debian/Ubuntu/WSL)

Цей процес передусім орієнтований на Unix-like середовище. На Windows практичним шляхом є WSL.

Встановлення базових інструментів:

```bash
sudo apt update
sudo apt install texlive-binaries build-essential
```

Перевірка:

```bash
command -v ctangle
command -v cweave
ctangle --version
```

Для PDF-гілки `pdftex primes.tex` може спочатку завершитися помилкою:

```text
I can't find file `cwebmac`.
```

Перевірене виправлення для Debian/Ubuntu/WSL:

```bash
sudo apt install texlive-extra-utils texlive-formats-extra
kpsewhich cwebmac.tex
```

Після цього:

```bash
cweave primes.w
pdftex primes.tex
```

Наведені назви пакетів утворюють перевірений Debian/Ubuntu/WSL-маршрут; в інших дистрибутивах назви можуть відрізнятися.

## Файли, що з’являються після виконання обох гілок

- `COMPANION.md`  
  Документація цього companion-прикладу. Фіксується в репозиторії.
- `primes.w`  
  Канонічний CWEB literate source. Фіксується в репозиторії.
- `primes.c`  
  Згенерований командою `ctangle primes.w`. Машинноорієнтований C-вихідний текст. Ручне редагування заборонене. Ігнорується.
- `primes`  
  Скомпільований виконуваний файл. Ігнорується.
- `output.txt`  
  Локально збережений вивід програми для smoke-check. Ігнорується.
- `primes.tex`  
  Згенерований командою `cweave primes.w`. TeX source для читабельного документа. Ігнорується.
- `primes.pdf`  
  Згенерований командою `pdftex primes.tex`. Читабельний відрендерений документ. Ігнорується.
- `primes.idx`  
  Службовий індексний файл weave/PDF-процесу. Ігнорується.
- `primes.scn`  
  Службовий файл секцій weave/PDF-процесу. Ігнорується.
- `primes.toc`  
  Службовий файл змісту weave/PDF-процесу. Ігнорується.
- `primes.log`  
  TeX build log. Ігнорується.

Згенеровані файли навмисно виключено через `.gitignore` цього каталогу.

## Подяки і посилання

- Дональд Е. Кнут і Сільвіо Леві — основні автори CWEB.
- Сучасну розробку і супровід зазначено у виводі TeX Live `CTANGLE`: <https://github.com/ascherer/cweb>.

- Дональд Е. Кнут і Сільвіо Леві, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
