
print()
"""
O Modulo shutil
permiti copiar, mover, renomear, apagar arquivos.
comandos shutil:
import shutil, shutil.copy() => Chamar shutil.copy( origem , destino ) copiará o 
arquivo no path origem para a pasta no path destino . (Tanto origem quanto 
destino são strings.) Se destino for o nome de um arquivo, ele será usado como 
o novo nome do arquivo copiado. Essa função retorna uma string com o path do arquivo copiado
exemplo : import shutil
          os.listdir()
          shutil.copy('orige do aarquivo', '/destino do arquivo/')
             
          
          obs : shutil.copy() copiar apenas um arquivo
          """
import os, shutil

print("Arquivos que estão presentes no diretório", os.listdir())
def copia_arquivos():
    arquivos = os.listdir()
    print(arquivos)
    while True:
        print("Preparando arquivos para transporte! Aguarde ...")
        movendo_arquivo = shutil.copy('test.txt', 'repositorioTeste')
        print("Arquivo movido com sucesso para, ", movendo_arquivo)
        break
    return 'OK vamos para o próximo bloco de código.'

copia_arquivos()