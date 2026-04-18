# ex1
def comprimento_string(string):
    return len(string)

texto = "teste texto"

print("ex1")
print(comprimento_string(texto))
print("-" * 20)


def inversao_string(string):
    return string[::-1]

print("ex2")
print(inversao_string(texto))
print("-" * 20)

#ex3
def contar_vogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador

def contar_consoantes(string):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in string:
        if char.isalpha() and char not in vogais:
            contador += 1
    return contador

print("ex3")
print("Vogais:", contar_vogais(texto))
print("Consoantes:", contar_consoantes(texto))
print("-" * 20)

#ex4
def remover_espacos_extra(string):
    return ' '.join(string.split())

print("ex4")
texto_com_espacos = "   teste   texto   "
print(remover_espacos_extra(texto_com_espacos))
print("-" * 20)

#ex5
def verificar_palindromo(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    else:
        return False
    
print("ex5")
texto_palindromo = "A man a plan a canal Panama"
print(verificar_palindromo(texto_palindromo))
print("-" * 20)

#ex6
def tokenizar_string(string):
    string_tokenizada = string.split()
    string_minúscula = [x.lower() for x in string_tokenizada]
    string_limpa = [x.strip('.,!?;:()') for x in string_minúscula]

    return string_limpa

print("ex6")
texto_tokenizar = "Teste de tokenização, com pontuação!"
print(tokenizar_string(texto_tokenizar))
print("-" * 20)

#ex7
def substituir_letras(string, letra_antiga, letra_nova):
    for x in string:
        if x == letra_antiga:
            string[string.find(letra_antiga)] = letra_nova
    return string

print("ex7")
texto_substituir = "teste texto"
print(substituir_letras(texto_substituir, "t", "T"))
print("-" * 20)