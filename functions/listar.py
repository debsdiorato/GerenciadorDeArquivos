import os 

def listar_arquivos(caminho):
    try: 
        return os.listdir(caminho)
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")
        return []