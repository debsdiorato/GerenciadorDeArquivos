#mostrar conteudo do diretório os.listdir()
#criar pastar os.mkdir() e open() para criar arquivos
#os.rename para renomear arquivos
#os.remove para deletar arquivos
#os.rmdir para deletar pastas e shutil.rmtree para deletar pastas com arquivos
from tkinter import *
from tkinter import ttk
import os
from functions.listar import listar_arquivos as listar_arquivos_func #importa a função listar_arquivos do arquivo listar.py
#criar a classe principal e passar a janela como argumento de inicialização
class GerenciadorArquivos():
                                #JANELA
    def __init__(self, root):#init para inicializar a classe
        self.root = root #root é a janela principal
        self.root.title("Gerenciador de Arquivos") #titulo da janela
        self.root.geometry("600x400") #tamanho da janela
        self.root.configure(bg="#b5baba") #cor de fundo da janela
        
        usuario = os.getlogin() #pega o nome do usuario logado
                                #Visual
        lbl_usuario = Label(self.root, text=f"Usuário Conectado: {usuario}", bg="#b5baba", font=("Open Sans", 12))
        lbl_usuario.pack(pady=10) #coloca o label na tela

        # Botão para listar arquivos
        btn_mover = Button(self.root, text="Mover", command=self.mover_arquivos, justify="center")
        btn_mover.pack(pady=3)

        # Botão para criar arquivo
        btn_criar = Button(self.root, text="Criar", command=self.criar_arquivo)
        btn_criar.pack(pady=3)

        # Botão para deletar arquivo
        btn_deletar = Button(self.root, text="Deletar", command=self.deletar_arquivo)
        btn_deletar.pack(pady=3)

        btn_listar = Button(
            self.root,
            text="Listar Arquivos",
            command=lambda: self.listar_arquivos(os.path.join(os.environ['USERPROFILE'], 'Documents'))
        )
        btn_listar.pack(pady=3)

        
        self.listbox = Listbox(self.root, width=50, height=15)
        self.listbox.pack(pady=10)
            

        # Chama a função para listar arquivos ao iniciar
        # FUNCOES DOS BOTOES
        self.listar_pastas_principais()
    def listar_pastas_principais(self):
        self.listbox.delete(0,END)
        user_profile = os.environ['USERPROFILE'] #pega o caminho do usuario logado(do pc dele)
        pastas= {
            "Documentos": "Documents",
            "Imagens": "Pictures",
            "Downloads": "Downloads",
            "Música": "Music",
            "Vídeos": "Videos",
        }

        for nome, pasta in pastas.items():
            caminho = os.path.join(user_profile, pasta) #(junta o caminho do usuario com a pasta)
            if os.path.exists(caminho): #verifica se o caminho existe
                self.listbox.insert(END, nome)


    def mover_arquivos(self):
        print("Movendo arquivos...")

    def criar_arquivo(self):
        print("Criando arquivo...")

    def deletar_arquivo(self):
        print("Deletando arquivo...")

    def listar_arquivos(self, caminho):
        arquivos = listar_arquivos_func(caminho)
        self.listbox.delete(0, END)
        if arquivos:
            for arquivo in arquivos:
                self.listbox.insert(END, arquivo)
        else:
            self.listbox.insert(END, "Nenhum arquivo encontrado.")
            



#instancia para rodar a aplicação, diz que a classe GerenciadorArquivos é a principal e tudo que ela tem será executado
if __name__ == "__main__":
    root = Tk()
    app = GerenciadorArquivos(root)
    root.mainloop()
