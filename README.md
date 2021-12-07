Запуск докер контейнера
- docker build -t python_test .
- docker run --rm -p 5000:5000 --name python_test python_test:latest

Результатом будет json объект с результатами тестов