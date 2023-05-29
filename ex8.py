salario = float(input("Digite o salario do funcionario:"))

if salario > 8250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

    novo_salario = salario + aumento 

print("O valor do aumento e: R$", aumento)
print("O novo salario e: R$", novo_salario)