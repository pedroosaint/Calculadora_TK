import tkinter as tk


ROSA_FUNDO = "#FFD6E8"
ROSA_NUMERO = "#FFB3D1"
ROSA_OPERADOR = "#FF8CBE"
ROSA_ESPECIAL = "#F7A8C8"
ROSA_IGUAL = "#E75B9B"
ROSA_CLARO = "#FFC4DD"
TEXTO = "#7A2E55"
FONTE = ("Comic Sans MS", 16, "bold")

janela = tk.Tk()
janela.title("Calculadora Rosa 🎀")
janela.configure(bg=ROSA_FUNDO, padx=12, pady=12)
janela.resizable(False, False)

for coluna in range(4):
    janela.columnconfigure(coluna, weight=1, uniform="colunas", minsize=90)

janela.rowconfigure(0, weight=0)

for linha in range(1, 6):
    janela.rowconfigure(linha, weight=1, uniform="linhas", minsize=80)


numero1 = 0
operador = ""
erro = False


# Digitar números
def digitar_0():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "0")
    visor.config(state="readonly")


def digitar_1():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "1")
    visor.config(state="readonly")


def digitar_2():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "2")
    visor.config(state="readonly")


def digitar_3():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "3")
    visor.config(state="readonly")


def digitar_4():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "4")
    visor.config(state="readonly")


def digitar_5():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "5")
    visor.config(state="readonly")


def digitar_6():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "6")
    visor.config(state="readonly")


def digitar_7():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "7")
    visor.config(state="readonly")


def digitar_8():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "8")
    visor.config(state="readonly")


def digitar_9():
    global erro
    visor.config(state="normal")
    if erro:
        visor.delete(0, tk.END)
        erro = False
    visor.insert(tk.END, "9")
    visor.config(state="readonly")


def digitar_ponto():
    global erro

    visor.config(state="normal")

    if erro:
        visor.delete(0, tk.END)
        erro = False

    if "." not in visor.get():

        if visor.get() == "":
            visor.insert(tk.END, "0.")

        else:
            visor.insert(tk.END, ".")

    visor.config(state="readonly")


# Escolher a operação
def calcular(sinal):
    global numero1, operador

    if operador != "":
        return

    if visor.get() == "":
        return

    numero1 = float(visor.get())
    operador = sinal

    visor.config(state="normal")
    visor.delete(0, tk.END)
    visor.config(state="readonly")


def digitar_mais():
    calcular("+")


def digitar_menos():
    calcular("-")


def digitar_multiplicacao():
    calcular("*")


def digitar_divisao():
    calcular("/")


# Mostrar o resultado
def igual():
    global numero1, operador, erro

    if visor.get() == "" or operador == "":
        return

    numero2 = float(visor.get())

    if operador == "+":
        resultado = numero1 + numero2

    elif operador == "-":
        resultado = numero1 - numero2

    elif operador == "*":
        resultado = numero1 * numero2

    elif operador == "/":
        if numero2 == 0:
            visor.config(state="normal")
            visor.delete(0, tk.END)
            visor.insert(0, "Erro, divisão por zero!")
            visor.config(state="readonly")

            operador = ""
            erro = True
            return

        resultado = numero1 / numero2

    if resultado == int(resultado):
        resultado = int(resultado)

    visor.config(state="normal")
    visor.delete(0, tk.END)
    visor.insert(0, str(resultado))
    visor.config(state="readonly")

    operador = ""


# Limpar tudo
def limpar():
    global numero1, operador, erro

    numero1 = 0
    operador = ""
    erro = False

    visor.config(state="normal")
    visor.delete(0, tk.END)
    visor.config(state="readonly")


# Apagar último número
def apagar_um():
    global erro

    if erro:
        return

    texto = visor.get()

    if texto:
        visor.config(state="normal")
        visor.delete(len(texto) - 1, tk.END)
        visor.config(state="readonly")


visor = tk.Entry(
    janela,
    justify="right",
    font=("Comic Sans MS", 28, "bold"),
    bg="white",
    fg=TEXTO,
    bd=0,
    state="readonly"
)

