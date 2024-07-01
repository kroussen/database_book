# database_book

<h2>Установка зависимостей</h2>

<code>pip install -r 'requirements.txt''</code>

<h2>Настройка конфигурации</h2>

В файле config.py укажите параметры подключения к вашей базе данных PostgreSQL:

<code>DB_NAME = 'your_database_name' </br>
DB_HOST = 'localhost' </br>
DB_PORT = '5432' </br>
DB_USER = 'your_database_user' </br>
DB_PASS = 'your_database_password'
</code>

<h2>Создание базы данных</h2>

<code>
psql: CREATE DATABASE your_database_name;
</code>
<br></br></br>