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
while emtiaz_player1 <=2 or emtiaz_player2 <=2:
    if emtiaz_player1 == 2 :
        print("player2 is win va payan bazi")
    elif emtiaz_player2 == 2 :
        print("player2 is win va payan bazi")

    player1 = input("entekhab shoma , dast rast ast ya dast chap ? ")

    randomnumber = random.randint(1, 4)
    print(randomnumber)


    if randomnumber == 1 :
        player2 = "dast rast gol"
    elif randomnumber == 2 :
        player2 = "dast rast pooch"
    elif randomnumber == 3 :
        player2 = "dast chap gol"
    elif randomnumber == 4 :
        player2 = "dast chap pooch"    
    print(player2)


    if player1 == "dast chap" and player2 == "dast chap pooch" :
        print("player2 is win")
        emtiaz_player2 +=1
    elif player1 == "dast chap" and player2 == "dast chap gol" :
        print("player1 is win")
        emtiaz_player1 +=1
    elif player1 == "dast rast" and player2 == "dast rast pooch" :
        print("player2 is win")
        emtiaz_player2 +=1
    elif player1 == "dast rast" and player2 == "dast rast gol" :
        print("player1 is win")
        emtiaz_player1 +=1 
    else:
        print("motasefane ye chizi eshtebahe .") 

        
    print(f"emtaiz player1 : {emtiaz_player1}")
    print(f"emtiaz player2 : {emtiaz_player2}")
    print("====================================================")     
        