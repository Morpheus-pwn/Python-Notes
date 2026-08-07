# write a python program to create a library management system with the following features:
# 1.use sequence data type to store the book names,author names and member names
# 2.perform indexing and slicing operations on book names, member names and list of books
# 3. use string methods to convert book name to uppercase and remove extra spaces from member names
# 4. demonstrate that strings are immutable by trying to change a character in a book name
# 5. use list methods to add new books, remove issued books and sort the list of books
# 6. use list comprehension to Display available books, Filter books starting with a specific letter and Create uppercase book lists.
# 7. store fixed book categories using tuples.
# 8. demonstrate that tuples cannot be modified after creation
# 9. use sets to automatically remove duplicate genres or duplicate book names
# 10.


book_name=["python","java","c++","javascript"]
member_names=["Alice","Bob","Charlie","pawan","tiswin","edwin"]
list_of_books=[]
author_names=["jk rowling","stephen king","david wallace","charles dickens"]

def add_book():
    book = input("Enter the name of the book: ")
    author = input("Enter the name of the author: ")
    list_of_books.append({"book": book, "author": author})
    print(f"Book '{book}' by {author} added successfully.")

def main():
    print("Welcome to the Library Management System")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Issue a book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()