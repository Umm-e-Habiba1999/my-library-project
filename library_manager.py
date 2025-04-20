import json
import os

# File to store library data
FILE_NAME = 'library.txt'

# Load library from file
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save library to file
def save_library(library):
    with open(FILE_NAME, 'w') as file:
        json.dump(library, file, indent=4)

# Display menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Try again.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == 'yes' else False

    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    found = False
    for book in library:
        if book['title'].lower() == title:
            library.remove(book)
            found = True
            print("Book removed successfully!")
            break
    if not found:
        print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    keyword = input("Enter the title/author: ").strip().lower()
    matches = []

    for book in library:
        if (choice == '1' and keyword in book['title'].lower()) or \
           (choice == '2' and keyword in book['author'].lower()):
            matches.append(book)

    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, start=1):
            status = "Read" if book['read'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for i, book in enumerate(library, start=1):
        status = "Read" if book['read'] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display statistics
def display_stats(library):
    total = len(library)
    if total == 0:
        print("No books in library.")
        return
    read_count = sum(1 for book in library if book['read'])
    percent = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent:.1f}%")

# Main loop
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_stats(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
