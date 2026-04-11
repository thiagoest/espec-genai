import requests
import threading

URL = "http://127.0.0.1:8000/teste_async"

def fazer_requisicao(i):
    response = requests.get(URL, params={"id": i})
    print(response.text)

threads = []

for i in range(1, 101):
    t = threading.Thread(target=fazer_requisicao, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()