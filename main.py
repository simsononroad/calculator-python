import sqlite3
question = ""
def initDB():
    con = sqlite3.connect("szamolasok.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE history(egyenloseg, eredmeny, egyben)")
    except:
        pass


def menu():
    while True:
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
    feladvany = input("Írd be a feladványt\n>>>")
    global question
    question = feladvany
    operatorokp = "+"
    operatorokm = "-"
    operatoroksz = "*"
    operatoroko = "/"
    
    if operatorokp in feladvany or operatorokm in feladvany or operatoroksz in feladvany or operatoroko in feladvany:
        szamolas()
    else:
        print("A számolásnak tartalmaznia kell legalább egy operátort")
        check()    
            
    

def szamolas():
    con = sqlite3.connect("szamolasok.db")
    cur = con.cursor()
    eredmeny = eval(question)
    teljes = f"{question} = {eredmeny}"
    print(teljes)
    ins = cur.execute(f"insert into history (egyenloseg, eredmeny, egyben) values ('{question}','{eredmeny}', '{teljes}')")
    con.commit()
    menu()

def history():
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
