# 1. Ler log de treinamento, calcular média e desvio padrão de tempos

import re
import statistics

def calcular_media_desvio(log_file):
    tempos = []
    with open(log_file, 'r', encoding='utf-8') as file:
        for linha in file:
            match = re.search(r"Tempo de execução:\s*([\d.]+)s", linha)
            if match:
                tempos.append(float(match.group(1)))
    
    if tempos:
        media = statistics.mean(tempos)
        desvio = statistics.stdev(tempos)
        print(f"Média: {media:.2f}s")
        print(f"Desvio padrão: {desvio:.2f}s")
    else:
        print("Nenhum tempo encontrado no arquivo.")

calcular_media_desvio("log.txt")


# 2. Escrever dados em um arquivo CSV

import csv

def escrever_csv(nome_arquivo):
    pessoas = [
        {"Nome": "Ana", "Idade": 25, "Cidade": "São Paulo"},
        {"Nome": "Bruno", "Idade": 30, "Cidade": "Rio de Janeiro"},
        {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"}
    ]

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ["Nome", "Idade", "Cidade"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for pessoa in pessoas:
            escritor.writerow(pessoa)


escrever_csv("pessoas.csv")


# 3. Ler dados de um arquivo CSV e exibir

import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")


ler_csv("pessoas.csv")


# 4. Ler e escrever dados em um arquivo JSON

import json

def escrever_json(nome_arquivo):
    pessoa = {
        "Nome": "Lucas",
        "Idade": 28,
        "Cidade": "Curitiba"
    }

    with open(nome_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)

def ler_json(nome_arquivo):
    with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
        pessoa = json.load(arquivo)
        print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Cidade: {pessoa['Cidade']}")


escrever_json("pessoa.json")
ler_json("pessoa.json")