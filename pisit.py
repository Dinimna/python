nom= input("quel est votre nom ? ")
age= input("quel est votre age ? ")

try:
    age_prochain = int(age) +1
except:
    print("ERREUR: vous devez rentrer un nombre pour l'age")
else:
    print("Vous vous appelez " + nom + " , vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age_prochain) + " ans")