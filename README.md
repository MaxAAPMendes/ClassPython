# ClassPython
Class course and learn of Python
#AULA 1***********************
#Python é case sensitive
print('essa é a função print')
print (2+5)
print('o resultado da soma é: ', 2+5)


#AULA 2***********************
#variáveis
#não há necessidade de declarar as variáveis

Minha_idade = 31
meu_nome = 'Max'
print('minha idade é ',Minha_idade)

type(Minha_idade)
type(meu_nome)
#type exibe o tipo de dados da variável

print('Meu nome é: ', meu_nome, 'e minha idade é: ', Minha_idade)

#AULA 2 a 5***********************
#tipos de dados de variáveis

nome = 'Max' #string
type(nome)
sobrenome = "Pinheiro"
#concatenar
nomeCompleto = nome +' '+sobrenome
print(nomeCompleto)

#comprimento de uma variável
len(nomeCompleto)

nomeCompleto[0] #índice para a primeira letra da string - array

nomeCompleto[-1] #vai percorrer de tras pra frente, neste caso retorna a última letra

#slicing - fatiar uma variável
nomeCompleto[0:2]
#o resultado será as duas primeiras letras
nomeCompleto[-2:-1]
#resultado será as duas últimas letras da palavra


#AULA 6***********************
#tipos de dados númericos

num1 = 2 #int
num2 = 5.5 #float

#condição if
if num2 > num1:
    print('é maior')
else:
     print('é menor')

#**********importar módulos

#math é um módulo matemático
import math #o módulo possui várias funções
#exemplo:
math.sqrt(16) #raiz quadrada de 16


#recebendo dados do usuário
nome = input('Digite seu nome:')
print(nome)
#input retorna um dado do tipo string

#conversão de tipos de dados
num1 = int(input('Digite um número:'))
num2 = int(input('digite o segundo número:'))
resultado = num1 + num2
print(resultado)

#AULA 8***********************
#listas e tuplas

#tuplas***********************************
meses = ('janeiro', 'fevereiro', 'março')
#as tuplas são imutávies

len(meses)#tamanho da tupla

'maio' in meses#resultado falso

lista = list(meses)#converte a tupla em lista
tupla = tuple(lista)#converte a lista em tupla


#listas***********************************
alunos = ['maria', 'joao', 'jose']

#add um item a uma lista:
alunos.append('ricardo')
print(alunos) #resultado ['maria', 'joao', 'jose', 'ricardo']

#para add um item na 2ª posição, por exemplo
alunos.insert(1, 'paula')
print(alunos) #resultado ['maria', 'paula', 'joao', 'jose', 'ricardo']

#mostrar índice da lista
alunos.index("joao")

#contar quantos itens tem 
alunos.count("maria")

#alterar a ordem dos itens da lista
alunos.reverse()

#ordenar a lista
alunos.sort()

#remover itens da lista
alunos.pop(1) #exclui o 2º elemento
alunos.remove('paula')#exclui o elemento específico

#concatenar
alunos2 = ['joana', 'jorge']
totalAlunos = alunos + alunos2
print(totalAlunos)#resultado ['joao', 'maria', 'ricardo', 'joana', 'jorge']

indice = 2
print(totalAlunos[indice]) #resultado 'ricardo'

#exercício 8
#criar uma tupla para guardar meses do ano
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
data_nasc = input('Qual a sua data de nascimento?')
mes = data_nasc[3:4]
print('você nasceu no mês de ', meses[int(mes)-1])





# conversão para float num2 = float(input('digite o segundo número:'))

#AULA 10***********************
#DICIONÁRIOS
#os itens de um dicionário são sempre formados por um par: uma chave e um valor
#a chave não é uma variável
joao = {'nome':'joao',
        'sobrenome': 'pereira',
        'profissão': 'programador python',
        'filhos': ['pedro', 'maria']
        }
# type(joao)
# resultado: class 'dict'
print(joao) #resultado {'nome': 'joao', 'sobrenome': 'pereira', 'profissão': 'programador python', 'filhos': ['pedro', 'maria']}
print(joao['profissão']) #resultado: 'programador python'

len(joao) #resultado: 4
del joao['filhos'] #exclui os filhos

joao['profissão'] = 'aposentado' #resultado substitui 'programdor python' por 'aposentado'

'sobrenome' in joao #o resultado será true

#looping for

for x in joao:
    print(x) #resultado:nome, sobrenome, profissão

for x in joao:
    print(x+' :'+joao[x])#resultado
                            #nome: joao
                            #sobrenome: pereira
                            # profissão: aposentado

