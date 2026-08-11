# Companion

## 1. Краткое введение

R Markdown демонстрирует workflow воспроизводимого отчёта (reproducible-report workflow). В этом companion `primes.Rmd` — канонический документ-источник; render выполняет R code chunk и создаёт `primes.html`.

Это dynamic-document workflow: проза и исполняемые chunks живут в одном исходном документе. Это не строгий Knuth-style WEB и не канонический tangle/weave-конвейер генерации исходников.

## 2. Модель источника и компактный pipeline

R Markdown-источник:

- `primes.Rmd`

Ветка срендеренного отчёта:

- `primes.Rmd -> rmarkdown::render() -> knitr -> pandoc -> primes.html`

Пояснения:

- `primes.Rmd` содержит Markdown-прозу и исполняемые R chunks.
- `rmarkdown::render()` запускает рендеринг.
- `knitr` выполняет R chunks и подготавливает промежуточное Markdown-представление.
- `pandoc` конвертирует промежуточный документ в HTML.
- `primes.html` — сгенерированный вывод, его не нужно коммитить.
- В отличие от `01-cweb`, `02-noweb-like` и `03-org-babel`, этот companion не генерирует канонический машинно-ориентированный исходный файл.
- В отличие от `05-jupyter`, это не в первую очередь интерактивный notebook, а workflow с рендерингом отчёта.

## 3. Что такое R Markdown / Rmd / knitr / rmarkdown / Pandoc / RStudio

- **R Markdown**: формат документа, объединяющий Markdown-прозу и исполняемые code chunks.
- **`.Rmd`**: R Markdown source file.
- **R**: язык/рантайм, на котором выполняются chunks в этом companion.
- **`knitr`**: движок, который выполняет chunks и вставляет результат в документ.
- **`rmarkdown`**: R package, координирующий render.
- **Pandoc**: слой конвертации документа, используемый для HTML и других форматов.
- **RStudio (Posit)**: опциональная IDE/GUI для R и R Markdown. Полезна, но не требуется для CLI-проверки.

Краткая формула:

- R Markdown: Markdown + исполняемые code chunks
- `.Rmd`: канонический R Markdown source file
- `knitr`: выполнение chunks и вставка результата
- `rmarkdown::render()`: точка входа для render
- Pandoc: слой конвертации документа
- RStudio: опциональная IDE/GUI, не требуется для CLI-проверки

## 4. Команды рендеринга

Из `examples/ru/06-rmarkdown`:

```bash
Rscript -e 'rmarkdown::render("primes.Rmd")'
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Ожидаемые маркеры для smoke-check:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `6571      6997      7499      7919`

Примечание: console output R в HTML может иметь префикс `##` от `knitr`. Это нормально.

Украинская ветка включена в тот же render-маршрут и locale validation; перед публикацией нужно выполнить документированную команду рендера и зафиксировать evidence. Имеющиеся ручные проверки рендера охватывают `examples/en/06-rmarkdown` и `examples/ru/06-rmarkdown`.

Наблюдавшиеся успешные версии при ручном тесте:

- `rmarkdown`: `2.31`
- `rmarkdown::pandoc_version()`: `3.1.3`

Это именно протестированные версии, а не минимально требуемые.

## 5. Почему не просто комментарии?

Обычные комментарии:

- пояснение прикреплено к коду.

R Markdown:

- проза, исполняемые R chunks и срендеренный результат живут вместе в одном report source.

Важное отличие: R Markdown не про извлечение исходника для компилятора как основную цель. Основная цель — генерация воспроизводимого rendered report из документа с исполняемыми chunks.

Короткая формула:

- Обычные комментарии: пояснение прикреплено к коду.
- R Markdown: отчёт содержит объяснение, исполняемые chunks и срендеренный результат.

## 6. Место в наборе

`06-rmarkdown` показывает ветвь reproducible reports в companion-наборе. Он полезен для отчётов, статистических документов и срендеренных вычислительных нарративов, но ближе к публикации документа, чем к канонической WEB-style генерации исходника. Полное сравнение всех companion-вариантов см. в корневом README.

## 7. Установка: локальная корневая `.rlib`

Документируемый маршрут: чистый WSL/Linux-путь с project-local библиотекой пакетов.

Из корня `Literate-Companion-Implementations`:

