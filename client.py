from socket import *
from constCS import *
import threading
import time
import random

def send_request(host, port, operation, numbers):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        
        message = f"{operation} {' '.join(map(str, numbers))}"
        
        start_time = time.time()
        
        s.send(str.encode(message))
        
        response = s.recv(1024)
        
        elapsed_time = time.time() - start_time
        
        print(f"Thread {threading.current_thread().name}: {message} = {bytes.decode(response)} (tempo: {elapsed_time:.2f}s)")
        
        s.close()
        return elapsed_time
    except Exception as e:
        print(f"Erro na thread {threading.current_thread().name}: {e}")
        return None

def run_sequential_test(num_requests=5):
    print("\n" + "="*70)
    print("TESTE SEQUENCIAL (SEM THREADS)")
    print("="*70)
    
    total_time = 0
    
    for i in range(num_requests):
        operation = random.choice(["add", "subtract", "multiply", "divide"])
        numbers = [random.randint(1, 10) for _ in range(random.randint(2, 5))]
        
        elapsed = send_request(HOST, PORT, operation, numbers)
        if elapsed:
            total_time += elapsed
    
    print(f"\nTempo total sequencial: {total_time:.2f}s")
    return total_time

def run_parallel_test(num_threads=5):
    print("\n" + "="*70)
    print("TESTE PARALELO (COM THREADS NO CLIENTE)")
    print("="*70)
    
    threads = []
    results = [None] * num_threads
    
    start_time = time.time()
    
    for i in range(num_threads):
        operation = random.choice(["add", "subtract", "multiply", "divide"])
        numbers = [random.randint(1, 10) for _ in range(random.randint(2, 5))]
        
        thread = threading.Thread(
            target=lambda idx=i: results.__setitem__(idx, send_request(HOST, PORT, operation, numbers)),
            name=f"Cliente-{i+1}"
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    total_time = time.time() - start_time
    individual_times = sum(t for t in results if t is not None)
    
    print(f"\nTempo total paralelo: {total_time:.2f}s")
    print(f"Soma dos tempos individuais: {individual_times:.2f}s")
    print(f"Ganho de desempenho: {individual_times/total_time:.2f}x")
    
    return total_time, individual_times

def main():
    print("="*70)
    print("======= TESTES DE DESEMPENHO - CALCULADORA REMOTA =======")
    print("="*70)

    num_requests = 5

    seq_time = run_sequential_test(num_requests)

    par_time, individual_times = run_parallel_test(num_requests)

    print("\n" + "="*70)
    print("COMPARAÇÃO FINAL")
    print("="*70)
    print(f"Tempo sequencial: {seq_time:.2f}s")
    print(f"Tempo paralelo: {par_time:.2f}s")
    print(f"Aceleração: {seq_time/par_time:.2f}x")
    print("="*70)

if __name__ == "__main__":
    main()