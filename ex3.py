nota1 = float( input("Informe uma nota: ") )
nota2 = float( input("Informe uma nota: ") )
nota3 = float( input("Informe uma nota: ") )

media = (nota1 + nota2 + nota3)/3

if media >= 6:
    print ("Aprovado")
else:
    if media >= 5:
        print ("Conselho de classe")
    else:
        print ("Reprovado")
 
print("Sua media foi: ", media)