#método get
joao.get('nome', 'esta informação não consta no cadastro')#caso não ache o 'nome', caso contrário retorna a msg
#resultado: 'joao'
joao.get('idade', 'esta informação não consta no cadastro')

#adicionando itens
joao['filhos'] = ['pedro','maria']
joao['filhos'].append('jorge')
print(joao['filhos'])#resultado: 'pedro', 'maria', 'jorge'

#apagando todas as informações de um dicionário. exclui apenas o conteúdo
joao.clear()
print(joao)#resultado: ''

#AULA 11***********************
#DICIONÁRIOS - método get

cores = {'branco': 'white',
         'vermelho': 'red',
         'verde': 'green'
    }
cor = input('Qual cor deseja traduzir:').lower()
#lower() transformará tudo o que for digitado em minúsculo
traducao = cores.get(cor, 'Cor não localizada')#primeiro parametro a variavel pesquisada
#segundo parâmetro a msg caso não encontre
print(traducao)




#AULA 12 **********************
#if, elif e else

idade = 18
if idade == 18:
    print('é 18')
    print('isso ainda está dentro do if')
print('não é 18')
#no if a edentação diz o que está dentro ou fora da condição

if idade > 18:
    print('maior que 18')
else:
    print('é diferente de 18')

if idade > 18:#se
    print('maior que 18')
elif idade == 18:  #senão se
        print('é 18')
else:
    print('menor que 18')

#operador diferente
if idade != 18:
    print('é diferente de 18')

#vazio ou zero são considerados falsos
#qq valor diferente disso é considerado verdadeiro
y = 0
if y:
    print('verdadeiro')
else:
    print('falso')


#AULA 13 **********************
#sexo = input('Digite o sexo M ou f:').lower()#lower se a pessoa digitar minusculo ou maiuscula

idade = int(input('digite a idade: '))
sexo = input('Digite o sexo M ou f:').lower()

if sexo == 'm':
    if idade < 18:
        print('homem menor de idade')
    else:
        print('homem maior de idade')

elif sexo == 'f':
    if idade < 18:
        print('mulher menor de idade')
    else:
        print('mulher maior de idade')
else:
    print('erro na entrada de dados')


#operadores logicos and e or

if idade == 18 and sexo == 'm':
    print('18 anos e masculino')

if idade == 18 or sexo != 'f':
    print('ou tem 18 anos ou é masculino')

#AULA 14 **********************


#AULA 15 **********************
#while

x = 0
pessoas = []#isso é uma lista vazia

while x < 4:
    nome = input('Qual o seu nome?')
    x += 1
    pessoas.append(nome)#append vai adicionando elementos à lista

print(pessoas)


x = 0
pessoas = []#isso é uma lista vazia

while 'joao' not in pessoas:
    nome = input('Qual o seu nome?')
    x += 1
    pessoas.append(nome)#append vai adicionando elementos à lista

print(pessoas)

#para while, pode ser add um continue ou break
#o continue faz com que volte ao início do loop sem executar o que está abaixo
#o break força a saída do loop



x = 0
pessoas = []#isso é uma lista vazia

while 'joao' not in pessoas:
    nome = input('Qual o seu nome?')
    if nome == 'joao':
        break
    x += 1
    pessoas.append(nome)#append vai adicionando elementos à lista

print(pessoas)

#aula 16*******************************************
#loop for

compras = ['arroz', 'feijão', 'carne']#isso é uma lista

for i in compras:
    print(i)#resultado arroz, feijao e carne
#***********
nome = 'max'

for i in nome:
    print(i)#resultado m, a, x
#***********
vendas = [100, 200, 300]

total = 0

for i in vendas:
    total += i
    
print(total)#resultado 600
#***********

#dicionário
cores = {'verde': 'green',
         'branco': 'white',
         'vermelho': 'red'}

for i in cores:
    print(i)#resultado verde, branco e vermelho

cores = {'verde': 'green',
         'branco': 'white',
         'vermelho': 'red'}

for i in cores:
    print(cores[i])#resultado green, white e red

#***********

compras = [['arroz', 'feijão', 'carne'], ['sabonete', 'xampoo']]#isso é uma lista de lista

for i in compras:
    print(i)
#resultado
##['arroz', 'feijão', 'carne']
##['sabonete', 'xampoo']

for i in compras:
    for item in i:
        print(item)

#resultado
##arroz
##feijão
##carne
##sabonete
##xampoo

for i in range(0,10):
    print(i)

##resultado
##0
##1
##2
##3
##4
##5
##6
##7
##8
##9

#aula 17*******************************************
#Exercícios loops


repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('Digite o nome do produto:')
    preco = float(input('Digite o valor do produto:'))
    fatura.append([produto,preco])
    total += preco
    repetir = input('Deseja comprar mais algum produto? S ou N').lower()

