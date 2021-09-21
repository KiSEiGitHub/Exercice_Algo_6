def main():
    reponse = input("répondre oui ou non: ")
    if reponse in ["oui", "non"]:
        print(f"la réponse est {reponse}")
    elif len(reponse) >= 3:
        print("Y'a 3 caractères mais c'est pas bon")



if __name__ == '__main__':
    main()