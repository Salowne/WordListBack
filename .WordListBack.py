#!/usr/bin/python3
# /18/05/2022
# encoding: utf-8
# Progamador por Hobby.

"""
MIT License

Copyright (c) 2022 Zwdeff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__ = "Zwdeff"
__version__ = "0.3"

"""
# Bem Vindo ao WordlistBack um script pequeno feito pra criacao de
# Lista de palavras Para Brutforce: []
# Jamail_Magnestar_ Script [Beta] [Versao +0.0+] Senhas para Brutforce:
# este script foi criado em versao 0.0 Hoje esta em sua versao 0.3 ,
"""

from os import system
from sys import *
from time import *
import random
"""
try:
  import itertools
except ImportError:
   try:
      system("sudo pip3 install itertools")
   except ImportError:
      print("\033[0;31mError: Por favor Instale "\
           +"itertools, para Proseguir [com pip3].\033[m")
"""

u1='\033[1;31m'
u2='\033[1;32m'
u3='\033[1;33m'
u4='\033[1;34m'
u5='\033[1;35m'
u6='\033[1;36m'
u7='\033[1;37m'
u0='\033[m'


__banner__ = u7+'000000000000000000000000000000000000000000000\n'\
            +'8=88=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=88=8\n'\
            +'[LORD] [YUKI][Snow/Lord] Word List para Backdoor.\n'\
            +'[LORD] [YUKI] CP09 ENDGame Backdoor:\n'\
            +'[LORD] [SQL] Ctrl C D X Y N Z: New Mornigstar:\n'\
            +'[LORD] ????????????????: N00B Big Bang:\n'\
            +'8=88=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=88=8\n'\
            +'000000000000000000000000000000000000000000000\n\n'+u0

__infoScript__ = u4+'Author: '+u7+ __author__ +\
                 u4+'\nVersao: '+u7+ __version__ +'\n\n'+ u0
__updateZIEE__ = u6+'Escolha sua opcao para a criacao da Wordlist.\n'\
              +u1+'+ -- -- +=[ - Wordlist Combinacoes 0, 1, 2, 3 em Desenvolvimento. ]\n'\
              +u1+'+ -- -- +=[ - Jamail_Magnestar Para voltar para Home. ]\n'\
              +u1+'1 - Wordlist Normal de 4 Combinacoes.\n'\
              +u1+'2 - Wordlist de 5 Combinacoes.\n'\
              +u1+'3 - Wordlist de 6 Combinacoes. (Nivel Hard).\n'\
              +u1+'4 - Wordlist de 7 Combinacoes. (Nivel Hard).\n'\
              +u1+'5 - Wordlist de 8 Combinacoes. (Nivel Hard).\n'\
              +u1+'0 - Ctrl C, Ctrl Z or exit para Sair.\n\n'

if version_info < (3, 0):
   print(u1+'Error: Progama suportado somente em Python3x.'+u0)
   sleep(2)
   exit()

# Uma lista de palavras pode conter ate 8 combinacoes que voce pode utilizar
# na criacao de suas senhas. Na Opcao Hard voce esta sujeito a ter uma senha
# muito grande entao utilize as melhores palavaras ou nao obterar o resultado
# esperado fazendo isso voce pode usar mais letras para que sua lista de senhas
# seja mais afundo na possivel senha que voce deseja obter, utilize frazes
# pequenas para que suas senhas nao fique muito grandes.

system("clear")
def Going():
  try:

# BANNER DA SEGUNDA DIVISAO../;
# [2] SEGUNDA DIVISAO../;

     print(u4+"Bem-vindo ao Gerador de Lista de palavras."+u0)
     print(u7+"Hawaii I am really sorry. [-] []: [-] [-] [-] []: [-]"+u0)
     print(u4+"Script em Desenvolvimento, Crie sua Wordlist.\n"+u0)
     print(__banner__)
     print(__infoScript__)
     print(__updateZIEE__)
     print(u5+"Crie sua Lista de senhas Escolhas as combinacoes ..\n\n"+u0)
     sora = input(u4+"Going input in G*: "+u0)

     while True:
        def Generate():
          try:
             def Erro():
               try:
                  def inteiro():
                    try:
                       if sora == "exit" or sora == "EXIT" or sora == "Exit"\
                        or sora == "Sair" or sora == "SAIR" or sora == "sair"\
                         or sora == "0" or sora == "00":
                          print(u1+"Going Out .."+u0)
                          sleep(2)
                          exit()

                       elif sora == "99":
                            print(u1+"Going Out .."+u0)
                            sleep(2)
                            exit()

                       elif sora == "06" or sora == "6":
                            system("clear")
                            Going()

                            """
                            def npr():
                              try:
                                 print(u1+"Bem vindo ao (Nivel Hard). Combinacao 3"+u0)
                                 try:
                                    may = int(input(u4\
                                                    +"Enter: Numero de Quantas"\
                                                    +" Combinacoes *: "))
                                 except Exception:
                                    print(u1+"Erro: Utilize Somente Numeros Ex: 88"+u0)
                                    sleep(5)
                                    system("clear")
                                    Going()

                                 if may <= 10:
                                    count = 0
                                    data = []
                                    lists = []
                                    for i in range(0, may):
                                        u = input(u4+"Enter: Elemento Para Matris: *: "\
                                                    +"\033[m")
                                        data.append(u)
                                    try:
                                       limite = int(input(u6+"Quantas senhas a ser Gerada: *: "\
                                                            +"\033[m"))
                                    except Exception:
                                       print(u1+"Utilize somente numeros."+u0)
                                       sleep(5)
                                       system("clear")
                                       Going()

                                    chars = "".join(data)
                                    for i in range(1, len(chars) + 1):
                                        for p in itertools.permutations(data, len(data)):
                                            lists.append("".join(p))
                                    passl = open(input(u4+"\nEnter: Nome para o Arquivo: *: ")\
                                                         +".txt", 'w')

                                    for item in lists:
                                        print(u2+str(item)+u0)
                                        passl.write(str(item) + "\n")
                                        count = count +1

                                        if count == limite:
                                           passl.close()
                                           print(u2+"Passwords salvos no Arquivo "\
                                                   +passl.name+"\033[m")
                                           sleep(4)
                                           Going()
                                 else:
                                     print(u1+"Erro: Utilize numeros entre 1 e 10"+\
                                             +"\033[m")
                                     npr()

                              except Exception as e:
                                 print(e)
                            if __name__ == "__main__":
                               npr()
                            """

                       elif sora == "CLOSEPH" or sora == "closeph" or sora == "closePH"\
                         or sora == "Close" or sora == "close" or sora == "CLOSE"\
                          or sora == "Closep" or sora == "closep" or sora == "CLOSEP"\
                           or sora == "ClosePH" or sora == "Clear" or sora == "clear"\
                            or sora == "CLEAR" or sora == "Closeph":

                            print(u1+"CLOSEPH for Home!"+u0)
                            sleep(2)
                            system("clear")
                            Going()

                       elif sora == "Jamail_Magnestar" or sora == "jamail_magnestar"\
                         or sora == "Jamail_magnestar" or sora == "jamail_Magnestar":
                            print(u1+"CLOSEPH for Home!"+u0)
                            sleep(2)
                            system("clear")
                            Going()

                       elif sora == "2" or sora == "02":
                          def sora2():
                            try:
                               count = 0
                               print(u6+"Crie suas senhas de 5"\
                                     +" Combinacoes."+u0)
                               nu1 = input(u3+"Entrer com a 1*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nu1 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora2()

                               if " " in nu1:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora2()

                               if nu1 == "Jamail_Magnestar"\
                                or nu1 == "jamail_magnestar"\
                                 or nu1 == "Jamail_magnestar"\
                                  or nu1 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nu2 = input(u3+"Entrer com a 2*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)

                               if nu2 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora2()

                               if " " in nu2:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora2()

                               if nu2 == "Jamail_Magnestar"\
                                or nu2 == "jamail_magnestar"\
                                 or nu2 == "Jamail_magnestar"\
                                  or nu2 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nu3 = input(u3+"Entrer com a 3*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)

                               if nu3 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora2()

                               if " " in nu3:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora2()

                               if nu3 == "Jamail_Magnestar"\
                                or nu3 == "jamail_magnestar"\
                                 or nu3 == "Jamail_magnestar"\
                                  or nu3 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nu4 = input(u3+"Entrer com a 4*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)

                               if nu4 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora2()

                               if " " in nu4:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora2()

                               if nu4 == "Jamail_Magnestar"\
                                or nu4 == "jamail_magnestar"\
                                 or nu4 == "Jamail_magnestar"\
                                  or nu4 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nu5 = input(u3+"Entrer com a 5*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)

                               if nu5 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora2()

                               if " " in nu5:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora2()

                               if nu5 == "Jamail_Magnestar"\
                                or nu5 == "jamail_magnestar"\
                                 or nu5 == "Jamail_magnestar"\
                                  or nu5 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               sleep(2)

                               arq = open(input(u2+"\n\nEntre com o nome"\
                                        +" do Arquivo *: "+u0)+ ".txt", "w")

                               if arq.name == "Jamail_Magnestar.txt"\
                                or arq.name == "jamail_magnestar.txt"\
                                 or arq.name == "Jamail_magnestar.txt"\
                                  or arq.name == "jamail_Magnestar.txt":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               print(u2+"Gerando Wordlist."+u0)
                               if arq != "":
                                  sleep(2)
                               else:
                                  Erro()


                               enb = input(u4+"Quantas senhas a ser"\
                                          +" Gerada? *: "+u0)
                               if enb == "Jamail_Magnestar"\
                                or enb == "jamail_magnestar"\
                                 or enb == "Jamail_magnestar"\
                                  or enb == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               enb = int(enb)
                               if enb != int(enb):
                                  print(u1+"Error: Para esta operacao use"\
                                       +" numeros inteiros. EX: 0665."+u0)
                                  sleep(4)
                                  Erro()

                               else:
                                  sleep(1)
                               sleep(2)

                               deff = [''+nu1+'',\
                                       ''+nu2+'', ''+nu3+'',\
                                       ''+nu4+'',''+nu5+'']
                               for i in range(enb):
                                   count = count +1
                                   nu1 = random.choice(deff)
                                   nu2 = random.choice(deff)
                                   nu3 = random.choice(deff)
                                   nu4 = random.choice(deff)
                                   nu5 = random.choice(deff)
                                   arq.write(str(nu1)+str(nu2)+str(nu3)\
                                            +str(nu4)+str(nu5)+'\n')
                                   print(u3+str(nu1)+str(nu2)\
                                        +str(nu3)+str(nu4)+str(nu5)+u0)

                                   if int(count) == int(enb)+1:
                                      arq.close()

                               sleep(2)
                               print("\n")
                               print(u2+'\nCompleto. '+str(enb)\
                                    +' Senhas salvas no Arquivo %s\033[m' %(arq.name))
                               sleep(1)
                               ext = input(u4+"Deseja sair do Script-PROGAMA"\
                                          +" (Y/n) *: "+u0)
                               if ext == 'y' or ext == 'Y':
                                  print(u1+"Going Out .."+u0)
                                  sleep(2)
                                  exit()

                               if ext == 'n' or ext == 'N':
                                  print(u3+"Voltando para Casa."+u0)
                                  sleep(2)
                                  Going()

                            except Exception as e:
                               print(e)
                          if __name__ == "__main__":
                             sora2()

#/; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /;
# [3] TERCEIRA DIVISAO../*;
# Script simples para/Gerar Listas de Palavras/WordList.
#/; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /; /;

                       elif sora == "3" or sora == "03":
                          def sora3():
                            try:
                               count = 0
                               print(u1+"Bem vindo ao (Nivel Hard)."+u0)
                               print(u6+"Crie suas senhas de 6"\
                                     +" Combinacoes."+u0)
                               nn1 = input(u7+"Entrer com a 1*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nn1 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora3()

                               if " " in nn1:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora3()

                               if nn1 == "Jamail_Magnestar"\
                                or nn1 == "jamail_magnestar"\
                                 or nn1 == "Jamail_magnestar"\
                                  or nn1 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nn2 = input(u7+"Entrer com a 2*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nn2 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora3()

                               if " " in nn2:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora3()
                               if nn2 == "Jamail_Magnestar"\
                                or nn2 == "jamail_magnestar"\
                                 or nn2 == "Jamail_magnestar"\
                                  or nn2 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nn3 = input(u7+"Entrer com a 3*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nn3 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora3()

                               if " " in nn3:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora3()

                               if nn3 == "Jamail_Magnestar"\
                                or nn3 == "jamail_magnestar"\
                                 or nn3 == "Jamail_magnestar"\
                                  or nn3 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nn4 = input(u7+"Entrer com a 4*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nn4 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora3()

                               if " " in nn4:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora3()

                               if nn4 == "Jamail_Magnestar"\
                                or nn4 == "jamail_magnestar"\
                                 or nn4 == "Jamail_magnestar"\
                                  or nn4 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nn5 = input(u7+"Entrer com a 5*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nn5 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora3()

                               if " " in nn5:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora3()

                               if nn5 == "Jamail_Magnestar"\
                                or nn5 == "jamail_magnestar"\
                                 or nn5 == "Jamail_magnestar"\
                                  or nn5 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nn6 = input(u7+"Entrer com a 6*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nn6 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora3()

                               if " " in nn6:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora3()

                               if nn6 == "Jamail_Magnestar"\
                                or nn6 == "jamail_magnestar"\
                                 or nn6 == "Jamail_magnestar"\
                                  or nn6 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               sleep(2)

                               arq = open(input(u2+"\n\nEntre com o nome"\
                                        +" do Arquivo *: "+u0)+ ".txt", "w")

                               if arq.name == "Jamail_Magnestar.txt"\
                                or arq.name == "jamail_magnestar.txt"\
                                 or arq.name == "Jamail_magnestar.txt"\
                                  or arq.name == "jamail_Magnestar.txt":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               print(u2+"Gerando Wordlist."+u0)
                               if arq != "":
                                  sleep(2)

                               else:
                                  Erro()

                               enb = input(u4+"Quantas senhas a ser"\
                                          +" Gerada? *: "+u0)

                               if enb == "Jamail_Magnestar"\
                                or enb == "jamail_magnestar"\
                                 or enb == "Jamail_magnestar"\
                                  or enb == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               enb = int(enb)
                               if enb != int(enb):
                                  print(u1+"Error: Para esta operacao use"\
                                       +" numeros inteiros. EX: 0665."+u0)
                                  sleep(4)
                                  Erro()

                               else:
                                  sleep(1)

                               sleep(2)
                               deff = [''+nn1+'',\
                                       ''+nn2+'', ''+nn3+'',\
                                       ''+nn4+'',''+nn5+'',\
                                       ''+nn6+'']
                               for i in range(enb):
                                   count = count +1
                                   nn1 = random.choice(deff)
                                   nn2 = random.choice(deff)
                                   nn3 = random.choice(deff)
                                   nn4 = random.choice(deff)
                                   nn5 = random.choice(deff)
                                   nn6 = random.choice(deff)
                                   arq.write(str(nn1)+str(nn2)+str(nn3)\
                                            +str(nn4)+str(nn5)+str(nn6)+'\n')
                                   print(u3+str(nn1)+str(nn2)\
                                        +str(nn3)+str(nn4)\
                                        +str(nn5)+str(nn6)+u0)

                                   if int(count) == int(enb)+1:
                                      arq.close()

                               sleep(2)
                               print("\n")
                               print(u2+'\nCompleto. '+str(enb)\
                                    +' Senhas salvas no Arquivo %s\033[m' %(arq.name))
                               sleep(1)

                               ext = input(u4+"Deseja sair do Script-PROGAMA"\
                                          +" (Y/n) *: "+u0)
                               if ext == 'y' or ext == 'Y':
                                  print(u1+"Going Out .."+u0)
                                  sleep(2)
                                  exit()

                               if ext == 'n' or ext == 'N':
                                  print(u3+"Voltando para Casa."+u0)
                                  sleep(2)
                                  Going()

                            except Exception as e:
                               print(e)
                          if __name__ == "__main__":
                             sora3()

# [4] QUARTA DIVISAO../;

                       elif sora == "4" or sora == "04":
                          def sora4():
                            try:
                               count = 0
                               print(u1+"Bem vindo ao (Nivel Hard)."+u0)
                               print(u6+"Crie suas senhas de 7"\
                                    +" Combinacoes."+u0)

                               ao1 = input(u7+"Entrer com a 1*"\
                                          +" combinacao para"\
                                          +" Gerar Ex: @$& *: "+u0)
                               if ao1 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora4()

                               if " " in ao1:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora4()

                               if ao1 == "Jamail_Magnestar"\
                                or ao1 == "jamail_magnestar"\
                                 or ao1 == "Jamail_magnestar"\
                                  or ao1 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               ao2 = input(u7+"Entrer com a 2*"\
                                          +" combinacao para"\
                                          +" Gerar Ex: @$& *: "+u0)
                               if ao2 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora4()

                               if " " in ao2:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora4()

                               if ao2 == "Jamail_Magnestar"\
                                or ao2 == "jamail_magnestar"\
                                 or ao2 == "Jamail_magnestar"\
                                  or ao2 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               ao3 = input(u7+"Entrer com a 3*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if ao3 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora4()

                               if " " in ao3:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora4()

                               if ao3 == "Jamail_Magnestar"\
                                or ao3 == "jamail_magnestar"\
                                 or ao3 == "Jamail_magnestar"\
                                  or ao3 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               ao4 = input(u7+"Entrer com a 4*"\
                                          +" combinacao para"\
                                          +" Gerar Ex: @$& *: "+u0)
                               if ao4 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora4()

                               if " " in ao4:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora4()

                               if ao4 == "Jamail_Magnestar"\
                                or ao4 == "jamail_magnestar"\
                                 or ao4 == "Jamail_magnestar"\
                                  or ao4 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               ao5 = input(u7+"Entrer com a 5*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if ao5 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora4()

                               if " " in ao5:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora4()

                               if ao5 == "Jamail_Magnestar"\
                                or ao5 == "jamail_magnestar"\
                                 or ao5 == "Jamail_magnestar"\
                                  or ao5 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               ao6 = input(u7+"Entrer com a 6*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if ao6 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora4()

                               if " " in ao6:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora4()

                               if ao6 == "Jamail_Magnestar"\
                                or ao6 == "jamail_magnestar"\
                                 or ao6 == "Jamail_magnestar"\
                                  or ao6 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               ao7 = input(u7+"Entrer com a 7*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if ao7 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora4()

                               if " " in ao7:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora4()

                               if ao7 == "Jamail_Magnestar"\
                                or ao7 == "jamail_magnestar"\
                                 or ao7 == "Jamail_magnestar"\
                                  or ao7 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               sleep(2)

                               arq = open(input(u2+"\n\nEntre com o nome"\
                                        +" do Arquivo *: "+u0)+ ".txt", "w")

                               if arq.name == "Jamail_Magnestar.txt"\
                                or arq.name == "jamail_magnestar.txt"\
                                 or arq.name == "Jamail_magnestar.txt"\
                                  or arq.name == "jamail_Magnestar.txt":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               print(u2+"Gerando Wordlist."+u0)
                               if arq != "":
                                  sleep(2)

                               else:
                                  Erro()

                               enb = input(u4+"Quantas senhas a ser"\
                                          +" Gerada? *: "+u0)

                               if enb == "Jamail_Magnestar"\
                                or enb == "jamail_magnestar"\
                                 or enb == "Jamail_magnestar"\
                                  or enb == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               enb = int(enb)
                               if enb != int(enb):
                                  print(u1+"Error: Para esta operacao use"\
                                       +" numeros inteiros. EX: 0665."+u0)
                                  sleep(4)
                                  Erro()

                               else:
                                  sleep(1)

                               sleep(2)

                               deff = [''+ao1+'',\
                                       ''+ao2+'', ''+ao3+'',\
                                       ''+ao4+'',''+ao5+'',\
                                       ''+ao6+'', ''+ao7+'']
                               for i in range(enb):
                                   count = count +1
                                   ao1 = random.choice(deff)
                                   ao2 = random.choice(deff)
                                   ao3 = random.choice(deff)
                                   ao4 = random.choice(deff)
                                   ao5 = random.choice(deff)
                                   ao6 = random.choice(deff)
                                   ao7 = random.choice(deff)
                                   arq.write(str(ao1)+str(ao2)\
                                            +str(ao3)+str(ao4)\
                                            +str(ao5)+str(ao6)\
                                            +str(ao7)+'\n')
                                   print(u3+str(ao1)+str(ao2)\
                                            +str(ao3)+str(ao4)\
                                            +str(ao5)+str(ao6)\
                                            +str(ao7)+u0)

                                   if int(count) == int(enb)+1:
                                      arq.close()

                               sleep(2)
                               print("\n")
                               print(u2+'\nCompleto. '+str(enb)\
                                    +' Senhas salvas no Arquivo %s\033[m' %(arq.name))
                               sleep(1)

                               ext = input(u4+"Deseja sair do Script-PROGAMA"\
                                          +" (Y/n) *: "+u0)
                               if ext == 'y' or ext == 'Y':
                                  print(u1+"Going Out .."+u0)
                                  sleep(2)
                                  exit()

                               if ext == 'n' or ext == 'N':
                                  print(u3+"Voltando para Casa."+u0)
                                  sleep(2)
                                  Going()

                            except Exception as e:
                               print(e)
                          if __name__ == "__main__":
                             sora4()

# [5] QUINTA DIVISAO../;

                       elif sora == "5" or sora == "05":
                          def sora5():
                            try:
                               count = 0
                               print(u1+"Bem vindo ao (Nivel Hard)."+u0)
                               print(u6+"Crie suas senhas de 8"\
                                    +" Combinacoes."+u0)

                               op1 = input(u7+"Entrer com a 1*"\
                                          +" combinacao para"\
                                          +" Gerar Ex: @$& *: "+u0)
                               if op1 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora5()

                               if " " in op1:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora5()

                               if op1 == "Jamail_Magnestar"\
                                or op1 == "jamail_magnestar"\
                                 or op1 == "Jamail_magnestar"\
                                  or op1 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               op2 = input(u7+"Entrer com a 2*"\
                                          +" combinacao para"\
                                          +" Gerar Ex: @$& *: "+u0)
                               if op2 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora5()

                               if " " in op2:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora5()

                               if op2 == "Jamail_Magnestar"\
                                or op2 == "jamail_magnestar"\
                                 or op2 == "Jamail_magnestar"\
                                  or op2 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               op3 = input(u7+"Entrer com a 3*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if op3 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora5()

                               if " " in op3:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora5()

                               if op3 == "Jamail_Magnestar"\
                                or op3 == "jamail_magnestar"\
                                 or op3 == "Jamail_magnestar"\
                                  or op3 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               op4 = input(u7+"Entrer com a 4*"\
                                          +" combinacao para"\
                                          +" Gerar Ex: @$& *: "+u0)
                               if op4 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora5()

                               if " " in op4:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora5()

                               if op4 == "Jamail_Magnestar"\
                                or op4 == "jamail_magnestar"\
                                 or op4 == "Jamail_magnestar"\
                                  or op4 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               op5 = input(u7+"Entrer com a 5*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if op5 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora5()

                               if " " in op5:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora5()

                               if op5 == "Jamail_Magnestar"\
                                or op5 == "jamail_magnestar"\
                                 or op5 == "Jamail_magnestar"\
                                  or op5 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               op6 = input(u7+"Entrer com a 6*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if op6 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora5()

                               if " " in op6:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora5()

                               if op6 == "Jamail_Magnestar"\
                                or op6 == "jamail_magnestar"\
                                 or op6 == "Jamail_magnestar"\
                                  or op6 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               op7 = input(u7+"Entrer com a 7*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if op7 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora5()

                               if " " in op7:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora5()

                               if op7 == "Jamail_Magnestar"\
                                or op7 == "jamail_magnestar"\
                                 or op7 == "Jamail_magnestar"\
                                  or op7 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               op8 = input(u7+"Entrer com a 8*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if op8 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora5()

                               if " " in op8:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora5()

                               if op8 == "Jamail_Magnestar"\
                                or op8 == "jamail_magnestar"\
                                 or op8 == "Jamail_magnestar"\
                                  or op8 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               sleep(2)
                               arq = open(input(u2+"\n\nEntre com o nome"\
                                        +" do Arquivo *: "+u0)+ ".txt", "w")
                               if arq.name == "Jamail_Magnestar.txt"\
                                or arq.name == "jamail_magnestar.txt"\
                                 or arq.name == "Jamail_magnestar.txt"\
                                  or arq.name == "jamail_Magnestar.txt":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               print(u2+"Gerando Wordlist."+u0)
                               if arq != "":
                                  sleep(2)

                               else:
                                  Erro()

                               enb = input(u4+"Quantas senhas a ser"\
                                          +" Gerada? *: "+u0)
                               if enb == "Jamail_Magnestar"\
                                or enb == "jamail_magnestar"\
                                 or enb == "Jamail_magnestar"\
                                  or enb == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               enb = int(enb)
                               if enb != int(enb):
                                  print(u1+"Error: Para esta operacao use"\
                                       +" numeros inteiros. EX: 0665."+u0)
                                  sleep(4)
                                  Erro()

                               else:
                                  sleep(1)

                               sleep(2)
                               deff = [''+op1+'', ''+op8+'',\
                                       ''+op2+'', ''+op3+'',\
                                       ''+op4+'',''+op5+'',\
                                       ''+op6+'', ''+op7+'']
                               for i in range(enb):
                                   count = count +1
                                   op1 = random.choice(deff)
                                   op2 = random.choice(deff)
                                   op3 = random.choice(deff)
                                   op4 = random.choice(deff)
                                   op5 = random.choice(deff)
                                   op6 = random.choice(deff)
                                   op7 = random.choice(deff)
                                   op8 = random.choice(deff)
                                   arq.write(str(op1)+str(op2)\
                                            +str(op3)+str(op4)\
                                            +str(op5)+str(op6)\
                                            +str(op7)+str(op8)+'\n')
                                   print(u3+str(op1)+str(op2)\
                                            +str(op3)+str(op4)\
                                            +str(op5)+str(op6)\
                                            +str(op7)+str(op8)+u0)

                                   if int(count) == int(enb)+1:
                                      arq.close()

                               sleep(2)
                               print("\n")
                               print(u2+'\nCompleto. '+str(enb)\
                                    +' Senhas salvas no Arquivo %s\033[m' %(arq.name))
                               sleep(1)
                               ext = input(u4+"Deseja sair do Script-PROGAMA"\
                                          +" (Y/n) *: "+u0)
                               if ext == 'y' or ext == 'Y':
                                  print(u1+"Going Out .."+u0)
                                  sleep(2)
                                  exit()

                               if ext == 'n' or ext == 'N':
                                  print(u3+"Voltando para Casa."+u0)
                                  sleep(2)
                                  Going()

                            except Exception as e:
                               print(e)
                          if __name__ == "__main__":
                             sora5()
#
# Sakurabito Flores de cerejeira.
# [1] PRIMEIRA DIVISAO../;
# /Com o dia. Zwdeff ..../[];
#
                       elif sora == "1" or sora == "01":
                          def sora1():
                            try:
                               count = 0
                               print(u6+"Crie suas senhas"\
                                    +" de 4 Combinacoes."+u0)
                               nub1 = input(u3+"Entrer com a 1*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nub1 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora1()

                               if " " in nub1:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora1()

                               if nub1 == "Jamail_Magnestar"\
                                or nub1 == "jamail_magnestar"\
                                 or nub1 == "Jamail_magnestar"\
                                  or nub1 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nub2 = input(u3+"Entrer com a 2*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nub2 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora1()

                               if " " in nub2:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora1()

                               if nub2 == "Jamail_Magnestar"\
                                or nub2 == "jamail_magnestar"\
                                 or nub2 == "Jamail_magnestar"\
                                  or nub2 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nub3 = input(u3+"Entrer com a 3*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)
                               if nub3 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora1()

                               if " " in nub3:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora1()

                               if nub3 == "Jamail_Magnestar"\
                                or nub3 == "jamail_magnestar"\
                                 or nub3 == "Jamail_magnestar"\
                                  or nub3 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               nub4 = input(u3+"Entrer com a 4*"\
                                           +" combinacao para"\
                                           +" Gerar Ex: @$& *: "+u0)

                               if nub4 == "":
                                  print(u1+"Error: Argumento obrigatorio"\
                                       +" Ausente."+u0)
                                  print(u1+"Utilize alguma frase,"\
                                       +" simbolo ou Numero."+n0)
                                  sleep(4)
                                  sora1()

                               if " " in nub4:
                                  print(u1+"Error: Espacamento"\
                                        +" nao suportado."+u0)
                                  sleep(1)
                                  sora1()

                               if nub4 == "Jamail_Magnestar"\
                                or nub4 == "jamail_magnestar"\
                                 or nub4 == "Jamail_magnestar"\
                                  or nub4 == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               sleep(2)

                               arq = open(input(u2+"\n\nEntre com o nome"\
                                          +" do Arquivo *: "+u0)+ ".txt", "w")

                               if arq.name == "Jamail_Magnestar.txt"\
                                or arq.name == "jamail_magnestar.txt"\
                                 or arq.name == "Jamail_magnestar.txt"\
                                  or arq.name == "jamail_Magnestar.txt":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               print(u2+"Gerando Wordlist."+u0)
                               if arq != "":
                                  sleep(2)

                               else:
                                  Erro()

                               enb = input(u4+"Quantas senhas a ser"\
                                          +" Gerada? *: "+u0)

                               if enb == "Jamail_Magnestar"\
                                or enb == "jamail_magnestar"\
                                 or enb == "Jamail_magnestar"\
                                  or enb == "jamail_Magnestar":
                                  print(u1+"CLOSEPH for Home!"+u0)
                                  sleep(2)
                                  system("clear")
                                  Going()

                               enb = int(enb)
                               if enb != int(enb):
                                  print(u1+"Error: Para esta operacao use"\
                                        +" numeros inteiros. EX: 0665."+u0)
                                  sleep(4)
                                  Erro()

                               else:
                                  sleep(1)

                               sleep(2)

                               deff = [''+nub1+'',\
                                       ''+nub2+'', ''+nub3+'',\
                                       ''+nub4+'']
                               for i in range(enb):
                                   count = count +1
                                   nub1 = random.choice(deff)
                                   nub2 = random.choice(deff)
                                   nub3 = random.choice(deff)
                                   nub4 = random.choice(deff)
                                   arq.write(str(nub1)+str(nub2)+str(nub3)\
                                            +str(nub4)+'\n')
                                   print(u3+str(nub1)+str(nub2)\
                                        +str(nub3)+str(nub4)+u0)

                                   if int(count) == int(enb)+1:
                                      arq.close()

                               sleep(2)
                               print("\n")
                               print(u2+'\n\Completo. '+str(enb)\
                                    +' Senhas salvas no Arquivo %s\033[m' %(arq.name))
                               sleep(1)

                               ext = input(u4+"Deseja sair do Script-PROGAMA"\
                                          +" (Y/n) *: "+u0)

                               if ext == 'y' or ext == 'Y':
                                  print(u1+"Going Out .."+u0)
                                  sleep(2)
                                  exit()

                               if ext == 'n' or ext == 'N':
                                  print(u3+"Voltando para Casa."+u0)
                                  sleep(2)
                                  Going()

                            except Exception as e:
                               print(e)
                          if __name__ == "__main__":
                             sora1()

                       else:
                          system("clear")
                          Going()

                    except Exception:
                       print(u1+"Error: Use- Somente Numeros"\
                            +" Inteiros. Ex: 56282."+u0)
                       sleep(4)
                       Error()
                  if __name__ == "__main__":
                     inteiro()

               except Exception:
                  Erro()
                  sleep(2)
             if __name__ == "__main__":
                Erro()

          except Exception as e:
             print(e)
        if __name__ == "__main__":
           Generate()

        system("clear")
        sleep(3)
        Going()

#[Senhor da Neve] Lorde YUKI [Snow/Lord]#
  except Exception as e:
     print(e)

  except TypeError:
     print(u1+"Error: Argumento obrigatorio Ausente."+u0)
     sleep(2)
     Going()

################################# ###############################;# /;
################################# ################################;# /;
################################# ################################;# /;
################################# ################################# /;
################################# #################################;# /;
################################# ################################;# /;
################################# ################################;# /;
################################# #################################;# /;
#################################################################;# /;
#Programa em desenvolvimento feito para criar senhas para Brute Force;


  except SyntaxError:
     Going()
     sleep(2)

  except EOFError:
     ext = input(u4+"Deseja sair do progama (Y/n)? *: "+u0)
     if ext == 'y' or ext == 'Y':
        print(u1+"Going Out .."+u0)
        sleep(2)
        exit()

     if ext == 'n' or ext == 'N':
        print(u3+"Voltando para Casa."+u0)
        Going()

  except KeyboardInterrupt:
     print(u1+"Going Out .."+u0)
     sleep(2)
     exit()
if __name__ == '__main__':
   Going()
