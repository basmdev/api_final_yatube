# API для Yatube

## Описание

API для Yatube.

## Функциональность

- Возможность подиски и отписки для авторизованных пользователей;
- Возможность создавать, удалять и изменять посты для авторизованных пользователей;
- Возможность просмотра групп;
- Возможность добавления, изменения и удаления комментариев.

## Инструкция по установке

1. Клонируйте репозиторий:

   ```python
   git clone https://github.com/MAGFRG/api_final_yatube.git
   ```

2. Перейдите в папку проекта:

   ```python
   cd api_final_yatube/
   ```

3. Установите виртуальное окружение для проекта и активируйте его:

   ```python
   python -m venv venv
   ```
   ```python
   source venv/Scripts/activate
   ```

4. Установите зависимости:

   ```python
   pip install -r requirements.txt
   ```

5. Выполните миграции:

   ```python
   python3 manage.py migrate
   ```

6. Запустите проект:

   ```
   python manage.py runserver
   ```

## Примеры API-запросов

#### Получение токена

Отправьте POST-запрос на адрес `api/v1/jwt/create/` и передайте в `data`:

- Пример запроса:

   ```json
    {
      "username": "string",
      "password": "string"
    }
   ```

#### Создание поста

Отправьте POST-запрос на адрес `api/v1/posts/` и передайте обязательное поле `text`:

- Пример запроса:

   ```json
   {
     "text": "string"
   }
   ```

- Пример ответа:

   ```json
   {
     "id": 2,
     "author": "Admin",
     "text": "string",
     "pub_date": "2023-04-28T12:00:12.031054Z",
     "image": null,
     "group": null
   }
   ```

#### Комментирование поста пользователя

Отправьте POST-запрос на адрес `api/v1/posts/{post_id}/comments/` и передайте обязательные поля `post` и `text`:

- Пример запроса:

   ```json
   {
     "post": 1,
     "text": "string"
   }
   ```

- Пример ответа:

   ```json
   {
     "id": 1,
     "author": "Admin",
     "text": "string",
     "created": "2023-04-28T12:05:13.143865Z",
     "post": 1
   }
   ```
