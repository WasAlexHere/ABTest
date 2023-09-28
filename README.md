# ABTest

### Запуск сервиса:
1. Скачать Docker (Docker Desktop)
2. Из каталога *ABTest* вызвать команду
    > docker build -t abtest .
3. Убедиться, что образ собрался. Вызвать команду:
    > docker images
4. Получить id докер образа и запустить его с помощью команды:
    > docker run -p 8080:8080 <id докер образа>

### Запуск тестов:
- Установка всех зависимостей, вызвать команду:
    > pip install -r requirements.txt
- Запуск авто тестов:
    > pytest tests


### Тестовая документация:
В проекте есть два документа: **CHEСKLIST.md** и **BUGS.md**:
- В **СHEСKLIST.md** содержится лист проверок сервиса, по которым были написаны авто тесты;
- В **BUGS.md** содержатся найденные баги в ходе тестирования сервиса.