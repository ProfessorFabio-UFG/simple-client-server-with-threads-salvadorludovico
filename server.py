from socket import *
from constCS import *
import threading
import time


def handle_client(conn, addr):
    print(f"Nova conexão de {addr}")
    
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print(f"Cliente {addr} desconectado.")
                break
                
            decoded_data = bytes.decode(data)
            print(f"Dados recebidos de {addr}: {decoded_data}")
            
            response = handle_request(decoded_data)
            conn.send(str.encode(response))
        except Exception as e:
            print(f"Erro na conexão com {addr}: {e}")
            break
    
    conn.close()

def process_add(args):
    result = 0
    for arg in args:
        result += int(arg)
    time.sleep(2)  
    return result

def process_subtract(args):
    if not args:
        return 0
    result = int(args[0])
    for arg in args[1:]:
        result -= int(arg)
    time.sleep(2)  
    return result

def process_multiply(args):
    result = 1
    for arg in args:
        result *= int(arg)
    time.sleep(2)  
    return result

def process_divide(args):
    if not args:
        return "Erro: Sem argumentos"
    result = int(args[0])
    for arg in args[1:]:
        if int(arg) == 0:
            return "Erro: Divisão por zero"
        result /= int(arg)
    time.sleep(2)  
    return result

def handle_request(decoded_data):
    command_map = {
        "add": process_add,
        "multiply": process_multiply,
        "subtract": process_subtract,
        "divide": process_divide
    }

    parts = decoded_data.split()
    if not parts:
        return "Comando vazio"
        
    function = parts[0]
    func = command_map.get(function)

    if func:
        try:
            result = func(parts[1:])
            return str(result)
        except Exception as e:
            return f"Erro ao processar: {e}"
    else:
        return "Comando Desconhecido"

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print("Servidor com threads ativo. Esperando conexões...")

    try:
        while True:
            conn, addr = s.accept()
            
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.daemon = True  
            client_thread.start()
            print(f"Thread ativa para cliente {addr}. Threads ativas: {threading.active_count()-1}")
    except KeyboardInterrupt:
        print("\nServidor interrompido manualmente.")
    finally:
        s.close()

if __name__ == "__main__":
    main()