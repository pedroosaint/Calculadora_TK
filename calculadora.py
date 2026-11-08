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


def digitar_0():
    visor.insert(tk.END, "0")

def digitar_1():
    visor.insert(tk.END, "1")

def digitar_2():
    visor.insert(tk.END, "2")

def digitar_3():
    visor.insert(tk.END, "3")

def digitar_4():
    visor.insert(tk.END, "4")

def digitar_5():
    visor.insert(tk.END, "5")

def digitar_6():
    visor.insert(tk.END, "6")

def digitar_7():
    visor.insert(tk.END, "7")

def digitar_8():
    visor.insert(tk.END, "8")

def digitar_9():
    visor.insert(tk.END, "9")

def digitar_ponto():
    visor.insert(tk.END, ".")


def digitar_mais():
    visor.insert(tk.END, "+")

def digitar_menos():
    visor.insert(tk.END, "-")

def digitar_multiplicacao():
    visor.insert(tk.END, "×")

def digitar_divisao():
    visor.insert(tk.END, "÷")


def limpar():
    visor.delete(0, tk.END)

def apagar_um():
    texto = visor.get()
    if texto:
        visor.delete(len(texto) - 1, tk.END)

def igual():
    
    expressao = visor.get().replace("×", "*").replace("÷", "/")
    
    try:
        
        resultado = eval(expressao, {"__builtins__": {}})
        if resultado == int(resultado):
            resultado = int(resultado)
        else:
            resultado = round(resultado, 10)
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    
    except ZeroDivisionError:
        
        visor.delete(0, tk.END)
        visor.insert(0, "Erro! Divisão por zero.")
    
    except Exception:
        
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")


visor = tk.Entry(janela, justify="right", font=("Comic Sans MS", 28, "bold"), bg="white", fg=TEXTO, bd=0)

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