# Общие сведения

API имеет 3 эндпоинта:\
\
для выполнения первых двух запросов необходимо указать bearer токен в заголовке
1) `/get_item/{id}` - для получения информации об объявлении.

2) `/create_item/` - для создания записи в бд.\
Тело запроса имеет вид: 
`{
  "title": "string",
  "id": 0,
  "author": "string",
  "views": 0,
  "position": 0
}`

3) `/login` - для получения токена, необходимого для авторизации.

## Авторизация
Авторизация выполнена через JWT содержащий ip адрес клиента, который сравнивается с вайтлистом. Вайтлист определен в файле `config.py` переменной `allowed_hosts`


