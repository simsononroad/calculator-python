import sqlite3
question = ""
def initDB():
    con = sqlite3.connect("szamolasok.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE history(egyenloseg, eredmeny)")
    except:
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
    print(question)
    eredmeny = eval(question)
    print(eredmeny)
    ins = cur.execute(f"insert into history (egyenloseg, eredmeny) values ('{question}','{eredmeny}')")
    con.commit()


if __name__ == "__main__":
    initDB()
    check()
