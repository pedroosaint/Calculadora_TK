expressao = visor.get().replace("×", "*").replace("÷", "/")

    try:
        numeros = []
        operadores = []
        numero = ""

        for caractere in expressao:
            if caractere.isdigit() or caractere == ".":
                numero += caractere
            else:
                numeros.append(float(numero))
                numero = ""
                operadores.append(caractere)

        numeros.append(float(numero))

        i = 0
        while i < len(operadores):
            if operadores[i] == "*":
                numeros[i] *= numeros[i + 1]
            elif operadores[i] == "/":
                numeros[i] /= numeros[i + 1]
            else:
                i += 1
                continue

            numeros.pop(i + 1)
            operadores.pop(i)

        resultado = numeros[0]

        for i in range(len(operadores)):
            if operadores[i] == "+":
                resultado += numeros[i + 1]
            else:
                resultado -= numeros[i + 1]

        resultado = round(resultado, 10)

        if resultado == int(resultado):
            resultado = int(resultado)