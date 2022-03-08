from os import system
def main():
    # ==============================================================
    def prepare(PhraseEnClair):
        "Cette fonction permet de remplacer les caractères accentués du texte par leurs équivalents sans accents"
        li1 = ["âà","éèêë","îï","ô","ûü","ç"]
        li2 = ["A","E","I","O","U","C"]
        for i,letter in enumerate(PhraseEnClair):
            for j,accent in enumerate(li1):
                if letter in accent:
                    PhraseEnClair = PhraseEnClair.replace(letter,li2[j]) 
        return PhraseEnClair.upper()
    # ==============================================================
    def cryptor(PhraseEnClair, a = 11, b = 3):
        "cette fonction permet de crypter le texte en clair"
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        PhraseEnClair = prepare(PhraseEnClair)
        cryptedPhrase = list()
        for x in PhraseEnClair:
            if x in ALPHABET:
                val = ord(x)
                if val >= 65 and val <= 90:
                    y = (( (val-65) * a ) + b ) % 26
                    # plainText = plainText.replace(x,chr(y+65)) 
                    cryptedPhrase.append(chr(y+65))
            else:
                cryptedPhrase.append(x)
        return "".join(cryptedPhrase)
    # ==============================================================
    def decryptor(PhraseEnClair, a = 11, b = 3):
        "Cette fonction a pour rôle de décrypter un texte"
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        PhraseEnClair = prepare(PhraseEnClair)
        decryptedPhrase = list()
        for index,x in enumerate(PhraseEnClair):
            if x in ALPHABET:
                val = ord(x)
                maxVal = 26
                if val >= 65 and val <= 90:
                    while maxVal >= 0 and (( maxVal * a) + b) % 26 != (val-65):
                        maxVal -=1
                    if maxVal >= 0:
                        decryptedPhrase.append(chr(maxVal+65))
            else:
                decryptedPhrase.append(x)
        return "".join(decryptedPhrase)
    def start(text):
        "Cette fonction permet de vérifier si le texte récuperé est une chaine ou non"
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        j = 0
        for i in text:
            if i.upper() in ALPHABET:
                j +=1
        if j == 0:
            return False
        return True

    welcomeText = " Make your choice - 1 : Encrypt - 2 : Decryption  "

    print(welcomeText)
    choice = input()
    while True:
        try:
            choice = int(choice)
        except :
            print("No character other than an integer can be accepted !")
        if choice != 1 and choice != 2:
            print("You only have two choices, 1 or 2.")
            choice = input()
        else:
            break

    if(choice == 1 ):
        while True :
            print("Enter your text to encrypt :")
            text = input()
            if(start(text)):
                print("Enter the value of A : ") 
                ok = False
                while ok != True:
                    a = input()
                    try:
                        a = int(a)
                        if type(a) is int:
                            ok = True
                    except :
                        print("The value of A must be a positive integer")
                
                print("Enter the value of B :")
                ok = False
                while ok != True:
                    b = input()
                    try:
                        b = int(b)
                        if type(b) is int :
                            if b < a:
                                ok = True
                            else:
                                print("The value of B must be lower than A.")
                                ok = False
                    except :
                        print("The value of B must be a positive integer")
                print("--------------The text is successfully crypted ;)--------------")
                print(cryptor(text,a,b).center(50))
                
                response = ""
                while response.lower() != "y" and response.lower() != "n" :
                    print("Do like to continue ? (y / n)")
                    response = input()
                if(response.lower() == "y" ):
                    main() # Rappel de la fonction principale(main) pour rélancer le programme
                print("Goodbye ...")
                break
            else:    
                print("Your text ({}) does not contain any alphabetical letter :(".format(text))
                print("Do you like to try again ? (y / n)")
                answer = ""
                while answer.lower() != "n" and answer.lower() != "y":
                    answer = input()
                    if answer.lower() != "n" and answer.lower() != "y":
                        print("Yes (y) or No (n) please !")
                if(answer.lower() == "n" ):
                    print("End ...")
                    break
        
    if(choice == 2 ):
        while True :
            print("Enter your text to decrypt :")
            text = input()
            if(start(text)):
                print("Enter the value of A : ") 
                ok = False
                while ok != True:
                    a = input()
                    try:
                        a = int(a)
                        if type(a) is int:
                            ok = True
                    except :
                        print("The value of A must be a positive integer")
                
                print("Enter the value of B :")
                ok = False
                while ok != True:
                    b = input()
                    try:
                        b = int(b)
                        if type(b) is int:
                            if b < a:
                                ok = True
                            else:
                                print("The value of B must be lower than A.")
                                ok = False
                    except :
                        print("The value of B must be a positive integer")
                print("--------------The text is successfully decrypted ;)--------------")
                print(decryptor(text,a,b).center(50))
                
                response = ""
                while response.lower() != "y" and response.lower() != "n" :
                    print("Do you like to continue ? (y / n)")
                    response = input()
                if(response.lower() == "y" ):
                    main() # Rappel de la fonction principale(main) pour rélancer le programme
                print("Goodbye ...")
                break
            else:    
                print("Your text ({}) does not contain any alphabetical character :(".format(text))
                print("Do you like to try again ? (y / n)")
                answer = ""
                while answer.lower() != "n" and answer.lower() != "y":
                    answer = input()
                    if answer.lower() != "n" and answer.lower() != "y":
                        print("Yes (y) ou No (n) Please !")
                if(answer.lower() == "n" ):
                    print("End ...")
                    break
if __name__ == '__main__':
    main()
    system("pause")
