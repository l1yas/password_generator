import random
import string


characters = string.digits + string.ascii_letters + "/*-+=][}{!@#$%^&*()'"


def generate_password(characters) :
    lgr = int(input("Password Length: "))
    mdp = ""
    for i in range(lgr):
        mdp += random.choice(characters)
    print(mdp)

generate_password(characters)
