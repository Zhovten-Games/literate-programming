# Companion

Quarto — це система executable documents / computational publishing. У цьому companion `primes.qmd` рендериться у `primes.html`: Quarto виконує вбудований Python-код, а потім складає HTML-документ через rendering pipeline.

## Модель джерела і компактний pipeline

Quarto-джерело:

- `primes.qmd`

Гілка відрендереної публікації:

- `primes.qmd -> Quarto render -> Python/Jupyter kernel -> Pandoc -> primes.html`

`primes.qmd` — канонічне Quarto-джерело. `primes.html` — згенерований артефакт рендера. Результатом є публікаційний документ, тоді як `01-cweb`, `02-noweb-like` і `03-org-babel` генерують або складають машинно-орієнтований вихідний текст перед компіляцією.

## Що таке Quarto / .qmd / executable documents

- Quarto: система executable documents / computational publishing
- `.qmd`: Markdown + YAML-метадані + виконувані кодові блоки
- Python/Jupyter kernel: виконує вбудований Python-блок
- Pandoc/render pipeline: складає `primes.html`

## Команди гілки рендера

Із цього каталогу:

```bash
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Очікувані маркери виводу:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `      6571      6997      7499      7919`

Smoke-check шукає маркери у відрендереному `primes.html`, а не у звичайному текстовому файлі виводу.

## Маркери / синтаксис документа

- YAML front matter між рядками `---` задає метадані: заголовок, формат, параметри виконання.
- Markdown-проза формує читабельний наративний шар.
- Fenced code block із `{python}` відкриває виконуваний Python-блок.
- Quarto виконує кодовий блок під час рендера.
- Вивід вбудовується у підсумковий HTML.
- У цьому companion код друкує посторінкову таблицю простих чисел.

## Чому самих коментарів недостатньо?

Звичайні коментарі:

- пояснення прикріплено до коду.

Quarto:

- обчислення вбудовано у публікований документ.

CWEB/noweb/Org Babel зберігають сильнішу модель source generation, де машинний вихідний текст видобувається або складається окремо. У Quarto центром є відрендерена публікація, що поєднує текст, код і обчислений вивід.

## Місце у наборі

`04-quarto` показує гілку executable documents / computational publishing. Він корисний, коли головною метою є відрендерений документ, що поєднує текст, код і обчислений вивід. Строгу WEB-style генерацію вихідного тексту представляють інші варіанти: мінімальний C++ literate source-generation маршрут — `02-noweb-like`, історична tangle/weave-модель — `01-cweb`, середовище Emacs/Org-mode — `03-org-babel`.

Повне порівняння всіх companion-варіантів наведено в кореневому README і порівняльній таблиці.

## Встановлення: основний WSL/Linux-маршрут

Основним перевіреним маршрутом для цього companion був WSL/Linux.

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Quarto слід установлювати з офіційної сторінки завантаження через актуальний Ubuntu/Debian `.deb`-пакет:

```bash
cd /tmp
wget https://github.com/quarto-dev/quarto-cli/releases/download/vX.Y.Z/quarto-X.Y.Z-linux-amd64.deb
sudo apt install ./quarto-X.Y.Z-linux-amd64.deb
quarto --version
```

Замініть `X.Y.Z` на актуальну версію з офіційної сторінки завантаження Quarto.

## Примітки щодо Python/Jupyter-середовища

Перевірена конфігурація використовувала одне спільне віртуальне середовище у корені `Literate-Companion-Implementations/.venv`.

Із кореня `Literate-Companion-Implementations`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter
```

Перевірка:

```bash
which python
python -m jupyter --version
```

Очікувана форма `which python`:

- `.../Literate-Companion-Implementations/.venv/bin/python`

Спільний `.venv` використовується для `examples/en/04-quarto`, `examples/uk/04-quarto` і `examples/ru/04-quarto`, усуваючи потребу в окремому середовищі для кожного мовного каталогу.

Перевірка трьох мовних гілок:

```bash
cd examples/en/04-quarto
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html

cd ../../uk/04-quarto
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html

cd ../../ru/04-quarto
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Запускайте `quarto render` з активованого `.venv`, щоб Quarto бачив установлені в ньому пакети Jupyter/Python.

## Примітки для Windows

Windows-маршрут можливий, проте основним перевіреним маршрутом для цього companion був WSL/Linux.

- Quarto має Windows-інсталятор.
- Нативний рендер у Windows може працювати, якщо Quarto і Python/Jupyter встановлені та доступні у `PATH`.

Перевірки:

```powershell
where.exe quarto
quarto --version
where.exe python
python --version
python -m jupyter --version
```

Якщо утиліти не знайдено:

- додайте Quarto і Python до `PATH`;
- встановіть Jupyter в активне Python-середовище.

Відтворюваним перевіреним маршрутом для цього companion залишається WSL/Linux із кореневим `.venv`.

## Troubleshooting / коротка діагностика

- Якщо Quarto не виконує Python-блоки, переконайтеся, що `.venv` активовано і `jupyter` встановлено.
- Якщо `quarto render primes.qmd` виконано успішно, ключовим маркером є `Output created: primes.html`.
- Якщо `grep` нічого не знайшов, перевірте `primes.html` і переконайтеся, що вивід коду вбудовано у документ.
- Якщо заважають відмінності line endings між Windows і WSL, використовуйте стабільні LF-закінчення у `.qmd`.

## Файли, що з’являються

- `COMPANION.md`
  Документація цього companion-прикладу. Фіксується в репозиторії.
- `primes.qmd`
  Канонічне Quarto-джерело. Фіксується в репозиторії.
- `primes.html`
  Відрендерений HTML-вивід. Генерується та ігнорується.
- `primes.quarto_ipynb`
  Можливий проміжний артефакт виконання Quarto. Генерується та ігнорується, якщо з’являється.
- `.quarto/`
  Можливий локальний каталог кешу/стану Quarto. Генерується та ігнорується.
- `*_files/`
  Можливий каталог допоміжних файлів Quarto. Генерується та ігнорується.
- `.venv/`
  Локальне спільне Python-середовище в корені проєкту. Генерується та ігнорується.

## Подяки і посилання

- Офіційний сайт і документація Quarto: <https://quarto.org/>
- Сторінка завантаження Quarto: <https://quarto.org/docs/download/>
- Quarto Python computations: <https://quarto.org/docs/computations/python.html>
- Порівняльне джерело про CWEB: Дональд Е. Кнут і Сільвіо Леві, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
