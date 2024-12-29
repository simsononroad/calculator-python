import sqlite3
question = ""
import datetime
import os
import time

def initDB():
    con = sqlite3.connect("szamolasok.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE history(egyenloseg, eredmeny, egyben, date)")
    except:
        pass


def menu():
    while True:
        os.system("cls")
        print("Menü")
        menu = input("Előzmények(e), Számolás(sz), kilépés(k)")
        if menu == "e":
            history()
            break
        elif menu == "sz":
            check()
            break
        elif menu == "k":
            pass
            break
        else:
            pass

        
    

def check():
    os.system("cls")
    print("Menü > számolás")
    feladvany = input("Írd be a feladványt\n>>>")
    global question
    question = feladvany
    operatorokp = "+"
    operatorokm = "-"
    operatoroksz = "*"
    operatoroko = "/"
    
    if operatorokp in feladvany or operatorokm in feladvany or operatoroksz in feladvany or operatoroko in feladvany:
        szamolas()
    elif feladvany == "exit":
        menu()
    else:
        print("A számolásnak tartalmaznia kell legalább egy operátort")
        time.sleep(1.8)
        check()    
            
    

def szamolas():
    con = sqlite3.connect("szamolasok.db")
    cur = con.cursor()
    eredmeny = eval(question)
    teljes = f"{question} = {eredmeny}"
    print(teljes)
    time = datetime.datetime.now()
    nowtime = time.strftime("%Y.%m.%d - %H:%M:%S")
    ins = cur.execute(f"insert into history (egyenloseg, eredmeny, egyben, date) values ('{question}','{eredmeny}', '{teljes}', '{nowtime}')")
    con.commit()
    menu()

def history():
    os.system("cls")
    print("Menü > előzmények")
    con = sqlite3.connect("szamolasok.db")
    cur = con.cursor()
    ins = cur.execute(f"select egyben FROM history")
    teljes = cur.fetchall()
    for minden in teljes:
        minden = minden[0]
        print(minden)
    menu()


if __name__ == "__main__":
    initDB()
    menu()
