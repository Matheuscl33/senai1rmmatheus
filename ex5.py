def calcular_novo_salario(salario):
    reajuste = salario * 0,12
    novo_salario = salario + reajuste
    return novo_salario

salario_atual = float( input("Digite o salario atual do funcionario: ") )

novo_salario = calcular_novo_salario(salario_atual)

print("O novo salario com 12% de reajuste e:", novo_salario)