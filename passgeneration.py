import random
#este programa te ayudara a generar una posible clave segura
letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
passw="default"
passw=""
for i in range(0,7):
    passw=passw+letras[random.randint(0, 25)]
print("La clave propuesta es",passw)