
#Projeto: Mini chatbot
#Autor: Thomas Martins
#Data: 30/07/2025

#Descrição:
# Este é um pequeno chatbot que tem como objetivo conversar sobre programação de forma simples.
# Ele é projetado para ser um projeto de portfólio e não possui funcionalidades avançadas.
# Ele pode responder perguntas básicas sobre Python, JavaScript, HTML e CSS.
# Ele é um projeto simples, mas pode ser expandido no futuro para incluir mais funcionalidades e conhecimentos.

#Tecnologias utilizadas:
# - Python 3.x
# - Biblioteca padrão (sem dependências externas)
# - Tempo de espera para simular uma conversa mais natural.




#Um pequeno chatbot para perguntas simples

import time
import random

print('Olá! Eu sou um chatbot simples. Com o intuito de ter projetos para meu curriculo.')
time.sleep(1)
print('Minha função é de ter uma conversa simples sobre programação com você.')
time.sleep(2)
print('Tenho conhecimento sobre: Python, JavaScript, HTML, CSS (Básico)')
time.sleep(3)


#Inicio de conversa
#futura mudança (adicionar um sistema de escolha do bot usando random onde ele chuta a linguagem do usuario)
start = input('Vamos começar? (sim/não): ').strip().lower()
if start == 'sim':
    print('Ótimo! Sobre o que você gostaria de conversar? ')

else:
    print('Ah, tudo bem! Se mudar de ideia, é so chamar')



#Pergunta sobre o tipo de linguagem
tipo = input('Você gostaria de falar sobre Python, JavaScript, HTML ou CSS ').strip().lower()

#respostas baseadas na linguagem escolhida
#terminar as escritas das respostas
if tipo =='python':
    print('Python: É uma linguagem de programação versátil e fácil de aprender. \
Usada para desenvolvimento web, automação, ciência de dados, inteligência artificial e muito mais. \
Seu código é limpo e legível, ideal para iniciantes e profissionais.')

elif tipo =='JavaScript':
    print('JavaScript: É uma linguagem de programação amplamente utilizada para desenvolvimento web. \
Permite criar páginas interativas e dinâmicas. É a linguagem principal para desenvolvimento front-end e também pode ser usada no back-end com Node.js.')

elif tipo =='HTML':
    print('HTML: É a linguagem de marcação padrão para criar páginas da web. \
Ele estrutura o conteúdo na web usando elementos como cabeçalhos, parágrafos, links e imagens. \
HTML é fundamental para o desenvolvimento web e é frequentemente usado em conjunto com CSS e JavaScript.')

elif tipo =='CSS':
    print('CSS: É a linguagem de estilo usada para descrever a apresentação de documentos HTML. \
Com o CSS, você pode controlar o layout, as cores, as fontes e outros aspectos visuais das páginas da web. \
É uma parte essencial do desenvolvimento front-end e permite criar designs responsivos e atraentes.')