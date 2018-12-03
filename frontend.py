from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_row
        #listbox1.curselection() return the ID as list  But
        #listbox1.curselection()[0] return ID as INTEGER
        index = listbox1.curselection()[0]
        #listbox1.get(index) command will pick row/touple using index
        selected_row = listbox1.get(index)

        #Now we will fill Title, Author, Year and ISBN entry automatically
        #fill the Title entry
        titleEntry.delete(0, END)
        titleEntry.insert(END, selected_row[1])

        #fill Author entry
        authorEntry.delete(0, END)
        authorEntry.insert(END, selected_row[2])

        #fill Year Entry
        yearEntry.delete(0, END)
        yearEntry.insert(END, selected_row[3])

        #fill ISBN Entry
        isbnEntry.delete(0, END)
        isbnEntry.insert(END, selected_row[4])

    except IndexError:
        pass



####################################################################################################################
#Configure listbox1 of frontend and  viewall_Bookdb() of backend
#View all from database
def view_command():
    listbox1.delete(0, END)
    for row in backend.viewall_Bookdb():
        listbox1.insert(END, row)

#Configure listbox1 of frontend and search_Bookdb(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()) of backend
#title_text, author_text, year_text, isbn_text are Entry of frontend
# .get() method get data from Entry and make it as String
#Search all from database
def search_command():
    listbox1.delete(0, END)
    for row in backend.search_Bookdb(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listbox1.insert(END, row)


#Configure frontend and search_Bookdb(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()) of backend
#Configure listbox1 with frontend to see the newly added book in Listbox
#Add book to database
def addBook_command():
    backend.add_Bookdb(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    #listbox1.delete(0, END) = Make listbox empty
    listbox1.delete(0, END)
    listbox1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


#Configure listbox1 of frontend and  delete_Bookdb() of backend to delete books
#Delete books from database
def deleteBook_command():
    backend.delete_Bookdb(selected_row[0])


#Configure listbox1 of frontend and  update_Bookdb() of backend to delete books
#Update any books in database
def updateBook_command():
    backend.update_Bookdb(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


#close window
def closeWindow_command():
    window.destroy()


#Window Start.....
window = Tk()
window.title("Book Store")
#window.configure(background="BLUE")


#############################################################################################
#Label Description
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)


###############################################################################################
#Entry Descriptions
title_text = StringVar()
titleEntry = Entry(window, textvariable=title_text)
titleEntry.grid(row=0, column=1)

author_text = StringVar()
authorEntry = Entry(window, textvariable=author_text)
authorEntry.grid(row=0, column=3)

year_text = StringVar()
yearEntry = Entry(window, textvariable=year_text)
yearEntry.grid(row=1, column=1)

isbn_text = StringVar()
isbnEntry = Entry(window, textvariable=isbn_text)
isbnEntry.grid(row=1, column=3)


#############################################################################################
#ListBox Description
listbox1 = Listbox(window, height=12, width=30)
listbox1.grid(row=2, column=0, rowspan=6, columnspan=2)

#ScrollBar Descriptions
scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)

#Listbox and Scrollbar configuration
listbox1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=listbox1.yview)

#Bind Listbox1 to grap the ID of selected touple
# .bind() = binde widget and event combindly
listbox1.bind("<<ListboxSelect>>", get_selected_row)



##########################################################################################
#Button Descriptions
ViewBtn = Button(window, text="View All", width=15, command=view_command)
ViewBtn.grid(row=2, column=3)

SearchBtn = Button(window, text="Search", width=15, command=search_command)
SearchBtn.grid(row=3, column=3)

AddBookBtn = Button(window, text="Add Book", width=15, command=addBook_command)
AddBookBtn.grid(row=4, column=3)

UpdateBookBtn = Button(window, text="Update Book", width=15, command=updateBook_command)
UpdateBookBtn.grid(row=5, column=3)

DeleteBookBtn = Button(window, text="Delete Book", width=15, command=deleteBook_command)
DeleteBookBtn.grid(row=6, column=3)

CloseStoreBtn = Button(window, text="Close Store", width=15, command=closeWindow_command)
CloseStoreBtn.grid(row=7, column=3)

# Window close...
window.mainloop()
