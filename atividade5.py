# Exercício 1: Função que calcula a gorjeta

def calcular_gorjeta(valor_conta, porcentagem):
    gorjeta = valor_conta * (porcentagem / 100)
    return gorjeta

conta = 120.00
porcentagem = 10
print(f"Gorjeta: R${calcular_gorjeta(conta, porcentagem):.2f}")


# Exercício 2: Função que calcula a idade em dias

from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade * 365

print(f"Idade em dias: {idade_em_dias(2000)}")


# Exercício 3: Verifica se é palíndromo


def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum()) 
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

print(eh_palindromo("A cara rajada da jararaca"))
print(eh_palindromo("Olá mundo"))