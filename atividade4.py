# Exercício 1: Gerador de senha aleatória com random

import random
import string

def gerar_senha(qtd_caracteres):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(qtd_caracteres))
    return senha

tamanho = int(input("Quantos caracteres a senha deve ter? "))
senha = gerar_senha(tamanho)
print(f"Senha gerada: {senha}")


# Exercício 2: Gerador de perfil aleatório com API Random User Generator

import requests

def gerar_perfil():
    url = 'https://randomuser.me/api/'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao consultar a API.")

gerar_perfil()


# Exercício 3: Consulta de endereço via API ViaCEP

import requests

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if 'erro' not in dados:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
        else:
            print("CEP não encontrado.")
    else:
        print("Erro na consulta.")

cep_input = input("Digite o CEP (somente números): ")
consultar_cep(cep_input)


# Exercício 4: Cotação de moeda via AwesomeAPI

import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            print(f"Moeda: {moeda} para BRL")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Valor máximo: R$ {info['high']}")
            print(f"Valor mínimo: R$ {info['low']}")
            print(f"Data e hora: {info['create_date']}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao consultar a cotação.")

codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(codigo_moeda)