namekarbari = input("lotfan name karbari khod ra vared konid :")
while namekarbari!= "1400123056" :
    print("motasefaneh namekarbari shoma eshtebah ast")
    namekarbari = input("lotfan name karbari khod ra vared konid :")

password = input("lotfan password khod ra vared konid :")
while password!= "0025343297" :
    print("motasefaneh password shoma eshtebah ast")
    password = input("lotfan password khod ra vared konid :")   

import random

emtiaz_player1 = 0
emtiaz_player2 = 0
while emtiaz_player1 <=3 or emtiaz_player2 <=3:
    if emtiaz_player1 == 3 :
        print("player1 is win va payan bazi")
        break
    elif emtiaz_player2 == 3 :
        print("player2 is win va payan bazi")  
        break  
    



    player1 = input("player1 , lotfan harekat khod ra entekhab konid :").lower()
    randomnumber = random.randint(1, 3)
    print(randomnumber)


    if randomnumber == 1:
        player2 = "sang"
    elif randomnumber == 2:
        player2 == "kaghaz"
    elif randomnumber == 3:
        player2 = "gheychi"

    print(player2)  



    if player1 == player2 :
        print("mosavi")
    elif player1 == "sang" and player2 == "kaghaz":
        print("player2 win")   
        emtiaz_player2 += 1 
    elif player1 == "sang" and player2 == "gheychi":
        print("player1 win")
        emtiaz_player1 += 1
    elif player1 == "kaghaz" and player2 == "sang":
        print("player1 win")
        emtiaz_player1 += 1
    elif player1 == "kaghaz" and player2 == "gheychi":
        print("player2 win")
        emtiaz_player2 += 1
    elif player1 == "gheychi" and player2 == "sang":
        print("player2 win")
        emtiaz_player2 += 1
    elif player1 == "gheychi" and player2 == "kaghaz":
        print("player1 win")
        emtiaz_player1 += 1
    else:
        print("ye chizi eshtebahe!")
    print(f"emtaiz player1 : {emtiaz_player1}")
    print(f"emtiaz player2 : {emtiaz_player2}")
    print("====================================================")
    
