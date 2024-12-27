import sqlite3
question = ""
def initDB():
    con = sqlite3.connect("szamolasok.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE history(id INT PRIMARY KEY AUTOINCREMENT ,egyenloseg, eredmeny)")
        
    except:
        pass


def check():
    feladvany = input("Írd be a feladványt\n>>>")
    global question
    question = feladvany
    operatorok = ["+", "/", "-", "*", "."]
    for operators in operatorok:
        print(operators)
        if feladvany in operators:
            szamolas()
        else:
            print("A számolásnak tartalmaznia kell legalább egy operátort")
            check()    
            
    

def szamolas():
    print(question)
    try:
        eredmeny = int(eval(question))
    except:
        print("Ez nem egy helyes feladvány!")

if __name__ == "__main__":
    initDB()
    check()