visor.grid(row=0, column=0, columnspan=4, sticky="ew", padx=4, pady=(0, 14), ipady=20)


botao_c = tk.Button(janela, text="C", command=limpar,
                    font=FONTE, bg=ROSA_ESPECIAL, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_c.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)


botao_apagar = tk.Button(janela, text="⌫", command=apagar_um,
                         font=FONTE, bg=ROSA_ESPECIAL, fg=TEXTO,
                         activebackground=ROSA_CLARO, bd=0)

botao_apagar.grid(row=1, column=1, sticky="nsew", padx=4, pady=4)


botao_divisao = tk.Button(janela, text="÷", command=digitar_divisao,
                          font=FONTE, bg=ROSA_OPERADOR, fg="white",
                          activebackground="#FF9FCB", bd=0)

botao_divisao.grid(row=1, column=2, sticky="nsew", padx=4, pady=4)


botao_multiplicacao = tk.Button(janela, text="×", command=digitar_multiplicacao,
                                font=FONTE, bg=ROSA_OPERADOR, fg="white",
                                activebackground="#FF9FCB", bd=0)

botao_multiplicacao.grid(row=1, column=3, sticky="nsew", padx=4, pady=4)


botao_7 = tk.Button(janela, text="7", command=digitar_7,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_7.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)


botao_8 = tk.Button(janela, text="8", command=digitar_8,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_8.grid(row=2, column=1, sticky="nsew", padx=4, pady=4)


botao_9 = tk.Button(janela, text="9", command=digitar_9,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_9.grid(row=2, column=2, sticky="nsew", padx=4, pady=4)


botao_menos = tk.Button(janela, text="-", command=digitar_menos,
                        font=FONTE, bg=ROSA_OPERADOR, fg="white",
                        activebackground="#FF9FCB", bd=0)

botao_menos.grid(row=2, column=3, sticky="nsew", padx=4, pady=4)


botao_4 = tk.Button(janela, text="4", command=digitar_4,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_4.grid(row=3, column=0, sticky="nsew", padx=4, pady=4)


botao_5 = tk.Button(janela, text="5", command=digitar_5,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_5.grid(row=3, column=1, sticky="nsew", padx=4, pady=4)


botao_6 = tk.Button(janela, text="6", command=digitar_6,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_6.grid(row=3, column=2, sticky="nsew", padx=4, pady=4)


botao_mais = tk.Button(janela, text="+", command=digitar_mais,
                       font=FONTE, bg=ROSA_OPERADOR, fg="white",
                       activebackground="#FF9FCB", bd=0)

botao_mais.grid(row=3, column=3, sticky="nsew", padx=4, pady=4)


botao_1 = tk.Button(janela, text="1", command=digitar_1,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_1.grid(row=4, column=0, sticky="nsew", padx=4, pady=4)


botao_2 = tk.Button(janela, text="2", command=digitar_2,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_2.grid(row=4, column=1, sticky="nsew", padx=4, pady=4)


botao_3 = tk.Button(janela, text="3", command=digitar_3,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_3.grid(row=4, column=2, sticky="nsew", padx=4, pady=4)


botao_igual = tk.Button(janela, text="=", command=igual,
                        font=FONTE, bg=ROSA_IGUAL, fg="white",
                        activebackground="#D44C8A", bd=0)

botao_igual.grid(row=4, column=3, rowspan=2, sticky="nsew", padx=4, pady=4)


botao_0 = tk.Button(janela, text="0", command=digitar_0,
                    font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                    activebackground=ROSA_CLARO, bd=0)

botao_0.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=4, pady=4)


botao_ponto = tk.Button(janela, text=".", command=digitar_ponto,
                        font=FONTE, bg=ROSA_NUMERO, fg=TEXTO,
                        activebackground=ROSA_CLARO, bd=0)

botao_ponto.grid(row=5, column=2, sticky="nsew", padx=4, pady=4)


janela.bind("<Return>", lambda e: igual())
janela.bind("<BackSpace>", lambda e: apagar_um())
janela.bind("<Escape>", lambda e: limpar())

janela.mainloop()
