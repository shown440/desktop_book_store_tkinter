import sqlite3
#import sqlite3 for work with Database and SQLite3 is built in Library of Python



#work with database in Python has 5 steps:
# 1. Connect to a database
# 2. Create a Cursor object
# 3. Write an SQL Query AND execute query in cursor
# 4. Commit changes
# 5. Close your Database Connection

#Create Database
def connect_Bookdb():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


#Add Book to the Database
def add_Bookdb(title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()


#View all books from Database
def viewall_Bookdb():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    # Dont use commit for view data from Database
    # Use "cur.fetchall()" in place of "conn.commit()" to Fetch data from Database
    rows = cur.fetchall()
    conn.close()
    return rows


#Search any book from Database
def search_Bookdb(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    # Dont use commit for view data from Database
    # Use "cur.fetchall()" in place of "conn.commit()" to Fetch data from Database
    rows = cur.fetchall()
    conn.close()
    return rows


#Delete any Book from Database
def delete_Bookdb(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id=?",(id,))
    conn.commit()
    conn.close()


#Update any Book details in Database
def update_Bookdb(id, title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?  WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()






#connect_Bookdb()
#add_Bookdb("JavaSE Programming", "Herbert Shield", 2010, 1996552654641)
#update_Bookdb(4, "Java ProgrammingII", "Herbert Shield", 2010, 1996552654641)
#delete_Bookdb(4)
#print(search_Bookdb(title="", author="Subin Haider", year="", isbn=""))
#print(viewall_Bookdb())
