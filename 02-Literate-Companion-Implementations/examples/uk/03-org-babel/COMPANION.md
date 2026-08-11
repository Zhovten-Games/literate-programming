# Companion

Цей companion показує Org Babel workflow навколо одного канонічного plain-text джерела: `primes.org`.

## Модель джерела і компактний конвеєр

Org Babel-джерело:

- `primes.org` (канонічне Org/Org Babel literate-джерело)

Машинна гілка:

- `primes.org -> emacs --batch / org-babel-tangle -> primes.cpp -> g++ -> primes -> output.txt`

`primes.cpp` генерується через tangling в Org Babel. На відміну від `02-noweb-like`, тут `primes.cpp` є локальним згенерованим артефактом і зазвичай ігнорується, якщо репозиторій не фіксує його навмисно як демонстрацію. Компілятор отримує лише `primes.cpp`, без маркерів Org.

## Що таке Emacs / Org-mode / Org Babel

Emacs — програмований текстовий редактор і розширюване текстове/робоче середовище. У цьому companion Emacs використовується як візуальний редактор і рушій обробки, що запускає Org Babel у batch-режимі.

Org-mode — режим структурованих plain-text документів у Emacs.

Org Babel — підсистема Org-mode для вихідних блоків: найменування, посилання, tangling у вихідні тексти, виконання й експорт.

Компактна формула:

- Emacs: програмований редактор / розширюване текстове середовище
- Org-mode: структуровані plain-text документи
- Org Babel: кодові блоки + tangling + виконання + експорт

## Команди машинної гілки (перевірений WSL-маршрут)

```bash
emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")'
g++ -std=c++17 -Wall -Wextra -pedantic primes.cpp -o primes
./primes > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

Маркер успішного tangling:

- `Tangled 1 code block from primes.org`

Очікувані маркери виводу програми:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `      6571      6997      7499      7919`

## Необов’язкова читабельна/export-гілка

Org-mode підтримує експорт документів, а Org Babel може брати участь у executable/literate documentation workflows.

Читабельна гілка / експорт:

- `primes.org -> Org export -> читабельні формати документів`

Цей companion перевіряє tangling/build-шлях. Експорт є частиною ширшої Org-екосистеми і необов’язковий для цього smoke-check.

## Маркери і синтаксис блоків (Org Babel)

- `* Heading` створює структуру документа.
- `#+name: constants` задає ім’я вихідного блока.
- `#+begin_src cpp` починає C++ вихідний блок.
- `#+end_src` завершує вихідний блок.
- `:tangle primes.cpp` задає файл для генерації.
- `:noweb yes` вмикає noweb-подібне розгортання.
- `<<constants>>` посилається на іменований блок.
- `org-babel-tangle-file` розкриває посилання і записує результат tangling.

C++-компілятор отримує лише згенерований `primes.cpp`, а не `.org`-документ.

## Чому самих коментарів недостатньо?

Звичайні коментарі:

- пояснення прикріплено до коду;
- вихідний текст залишається переважно орієнтованим на код.

Org Babel:

- кодові блоки живуть усередині структурованого пояснювального документа;
- іменовані блоки можна вводити там, де це краще для читача;
- tangling видобуває машинно-орієнтований вихідний текст.

Коротка формула:

- Звичайні коментарі: пояснення прикріплено до коду.
- Org Babel: код організовано всередині структурованого документа, а потім видобуто для машини.

## Місце у наборі

`03-org-babel` показує потужний сучасний literate workflow усередині Emacs/Org-mode. Він найповніше розкривається, коли Emacs/Org-mode прийнято як робоче середовище, і має вищий поріг входу порівняно з легшими C++-маршрутами. Повне порівняння всіх companion-варіантів наведено в кореневому README.

## Встановлення (основний WSL/Linux-маршрут)

```bash
sudo apt update
sudo apt install emacs-nox build-essential
```

Якщо потрібен повний графічний пакет:

```bash
sudo apt install emacs build-essential
```

Перевірка:

```bash
command -v emacs
emacs --version
g++ --version
```

Перевірене середовище:

- WSL / Debian/Ubuntu-подібне середовище.
- Перевірено Emacs 29.3.
- `emacs --batch ...` успішно виводив `Tangled 1 code block from primes.org`.

Практична примітка: під час встановлення на деяких системах може з’явитися діалог конфігурації Postfix як побічний ефект залежностей. Цей companion не потребує поштового сервера; у діалозі слід обрати `No configuration`.

## Примітки для Windows

Emacs можна встановити нативно у Windows.

- Сторінка GNU Emacs download описує installer/zip-варіанти.
- Windows binaries доступні через GNU mirrors/FTP.
- Рекомендований прямий каталог для цього проєкту: <https://ftp.gnu.org/gnu/emacs/windows/>.
- Для zip-встановлення можна використовувати `bin\runemacs.exe`.

Якщо Emacs відсутній у PATH, PowerShell не знайде `emacs` автоматично.

```powershell
where.exe emacs
emacs --version
```

Якщо не знайдено:

- додайте Emacs `bin` до PATH або
- запускайте `emacs.exe` повним шляхом, наприклад:

```powershell
& "C:\path\to\emacs\bin\emacs.exe" --batch primes.org -l org -l ob-tangle --eval "(org-babel-tangle-file \"primes.org\")"
```

Нативний tangling у Windows може працювати, але нативне складання також потребує окремого C++ toolchain, наприклад MSYS2/MinGW-w64 або Visual Studio Build Tools. Основним відтворюваним маршрутом для цього companion є WSL/Linux із повною перевіркою ланцюга.

## Примітка про редактори / VS Code

`primes.org` можна відкривати і редагувати в інших редакторах, зокрема у редакторах Windows і VS Code з розширеннями для Org. Це допоміжний шлях редагування.

Відтворюваний workflow цього companion використовує Emacs batch mode як процесор Org Babel. Для проєкту без Emacs/Org-mode як прийнятого середовища зазвичай практичнішим є `02-noweb-like`. Історичну повну tangle/weave-модель представляє `01-cweb`.

## Діагностика і поширені повідомлення

Під час перших batch-запусків Emacs може виводити:

```text
Could not read ‘org-id-locations’ from ~/.emacs.d/.org-id-locations, setting it to nil
```

Для цього companion повідомлення не є помилкою складання; воно означає, що локальний Org ID cache-файл ще не створено. Ключова ознака успіху:

- `Tangled 1 code block from primes.org`

Примітка про line endings за змішаного Windows/WSL-редагування: використовуйте LF для `.org` і згенерованого `.cpp`, якщо з’являються CR-артефакти.

```bash
sed -i 's/\r$//' primes.org
emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")'
```

## Файли, що з’являються

- `COMPANION.md`  
  Документація цього companion-прикладу. Фіксується в репозиторії.
- `primes.org`  
  Канонічне Org Babel literate-джерело. Фіксується в репозиторії.
- `primes.cpp`  
  Генерується через tangling в Org Babel. Ігнорується, якщо його не фіксують навмисно для демонстрації.
- `primes`  
  Скомпільований виконуваний файл. Ігнорується.
- `output.txt`  
  Локально збережений вивід для smoke-check. Ігнорується.

## Подяки і посилання

- Завантаження GNU Emacs: <https://www.gnu.org/software/emacs/download.html>
- Windows-каталог GNU Emacs на FTP: <https://ftp.gnu.org/gnu/emacs/windows/>
- Org manual: видобування вихідного коду: <https://orgmode.org/manual/Extracting-Source-Code.html>
- Порівняльне джерело про CWEB: Дональд Е. Кнут і Сільвіо Леві, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
