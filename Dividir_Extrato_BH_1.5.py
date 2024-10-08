
import customtkinter as ctk
from tkinter.filedialog import askdirectory, askopenfilename
import PyPDF2 as pdf
import time


################################################################################
#### Função para dividir o arquivo

def split_pdf_by_employees():

    
    # Abra o arquivo PDF
    try:

        total_steps = 5  # Ajuste para o número de passos no seu procedimento
        for i in range(total_steps):
            time.sleep(0.1)  # Simulação do tempo de processamento
            progresso = i / total_steps
            barra_progresso.set(progresso)  # Atualiza a barra de progresso
            percentual_processo.configure(text=f'{int(progresso * 100)}%')  # Atualiza o label com o percentual
            div_extrato_pdf.update_idletasks()  # Atualiza a interface


        with open(entry_arquivo.get(), 'rb') as pdf_file:
            pdf_reader = pdf.PdfReader(pdf_file)


            # Lista para armazenar os nomes dos funcionários
            nomes_funcionarios = []
            # Iterar por todas as páginas do PDF
            for i in range(len(pdf_reader.pages)):
                pagina = pdf_reader.pages[i]
                texto = pagina.extract_text().split('\n')
    
                # Extrair o nome do funcionário
                linha_nome = texto[2].strip()  # indice 2
                nome_sem_digitos = linha_nome.lstrip('0123456789')
                nome = nome_sem_digitos.replace(' Funcionário  :', '').strip()
    
                # Adicionar o nome à lista
                nomes_funcionarios.append(nome)

                for i, employee in enumerate(nomes_funcionarios):
                    # Crie um escritor de PDF
                    pdf_writer = pdf.PdfWriter()

                    # Adicione a página correspondente ao funcionário
                    pdf_writer.add_page(pdf_reader.pages[i])

                    # Escreva a nova página em um novo arquivo PDF
                    output_path = f"{entry_diretorio.get()}/{employee}.pdf"
                with open(output_path, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
    except Exception as e:
        exibir_mensagem_erro(f"Ocorreu um erro: {e}")

    conclusao()


################################################################################
#### Função para chamar a barra de progresso e a funão principal
def iniciar_processo():
    barra_progresso.set(0)  # Reseta a barra de progresso
    split_pdf_by_employees()  # Executa a função principal

    
################################################################################
#### Função para exibir mensagem de erro ao usuário:

def exibir_mensagem_erro(mensagem):
    janela_erro = ctk.CTkToplevel(div_extrato_pdf)
    janela_erro.title("Erro")

    # Estimativa de largura da janela com base na largura da mensagem
    largura_mensagem = len(mensagem) * 8  # 8 pixels por caractere é uma estimativa
    largura_mensagem = max(300, largura_mensagem)  # Largura mínima de 300 pixels

    janela_erro.geometry(f"{largura_mensagem}x150")  # Altura fixa de 150 pixels

    label = ctk.CTkLabel(master=janela_erro, text=mensagem, wraplength=largura_mensagem - 20)
    label.pack(pady=20, padx=10)

    botao = ctk.CTkButton(master=janela_erro, text="OK", command=janela_erro.destroy)
    botao.pack(pady=10)
    barra_progresso.set(0)

    janela_erro.transient()
    janela_erro.grab_set() 
    percentual_processo.configure(text=f'{int(0)}%')
    percentual_processo.grid(row=6, column=0, padx=20, pady=20, columnspan=5) 
    janela_erro.mainloop()
    div_extrato_pdf.wait_window(janela_erro)


################################################################################
#### Função para exibir mensagem de conclusão:

def conclusao():
    jan_conclusao = ctk.CTkToplevel(div_extrato_pdf)
    jan_conclusao.title("Relatório OK")
    jan_conclusao.geometry("320x150")

    label_conclusao = ctk.CTkLabel(master=jan_conclusao, text='Documento dividido!!')
    label_conclusao.pack(pady=20, padx=10)

    botao = ctk.CTkButton(master=jan_conclusao, text="OK", command=jan_conclusao.destroy)
    botao.pack(pady=10)
    barra_progresso.set(5)
 
    jan_conclusao.grab_set()  
    percentual_processo.configure(text=f'{int(100)}%')
    percentual_processo.grid(row=6, column=0, padx=20, pady=20, columnspan=5) 
    jan_conclusao.mainloop()
    jan_conclusao.mainloop()
    div_extrato_pdf.wait_window(jan_conclusao)


################################################################################
#### Função para pegar caminho do arquivo e diretório para salvar:

def caminho_arquivo():
    arquivo = askopenfilename(title='Selecione o arquivo.pdf:')
    entry_arquivo.delete(0, ctk.END)
    entry_arquivo.insert(0, arquivo)

def caminho_diretorio():
    diretorio = askdirectory(title='Escolha a pasta para salvar os arquivos:')
    entry_diretorio.delete(0, ctk.END)
    entry_diretorio.insert(0, diretorio)

##################################################################################
#### Janela de Interface

div_extrato_pdf = ctk.CTk()
div_extrato_pdf.geometry("1030x320")
div_extrato_pdf.resizable(width=False, height=False)
div_extrato_pdf.title('Dividir Extrato BH')
#janela.iconify() #fecha a janela/aplicação
#janela.deiconify #abre a janela/aplicação
div_extrato_pdf._set_appearance_mode('system') #Tema da aplicação

label_arquivo = ctk.CTkLabel(master=div_extrato_pdf, text='Caminho/Nome Arquivo.pdf (Sem Aspas): ')
label_arquivo.grid(row=0, column=0, padx=10, pady=30)

label_diretorio = ctk.CTkLabel(master=div_extrato_pdf, text='Diretório para salvar Reports (Sem Aspas): ')
label_diretorio.grid(row=1, column=0, padx=10, pady=10)

entry_arquivo = ctk.CTkEntry(master=div_extrato_pdf, width= 700, placeholder_text='caminho/arquivo.pdf (sem aspas) ...', fg_color='#575757')
entry_arquivo.grid(row=0, column=1, padx=10, pady=10)

entry_diretorio = ctk.CTkEntry(master=div_extrato_pdf, width=700, placeholder_text='diretorio para salvar reports (sem aspas) ...', fg_color='#575757')
entry_diretorio.grid(row=1, column=1, padx=10, pady=10)


##################################################################################

botao_dividir = ctk.CTkButton(master=div_extrato_pdf, text='Dividir pdf', command=iniciar_processo)
botao_dividir.grid(row=4, column=0, padx=10, pady=10, columnspan=5, ipadx=80)

botao_arquivo = ctk.CTkButton(master=div_extrato_pdf, text='Ir...', width=10, height=30, command=caminho_arquivo)
botao_arquivo.grid(row=0, column=2)

botao_diretorio = ctk.CTkButton(master=div_extrato_pdf, text='Ir...', width=10, height=30, command=caminho_diretorio)
botao_diretorio.grid(row=1, column=2)


barra_progresso = ctk.CTkProgressBar(master=div_extrato_pdf, width=900)
barra_progresso.grid(row=5, column=0, padx=20, pady=20, columnspan=5)
barra_progresso.set(0)
percentual_processo = ctk.CTkLabel(div_extrato_pdf, text="0%")
percentual_processo.grid(row=6, column=0, padx=20, pady=20, columnspan=5)

div_extrato_pdf.mainloop()

