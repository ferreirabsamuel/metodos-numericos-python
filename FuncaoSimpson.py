def funcao():
    return (0.1 * (z**3) - 1.5 * (z**2) + 10*z +20)

z  = 0.0
indice = 0
par = 0
impar = 0
primeirovalor = 0
ultimovalor = 0

while (indice <= 30):

    wsoma = funcao()
    print("O valor da iteração de índice {} é: {}".format(indice, wsoma))

    if indice % 2 == 0:
        par += wsoma
    else:
        impar += wsoma

    if indice == 0:
        primeirovalor += wsoma
    elif indice == 30:
        ultimovalor += wsoma

    z += 0.5
    indice += 1

def simpson():
    return (h / 3  *(( primeirovalor + ultimovalor) + (4 *impar )+ 2 * (par - ultimovalor - primeirovalor)))

h = 0.5
resultado = simpson()

print("-"*54)
print("O resultado da aplicação do Método de Simpson sobre a função é: {:.3f}".format(resultado))
