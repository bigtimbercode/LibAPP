import random

class Book:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.user_name = None

FICTION_BOOK_COUNT = 11

def generate_book_library():
    fiction_books = [
        "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby",
        "Moby-Dick", "War and Peace", "The Catcher in the Rye", "The Hobbit",
        "Brave New World", "The Lord of the Rings", "Crime and Punishment"
    ]

    non_fiction_books = [
        "Sapiens: A Brief History of Humankind", "Educated", "Becoming", "The Immortal Life of Henrietta Lacks",
        "The Diary of a Young Girl", "Thinking, Fast and Slow", "The Power of Habit", "Freakonomics",
        "Guns, Germs, and Steel", "Quiet: The Power of Introverts in a World That Can't Stop Talking"
    ]

    book_library = []
    code = 1

    for title in fiction_books:
        book_library.append(Book(f"#{code:03d}", title))
        code += 1

    for title in non_fiction_books:
        book_library.append(Book(f"#{code:03d}", title))
        code += 1

    return book_library

def display_books(book_library):
    print("Books available in the library:")
    for book in book_library:
        if not book.user_name:
            print(f"{book.code}: {book.title}")

def display_checked_out_books(book_library):
    print("Checked out books:")
    for book in book_library:
        if book.user_name:
            print(f"{book.code}: {book.title} (Checked out by {book.user_name})")

def checkout_books(book_library, book_count):
    books_to_checkout = []
    for _ in range(book_count):
        display_books(book_library)
        choice = input("Enter the code of the book you want to check out: ")

        found_book = None
        for book in book_library:
            if choice.lower() == book.code.lower():
                found_book = book
                break

        if found_book:
            if found_book.user_name:
                print(f"Sorry, this book is already checked out by {found_book.user_name}.")
            else:
                books_to_checkout.append(found_book)
        else:
            print("Invalid code. Please try again.")

    user_name = input("Enter your name: ")
    for book in books_to_checkout:
        book.user_name = user_name

def return_books(book_library):
    while True:
        display_books(book_library)
        choice = input("Enter the code of the book you want to return or 'done' when you are done: ")

        if choice.lower() == "done":
            return
        else:
            found_book = None
            for book in book_library:
                if choice.lower() == book.code.lower():
                    found_book = book
                    break

            if found_book:
                if found_book.user_name:
                    found_book.user_name = None
                else:
                    print("This book is not checked out.")
            else:
                print("Invalid code. Please try again.")

def main():
    total_books = 10
    book_library = generate_book_library()

    while True:
        print("\nGood day, what do you want to do today?")
        print("Here are the options we have:")
        print("1. Check out books")
        print("2. Return books")
        print("3. List all books in library")
        print("4. List all checked out books")
        print("5. Exit")
        option = input("Which option would you like? Enter the option number: ")

        if option == "1":
            print("Here are the sections we have:")
            print("1. Fiction")
            print("2. Non-Fiction")

            section = input("Which section would you like to explore? Enter the section number: ")

            if section == "1":
                fiction_books = book_library[:FICTION_BOOK_COUNT]
                num_books = int(input("How many books do you want to checkout? (up to 10) "))
                num_books = min(num_books, 10)
                checkout_books(fiction_books, num_books)
            elif section == "2":
                non_fiction_books = book_library[FICTION_BOOK_COUNT:]
                num_books = int(input("How many books do you want to checkout? (up to 10) "))
                num_books = min(num_books, 10)
                checkout_books(non_fiction_books, num_books)
            else:
                print("Invalid section number. Please try again.")
        elif option == "2":
            return_books(book_library)
        elif option == "3":
            display_books(book_library)
        elif option == "4":
            display_checked_out_books(book_library)
        elif option == "5":
            break
        else:
            print("Invalid option number. Please try again.")

        print(f"The Big Timber Library has {len([book for book in book_library if not book.user_name])} book(s) remaining.")
        print(f"There are {len([book for book in book_library if book.user_name])} book(s) checked out.")

main()
