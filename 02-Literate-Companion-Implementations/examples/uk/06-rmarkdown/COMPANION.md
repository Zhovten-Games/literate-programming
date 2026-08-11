# Companion

## 1. Короткий вступ

R Markdown демонструє workflow відтворюваного звіту (reproducible-report workflow). У цьому companion `primes.Rmd` є канонічним документом-джерелом; render виконує R code chunk і створює `primes.html`.

Це dynamic-document workflow: проза і виконувані chunks живуть в одному вихідному документі. За своєю моделлю він відрізняється від строгого Knuth-style WEB і канонічного tangle/weave-конвеєра генерації вихідних текстів.

## 2. Модель джерела і компактний pipeline

R Markdown-джерело:

- `primes.Rmd`

Гілка відрендереного звіту:

- `primes.Rmd -> rmarkdown::render() -> knitr -> pandoc -> primes.html`

Пояснення:

- `primes.Rmd` містить Markdown-прозу і виконувані R chunks.
- `rmarkdown::render()` запускає рендеринг.
- `knitr` виконує R chunks і готує проміжне Markdown-представлення.
- `pandoc` конвертує проміжний документ у HTML.
- `primes.html` є згенерованим виводом та ігнорується системою контролю версій.
- `01-cweb`, `02-noweb-like` і `03-org-babel` генерують канонічний машинно-орієнтований вихідний файл, тоді як цей companion генерує звіт.
- Порівняно з `05-jupyter`, основною моделлю є workflow із рендерингом звіту, а не інтерактивний notebook.

## 3. Що таке R Markdown / Rmd / knitr / rmarkdown / Pandoc / RStudio

- **R Markdown**: формат документа, що поєднує Markdown-прозу і виконувані code chunks.
- **`.Rmd`**: R Markdown source file.
- **R**: мова/runtime, якою виконуються chunks у цьому companion.
- **`knitr`**: рушій, що виконує chunks і вставляє результат у документ.
- **`rmarkdown`**: R package, що координує render.
- **Pandoc**: шар конвертації документа, який використовується для HTML та інших форматів.
- **RStudio (Posit)**: необов’язкова IDE/GUI для R і R Markdown. Вона корисна, але не потрібна для CLI-перевірки.

Коротка формула:

- R Markdown: Markdown + виконувані code chunks
- `.Rmd`: канонічний R Markdown source file
- `knitr`: виконання chunks і вставлення результату
- `rmarkdown::render()`: точка входу для render
- Pandoc: шар конвертації документа
- RStudio: необов’язкова IDE/GUI, що не потрібна для CLI-перевірки

## 4. Команди рендерингу

Із `examples/uk/06-rmarkdown`:

```bash
Rscript -e 'rmarkdown::render("primes.Rmd")'
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Очікувані маркери для smoke-check:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `6571      6997      7499      7919`

Примітка: console output R в HTML може мати префікс `##` від `knitr`. Це очікувана поведінка.

Українську гілку включено до того самого render-маршруту і locale validation; перед публікацією слід виконати документовану команду рендера та зафіксувати evidence. Наявні ручні перевірки рендера охоплюють `examples/en/06-rmarkdown` і `examples/ru/06-rmarkdown`.

Успішні версії, зафіксовані під час ручного тесту:

- `rmarkdown`: `2.31`
- `rmarkdown::pandoc_version()`: `3.1.3`

Це протестовані версії, а не мінімальні вимоги.

## 5. Чому самих коментарів недостатньо?

Звичайні коментарі:

- пояснення прикріплено до коду.

R Markdown:

- проза, виконувані R chunks і відрендерений результат живуть разом в одному report source.

Визначальна відмінність: основною метою R Markdown є генерація відтворюваного rendered report із документа з виконуваними chunks, а не видобування вихідного тексту для компілятора.

Коротка формула:

- Звичайні коментарі: пояснення прикріплено до коду.
- R Markdown: звіт містить пояснення, виконувані chunks і відрендерений результат.

## 6. Місце у наборі

`06-rmarkdown` показує гілку reproducible reports у companion-наборі. Він корисний для звітів, статистичних документів і відрендерених обчислювальних наративів та перебуває ближче до публікації документа, ніж до канонічної WEB-style генерації вихідного тексту. Повне порівняння всіх companion-варіантів наведено в кореневому README.

## 7. Встановлення: локальна коренева `.rlib`

Документований маршрут: чистий WSL/Linux-шлях із project-local бібліотекою пакетів.

Із кореня `Literate-Companion-Implementations`:

