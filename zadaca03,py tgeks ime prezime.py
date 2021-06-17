import re
# pocinje s J, broj(0-5),razmak i završava sa č
zamjena="^J.*[0-5]\s.*č$"
while 1:
    string=input("Unesite string:")
    result=re.search(zamjena ,string)
    if result:
        break 
    else:
        print("Nema podudaranja.")

print("Izvršeno podudaranje")
