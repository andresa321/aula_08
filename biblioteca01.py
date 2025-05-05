def imprimirnome(nome):
    print(f"ola {nome}")

def numeros(t):
    #x para colocar os numeros
    for x in range(1,t+1,1):
        #y para contar ele de 0 ate x
        for j in range(0,x):
            print(x, end=" ")
        print()

def contar_vogais(texto):
  #vogais para achar no texto
    vogais = "aeiou"
  #contador para contar as vogais
    contador = 0
    for x in texto:
        if x in vogais:
            contador += 1
    print(contador)

def estoque(produto,qtdd,valorunitario):
    valortotal=qtdd*valorunitario
    return produto,valortotal

def numero(n):
    resposta="z"
    if n > 0:
        resposta="P"
    elif n < 0:
        resposta="N"
    return resposta

def somar(*num):
    soma = 0
    for x in range(len(num)):
        soma = soma + num[x]
        print(soma)

def letras(texto):
    contador = 0
    for x in range(len(texto)-1,-1,-1):
        print(texto[x], end=" ")
        if texto[x] not in " ":
            contador+=1
    print(f"\n {contador}")

def lista(l):
    nova_lista=[]
    for x in l:
        if x not in nova_lista:
            nova_lista.append(x)
        print(lista)
        print(nova_lista)








