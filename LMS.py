'''import pandas as pd

# Load the Excel file
def load_data(file_name="C:/Users/arup_/OneDrive/Documents/Visual Studio 2017/lib_data2.xlsx"):
    try:
        df = pd.read_excel(file_name, sheet_name='Sheet1', engine='openpyxl')
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        df = pd.DataFrame(columns=['ID', 'Title', 'Author', 'Genre', 'Available'])
    return df

# Save the DataFrame to the Excel file
def save_data(df, file_name="C:/Users/arup_/OneDrive/Documents/Visual Studio 2017/lib_data2.xlsx"):
    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)

# View all books
def view_books():
    df = load_data()
    print(df)


# Add a new book
def add_book(id, title, author, genre):
    df = load_data()
    new_book = pd.DataFrame([[id, title, author, genre, 'Yes']], columns=df.columns)
    df = pd.concat([df, new_book], ignore_index=True)
    save_data(df)
    print("Book added successfully.")

# Borrow a book by genre
def borrow_book_by_genre():
    genre = input("Enter the genre of the book you want to borrow: ")
    df = load_data()
    available_books = df[(df['Genre'].str.contains(genre, case=False, na=False)) & (df['Available'] == 'Yes')]
    if available_books.empty:
        print(f"No available books found in the genre: {genre}")
    
    print("Available books:")
    print(available_books)
    
    try:
        book_id = int(input("Enter the ID of the book you want to borrow: "))
        if book_id in available_books['ID'].values:
            df.loc[df['ID'] == book_id, 'Available'] = 'No'
            save_data(df)
            print("Book borrowed successfully.")
        else:
            print("Invalid book ID.")
    except ValueError:
        print("Invalid input. Please enter a valid book ID.")

# Return a book
def return_book(id):
    df = load_data()
    if id in df['ID'].values:
        df.loc[df['ID'] == id, 'Available'] = 'Yes'
        save_data(df)
        print("Book returned successfully.")
    else:
        print("Book ID not found.")

# Main menu
def main():
    while True:
        print("\nLibrary Management System")
        print("1. View Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_books()
        elif choice == 2:
            id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            add_book(id, title, author, genre)
        elif choice == 3:
            borrow_book_by_genre()
        elif choice == 4:
            id = int(input("Enter book ID to return: "))
            return_book(id)
        elif choice == 5:
            break #quit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()'''
import MySQLdb as m

conn = m.connect(host = "localhost", user = "root", password = "Arup@123", database = "library")

def add_book():
    book_name = input("Enter book name: ")
    book_code = input("Enter book code: ")
    total_b = input("Total books: ")
    sub = input("Enter Subject: ")
    data = (book_name, book_code, total_b, sub)
    sql = "insert into books values(%s,%s,%s,%s)"
    c = conn.cursor()
    c.execute(sql,data)
    conn.commit()
    print(">---------------------------------------------------------------------------<")
    print("Data Entered Successfully.")
    main()
def issue_book():
    name = input("Enter your name: ")
    reg_no = input("Enter reg no: ")
    book_code = input("Enter book code: ")
    date = input("Enter Date: ")
    data = (name, reg_no, book_code, date)
    sql = "insert into issue values(%s,%s,%s,%s)"
    c = conn.cursor()
    c.execute(sql,data)
    conn.commit()
    print(">---------------------------------------------------------------------------<")
    print(f"Book issued to: {name} on {date}")
    book_up(book_code, 1)

    
def submit_book():
    name = input("Enter your name: ")
    reg_no = input("Enter reg no: ")
    book_code = input("Enter book code: ")
    date = input("Enter Date: ")
    data = (name, reg_no, book_code, date)
    sql = "insert into submit values(%s,%s,%s,%s)"
    c = conn.cursor()
    c.execute(sql,data)
    conn.commit()
    print(">---------------------------------------------------------------------------<")
    print(f"Book submitted from: {name} on {date}")
    book_up(book_code, 1)
def book_up(book_code, u):
    sql = "select total from books where b_code = %s"
    data = (book_code,)
    c = conn.cursor()
    c.execute(sql,data)
    myresult = c.fetchone()
    t = myresult[0] + u
    ql = "update books set total = %s where b_code = %s"
    d = (t, book_code)
    c.execute(ql,d)
    conn.commit()
    main()
def del_books():
    book_code = input("Enter book code: ")
    sql = "delete from books where b_code = %s"
    data = (book_code,)
    c = conn.cursor()
    c.execute(sql,data)
    conn.commit()
    main()
def dis_books():
    sql = "select * from books"
    c = conn.cursor()
    c.execute(sql)
    my_result = c.fetchall()
    for result in my_result:
        print(f"Book Name: {result[0]}")
        print(f"Book code: {result[1]}")
        print(f"Total: {result[2]}")
        print(">-------------------------<")
    main()



def main():
    print("""   
                          LIBRARY MANAGER
          1. ADD BOOK
          2. ISSUE BOOK
          3. SUBMIT BOOK
          4. DELETE BOOK
          5. DISPLAY BOOKS
          """)
    choice = int(input("Enter your choice(1-5): "))
    print(">---------------------------------------------------------------------------<")
    if choice == 1:
        add_book()
    elif choice == 2:
        issue_book()
    elif choice == 3:
        submit_book()
    elif choice == 4:
        del_books()
    elif choice == 5:
        dis_books()
    else:
        quit()
main()
        



