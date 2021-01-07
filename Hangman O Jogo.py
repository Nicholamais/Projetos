import random
from tkinter import *

comida = ['pão', ' cereal', '   queijo', '  croissant', '  ovo', '  peixe', '  ketchup',
          ' maionese', ' Macarrão', ' panquecas', '  pizza', ' amendoim', ' arroz', '  salada', 'sanduíche', ' camarão',
          'torrada', 'presunto', 'purê']

profissão = ['professor', 'jogador', 'médico', 'engenheiro', 'arquiteto', 'pedreiro', 'cozinheiro', 'músico', 'artista',
             'pintor', 'escritor', 'jornalista', 'diretor'
    , 'ator', 'prefeito', 'presidente', 'político', 'vereador', 'piloto', 'encanador', 'garçom', 'militar']

objeto = ['óculos', 'lápis', 'borracha', 'apontador', 'mesa', 'cadeira', 'cama', 'sofá', 'televisão', 'lâmpada',
          'porta', 'caixa', 'armário', ' livro', 'caderno'
    , 'camiseta', 'calça', 'bota', 'carregador', 'celular', 'câmera', 'gravador', 'computador', 'violão', 'guitarra',
          'bateria', 'carro', 'moto', 'avião', 'navio',
          'parede', 'sapato', 'meia', 'desodorante', 'perfume', 'prato', 'panela', 'garfo', 'faca', 'colher', 'tijolo',
          'concreto', 'poste', 'lamparina', 'retrato',
          'torradeira']

cor = ['vermelho', 'verde', 'azul', 'amarelo', 'roxo', 'rosa',
       'marrom', 'preto', 'branco', 'laranja', 'ciano', 'cinza']

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'ú', 'ç']

lista = [comida, profissão, objeto, cor]
a = random.randint(1, 4)
palavras = random.choice(lista[a - 1]).strip()
palavra = list(palavras)
palavrajogador = []

if a == 1:
    a = 'comida'

elif a == 2:
    a = 'profissão'

elif a == 3:
    a = 'objeto'

else:
    a = 'cor'


def fechar():
    janela.destroy()


def escrever(arg):
    global j, tentativas
    tentativas -= 1
    i = 0
    for x in palavra:
        if arg == x:
            d[i] = arg
            e = " ".join(d)
            resposta2.config(text=e)
            j += 1

        i += 1

    if not arg in palavra:
        j += 1
        palavrajogador.append(arg)
        widget.config(text="|  Letras erradas: " + " ,".join(palavrajogador))
        widget.update()

    if d == palavra:
        print("Ganhou")
        aviso.config(text="GANHOU")
        aviso.place(relx=0.2, rely=0.4)

        for x in letras.winfo_children():
            x.config(state='disabled')

    elif tentativas == 0:
        aviso.config(text="PERDEU")
        aviso.place(relx=0.2, rely=0.4)

        for x in letras.winfo_children():
            x.config(state='disabled')

    Tentativas.config(text=f"Tentativas: {tentativas}")


janela = Tk()
janela.title("Hangman")
janela["bg"] = 'sky blue'
janela.attributes("-fullscreen", True)

nome = Label(janela, text='Hangman', width = 20, height = 20)
nome.place(relx=0.5, rely=0.1, anchor='center')
nome.configure(font="-family {Euphorigenic} -size 27 -weight bold -slant italic", bg='skyblue')

d = ['_ '] * len(''.join(palavra))
e = d
j = 0
tentativas = 15


resposta = Label(janela, text='dica: '+a)
resposta.place(relx=0.5, rely=0.4, anchor='center')

resposta2 = Label(janela, text="".join(d))
resposta2.place(relx=0.5, rely=0.3, anchor='center')

aviso = Label(janela)

dados = LabelFrame(janela)

Tentativas = Label(dados, text=f"Tentativas: {tentativas} ")
Tentativas.grid(row=1, column=1,padx=1)
Tentativas.update()

widget = Label(dados, text="|  Letras erradas:")
widget.grid(row=1,column=2,padx=1)

dados.place(relx=0.35, rely=0.45)

letras = LabelFrame(janela, text='Letras')

for num in range(1, 35):
    if num < 13:
        x = Button(letras, text=(alfa[num - 1]), padx=10,state=NORMAL, command=lambda letra=alfa[num - 1]: escrever(letra)).grid(
            row=1, column=num)

        num += 1
    if 12 < num < 25:
        opcao = (
            Button(letras, text=(alfa[num - 1]), padx=10,state=NORMAL, command=lambda letra=alfa[num - 1]: escrever(letra)).grid(
                row=2, column=num - 12))

        num += 1
    if 24 < num < 27:
        opcao = (
            Button(letras, text=(alfa[num - 1]), padx=10, state=NORMAL,command=lambda letra=alfa[num - 1]: escrever(letra)).grid(
                row=3, column=num - 19))

        num += 1
    if 26 < num < 35:
        opcao = (
            Button(letras, text=(alfa[num - 1]), padx=10,state=NORMAL, command=lambda letra=alfa[num - 1]: escrever(letra)).grid(
                row=4, column=num - 24))

        num += 1

letras.place(relx=0.35, rely=0.5)

sair = Button(janela, text='Sair', width=10, command=fechar)
sair.place(relx=0.5, rely=1, anchor='s')

janela.mainloop()
