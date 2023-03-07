#Soma Recursiva
'''
def SomaRecursiva(N):
    if(N == 0):
        return 0
    else:
        return N + SomaRecursiva(N - 1)


num = int(input("Informe um número: "))
print("O valor da soma é: ",SomaRecursiva(num))
'''
#Multiplicação recursiva usando apenas somas
def MultiplicacaoRecursiva(num,multiplicador):
    if(multiplicador == 1):
        return num
    else:
        return num + MultiplicacaoRecursiva(num,multiplicador-1)

numero = int(input("Informe um número: "))
vezesMultiplicado = int(input("Informe quantas vezes o número será multiplicado: "))

print("O resultado da multiplicação é: ",MultiplicacaoRecursiva(numero,vezesMultiplicado))
