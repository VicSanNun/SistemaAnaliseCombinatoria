# @author: Victor Nunes
# @email: victornunes470@gmail.com

#--------------FUN��ES---------------------------------
#Fun��o para Calcular Fatorial
#Est� excedendo o limite de recurs�o, Tentar escrever o c�digo em C ou em Java

import sys

sys.setrecursionlimit(15000)
def fat(n):
  if(n == 0 or n == 1):
    return 1
  else:
    return (n*(fat(n-1)))

#Fun��o para Calcular Arranjo
def arranjo(p,n):
  return (fat(n)/(fat(p)*(fat(n-p))))

#Fun��o para Calcular Combina��o
def combinacao(p,n):
  return (fat(n)/fat(n-p))
#--------------------------------------------------------
  
#C�digo Principal

#Op��es
print("F - Fatorial")
print("A - Arranjo")
print("C - Combina��o \n")

#V�riavel de Escolha
escolha = input("Qual Opera��o voc� quer?")

if(escolha == "F"):
  n = int(input("Qual n�mero voc� quer calcular o Fatorial? "))
  print("\n")
  print ("O resultado �:",fat(n))

elif(escolha == "A"):
  n = int(input("Qual n? "))
  p = int(input("Qual p? "))
  print("\n")
  print ("O resultado �:",arranjo(p,n))
  
elif(escolha == "C"):
  n = int(input("Qual n? "))
  p = int(input("Qual p? "))
  print("\n")
  print ("O resultado �:",combinacao(p,n))
  