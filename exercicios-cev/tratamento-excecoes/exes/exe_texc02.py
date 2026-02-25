import urllib
import urllib.request

try:
    verifica_conexao = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('Erro ao tentar conectar a internet.')
else:
    print('Conexão feita com sucesso.')