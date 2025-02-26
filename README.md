# File-sharing
![banner_files.png](banner_files.png)

---

Сайт для хранения различных документов с возможностью их открытия в браузере

Это приложение написано на Django и Django REST Framework.

---

## Установка и настройка
### 1. Клонирование репозитория

```bash 
https://github.com/synapse-global/synapse-file-sharing.git
```
### 2. Переход в каталог проекта

```bash
cd file-sharing
```

### 3. Создание .env и добавление необходимых переменных

```bash
cp .env.example .env
```
### 4. Запуск сборки docker-контейнера

```bash
docker-compose up --build
```

### 5. Создание учетной записи администратора

```bash
docker-compose exec web python manage.py createsuperuser
```

### 6. Скачивание статических файлов
```bash
docker-compose exec web python manage.py collectstatic
```

### 7. Переход в администрацию сайта, где хранятся все файлы
В браузере перейдите по адресу http://127.0.0.1:8025/admin/login/

Введите логин и пароль администратора

---

# Документация проекта

<details>
<summary style="font-weight: bold; font-size: large">
Модели
</summary>

### [Files](core/models.py#L3) - Файлы

- file - хранит в себе файлы
- key - уникальный ключ для открытия файла в браузере
- name - наименование вашего файла
</details>

<details>
<summary style="font-weight: bold; font-size: large">
Администрирование Django
</summary>

### [FilesAdmin](core/admin.py#L9) - Администрирование модели файлов 

Функция file_url генерирует ссылку с помощью ключа файла, по которой можно перейти и посмотреть файл в браузере

```python
def file_url(self, obj):
    url = settings.URL_ADMIN + str(obj.key)
    return mark_safe(f'<a href="{url}" target="_blank"> {url} </a>')
```

URL_ADMIN - хост, по которому будут открываться файлы

- ```readonly_fields``` - нередактируемые поля
- ```fields``` - поля, отображаемые в объекте администрировании django данной модели
- ```search_fields``` - поля, по которым может осуществляться поиск файлов
- ```list_display``` - поля, отображаемые на странице модели администрировании django

</details>


<details>
<summary style="font-weight: bold; font-size: large">
Представления
</summary>

### [get_file](core/views.py#L7) - Открытие файла в браузере
Данная функция позволяет открывать файлы внутри браузера
</details>
