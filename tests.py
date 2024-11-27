import os
from library import Library

TEST_DATA_FILE = "test_library.json"

def setup_library():
    """Создает экземпляр библиотеки с тестовым файлом данных"""
    library = Library()
    library.DATA_FILE = TEST_DATA_FILE
    return library

def cleanup():
    """Удаляет тестовый файл данных."""
    if os.path.exists(TEST_DATA_FILE):
        os.remove(TEST_DATA_FILE)

def test_add_book():
    print("Тест: Добавление книги")
    library = setup_library()
    library.add_book("Test Book", "Test Author", 2023)

    assert len(library.books) == 1, "Ошибка: Количество книг не соответствует"
    assert library.books[0].title == "Test Book", "Ошибка: Название книги не совпадает"
    assert library.books[0].author == "Test Author", "Ошибка: Автор книги не совпадает"
    assert library.books[0].year == 2023, "Ошибка: Год издания книги не совпадает"

    print("Пройдено")
    cleanup()

def test_delete_book():
    print("Тест: Удаление книги")
    library = setup_library()
    library.add_book("Book to Delete", "Author", 2022)
    book_id = library.books[0].id

    library.delete_book(book_id)

    assert len(library.books) == 0, "Ошибка: Книга не была удалена"
    print("Пройдено")
    cleanup()

def test_search_books():
    print("Тест: Поиск книги")
    library = setup_library()
    library.add_book("Unique Title", "Author", 2022)

    results = [book for book in library.books if book.title == "Unique Title"]
    assert len(results) == 1, "Ошибка: Поиск не нашел книгу"
    assert results[0].title == "Unique Title", "Ошибка: Найдена неправильная книга"
    print("Пройдено")
    cleanup()

def test_update_status():
    print("Тест: Обновление статуса книги")
    library = setup_library()
    library.add_book("Book with Status", "Author", 2022)
    book_id = library.books[0].id

    library.update_status(book_id, "выдана")
    assert library.books[0].status == "выдана", "Ошибка: Статус книги не обновился"

    print("Пройдено")
    cleanup()

def test_save_and_load_books():
    print("Тест: Сохранение и загрузка книг")
    library = setup_library()
    library.add_book("Saved Book", "Author", 2022)

    # Сохраняем книги и загружаем их заново
    library.save_books()
    new_library = setup_library()
    new_library.books = new_library.load_books()

    assert len(new_library.books) == 1, "Ошибка: Книги не загрузились"
    assert new_library.books[0].title == "Saved Book", "Ошибка: Данные книги повреждены при загрузке"
    print("Пройдено")
    cleanup()

def test_display_books():
    print("Тест: Отображение книг")
    library = setup_library()
    library.add_book("Displayed Book", "Author", 2022)

    library.display_books() 
    print("Пройдено (проверьте вывод в консоли)")
    cleanup()

def run_tests():
    test_add_book()
    test_delete_book()
    test_search_books()
    test_update_status()
    test_save_and_load_books()
    test_display_books()

if __name__ == "__main__":
    run_tests()
