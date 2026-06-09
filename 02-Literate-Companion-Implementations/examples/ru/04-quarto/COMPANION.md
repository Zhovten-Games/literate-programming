# Companion

Quarto — это система executable documents / computational publishing. В этом companion `primes.qmd` рендерится в `primes.html`: Quarto выполняет встроенный Python-код, а затем собирает HTML-документ через рендеринг-пайплайн.

## Модель источника и компактный pipeline

Quarto-источник:

- `primes.qmd`

Ветка срендеренной публикации:

- `primes.qmd -> Quarto render -> Python/Jupyter kernel -> Pandoc -> primes.html`

`primes.qmd` — канонический Quarto-источник. `primes.html` — сгенерированный артефакт рендера. Здесь результат — публикационный документ, а не генерация канонического программного исходника. Это отличается от `01-cweb`, `02-noweb-like` и `03-org-babel`, где перед компиляцией генерируется или собирается машинно-ориентированный исходник.

## Что такое Quarto / .qmd / executable documents

- Quarto: система executable documents / computational publishing
- `.qmd`: Markdown + YAML-метаданные + исполняемые кодовые блоки
- Python/Jupyter kernel: выполняет встроенный Python-блок
- Pandoc/render pipeline: собирает `primes.html`

## Команды ветки рендера

Из этого каталога:

```bash
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Ожидаемые маркеры вывода:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `      6571      6997      7499      7919`

Smoke-check ищет в срендеренном `primes.html`, а не в обычном текстовом файле вывода.

## Маркеры / синтаксис документа

- YAML front matter между строками `---` задаёт метаданные: заголовок, формат, опции выполнения.
- Markdown-проза формирует читаемый нарративный слой.
- Fenced code block с `{python}` открывает исполняемый Python-блок.
- Quarto выполняет кодовый блок во время рендера.
- Вывод встраивается в итоговый HTML.
- В этом companion код печатает постраничную таблицу простых чисел.

## Почему не просто комментарии?

Обычные комментарии:

- пояснение прикреплено к коду.

Quarto:

- вычисление встроено в публикуемый документ.

CWEB/noweb/Org Babel сохраняют более сильную модель source generation, где машинный исходник извлекается или собирается отдельно. В Quarto центр тяжести — срендеренная публикация, где вместе публикуются текст, код и вычисленный вывод.

## Место в наборе

`04-quarto` показывает ветвь executable documents / computational publishing. Он полезен, когда главная цель — срендеренный документ, объединяющий текст, код и вычисленный вывод. Это не лучший пример строгой WEB-style генерации исходника. Для минимального C++ literate source-generation маршрута см. `02-noweb-like`; для исторической tangle/weave-модели — `01-cweb`; для Emacs/Org-mode среды — `03-org-babel`.

Полное сравнение всех companion-вариантов см. в корневом README / сравнительной таблице.

## Установка: основной WSL/Linux маршрут

Для этого companion основным проверенным маршрутом был WSL/Linux.

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Quarto устанавливайте с официальной страницы загрузки через актуальный Ubuntu/Debian `.deb`-пакет:

```bash
cd /tmp
wget https://github.com/quarto-dev/quarto-cli/releases/download/vX.Y.Z/quarto-X.Y.Z-linux-amd64.deb
sudo apt install ./quarto-X.Y.Z-linux-amd64.deb
quarto --version
```

Замените `X.Y.Z` на актуальную версию с официальной страницы загрузки Quarto.

## Заметки по Python/Jupyter окружению

Проверенная конфигурация использовала одно общее виртуальное окружение в корне `Literate-Companion-Implementations/.venv`.

Из корня `Literate-Companion-Implementations`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter
```

Проверка:

```bash
which python
python -m jupyter --version
```

Ожидаемая форма `which python`:

- `.../Literate-Companion-Implementations/.venv/bin/python`

Общий `.venv` используется для `examples/en/04-quarto` и `examples/ru/04-quarto` и избавляет от отдельных окружений в каждом языковом каталоге.

Проверка обеих языковых веток:

```bash
cd examples/ru/04-quarto
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html

cd ../../en/04-quarto
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Запускайте `quarto render` из активированного `.venv`, чтобы Quarto видел установленные в нём пакеты Jupyter/Python.

## Заметки для Windows

Windows-маршрут возможен, но не был основным проверенным маршрутом для этого companion.

- У Quarto есть Windows-установщик.
- Нативный рендер в Windows может работать, если Quarto и Python/Jupyter установлены и доступны в `PATH`.

Проверки:

```powershell
where.exe quarto
quarto --version
where.exe python
python --version
python -m jupyter --version
```

Если утилиты не найдены:

- добавьте Quarto и Python в `PATH`;
- установите Jupyter в активное Python-окружение.

Для этого companion воспроизводимым проверенным маршрутом остаётся WSL/Linux с корневым `.venv`.

## Troubleshooting / короткая диагностика

- Если Quarto не выполняет Python-блоки, убедитесь, что `.venv` активирован и установлен `jupyter`.
- Если `quarto render primes.qmd` отработал успешно, ключевой маркер: `Output created: primes.html`.
- Если `grep` ничего не нашёл, проверьте `primes.html` и убедитесь, что вывод кода встроен в документ.
- Если мешают различия line endings между Windows и WSL, держите `.qmd` с устойчивыми LF-окончаниями.

## Какие файлы появляются

- `COMPANION.md`
  Документация для этого companion-примера. Коммитится.
- `primes.qmd`
  Канонический Quarto-источник. Коммитится.
- `primes.html`
  Срендеренный HTML-вывод. Генерируется и игнорируется.
- `primes.quarto_ipynb`
  Возможный промежуточный артефакт выполнения Quarto. Генерируется и игнорируется (если появляется).
- `.quarto/`
  Возможный локальный каталог кэша/состояния Quarto. Генерируется и игнорируется.
- `*_files/`
  Возможный каталог вспомогательных файлов Quarto. Генерируется и игнорируется.
- `.venv/`
  Локальное общее Python-окружение в корне проекта. Генерируется и игнорируется.

## Благодарности и ссылки

- Официальный сайт и документация Quarto: <https://quarto.org/>
- Страница загрузки Quarto: <https://quarto.org/docs/download/>
- Quarto Python computations: <https://quarto.org/docs/computations/python.html>
- Сравнительный источник по CWEB: Дональд Э. Кнут и Сильвио Леви, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
