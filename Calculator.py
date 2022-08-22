# Define uma função com  o nome "addition" que recebe os parametros "fnum" e "snum"
def addition(fnum, snum):
    result = fnum + snum        # Soma os valores recebidos
    print(result)               # Retorna o resultado


# Define uma função com  o nome "subtraction" que recebe os parametros "fnum" e "snum"
def subtraction(fnum, snum):
    result = fnum - snum        # Subtrai os valores recebidos
    print(result)               # Retorna o resultado


# Define uma função com  o nome "multiplication" que recebe os parametros "fnum" e "snum"
def multiplication(fnum, snum):
    result = fnum * snum        # Multiplica os valores recebidos
    print(result)               # Retorna o resultado


# Define uma função com  o nome "division" que recebe os parametros "fnum" e "snum"
def division(fnum, snum):
    result = fnum / snum        # Divide os valores recebidos
    print(result)               # Retorna o resultado


# Inicia uma estrutura de repetição
calc = 1
while calc == 1:

    numOne = float(input("Insert the first number\n>> "))                   # Armazena uma variavel **a)
    mathType = input("Select the operation\n1) +\n2) -\n3) *\n4) /\n>> ")   # **a)
    numTwo = float(input("Insert the second number\n>> "))                  # **a)

    if mathType == "1":                 # Verifica o valor da variavel **b)
        addition(numOne, numTwo)        # Chama a variavel e passa os parametros "numOne" e "numTwo" **c)

    elif mathType == "2":               # **b)
        subtraction(numOne, numTwo)     # **c)

    elif mathType == "3":               # **b)
        multiplication(numOne, numTwo)  # **c)

    elif mathType == "4":               # **b)
        division(numOne, numTwo)        # **c)

    else:                               # **b)
        print("There was a error, please try again\n\n\n\n\n")  # Retorna uma  mensagem de erro

    i = 1
    while i == 1:
        repeat = input("Do you want to repeat?\n(Y or N)\n>>")
        if repeat.lower() == "y" or repeat.lower() == "yes":
            i = 0

        elif repeat.lower() == "n" or repeat.lower() == "no":
            calc = 0
            i = 0

        else:
            print("Error 404")
