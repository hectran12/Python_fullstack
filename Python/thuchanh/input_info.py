import os

def ask():
    examp1 = input("Input exam1: ")
    examp2 = input("Input exam2: ")
    with open("account.txt","w",encoding="utf-8") as f:
        f.write(examp1+"\n")
        f.write(examp2+"\n")
    return [examp1,examp2]

def info_input():
    if os.path.isfile("account.txt") == True:
        askz = input("Do you want to use an old account? (y/n): ")
        if askz.lower() == "y":
            f = open("account.txt","r",encoding="utf-8")
            examp3 = [x.replace("\n","") for x in f]
            return examp3
        else:
            return ask()
    else:
        return ask()

print(info_input())