for i in fatura:
    print(i[0], '-', i[1])

#aula 18*******************************************
#Validação de dados

repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto:')
    try:#tenta realizar a operação
        preco = float(preco)

        if preco <= 0:
            print('o preço precisa ser maior que zero')
        else:
            valid_preco = True
    except:#se não conseguir realizar a opreção
        pront("Formato de preço inválido. Use apenas números e separe centavos com '.'")

##    while valid_preco == False:
##        preco = float(input('Digite o valor do produto:'))

    fatura.append([produto,preco])
    total += preco
    repetir = input('Deseja comprar mais algum produto? S ou N').lower()

for i in fatura:
    print(i[0], '-', i[1])


#aula 20*******************************************
#Funções

def nomedafunção():
    #comandos
    #comandos
#comandos fora da função


def mensagem():
    print('essa é uma função')

mensagem()#chamada da função

#***********

def mensagem(user):
    print('seja bem vindo, ', user, '!')

nome = input('qual o seu nome?').title() #title coloca primeira letra em maiúsculo

mensagem(nome) #resultado seja bem vindo, fulano!

#***********
def imc(peso, altura):
    valor_imc = peso / (altura*altura)
    return(valor_imc)
#fim da função

if imc(74, 1.82) > 32:
    print('obesidade')
else: print('tá de boa')


#aula 21e 22*******************************************
#Exercícios Funções

def imc(peso, altura):#calcula o imc
    imc = peso/ (altura*altura)
    return imc

def class_imc(sexo, peso, altura):
    valor_imc = imc(peso, altura)

    if sexo == 'm':
        if valor_imc < 20.7:
            return "Abaixo do peso"
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return "Peso Normal"
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return "Marginalmente acima do peso"
        elif valor_imc >= 27.8 and valor_imc < 31.1:
            return "Acima do peso ideal"
        elif valor_imc >= 31.1:
            return "Obesidade"
    else: return "erro de Cálculo"

    if sexo == 'm':
        if valor_imc < 19.1:
            return "Abaixo do peso"
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return "Peso Normal"
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return "Marginalmente acima do peso"
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return "Acima do peso ideal"
        elif valor_imc >= 32.3:
            return "Obesidade"
    else: return "erro de Cálculo"

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite seu sexo: M ou F').lower()
    if sexo != 'm' and sexo != 'f':
        print('valor inválido. digite M ou F.')
    else:
        valid_sexo = True
        print('\n')#pular linha

valid_peso = False
while valid_peso == False:
    peso = input('Digite o peso ex. 76.5')
    try:
        peso = float(peso)#converter pra float
        if peso <= 0 or peso > 350:
            print('Valor inválido. Número não pode ser 0 ou negativo nem acima de 350')
        else: valid_peso = True
        print('\n')#pular linha
    except:
        print('Use apenas números e separe os decimais com .')
        
        

valid_altura = False
while valid_altura == False:
    altura = input('Digite a altura ex. 1.8')
    try:
        altura = float(altura)#converter pra float
        if altura <= 0 or altura > 3:
            print('Valor inválido. Número não pode ser 0 ou negativo nem acima de 3')
        else: valid_altura = True
        print('\n')#pular linha
    except:
        print('Use apenas números e separe os decimais com .')
        
v_imc = str(imc(peso, altura))#converter em string para reduzir o número de casas decimais
c_imc = class_imc(sexo, peso, altura)

print('O seu imc é: ', v_imc[0:5])#slicing para reduzir o número de casas decimais
print('A sua classificação é ', c_imc)


#aula 23*******************************************
#criar e conectar módulos
#CONECTAR PROGRAMAS

import Nomedoarquivo as apelido

##comandos
#comandos

#chamada da função
Nomedoarq.Nomedafuncao


#aula 24*******************************************
#Módulos built-in
#módulos dos python

import math #módulo para operações matemáticas

math.ceil(3.2)#arredonda pra cima
math.floor(3.7)#arredondar pra baixo
math.fsum([1,2,3])#soma
vendas = [100,200,300]
math.fsum(vendas)
math.sqrt(16)#raiz quadrada


#*********************************
import time #módulo para hora e data

time.localtime()
hora = time.localtime().tm_hour
minuto = time.localtime().tm_min

print('Hora certa: ', hora, minuto)

time.clock()#mostra a quanto tempo a função foi chamada

inicio = time.clock()
fim = time.clock()
tempo = round(fim - inicio, 2)
#a função round arredonda as casas decimais, neste caso em duas casas


#aula 25*******************************************
#Módulos built-in
#módulos dos python

