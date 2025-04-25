# library_manager.py
import streamlit as st
import json
import os

# Load library from file if exists
LIBRARY_FILE = "library.txt"
library = []

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_library():
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f)

def add_book(title, author, year, genre, read):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)

def remove_book(title):
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]

def search_books(search_type, query):
    query = query.lower()
    if search_type == "Title":
        return [book for book in library if query in book["title"].lower()]
    else:
        return [book for book in library if query in book["author"].lower()]

def display_statistics():
    total = len(library)
    read_count = len([book for book in library if book["read"]])
    percent = (read_count / total * 100) if total else 0
    return total, percent

# Load existing library
library = load_library()

# Streamlit UI
st.title("📚 Personal Library Manager")

menu = ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add a Book":
    st.subheader("➕ Add a Book")
    title = st.text_input("Enter book title:")
    author = st.text_input("Enter author name:")
    year = st.number_input("Enter publication year:", min_value=0, step=1)
    genre = st.text_input("Enter genre:")
    read = st.radio("Have you read this book?", ("Yes", "No"))
    if st.button("Add Book"):
        add_book(title, author, int(year), genre, True if read == "Yes" else False)
        st.success("Book added successfully!")
        save_library()

elif choice == "Remove a Book":
    st.subheader("❌ Remove a Book")
    title = st.text_input("Enter the title of the book to remove:")
    if st.button("Remove Book"):
        remove_book(title)
        st.success("Book removed successfully!")
        save_library()

elif choice == "Search for a Book":
    st.subheader("🔍 Search for a Book")
    search_type = st.radio("Search by:", ["Title", "Author"])
    query = st.text_input(f"Enter {search_type.lower()}:")
    if query:
        results = search_books(search_type, query)
        if results:
            st.write("### Matching Books:")
            for i, book in enumerate(results, 1):
                status = "Read" if book["read"] else "Unread"
                st.write(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            st.warning("No matching books found.")

elif choice == "Display All Books":
    st.subheader("📖 Your Library")
    if library:
        for i, book in enumerate(library, 1):
            status = "Read" if book["read"] else "Unread"
            st.write(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.info("No books in the library.")

elif choice == "Display Statistics":
    st.subheader("📊 Library Statistics")
    total, percent = display_statistics()
    st.write(f"**Total books:** {total}")
    st.write(f"**Percentage read:** {percent:.2f}%")

   
       
       
