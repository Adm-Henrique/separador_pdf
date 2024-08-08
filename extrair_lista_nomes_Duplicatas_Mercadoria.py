

import PyPDF2 as pdf

# Abrir o arquivo PDF

abrir_pdf = pdf.PdfReader('H:\Python\pdf\MERCADORIA POR CLIENTE.PDF', 'rb')

# Lista para armazenar os nomes dos funcionários
nomes_cliente = []

# Iterar por todas as páginas do PDF
for i in range(len(abrir_pdf.pages)):
    pagina = abrir_pdf.pages[i]
    texto = pagina.extract_text().split('\n')
    
    # Extrair o nome do funcionário
    linha_nome = texto[13].strip()  # indice 13
    nome = linha_nome.replace('Cliente: ', '').strip()
    
    # Adicionar o nome à lista
    nomes_cliente.append(nome)

print('nomes_cliente: ', nomes_cliente)
 