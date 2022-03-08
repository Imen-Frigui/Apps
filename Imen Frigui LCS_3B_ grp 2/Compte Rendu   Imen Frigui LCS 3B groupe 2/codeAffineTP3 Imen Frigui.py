def prepare (phraseEnclair):
    li1=["âà","éèêë","îï","ô","ûü","ç"]
    li2=["A","E","I","O","U","C"]
    for i in phraseEnclair:
        for j in range(6):
            if i in li1[j]:
                phraseEnclair=phraseEnclair.replace(i,li2[j])
                break
    phraseEnclair=phraseEnclair.upper()
    return (phraseEnclair)
a=11
b=3

ch="QVBàààDéjklmzôjzmlzlçdsxoplknxmù"
print(ch)
ch=prepare(ch)
print("message Clair:",ch)
for i in range(len(ch)):
    y=(a*(ord(ch[i])-65)+b)%26
   
    x=chr(y+65)

    l=list(ch)

    l[i]=x
    ch="".join(l)
print("cles",a,"et",b)
print("message code:",ch)
for j in range(len(ch)):
       z=0
       
       y1=((((ord(ch[j])-65)+(z*26))-b)/a)
       while(y1!=int(y1)):
           z=z+1
           y1=((((ord(ch[j])-65)+(z*26))-b)/a)


       x1=chr(int(y1)+65)
       l=list(ch)
       l[j]=x1
       ch="".join(l)

print("message clair apres decryptage :",ch)
    
        
