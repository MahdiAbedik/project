namekarbari = input("lotfan name karbari khod ra vared konid :")
while namekarbari!= "1400123056" :
    print("motasefaneh namekarbari shoma eshtebah ast")
    namekarbari = input("lotfan name karbari khod ra vared konid :")

password = input("lotfan password khod ra vared konid :")
while password!= "0025343297" :
    print("motasefaneh password shoma eshtebah ast")
    password = input("lotfan password khod ra vared konid :")   

import random

randomnumber = random.randint(1, 2)

if randomnumber == 1 :
    seke = "shir"
elif randomnumber == 2 :
    seke = "khat"

print(seke)

if seke == "shir":
    print("toop baraye team persepolis va zamin baraye team esteghlal.")

elif seke == "khat" :
    print("toop baraye team esteghlal va zamin baraye team persepolis.")    

else :
    print("seke az dast davar oftad , seke dobare partab mishavad.")

