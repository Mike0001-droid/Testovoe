import json

class Book:
    def __init__(
        self, 
        id: int, 
        title: str, 
        author: str, 
        year: str, 
        status="в наличии"
    ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


class Library:
    DATA_FILE = "library.json"

    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        with open(self.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4, ensure_ascii=False)

    def add_book(self, title: str, author: str, year: str):
        new_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' успешно добавлена с ID {new_id}")

    def delete_book(self, book_id: int):
        book = next((book for book in self.books if book.id == book_id), None)
        if not book:
            print("Книга с таким ID не найдена")
            return
        self.books.remove(book)
        self.save_books()
        print(f"Книга с ID {book_id} успешно удалена")

    def search_books(self, query: str, field: str):
        if field not in ["title", "author", "year"]:
            print("Некорректное поле для поиска")
            return
        results = [book for book in self.books if str(getattr(book, field)).lower() == str(query).lower()]
        if results:
            for book in results:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
        else:
            print("Книги не найдены")

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def update_status(self, book_id: int, new_status: str):
        if new_status not in ["в наличии", "выдана"]:
            print("Некорректный статус. Выберите 'в наличии' или 'выдана'")
            return
        book = next((book for book in self.books if book.id == book_id), None)
        if not book:
            print("Книга с таким ID не найдена")
            return
        book.status = new_status
        self.save_books()
        print(f"Статус книги с ID {book_id} успешно обновлен на '{new_status}'")


class LibraryApp:
    def __init__(self):
        self.library = Library()

    def start(self):
        while True:
            print("\nУправление библиотекой книг")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Искать книгу")
            print("4. Отобразить все книги")
            print("5. Изменить статус книги")
            print("6. Выход")
            
            choice = input("Выберите действие: ")
            
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год издания книги: ")
                self.library.add_book(title, author, year)

            elif choice == "2":
                try:
                    book_id = int(input("Введите ID книги для удаления: "))
                    self.library.delete_book(book_id)
                except ValueError:
                    print("Некорректный ID")

            elif choice == "3":
                field = input("Искать по (title/author/year): ").strip().lower()
                query = input("Введите значение для поиска: ")
                self.library.search_books(query, field)

            elif choice == "4":
                self.library.display_books()

            elif choice == "5":
                try:
                    book_id = int(input("Введите ID книги для изменения статуса: "))
                    new_status = input("Введите новый статус (в наличии/выдана): ")
                    self.library.update_status(book_id, new_status)
                except ValueError:
                    print("Некорректный ID")
                    
            elif choice == "6":
                print("Выход из программы")
                break
            else:
                print("Некорректный выбор. Пожалуйста, выберите пункт из меню")

if __name__ == '__main__':
    app = LibraryApp()
    app.start()