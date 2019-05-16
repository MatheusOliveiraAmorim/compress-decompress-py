def leitura(nome):
    file = open(nome, 'r')
    lista = []
    for line in file:
        lista.append(line.rstrip())
    file.close()
    return (lista)

def criar(nome):
    file = open(nome, 'w')
    file.write('')
    file.close()

def escrever(nome, linha):
    file = open(nome, 'a')
    file.write(linha + '\n')
    file.close()

def sequencia(apontador, string):
    contador = 0
    caractere = string[apontador]
    i = 0
    while string[apontador + i] == caractere:
        contador += 1
        i += 1
        if apontador + i == len(string):
            break
    return (contador, caractere)

def compressao(string):
    apontador = 0
    resultado = ''
    while apontador < len(string):
        contador, res_temp = sequencia(apontador, string)
        if contador > 4:
            resultado = resultado + '$' + str(contador) + res_temp
        else:
            resultado = resultado + contador * res_temp
        apontador += contador
    return (resultado)

def descompressao(string):
    resultado = ''
    contador = 0
    while contador < len(string):
        if string[contador] == '0':
            resultado = resultado * int(string(contador - 1))
            contador += 2
        else:
            resultado = resultado + string[contador]
            contador += 1
    return (resultado)

criar('sup.txt')
linhas = leitura('supressao.txt')
for l in linhas:
    escrever('sup.txt', compressao(1))

criar('supressao1.txt')
linhas = leitura('supressao.txt')
for l in linhas:
    escrever('sup.txt', descompressao(1))