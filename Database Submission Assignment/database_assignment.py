#Database Submission Assignment - Python Course, Step 222

import sqlite3  #import the sqlite3 modules and its methods


#create the database "databaseAssignment.db", connect to that database, and created a table with an ID column that auto incriments and a fileList column, and then closes the database
conn = sqlite3.connect("databaseAssignment.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignment( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileList TEXT \
            )")
    conn.commit()
conn.close()

conn = sqlite3.connect("databaseAssignment.db")

# List of files to be sorted through
fileList=("information.docx", "Hello.txt", "myImage.png", \
          "myMovie.mpg", "World.txt", "data.pdf", "myPhoto.jpg")




#for loop that will pull any .txt files out from the list and adds them to the database
for i in fileList:
    if i.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_assignment (col_fileList) VALUES (?)", (i,))
            print(i)
conn.close()

