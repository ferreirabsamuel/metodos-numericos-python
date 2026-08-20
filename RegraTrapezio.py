def trapezio():
    return (0.1 * (z**3) - 1.5 * (z**2) + 10*z +20)

z  = 0.0
indice = 0
valores = 0
primeirovalor = 0
ultimovalor = 0

while (indice <= 30):

    wsoma = trapezio()
    print("O valor da iteração de índice {} é: {}".format(indice, wsoma))

    while True:
        if (indice>0 and indice<30):
            valores += wsoma
        break

    if indice == 0:
        primeirovalor += wsoma
    elif indice == 30:
        ultimovalor += wsoma

    z += 0.5
    indice += 1

def regratrapezio ():
    return h/2 * ( primeirovalor + (2 * valores  ) + ultimovalor )

h = 0.5

print("-"*54)
print("O resultado da aplicação da Regra dos Trapézios sobre a função é {:.3f}".format(regratrapezio()))
