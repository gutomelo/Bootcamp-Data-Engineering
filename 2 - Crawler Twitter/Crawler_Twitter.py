import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

## Cadastrar as chaves de Acesso
# Api Key
consumer_key = ""
# API secret key
consumer_secret = ""
# Access Token
access_token = "" 
# Access Token Secret
access_token_secret = ""

# Definir um arquivo de saída para armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets_{data_hoje}.txt", "w")

# Implementar uma classe para conexão com o Twitter
class MyListener(StreamListener):
    
    def on_data(self, data):
        #print(data)                    # Se quiser imprimir na tela os dados coletados
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True

    def on_error(self, status):
        print(status)

# Implementar a função Main
if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=["Trump"])     # Pesquisando pelo termo relacionado, no caso "Trump"

