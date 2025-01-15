def calcular_salarios(n, funcionarios):
    # Lista para armazenar os resultados
    resultados = []
    
    # Para cada funcionário na lista
    for funcionario in funcionarios:
        nome = funcionario['nome']
        horas_trabalhadas = funcionario['horas_trabalhadas']
        valor_hora = funcionario['valor_hora']
        
        # Calculando o salário
        salario = horas_trabalhadas * valor_hora
        
        # Formatação do resultado com duas casas decimais
        resultados.append(f"{nome}: {salario:.1f}")
    
    return resultados

# Leitura da entrada
n = int(input())  # Número de funcionários
funcionarios = []
for _ in range(n):
    nome = input()
    horas_trabalhadas = int(input())
    valor_hora = float(input())
    funcionarios.append({'nome': nome, 'horas_trabalhadas': horas_trabalhadas, 'valor_hora': valor_hora})

# Resultado
resultado = calcular_salarios(n, funcionarios)
for res in resultado:
    print(res)
