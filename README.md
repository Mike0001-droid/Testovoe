# Консольное приложение для управления библиотекой книг
Приложение позволяет добавлять, удалять, искать и отображать книги. 

## Класс Book
Класс Book() представляет сущность "Книга", имеет конструктор для создания экземпляров,
а также метод to_dict, который преобразует объект книги в словарь

| Название | Описание                                            |
|----------|-----------------------------------------------------|
| id	   | Уникальный идентификатор, генерируется автоматически|
| title    | Название книги                                      |
| author   | Автор книги                                         |
| year	   | Год издания                                         |
| status   | Статус книги: в наличии/выдана                      |

## Класс Library
Класс Library() представляет сущность "Библиотека", имеет атрибут DATA_FILE
для хранения названия файла и следующий набор методов:

| Название      | Описание                                                   |
|---------------|------------------------------------------------------------|
| init	        | Конструктор класса, использует метод load_books()          |
| load_books    | Создает экземпляры классы Book(), извлеченные из JSON файла|
| save_books    | Сохраняет измененное состояние книги                       |
| add_book	    | Создает экземпляр класса Book(), сохраняет в JSON файл     |
| delete_book   | Удаляет книгу                                              |
| search_books  | Ищет книгу среди всего списка, используя поиск по одному из|
|               | данных полей: title/author/year и значению этого поля      |
| display_books | Выводит на консоль книги, которые есть в наличии           |
| update_status | Обновляет статус у книги, сохраняет в JSON файл            |
