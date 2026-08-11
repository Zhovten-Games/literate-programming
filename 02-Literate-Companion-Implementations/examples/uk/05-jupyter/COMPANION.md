# Companion

## 1. Короткий вступ

Jupyter показує notebook-style literate computing. Його інтерактивний notebook workflow поєднує текст, кодові комірки, стан виконання і вивід комірок в одному `.ipynb`-документі. За своєю моделлю він відрізняється від строгого Knuth-style WEB і tangle/weave workflow.

У цьому companion `primes.ipynb` є notebook-документом, а `primes.py` — script companion для простої command-line sanity-check перевірки.

## 2. Модель джерел і компактний конвеєр

Notebook-джерело:

- `primes.ipynb`

Гілка виконання notebook:

- `primes.ipynb -> Jupyter kernel / nbconvert --execute -> primes.executed.ipynb`

Script sanity-гілка:

- `primes.py -> python3 -> output.txt`

Примітки:

- `primes.ipynb` — JSON notebook-документ.
- `primes.py` додано для швидкої перевірки алгоритму на рівні скрипта.
- `primes.executed.ipynb` генерується через `nbconvert --execute` й ігнорується системою контролю версій.
- Jupyter орієнтований на інтерактивний notebook, тоді як `01-cweb` / `02-noweb-like` / `03-org-babel` генерують канонічний машинно-орієнтований вихідний файл.
- Порівняно з `04-quarto`, основною моделлю авторингу є інтерактивний notebook, а не конвеєр відрендереної публікації.

## 3. Що таке Jupyter / .ipynb / kernels / notebook cells

- Jupyter: інтерактивна обчислювальна notebook-екосистема
- `.ipynb`: JSON-документ із комірками, metadata, execution count і outputs
- Kernel: runtime-процес, що виконує код і зберігає стан
- JupyterLab / Notebook: браузерний GUI для роботи з notebooks

GUI доступний, а відтворювана companion-перевірка використовує command-line виконання через `nbconvert`.

## 4. Команди script sanity-check

Із цього каталогу:

```bash
python3 primes.py > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

Очікувані маркери виводу:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `      6571      6997      7499      7919`

Це підтверджує коректність алгоритму і виводу через звичайний шлях Python-скрипта. Виконання notebook перевіряється окремо.

## 5. Команди виконання notebook

Із цього каталогу:

```bash
jupyter nbconvert --to notebook --execute primes.ipynb --output primes.executed.ipynb
grep "Page 1" primes.executed.ipynb && grep "Page 5" primes.executed.ipynb && grep "7919" primes.executed.ipynb
```

Очікувані маркери у виконаному notebook:

- `"The First 1000 Prime Numbers --- Page 1\n"`
- `"The First 1000 Prime Numbers --- Page 5\n"`
- `"      6571      6997      7499      7919\n"`

Ця команда виконує notebook у headless-режимі й записує `primes.executed.ipynb` із виводом виконаних комірок.

Українська гілка пройшла структурну валідацію і script smoke-check; перед публікацією слід виконати документовану команду `nbconvert --execute` та зафіксувати notebook-execution evidence. Наявна ручна перевірка підтверджує виконання скрипта і notebook в `examples/en/05-jupyter` та `examples/ru/05-jupyter`.

## 6. Примітки про GUI notebook

Із кореня `Literate-Companion-Implementations` з активованою `.venv`:

```bash
jupyter lab
```

або:

```bash
jupyter notebook
```

- JupyterLab — більш IDE-like інтерфейс: file browser, tabs, notebooks, text editor, terminal тощо.
- Jupyter Notebook — класичний notebook-інтерфейс.
- У WSL/Linux сервер зазвичай виводить локальний URL із токеном; його можна відкрити вручну у браузері Windows.
- GUI-використання для цього companion є необов’язковим.
- Відтворюваною перевіркою залишається `nbconvert --execute`.

## 7. Чому самих коментарів недостатньо?

Звичайні коментарі:

пояснення прикріплено до коду.

Jupyter:

обчислення і пояснення розкладено як інтерактивний notebook-зошит.

Визначальна відмінність: Jupyter орієнтований на interactive literate computing, а не на видобування вихідного коду для компілятора.

Hidden state: комірки можна виконувати поза порядком, тому видимий порядок notebook може не збігатися з фактичною execution history. Це основний ризик відтворюваності.

## 8. Місце у наборі

`05-jupyter` показує notebook-style literate computing. Він корисний для інтерактивного дослідження, навчання, прототипування і видимого виводу комірок, водночас несучи ризики hidden state і нелінійного порядку виконання. Строгу WEB-style генерацію вихідного тексту представляють інші варіанти. Повне порівняння всіх companion-варіантів наведено в кореневому README.

## 9. Встановлення: спільна коренева `.venv`

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

Та сама коренева `.venv` повторно використовується для `04-quarto` і `05-jupyter`.

Перевірка трьох мовних гілок:

```bash
cd examples/en/05-jupyter
python3 primes.py > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
jupyter nbconvert --to notebook --execute primes.ipynb --output primes.executed.ipynb
grep "Page 1" primes.executed.ipynb && grep "Page 5" primes.executed.ipynb && grep "7919" primes.executed.ipynb

