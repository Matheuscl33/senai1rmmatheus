def area(largura, comprimento):\
    return largura * comprimento

largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))

resultado = area(largura, comprimento)

print("A area do terreno e:", resultado, "metros quadrados.")