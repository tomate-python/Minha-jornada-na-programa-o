#Imprortando bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox


#Função para calcular a média
def calcular_media():
	nome = entry_nome.get()
	if not nome:
		messagebox.showerror('Erro!', 'Por favor, digite seu nome.')
		return
	try:
		nota1 = float(entry_nota1.get())
		nota2 = float(entry_nota2.get())
		resultado = (nota1 + nota2) / 2 
		if resultado >= 5:
			messagebox.showinfo('Resultado', 'Parabéns! Você foi aprovado com {:.1f} de média' . format(resultado))
		else:
			messagebox.showinfo('Resultado', 'Infelizmente, você foi reprovado com {:.2f} de média.'.format(resultado))
	except ValueError:
		messagebox.showerror('Erro!', 'Por favor, digite suas notas corretamente (utilize ponto "." para notas decimais)')

#botão para limpar os campos
def limpar_campo():
	entry_nome.delete(0, tk.END)
	entry_nota1.delete(0, tk.END)
	entry_nota2.delete(0, tk.END)


#========================================================================================
#Criando a janela principal de nome
janela = tk.Tk()
janela.configure(bg= '#f0f0f0')
janela.title('Calcilador de Média Escolar')
janela.geometry('300x200')
janela.configure(bg='lightblue')
label_nome = tk.Label(janela, text='Digite seu nome:')
label_nome.pack(pady=10)
label_nome.configure(bg="lightblue", fg='black', font=('Arial', 16, 'bold'))
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack(pady=5)

# Campo para a primeira nota
label_nota1 = tk.Label(janela, text='Digite sua primeira nota:')
label_nota1.pack()
label_nota1.configure(bg='lightblue', fg='black', font=('Arial', 16, 'bold'))
entry_nota1 = tk.Entry(janela)
entry_nota1.pack(pady=5)

# Campo para a segunda nota
label_nota2 = tk.Label(janela, text='Digite sua segunda nota:')
label_nota2.pack()
label_nota2.configure(bg='lightblue', fg='black', font=('Arial', 16, 'bold'))
entry_nota2 = tk.Entry(janela)
entry_nota2.pack(pady=5)

# Botão para calcular a média
botao = tk.Button(janela, text='Calcular Média', command=calcular_media)
botao.pack(pady=10)
botao.configure(bg='lightgreen', fg='black', font=('Arial', 14, 'bold'))

# Botão para limpar os campos
botao_limpar = tk.Button(janela, text='Limpar', command=limpar_campo)
botao_limpar.pack(pady=10)
botao_limpar.configure(bg='lightcoral', fg='black', font=('Arial', 14, 'bold'))



#=====================================================================================================================

#janela de faltas

def ver_faltas():
	janela_faltas = tk.Toplevel(janela)
	janela_faltas.title('Calculador de Faltas')
	janela_faltas.geometry('300x200')
	tk.Label(janela_faltas, text='Digite quantas aulas você tem no dia:').pack(pady=10)
	entry_aulas = tk.Entry(janela_faltas)
	entry_aulas.pack(pady=5)

	tk.Label(janela_faltas, text='Digite quantos dias você faltou:').pack(pady=10)
	entry_dias = tk.Entry(janela_faltas)
	entry_dias.pack(pady=5)

	def calcular_faltas():
		try:
			aulas = int(entry_aulas.get())
			dias = int(entry_dias.get())
			total_faltas = aulas * dias
			messagebox.showinfo('Faltas', f'Você faltou um total de {total_faltas} aulas.')
		except ValueError:
			messagebox.showerror('Erro!', 'Por favor, digite valores válidos para aulas e dias.')

	botao_calcular_faltas = tk.Button(janela_faltas, text='Calcular Faltas', command=calcular_faltas)
	botao_calcular_faltas.pack(pady=10)


# Botão para abrir a janela de faltas
botao_faltas = tk.Button(janela, text='Calcular Faltas', command=ver_faltas)
botao_faltas.pack(pady=10)
# O botão de calcular faltas agora é criado dentro da função ver_faltas


janela.mainloop()
