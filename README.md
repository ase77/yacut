<a id="anchor"></a>
# YaCut
## Описание:
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Используемые технологии:
Python, FLask, SQLAlchemy, SQLite

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Применить миграции:

```
flask db upgrade
```

Запустить проект:

```
flask run
```

Проект будет доступен по адресу:

```
http://127.0.0.1:5000/
```

### Автор проекта:

Моторин А.В.

[__В начало__](#anchor) :point_up:
