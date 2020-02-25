#Python Nested Lists
books_list = [("C", 896), ("C++", 599), ("Python", 1269)]
print("Books list with prices.")
ch = None
while ch != "0":
    print("\n0 - Exit")
    print("1 - Show Books List")
    print("2 - Add a Book")
    ch = input("Choice:")
    if ch == "0":
        print("Exiting...")
    elif ch == "1":
        print("\nBook\t\tPrice")
        for add_book in books_list:
            book_name, book_price = add_book
            print(book_name,"\t\t",book_price)
    elif ch == "2":
        book_name = input("\nEnter name of the book:")
        book_price = int(input("Enter its price:"))
        add_book = (book_name, book_price)
        books_list.append(add_book)
    else:
        print("Sorry, but",choice,"is not valid choice.")