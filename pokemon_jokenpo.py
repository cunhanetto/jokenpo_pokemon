import tkinter as tk
from tkinter import LabelFrame, Button, Label, PhotoImage
import random

def escolheu_charmander():
     jokenpo(escolha_usuario='charmander')

def escolheu_squirtle():
     jokenpo(escolha_usuario='squirtle')

def escolheu_bulbassauro():
     jokenpo(escolha_usuario='bulbassauro')

def jokenpo(escolha_usuario):
    escolha_computador = random.choice(['charmander', 'squirtle', 'bulbassauro'])
    if escolha_usuario == escolha_computador:
        mensagem = f'''
          Você: {escolha_usuario.upper()}
          Computador: {escolha_computador.upper()}
          Resultado: EMPATE!
        '''
    elif (escolha_usuario == 'charmander' and escolha_computador == 'bulbassauro') \
      or (escolha_usuario == 'squirtle' and escolha_computador == 'charmander') \
      or (escolha_usuario == 'bulbassauro' and escolha_computador == 'squirtle'):
          mensagem = f'''
            Você: {escolha_usuario.upper()}
            Computador: {escolha_computador.upper()}
            Resultado: VOCÊ VENCEU!
          '''
    else:
         mensagem = f'''
            Você: {escolha_usuario.upper()}
            Computador: {escolha_computador.upper()}
            Resultado: VOCÊ PERDEU!
          '''
    resultado.config(text=mensagem)

janela = tk.Tk()


frame = LabelFrame(janela, text='Qual você escolhe?', padx=10, pady=10)
frame.pack()

icone_charmander = PhotoImage(file='imagens/charmander.PNG')
icone_squirtle = PhotoImage(file='imagens/squirtle.PNG')
icone_bulbassauro = PhotoImage(file='imagens/bulbassauro.PNG')

Button(frame, text='charmander', command=escolheu_charmander, image=icone_charmander, compound=tk.LEFT).grid(column=0, row=1)
Button(frame, text='squirtle', command=escolheu_squirtle, image=icone_squirtle, compound=tk.LEFT).grid(column=1, row=1)
Button(frame, text='bulbassauro', command=escolheu_bulbassauro, image=icone_bulbassauro, compound=tk.LEFT).grid(column=2, row=1)

resultado = Label(frame, pady=10, padx=10, justify=tk.LEFT)
resultado.grid(column=0, row=2, columnspan=3)



janela.title('charmander, squirtle ou bulbassauro')
janela.geometry("600x300+500+200")
janela.mainloop()