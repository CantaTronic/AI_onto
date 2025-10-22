# How to synchronize

## 1. Клонируем репозиторий:

```
git clone git@github.com:CantaTronic/Filtering_AI_onto.git
cd repo
```

## 2. Создаём виртуальное окружение:

```
python3.12 -m venv env
source env/bin/activate
```

## 3. Устанавливаем зависимости:
```
pip install -r requirements.txt
```

## 4. Регистрируем Jupyter kernel с тем же именем:
```
python -m ipykernel install --user --name=nlp_env --display-name "Python (nlp_env)"
```

## 4.a. Проверяем:
```
jupyter kernelspec list
```

Должен появиться kernel nlp_env.

## 5. Работаем))
