print ('Imen Frigui LCS3')

#1
alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet,"\n")
print(ALPHABET,"\n")


#4
def main():
    text = input ('Entrez le message à chiffrer : ')
    offset = int (input('Entrez le décalage à utiliser : '))
    message = cesar(text, offset)
    print('Le message chiffré est : \n', message)


#2
def convert_text(text):
    return text.upper()

text = input("Type your text that you wanna Convert from lowercaes to uppercases : \n")


print ("\n",convert_text(text))





#3
def cesar(text, offset):

    text = convert_text(text)
    new_text = ""
    for char in text:
        if char in ALPHABET:
            new_text += swap(char, offset)
        else:
                new_text += char
    return new_text



#5
def swap(char, offset):
     index = ALPHABET.find(char)
     return ALPHABET[(index + offset) % 26]
if __name__ == '__main__':
    main()
def cesar(t,k):
    t,ch=t.upper(),""
    for i in t:
        r = ord(i)-k
        if r>=65:
            ch=ch+chr(r)
        else:
            while(r<65):
                r = r+26
            ch=ch+chr(r)
    return ch.lower()

text,key=input('Saisir un texte : '),int(input('Saisir la clef : '))

print(cesar(text,key))    

