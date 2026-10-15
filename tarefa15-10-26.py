import threading
import time

def processar_recurso():

    try:
        f = open("status.txt", "r")
        valor = f.read().strip()
        f.close()
    except:
        print("Erro: Arquivo status.txt nao encontrado!")
        return

    if valor == "0":
        print("Recurso disponível. Reservando recurso...")
        
        f = open("status.txt", "w")
        f.write("1")
        f.close()
        
        print("Utilizando recurso...")
        time.sleep(3)
        
        print("Liberando recurso...")
        
        f = open("status.txt", "w")
        f.write("0")
        f.close()
        
        print("Recurso liberado com sucesso!")

    elif valor == "1":
        print("Recurso ocupado. Tente novamente mais tarde.")

    else:
        print("Valor inválido no arquivo")


t1 = threading.Thread(target=processar_recurso, args=(1,))

t1.start()
