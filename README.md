# Тестовое задание

#### Необходимо разработать Python скрипт, который будет выполнять следующие функции:
1. Запрос данных погоды через API:
- Скрипт должен автоматически запрашивать данные погоды в текущий момент в районе Сколтеха через заданные промежутки времени (например, каждые 3 минуты) и добавлять в базу данных. Данные погоды включают: температуру в градусах Цельсия, направление и скорость ветра (в м/с, с указанием направления, например, ЮВ, СВ, С и т.д.), давление воздуха в миллиметрах ртутного столба, осадки (тип и количество в мм).

- Полученные данные должны быть добавлены в базу данных. 

2. Экспорт данных в Excel файл:

- Скрипт должен поддерживать команду из консоли для экспорта данных из БД в файл формата .xlsx.. Экспорт не должен прерывать процесс запроса данных о погоде.

#### Комментарии к выполнению:
- Использование Python 3;
- Для запросов к API можно использовать любой доступный ресурс, например open-meteo;
- Для работы с БД, рекомендуется использовать ORM SQLAlchemy;
- Файл .xlsx должен содержать все запрашиваемы поля и 10 последних полученных данных и загружаться в папку с проектом;
- Функции запроса и экспорта должны работать асинхронно; 
- Код должен быть чистым, с комментариями и соответствовать PEP8.