import random #módulo para número aleatórios

random.randint(0,10) #pega números de 0 a 10, neste caso

#****************criando um gerador de números - pra mega Sena
import random
def megasena():
    jogo = []
    while len(jogo) < 6:#enquanto jogo for menor que 6 - leg é comprimento, neste caso a qtd de elementos da lista
        num = random.randint(1,60)#escolher qq número entre 1 e sessenta
        if num in jogo:
            continue
        else:
            jogo.append(num)
    print(sorted(jogo))#sorted, função nativa do python - ordena lista

megasena()

#***********
alunos = ['joao', 'maria', 'pedro']
random.choice(alunos)#escolhe elementos, aleatoriamente na lista

#***********
random.sample(alunos, 2)#pega 2 elementos da lista


#aula 26*******************************************
#PIP gerenciador de comandos

pygames -> página para games em python

wxpython -> para estrutura de programas - layout visual inface com usuário

sqlalchemy -> para tratar com base de dados

beautiful soup documentantation - para web screping - para extrair conteúdos da internet

scypi.org 

#aula 26*******************************************

#montar um gráfico com módulo matplotlib.pyplot

x = [1,2,3,4,5]
y = ['a', 'b', 'c', 'd', 'e']

plt.xticks(x,y)#sticks cria legendas. 
plt.show()


#Livro Python Básico*******************************************
#for - página 49
nomes = ['jose', 'maria', 'pedro']
for i in nomes:
    print(i)
#resultado: jose, maria e pedro

dicionario = {'nome':'max', 'profissão': 'analista'}
for i in dicionario.keys():
    print(i)#resultado: nome e profissão

for i in dicionario.values():
    print(i)#resultado: max e analista

for i in dicionario:
    print(i)#resultado: nome e profissão

for i in range(5):
    print(i)#resultado 0,1,2,3,4

for i in range(3, 10):
    print(i)#resultado 3,4,5,6,7,8,9

#break**************
# sai completamente do loop
for i in range(3, 10):
    if i == 5:
        break
    print(i)#resultado: 3,4


#continue**************
#não executa mais nada naquele ciclo e parte para o próximo
for i in range(3, 10):
    if i == 5:
        continue
    print(i)#resultado: 3,4,5,6,7,8,9

#Livro Python Básico*******************************************
#while - página 53


i=0
while i < 5:
    print(i)
    i += 1
    #resultado 0,1,2,3,4


while True:
    nome = input("Digite o seu nome ou sair para sair:")
    if nome.lower() == "sair":
        break
    else:
        print("Nome digitado %s!" % nome.capitalize())

#lower() transforma tudo em minúsculo
#upper() transformatudo em maiúsculo
#capitalize() transforma a primeira letra em maíuscula, demais serão colocadas em minúsculo


#Livro Python Básico*******************************************
#funções - página 56

#função sem retorno e sem parâmetros
def imprime():
    print("Imprimiu")
imprime()#resultado: imprimiu


#função com retorno e com parâmetros
def cal(num):
    valor = num * 2
    return valor

base = 10
print(cal(base))#resultado: 20

#ou
def cal(num):
    valor = num * 2
    return valor
print(cal(10))#resultado: 20

#ou
def meunome(nome, idade):
    print("Meu nome é %s e tenho %d anos!" % (nome, idade))

meunome(nome="Max", idade=38)

def meunome(nome, idade):
    print("Meu nome é %s e tenho %d anos!" % (nome, idade))

meunome(idade=38, nome="Max")

#argumento *args e **kwargs
# *args com esse pode-se acessar os parâmetros como uma lista
#**kwrags pode-se acessar os oarâmetros como um dicionário

def print_tudo_2_vezes(*args):
for parametro in args:
print(parametro + "! " + parametro + "!")
print_tudo_2_vezes("Olá", "Python", "Felipe")
> Olá! Olá!
> Python! Python!
> Felipe! Felipe!

def print_info(**kwargs):
for parametro, valor in kwargs.items():
print(parametro + " - " + str(valor))
print_info(nome="Felipe", idade=30, nacionalidade="Brasil")
> nacionalidade - Brasil
> nome - Felipe
> idade - 30

#Livro Python Básico*******************************************
#módulo - página 60

def meunome(nome, idade):
    print("Meu nome é %s e tenho %d anos!" % (nome, idade))

#meunome(idade=38, nome="Max")


#importando apenas a função que deseja-se usar:

from nomedomodulo import nomedafuncao


#Livro Python Básico*******************************************
#datas - página 67

from datetime import date

print(date.today())

hoje = date.today()

