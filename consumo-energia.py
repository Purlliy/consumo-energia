import os
def centro(texto):
    print(texto.center(100))

#Entrada de dados
aparelho = input("Digite o aparelho do aparelho: ")
os.system('cls')

potencia = int(input("Digite a potência do aparelho em watts: "))
os.system('cls')

horasDia = float(input("Digite o tempo médio diário de uso do aparelho em horas: "))
os.system('cls')

#Processamento (cálculo do consumo mensal)
consumoMensal = (potencia * horasDia * 30) / 1000
custoEstimado = round(consumoMensal * 0.75, 2)

#Saída (exibição do consumo mensal e custo estimado)
centro(f"O aparelho: {aparelho}")
centro(f"Tem o consumo estimado de: {consumoMensal} kWh/mês")
centro(f"Com o custo estimado de: R$ {custoEstimado}")