#ex1
print ('-----EX1-----')
print('Hello World')
#ex2
print('------EX2------')
print(1234)
print(-123456789)
print(3,14)
print('6,02x')
print('-160217653X')
print('2+3i')
print('2-i7')
#ex3
print('------EX3------')
print('valeur', 23+8 ,'de type' , type(23+8))
print('valeur', 23.3-8.2 , 'de type' ,type(23.2-8.2))
print('valeur', (17+1j)-(17+1j) , type((17+1j)-(17+1j)))
print('valeur', ((3+1j) * (3-1j)) , type((3+1j) * (3-1j)))
print('valeur', (3+1j) * 0 , type( (3+1j) * 0))
print('valeur', 23 / 8, type( 23 / 8))
print('valeur', 23 // 8 , type(23 // 8))
print('valeur', 2.0 ** 16 , type(2.0 ** 16))
print('valeur', 0 **0 , type(0 **0))
print('valeur', (1j) ** 2  , type((1j) ** 2 ))
print('valeur', 24.0 % 8, type(24.0 % 8))
print('valeur', (2+4j) / (1+3j) , type((2+4j) / (1+3j) ))
#ex4
print('------EX4------')
texte=('je suis un texte')
nombre=15
dec=3,67
print(type(texte))
print(type(nombre))
print(type(dec))
#ex5
print('------EX5------')
H=int(input('donner le hauteur'))
R=int(input('donner le rayon'))
pi=3.14
V=((1/3)*3.14*H*R*R)
print('le volume d''un cone droit est',V)
print
#ex6
print('------EX6------')
for i in range( 10):
    print(i+1)
#ex7
print('------EX7------')
a=int(input('donner un nombre'))
b=int(input('donner un nombre'))
if (((a>0) & (b>0)) | ((a<0) & (b<0))):
    print('leur produit est postif')
else:
    print('leur produit est négative')
#ex8
print('------EX8------')
a=int(input('donner un nombre'))
b=int(input('donner un nombre'))
c=a
a=b
b=c
print(' a est ',a,' b est ',b)




    

