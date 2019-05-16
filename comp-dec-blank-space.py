#Abre o arquivo com o texto em modo de leitura(r)
file = open("./arquivo_original.txt", "r")
#Lê o conteúdo do arquivo aberto
ffile = file.read()
#Cria outros 2 arquivos em modo de escrita(w)
file2 = open("./arquivo_comprimido.txt", "w")
file3 = open("./arquivo_descomprimido.txt", "w")

#Variável para contar o espaço
i = 0

#Variável que armazenará o texto comprimido
strin = ""


########################################################################################################################
# COMPRESSÃO                                                                                                           #
########################################################################################################################


#Lista que armazenará todos os caracteres do arquivo
lst = []
#For que verificará cada linha do arquivo lido
for line in ffile:
    #For verificará cada caractere nas linhas arquivo lido e os adicionará a lista de caracteres
    for ch in line:
        #Adiciona o caractere a lista previamente criada
        lst.append(ch)

#Conta quantos itens da lista existem no total(contando com espaços em branco)
cod = len(lst)
#Seta um contador de caracteres para comparação
d = 0
#Enquanto o contador de caracteres for menor que o numero total de caracteres
while d < cod:
    #Se algum dos caracteres contados forem espaço em branco, então adiciona-se +1 ao contador de espaços em branco
    if lst[d] == " ":
        #Assim teremos o número total de espaço em branco
        i += 1
    elif i > 0:
        #Caso seja encontrado algum espaço em branco substitui-se por "b" mais o número de espaços em branco encontrados previamente e grava na variavel
        strin += "b"
        strin += str(i)
        #Ao fim, zera-se o contador de espaços em branco para não interferir em caracteres posteriores
        i = 0
    if lst[d] != " ":
        #Caso o caractere encontrado não seja um espaço em branco ele é simplesmente adicionado a variavel, sem nenhum tratamento
        strin += lst[d]
    #Realizado o processo de substituição, soma-se 1 no contador de caracteres
    d += 1
print(strin)
#Escreve a variável no arquivo previamente criado
file2.write(strin)

########################################################################################################################
# DESCOMPRESSÃO                                                                                                        #
########################################################################################################################

#Lista que armazenará o conteúdo descomprimido
lst2 = []

#Função que verifica se o parametro passado é um número inteiro
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Para cara caractere dentro da variável onde está armazenada o conteudo comprimido
for ch in strin:
    #Atribue-se o caractere a uma variável
    hi = ch
    #Utiliza a função para descobrir se o caractere é um número passando a variavel anterior como parametro
    ho = is_number(hi)
    if hi == "b":
        print("oi")
    elif ho == True:
        #Caso um número tenha sido encontrado na string transforma-se ele em um número inteiro
        hu = int(hi)
        #Adiciona-se o número de espaços em branco multiplicado pelo número encontrado anteriormente à lista
        #DISCLAIMER: Caso o documento possua algum trecho com mais de 9 espaços aqui o código interpretará cada número
        #individualmente, não devolvendo o devido número de espaços
        lst2.append(" " * hu)
    else:
        #caso não se trate de um espaço em branco, o caractere é apenas adicionado a lista
        lst2.append(ch)

#Transforma-se o conteúdo descomprimido em texto e o atribui a uma variável
res = str(lst2)

#cria variáveis auxiliares na construção do arquivo descomprimido
#contador comparativo
we = 0
#contador de elementos totais da lista
wo = len(lst2)
#Zera a variável com os elementos para reconstrui-la
res = ""

#Enquanto o contador for menor que o numero de elementos verificados na lista
while we < wo:
    #adiciona o caractere a variavel final
    res += lst2[we]
    #soma mais um no contador
    we += 1

#Escreve no arquivo o texto descomprimido obtido com a variável final
file3.write(res)

#Fecha os arquivos abertos
file.close()
file2.close()
file3.close()