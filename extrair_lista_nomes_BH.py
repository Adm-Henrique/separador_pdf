

import PyPDF2 as pdf

# Abrir o arquivo PDF

abrir_pdf = pdf.PdfReader('H:\Python\pdf\EXTRATO BANCO DE HORAS ANALITICO.PDF', 'rb')

# Lista para armazenar os nomes dos funcionários
nomes_funcionarios = []

# Iterar por todas as páginas do PDF
for i in range(len(abrir_pdf.pages)):
    pagina = abrir_pdf.pages[i]
    texto = pagina.extract_text().split('\n')
    
    # Extrair o nome do funcionário
    linha_nome = texto[2].strip()  # indice 2
    nome_sem_digitos = linha_nome.lstrip('0123456789')
    nome = nome_sem_digitos.replace(' Funcionário  :', '').strip()
    
    # Adicionar o nome à lista
    nomes_funcionarios.append(nome)

print(nomes_funcionarios)
