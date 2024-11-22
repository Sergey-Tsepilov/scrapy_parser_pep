# Асинхронный парсер PEP

## Технологии:

- Python 3.9.13
- Scrapy 2.5.1

## Установка (Windows):

1. Клонирование репозитория

```
git clone https://github.com/Sergey-Tsepilov/scrapy_parser_pep.git
```

2. Переход в директорию scrapy_parser_pep

```
cd scrapy_parser_pep
```

3. Создание виртуального окружения

```
python -m venv venv
```

4. Активация виртуального окружения

```
source venv/Scripts/activate
```

5. Обновите pip

```
python -m pip install --upgrade pip
```

6. Установка зависимостей

```
pip install -r requirements.txt
```

7. Для запуска парсинга PEP через Scrapy выполните команду:

```
scrapy crawl pep
```

8. Деактивация виртуального окружения

```
deactivate
```
