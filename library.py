book_name=["python","java","c++","javascript"]
member_names=["Alice wonderland","Bob","Charlie","pawan shaji","tiswin joy","edwin"]
list_of_books=[]
author_names=["jk rowling","stephen king","david wallace","charles dickens"]
genres = {"Python", "Java", "Python", "C++"}

def add_book():
    book = input("Enter the name of the book: ")
    author = input("Enter the name of the author: ")
    list_of_books.append({"book": book, "author": author})
    print(f"Book '{book}' by {author} added successfully.")
    for book in list_of_books:
        book['book'] = book['book'].upper()
        book['book'] = book['book'].strip()
        book['author'] = book['author'].strip()
    for book in list_of_books:
        print(f"Book: {book['book']}, Author: {book['author']}")

def view_books():
    for book in list_of_books:
        book['book'] = book['book'].sort()
        print(f"Book: {book['book']}, Author: {book['author']}")

    # filter books starting with a specific letter
    letter = input("Enter a letter to filter books starting with that letter: ")
    filtered_books = [book for book in list_of_books if book['book'].startswith(letter)]
    for book in filtered_books:
        print(f"Book: {book['book']}, Author: {book['author']}")

    

def search_book():
    book['book'].sort()
    book_name = input("Enter the name of the book to search: ")
    for book in list_of_books:
        if book['book'].lower() == book_name.lower():
            print(f"Book found: {book['book']} by {book['author']}")
            return
    print("Book not found.")

def issue_book():
    book_name = input("Enter the name of the book to issue: ")
    for book in list_of_books:
        if book['book'].lower() == book_name.lower():
            list_of_books.remove(book)
            print(f"Book '{book_name}' issued successfully.")
            return
    print("Book not found.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            issue_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Library Management System.")

if __name__ == "__main__":
    main()