```bash
sudo apt update
sudo apt install -y r-base r-base-dev pandoc libuv1-dev

mkdir -p .rlib
export R_LIBS_USER="$PWD/.rlib"

Rscript -e '.libPaths()'
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

Проверка:

```bash
Rscript -e '.libPaths()'
Rscript -e 'packageVersion("rmarkdown")'
Rscript -e 'rmarkdown::pandoc_version()'
```

Ожидается, что `.libPaths()` включает:

```text
.../Literate-Companion-Implementations/.rlib
```

Практические замечания:

1. Не запускайте `install.packages("rmarkdown")` напрямую в Bash: это R-синтаксис. Используйте `Rscript -e 'install.packages(...)'`.
2. Не ставьте project packages в системную библиотеку R (`/usr/local/lib/R/site-library` может быть недоступной для записи). Используйте локальную `.rlib`.
3. `R_LIBS_USER` действует только в текущей сессии. В новом терминале выполните:
   ```bash
   cd "/path/to/Literate-Companion-Implementations"
   export R_LIBS_USER="$PWD/.rlib"
   ```
4. Может понадобиться `libuv1-dev`, потому что в цепочке зависимостей CRAN возможно:
   ```text
   fs -> sass -> bslib -> rmarkdown
   ```
5. Для HTML-рендеринга нужен `pandoc`:
   ```bash
   command -v pandoc
   pandoc --version
   Rscript -e 'rmarkdown::pandoc_version()'
   ```
6. Для этого companion достаточно HTML-вывода; LaTeX/TinyTeX не нужен, если позже не добавится PDF.

## 8. Заметки про Windows

Маршрут через Windows возможен, но не является основным протестированным путём для этого companion.

- R можно установить нативно на Windows.
- RStudio — удобная GUI/IDE для R Markdown, но не обязательна для описанного CLI-маршрута.
- Инструменты должны быть доступны в `PATH`.
- Для нативного Windows-маршрута нужны R, пакет `rmarkdown` и Pandoc.

Проверки в PowerShell:

```powershell
where.exe Rscript
Rscript --version
Rscript -e "packageVersion('rmarkdown')"
Rscript -e "rmarkdown::pandoc_version()"
```

Для этого companion воспроизводимо протестированный маршрут — WSL/Linux с локальной корневой `.rlib`.

## 9. Диагностика и частые проблемы

### A. `install.packages` введён в Bash

Проблема:

```bash
install.packages("rmarkdown")
```

Это даёт синтаксические ошибки Bash, потому что `install.packages()` — синтаксис R.

Правильно:

```bash
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

### B. System R library is not writable

Проблема:

```text
'lib = "/usr/local/lib/R/site-library"' is not writable
```

Исправление:

```bash
mkdir -p .rlib
export R_LIBS_USER="$PWD/.rlib"
```

### C. Package not found after reopening terminal

Проблема: `rmarkdown` был установлен, но позже `Rscript -e 'packageVersion("rmarkdown")'` сообщает, что пакет не найден.

Причина: в новой shell-сессии не был экспортирован `R_LIBS_USER`.

Исправление:

```bash
cd "/path/to/Literate-Companion-Implementations"
export R_LIBS_USER="$PWD/.rlib"
Rscript -e '.libPaths()'
Rscript -e 'packageVersion("rmarkdown")'
```

### D. `fs` / `sass` / `bslib` / `rmarkdown` dependency failure

Проблема: установка падает, потому что `fs` не может собраться и сообщает о нехватке libuv.

Исправление:

```bash
sudo apt install -y libuv1-dev
rm -rf .rlib/00LOCK-*
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

### E. Pandoc not found

Исправление:

```bash
sudo apt install -y pandoc
command -v pandoc
pandoc --version
Rscript -e 'rmarkdown::pandoc_version()'
```

### F. Generated HTML

`primes.html` — сгенерированный вывод, его не нужно коммитить.

## 10. Сгенерированные файлы

- `COMPANION.md`  
  Документация для этого companion-примера. Коммитится как исходник.
- `primes.Rmd`  
  Канонический R Markdown-источник. Коммитится как исходник.
- `primes.html`  
  Срендеренный HTML от `rmarkdown::render("primes.Rmd")`. Генерируется и игнорируется.
- `primes.knit.md`  
  Возможный промежуточный Markdown от `knitr`/`rmarkdown` при рендеринге. Генерируется и игнорируется, если появляется.
- `*_files/`  
  Возможная директория ассетов для HTML. Генерируется и игнорируется.
- `.rlib/`  
  Локальная корневая библиотека R-пакетов для этого companion-набора. Генерируется и игнорируется.
- `.Rhistory`, `.RData`, `.Rproj.user/`  
  Локальные R/RStudio-артефакты. Генерируются и игнорируются.

Примечание: `primes.knit.md` — возможный промежуточный артефакт; он может как остаться после render, так и не остаться.

## 11. Благодарности / источники

- R Markdown documentation: <https://rmarkdown.rstudio.com/>
- R Markdown lesson / guide: <https://rmarkdown.rstudio.com/lesson-1.html>
- R Markdown render documentation: <https://rmarkdown.rstudio.com/docs/reference/render.html>
- knitr documentation: <https://yihui.org/knitr/>
- Pandoc: <https://pandoc.org/>
- Posit / RStudio IDE: <https://posit.co/products/open-source/rstudio/>
- Сравнительный источник по CWEB: Дональд Э. Кнут и Сильвио Леви, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
