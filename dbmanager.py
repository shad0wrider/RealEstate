import sqlite3 as sql
from sqlite3 import OperationalError , DatabaseError
import os 


def create_db(name:str):
    try:
        db = os.curdir+"/"+f"{name}.db"
        new_db = open(db)
        new_db.close()
        maincon = sql.connect(db)
        cursor = maincon.cursor()
        query = "create table properties (id int, name varchar ,location varchar , price float , area_sqft float , property_type varchar)"
        cursor.execute(query)
        return f"new db file at {os.path.abspath(db)}"
    except Exception as ie:
        return False

def db_shell(db_file="path"):
    while True:
        try:
            maincon = sql.connect(os.path.abspath(db_file))
            tmp = input("sql> ")
            if tmp.startswith(("INSERT","UPDATE","CREATE")):
                runit = maincon.execute(tmp)

            elif tmp =="quit":
                return main()
            

            else:
                runit = maincon.execute(tmp)
                print(runit.fetchall())
        except OperationalError as ie:
            print(ie,"Happened")
            return main()


def main():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    choice = input("1. Create Database\n2. SQL Shell\n\n> ")
    if choice == "1":
        name = input("Enter name for database filename: ")
        check = create_db(name)
        if check:
            print(check)
    elif choice == "2":
        db_path = input("Enter Full path of db file: ")
        if os.path.exists(db_path):
            db_shell(db_path)
        else:
            print("File not Found :(")
    else:
        print(f"option {choice} not found :(")

main()
