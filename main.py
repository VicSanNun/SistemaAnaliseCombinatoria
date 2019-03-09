# @author: Victor Nunes
# @email: victornunes470@gmail.com

#--------------FUNÇÕES---------------------------------
#Função para Calcular Fatorial
#Está excedendo o limite de recursão, Tentar escrever o código em C ou em Java

import sys

sys.setrecursionlimit(15000)
def fat(n):
  if(n == 0 or n == 1):
    return 1
  else:
    return (n*(fat(n-1)))

#Função para Calcular Arranjo
def arranjo(p,n):
  return (fat(n)/(fat(p)*(fat(n-p))))

#Função para Calcular Combinação
def combinacao(p,n):
  return (fat(n)/fat(n-p))
#--------------------------------------------------------
  
#Código Principal

#Opções
print("F - Fatorial")
print("A - Arranjo")
print("C - Combinação \n")

#Váriavel de Escolha
escolha = input("Qual Operação você quer?")

if(escolha == "F"):
  n = int(input("Qual número você quer calcular o Fatorial? "))
  print("\n")
  print ("O resultado é:",fat(n))

elif(escolha == "A"):
  n = int(input("Qual n? "))
  p = int(input("Qual p? "))
  print("\n")
  print ("O resultado é:",arranjo(p,n))
  
elif(escolha == "C"):
  n = int(input("Qual n? "))
  p = int(input("Qual p? "))
  print("\n")
  print ("O resultado é:",combinacao(p,n))
  