```bash
sudo apt update
sudo apt install -y r-base r-base-dev pandoc libuv1-dev

mkdir -p .rlib
export R_LIBS_USER="$PWD/.rlib"

Rscript -e '.libPaths()'
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

Перевірка:

```bash
Rscript -e '.libPaths()'
Rscript -e 'packageVersion("rmarkdown")'
Rscript -e 'rmarkdown::pandoc_version()'
```

Очікується, що `.libPaths()` містить:

```text
.../Literate-Companion-Implementations/.rlib
```

Практичні примітки:

1. `install.packages("rmarkdown")` є R-синтаксисом і запускається через `Rscript -e 'install.packages(...)'`, а не безпосередньо у Bash.
2. Project packages слід установлювати до локальної `.rlib`, оскільки системна бібліотека R (`/usr/local/lib/R/site-library`) може бути недоступною для запису.
3. `R_LIBS_USER` діє лише у поточній сесії. У новому терміналі виконайте:
   ```bash
   cd "/path/to/Literate-Companion-Implementations"
   export R_LIBS_USER="$PWD/.rlib"
   ```
4. Може знадобитися `libuv1-dev`, оскільки у ланцюзі залежностей CRAN можлива така послідовність:
   ```text
   fs -> sass -> bslib -> rmarkdown
   ```
5. Для HTML-рендерингу потрібен `pandoc`:
   ```bash
   command -v pandoc
   pandoc --version
   Rscript -e 'rmarkdown::pandoc_version()'
   ```
6. Для цього companion достатньо HTML-виводу; LaTeX/TinyTeX знадобиться лише після додавання PDF.

## 8. Примітки про Windows

Windows-маршрут можливий, проте основним протестованим шляхом для цього companion є WSL/Linux.

- R можна встановити нативно у Windows.
- RStudio — зручна GUI/IDE для R Markdown, але вона не є обов’язковою для описаного CLI-маршруту.
- Інструменти мають бути доступними у `PATH`.
- Нативний Windows-маршрут потребує R, пакета `rmarkdown` і Pandoc.

Перевірки у PowerShell:

```powershell
where.exe Rscript
Rscript --version
Rscript -e "packageVersion('rmarkdown')"
Rscript -e "rmarkdown::pandoc_version()"
```

Відтворюваним протестованим маршрутом для цього companion є WSL/Linux із локальною кореневою `.rlib`.

## 9. Діагностика і поширені проблеми

### A. `install.packages` уведено в Bash

Проблема:

```bash
install.packages("rmarkdown")
```

Це спричиняє синтаксичні помилки Bash, оскільки `install.packages()` є синтаксисом R.

Правильна команда:

```bash
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

### B. System R library is not writable

Проблема:

```text
'lib = "/usr/local/lib/R/site-library"' is not writable
```

Виправлення:

```bash
mkdir -p .rlib
export R_LIBS_USER="$PWD/.rlib"
```

### C. Package not found after reopening terminal

Проблема: `rmarkdown` було встановлено, але згодом `Rscript -e 'packageVersion("rmarkdown")'` повідомляє, що пакет не знайдено.

Причина: у новій shell-сесії не було експортовано `R_LIBS_USER`.

Виправлення:

```bash
cd "/path/to/Literate-Companion-Implementations"
export R_LIBS_USER="$PWD/.rlib"
Rscript -e '.libPaths()'
Rscript -e 'packageVersion("rmarkdown")'
```

### D. `fs` / `sass` / `bslib` / `rmarkdown` dependency failure

Проблема: встановлення завершується помилкою, оскільки `fs` не може скластися і повідомляє про нестачу libuv.

Виправлення:

```bash
sudo apt install -y libuv1-dev
rm -rf .rlib/00LOCK-*
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

### E. Pandoc not found

Виправлення:

```bash
sudo apt install -y pandoc
command -v pandoc
pandoc --version
Rscript -e 'rmarkdown::pandoc_version()'
```

### F. Generated HTML

`primes.html` є згенерованим виводом і не фіксується в репозиторії.

## 10. Згенеровані файли

- `COMPANION.md`  
  Документація цього companion-прикладу. Фіксується як джерело.
- `primes.Rmd`  
  Канонічне R Markdown-джерело. Фіксується як джерело.
- `primes.html`  
  Відрендерений HTML від `rmarkdown::render("primes.Rmd")`. Генерується та ігнорується.
- `primes.knit.md`  
  Можливий проміжний Markdown від `knitr`/`rmarkdown` під час рендерингу. Генерується та ігнорується, якщо з’являється.
- `*_files/`  
  Можливий каталог ресурсів для HTML. Генерується та ігнорується.
- `.rlib/`  
  Локальна коренева бібліотека R-пакетів для цього companion-набору. Генерується та ігнорується.
- `.Rhistory`, `.RData`, `.Rproj.user/`  
  Локальні R/RStudio-артефакти. Генеруються та ігноруються.

Примітка: `primes.knit.md` є можливим проміжним артефактом; після render він може залишитися або бути видаленим.

## 11. Подяки / джерела

- R Markdown documentation: <https://rmarkdown.rstudio.com/>
- R Markdown lesson / guide: <https://rmarkdown.rstudio.com/lesson-1.html>
- R Markdown render documentation: <https://rmarkdown.rstudio.com/docs/reference/render.html>
- knitr documentation: <https://yihui.org/knitr/>
- Pandoc: <https://pandoc.org/>
- Posit / RStudio IDE: <https://posit.co/products/open-source/rstudio/>
- Порівняльне джерело про CWEB: Дональд Е. Кнут і Сільвіо Леві, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
