def derivacao():
    return (0.1 * (z**3) - 1.5 * (z**2) + 10*z +20)

z  = 0.0
indice = 0
sete = 0
seteemeio = 0
oito = 0
alturatorre = 15

print("O ponto médio da torre é : {} metros".format(alturatorre/2 ))

while (indice <= 30):
    wsoma = derivacao()

    if (z == 7):
        sete += derivacao()

    elif (z == 7.5):
        seteemeio += derivacao()

    elif (z == 8):
        oito += derivacao()

    indice += 1
    z += 0.5

h = 0.5

dfprogressiva = (oito - seteemeio) / h
dfregressiva = (seteemeio - sete) / h
dfcentral = (oito - sete) / (h*2)

print("A diferença progressiva é: {:.3f}".format(dfprogressiva))
print("A diferença regressiva é: {:.3f}".format(dfregressiva))
print("A diferença central é: {:.3f}".format(dfcentral))
