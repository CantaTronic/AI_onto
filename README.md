# AI_onto — Setup and Usage

Этот README описывает, как настроить окружения для **локальной разработки** и **продакшена**.

### 0. Клонировать репозиторий

```
git clone git@github.com:CantaTronic/AI_onto.git
cd AI_onto
```

---

# Локальная разработка (Local)

### 1. Создаём виртуальное окружение
```
python3.12 -m venv env_local
source env_local/bin/activate
```

### 2. Устанавливаем зависимости
`requirements_local.in` содержит минимальный набор библиотек для тестирования на небольших CSV и локальных данных (`pandas, numpy, matplotlib, scraping`).

Установить torch без CUDA:
```
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

```
pip install -r requirements_local.in
```

### 3. Регистрируем Jupyter kernel
```
python -m ipykernel install --user --name=nlp_local --display-name "Python (nlp_local)"
```

### 4. Проверка
```
jupyter kernelspec list
```

Должно появиться ядро `nlp_local`.

### 5. Использование

- Запускаем `Jupyter Notebook / Lab`.
- Выбираем kernel Python `(nlp_local)` для работы с тестовыми данными и быстрых экспериментов.
- Можно работать без GPU, Qdrant и Mongo, только на CSV.
- Внутри ноутбука устанавливаем `ENV = "local"` в первой ячейке с кодом.

### 6. По окончании работы

```
deactivate
```

---

# Продакшн (Production)

### 1. Создаём виртуальное окружение
```
python3 -m venv env_prod
source env_prod/bin/activate
```

### 2. Устанавливаем зависимости
```
pip-compile requirements_prod.in
pip install -r requirements_prod.txt
```
`requirements_prod.txt` содержит полный набор библиотек для продакшн пайплайна: NLP, LLM, Qdrant, Mongo, GPU, scraping.

### 3. Регистрируем Jupyter kernel
```
python -m ipykernel install --user --name=nlp_prod --display-name "Python (nlp_prod)"
```

### 4. Проверка
```
jupyter kernelspec list
```
Должно появиться ядро `nlp_prod`.

### 5. Использование

- Запускаем `Jupyter Notebook / Lab`.
- Выбираем kernel Python `(nlp_prod)` для работы с большими данными, запуском LLM, Qdrant и Mongo.
- Внутри ноутбука устанавливаем `ENV = "prod"` в первой ячейке с кодом.
- Можно запускать полноценные скрипты и ноутбуки пайплайна с реальными данными.


### 6. По окончании работы
Сохраняем актуальные зависимости

```
pip freeze > requirements_prod.txt
deactivate
```
Файл `requirements_prod.txt` теперь зафиксирован с актуальными версиями всех библиотек.
