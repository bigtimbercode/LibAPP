class Book {
    constructor(code, title) {
        this.code = code;
        this.title = title;
        this.userName = null;
    }
}

const FICTION_BOOK_COUNT = 11;

let bookLibrary = generateBookLibrary();

function generateBookLibrary() {
    const fictionBooks = ["To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "Moby-Dick", "War and Peace", "The Catcher in the Rye", "The Hobbit", "Brave New World", "The Lord of the Rings", "Crime and Punishment"];

    const nonFictionBooks = ["Sapiens: A Brief History of Humankind", "Educated", "Becoming", "The Immortal Life of Henrietta Lacks", "The Diary of a Young Girl", "Thinking, Fast and Slow", "The Power of Habit", "Freakonomics", "Guns, Germs, and Steel", "Quiet: The Power of Introverts in a World That Can't Stop Talking"];

    let bookLibrary = [];
    let code = 1;

    for (const title of fictionBooks) {
        bookLibrary.push(new Book(`#${String(code).padStart(3, '0')}`, title));
        code++;
    }

    for (const title of nonFictionBooks) {
        bookLibrary.push(new Book(`#${String(code).padStart(3, '0')}`, title));
        code++;
    }

    return bookLibrary;
}

function displayBooks() {
    const libraryOutput = document.getElementById('library-output');
    libraryOutput.innerHTML = "Books available in the library: <br>";
    for (const book of bookLibrary) {
        if (!book.userName) {
            libraryOutput.innerHTML += `${book.code}: ${book.title} <br>`;
        }
    }
}

function displayCheckedOutBooks() {
    const libraryOutput = document.getElementById('library-output');
    libraryOutput.innerHTML = "Checked out books: <br>";
    for (const book of bookLibrary) {
        if (book.userName) {
            libraryOutput.innerHTML += `${book.code}: ${book.title} (Checked out by ${book.userName}) <br>`;
        }
    }
}

function checkoutBooks() {
    // Use prompt or a modal to get the number of books and username.
    const bookCount = Number(prompt("Enter the number of books you want to checkout: "));
    const userName = prompt("Enter your name: ");

    for (let i = 0; i < bookCount; i++) {
        const bookCode = prompt("Enter the code of the book you want to checkout: ");
        const book = bookLibrary.find(b => b.code === bookCode);
        if (book) {
            if (!book.userName) {
                book.userName = userName;
            } else {
                alert(`Sorry, this book is already checked out by ${book.userName}.`);
            }
        } else {
            alert("Invalid book code. Please try again.");
        }
    }
}

function returnBooks() {
    const bookCode = prompt("Enter the code of the book you want to return: ");
    const book = bookLibrary.find(b => b.code === bookCode);
    if (book) {
        if (book.userName) {
            book.userName = null;
        } else {
            alert("This book is not checked out.");
        }
    } else {
        alert("Invalid book code. Please try again.");
    }
}

function listBooks() {
    displayBooks();
}

function listCheckedOutBooks() {
    displayCheckedOutBooks();
}