cd ../../uk/05-jupyter
python3 primes.py > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
jupyter nbconvert --to notebook --execute primes.ipynb --output primes.executed.ipynb
grep "Page 1" primes.executed.ipynb && grep "Page 5" primes.executed.ipynb && grep "7919" primes.executed.ipynb

cd ../../ru/05-jupyter
python3 primes.py > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
jupyter nbconvert --to notebook --execute primes.ipynb --output primes.executed.ipynb
grep "Page 1" primes.executed.ipynb && grep "Page 5" primes.executed.ipynb && grep "7919" primes.executed.ipynb
```

## 10. Примітки для Windows

Windows-маршрут можливий, проте основним протестованим маршрутом для цього companion був WSL/Linux.

- Jupyter може запускатися нативно у Windows за наявності встановленого Python/Jupyter.
- Інструменти мають бути доступними у PATH.

Перевірка:

```powershell
where.exe python
python --version
python -m jupyter --version
```

Якщо не знайдено:

- установити Python;
- додати Python/Scripts до PATH;
- установити Jupyter в активне середовище.

Відтворюваним протестованим маршрутом для цього companion є WSL/Linux зі спільною кореневою `.venv`.

## 11. Діагностика і поширені проблеми

A. MissingIDFieldWarning

Під час ручного тесту виникало попередження:

```text
MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions.
```

Воно означає, що у notebook-комірках відсутні стабільні `id`, очікувані новими версіями `nbformat`. Після додавання `id` до всіх комірок попередження має зникнути.

B. Hidden state

Якщо notebook працює інтерактивно, але завершується помилкою в `nbconvert --execute`, причиною може бути hidden state або out-of-order execution. Відтворюваною перевіркою є чисте top-to-bottom виконання через `nbconvert`.

C. Kernel/Jupyter not found

Якщо `nbconvert` не запускається:

- активувати `.venv`;
- переконатися, що `jupyter` встановлено;
- виконати `python -m jupyter --version`.

D. Generated executed notebook

`primes.executed.ipynb` є generated output і не фіксується в репозиторії.

## 12. Згенеровані файли

- `COMPANION.md`  
  Документація цього companion-прикладу. Фіксується як джерело.
- `primes.ipynb`  
  Канонічний Jupyter notebook source. Фіксується як джерело.
- `primes.py`  
  Script companion для швидких command-line sanity-check перевірок. Фіксується як джерело.
- `output.txt`  
  Локально збережений вивід скрипта. Генерується та ігнорується.
- `primes.executed.ipynb`  
  Виконаний notebook, згенерований через `nbconvert --execute`. Генерується та ігнорується.
- `.ipynb_checkpoints/`  
  Локальний каталог checkpoint-файлів Jupyter. Генерується та ігнорується.
- `.venv/`  
  Спільна Python virtual environment, якщо її створено у `Literate-Companion-Implementations/.venv`. Генерується та ігнорується.

## 13. Подяки і посилання

- Документація Project Jupyter: [https://docs.jupyter.org/](https://docs.jupyter.org/)
- Документація JupyterLab: [https://jupyterlab.readthedocs.io/en/stable/](https://jupyterlab.readthedocs.io/en/stable/)
- Документація Jupyter Notebook: [https://jupyter-notebook.readthedocs.io/en/stable/notebook.html](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)
- Документація nbconvert: [https://nbconvert.readthedocs.io/](https://nbconvert.readthedocs.io/)
- nbconvert: виконання notebooks: [https://nbconvert.readthedocs.io/en/latest/execute_api.html](https://nbconvert.readthedocs.io/en/latest/execute_api.html)
- Порівняльне джерело про CWEB: Дональд Е. Кнут і Сільвіо Леві, “The CWEB System of Structured Documentation”: [https://www-cs-faculty.stanford.edu/~knuth/cweb.html](https://www-cs-faculty.stanford.edu/~knuth/cweb.html)