hoje2 = hoje.day, hoje.month
print("hojé é: %d-%d" % hoje2)

#Python para Iniciantes - Udemy*******************************************
#aula 11
#pass, break econtinue

num = 10
While True:
    num=num-1
    if (num==4):
        continue#continua a execução do código
    print(num)
    if (num==3):
        break#interrompe a execução
pass#apenas passa a frente sem interferir em nenhuma parte do código
    
    
#Curso Python Web Scraping*******************************************
#aula 8 - meu primeiro web scraping

from urllib.request import urlopen
http = urlopen("http://www.google.com")
print(http.read())

#O python oferece duas excelentes ferramentas para realizar as tarefas
#requests da biblioteca urllib para carregar as páginas e
#beautifulSoup para realizar a análise das informações 

#Curso Python Web Scraping*******************************************
#aula 9 - EXPRESSÕES REGULARES

#o módulo re do Python fornece suporte a expressões regulares
#exemplo

variavel = re.funcao(padrao, string, flag)
#padrao = expressões regulares
#string é o texto onde está sendo procurado

import re

texto = ("bb Esta é uma aula de Pythoon. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula.")

#*******SEARCH************************
#search procura o padrão dentro do texto
#search retorna A PRIMEIRA OCORRÊNCIA ENCONTRADA - retorna a POSIÇÃO
resultado = re.search("Esta", texto)#resultado;<re.Match object; span=(0, 4), match='Esta'>
# span(0, 4), significa a partir da primeira posição e menor que a 4ª
print(resultado)


import re
padrao = "Esta"
texto = ("Esta é uma aula de Pythoon. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula.")

resultado = re.search(padrao, texto)

print(resultado)#resultado: None - no caso o pardrão era igual a abacaxi

#*******GROUP************************
#PARA RETORNAR O CONTEÚDO USA A FUNÇÃO group
print(resultado.group())#resultado: Esta


#*******CARACTERES ESPECIAIS - PONTO ".")************************
#ELE IRÁ ENCONTRAR QUALQUER CARACTER EXCETO O ENTER. Para localizar enter usar DOTALL
import re
padrao = "."
texto = ("Esta é uma aula de Pythoon. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula 9999 528.")
resultado = re.search(padrao, texto)
print(resultado.group())#RESULTADO: E

#*******CARACTERES ESPECIAIS - circonflexo "^")************************
#LOCALIZA UM PADRÃO NO INÍCIO DO TEXTO
padrao = "^Esta"
#RESULTADO: Esta

#*******CARACTERES ESPECIAIS - cifrão "$")************************
#localiza o padrão do final do texto
padrao = "aula$"
#Resultado: aula.

#*******CARACTERES ESPECIAIS - contrabarra "\")************************
#Permite usar caracteres especiais como se fossem comum
padrao = "\."


#*******CARACTERES ESPECIAIS - COLCHETES "[]")************************
#RANGE DE CARACTERES
padrao = "\."

#*******CARACTERES ESPECIAIS - findall************************
#função que retorna todas as ocorrências
padrao = "[aéeP]"
resultado = re.findall(padrao, texto)
print(resultado)#resultado: ['a', 'é', 'a', 'a', 'a', 'e', 'P', 'a', 'a', 'a', 'é', 'e', 'e', 'e', 'e', 'a', 'e', 'e', 'e', 'e', 'e', 'a', 'a', 'a']


padrao = "[A-Z]"
resultado = re.findall(padrao, texto)
print(resultado)#resultado: ['E', 'P', 'E', 'E', 'R', 'E']

padrao = "[0-9]"
resultado = re.findall(padrao, texto)
print(resultado)#resultado: ['9', '9', '9', '9', '5', '2', '8']

#* retorna uma ou mais ocorrência "a*"
#+
# ? diz que aquele padrão não é obrigatório
padrao = ([0-9{2}][\.]?[0-9]{3})#diz que o ponto não é obrigatório
#\d busca por caractesres numéricos
#\D traz todos os caracteres que NÃO são números
#\s qq caracter de espaçamento "[\t\n\r\f\v]"
#\S qq caractere que NÃO SEJA DE  PESÇAMENTO
#\w caractere alfanumériico ou sublinhado "[a-zA-Z0-9_]"
#\W caractere que não seja alfanumérico ou sublinhado "[^a-zA-Z0-9_]"
#{} quantidade de ocorrência
padrao = "\d{2}"# localiza caracteres números com dois dígitos
# | ou lógico
# () grupo de expressões
padrao = "(a) | (\d)"#localizar a ou números

padrao = re.compile("e", re.IGNORECASE)#vai localizar todas as ocorrências, independente se maiúscula ou minúscula








































