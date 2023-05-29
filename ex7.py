velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Voce foi multado!")
    print ("O valor da multa e de R$", multa)