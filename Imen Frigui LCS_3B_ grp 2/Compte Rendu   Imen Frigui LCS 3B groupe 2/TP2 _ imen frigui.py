#EX1


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(alphabet," ")
print(ALPHABET," ")



#EX2

def convert_text(text):
    return text.upper()

text = input("\n Type your text that you wanna Convert from lowercaes to uppercases : \n\n")


print ("\n",convert_text(text))





#EX3



def cesar(text):
    dict=str.maketrans(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"," efghijklmnopqrstuvwxyzabcdEFGHIJKLMNOPQRSTUVWXYZABCD567891234")
    offset=text.translate(dict)
    return offset

text = input(" Type your text that you wanna Encrypt: \n")

print("\n",cesar(text))


print ("\n EX 3 deuxiéme methode : \n")

def cesar(text, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = ''
    for x in text:
        place = alphabet.find(x)
        ind = place+offset
        if ind > 25:
            ind = ind % 26
        output += alphabet[ind]
    return output
 
 
text = input("\n\n Type your text that you wanna Encrypt: \n")
offset = int(input("Type offset: \n"))
print("\n",cesar(text,offset))


#EX4
def swap(text, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = ''
    for x in text:
        place = alphabet.find(x)
        ind = place-offset
        if ind > 25:
            ind = ind % 26
        output += alphabet[ind]
    return output
 
 
text = input("Type your text that you wanna Decrypt:\n")
offset = int(input("Type offset:\n"))
print("\n",swap(text,offset))





   

