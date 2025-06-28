# 1. Conversor de Moeda

reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15


dolares = reais / taxa_dolar
euros = reais / taxa_euro

print("=== Conversor de Moeda ===")
print(f"Valor em Reais: R$ {reais:.2f}")
print(f"Em Dólares: US$ {dolares:.2f}")
print(f"Em Euros: € {euros:.2f}")


# 2. Calculadora de Desconto


produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20


valor_desconto = (desconto_percentual / 100) * preco_original
preco_final = preco_original - valor_desconto


print("\n=== Calculadora de Desconto ===")
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")



# 3. Calculadora de Média Escolar


nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3


print("\n=== Calculadora de Média Escolar ===")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média final: {media:.2f}")



# 4. Calculadora de Consumo de Combustível


distancia_km = 300
combustivel_litros = 25

consumo_medio = distancia_km / combustivel_litros


print("\n=== Consumo de Combustível ===")
print(f"Distância percorrida: {distancia_km} km")
print(f"Combustível gasto: {combustivel_litros} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")