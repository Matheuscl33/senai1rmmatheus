def converter_medida(metros):
    centimetros = metros * 1000
    milimetros = metros * 1000
    return centimetros, milimetros

metros = float(input("Digite o valor em metros: "))

centimetros, milimetros = converter_medida(metros)

print(f"{metros} metros equivalem a {centimetros} centimetros e {milimetros} milimetros.")