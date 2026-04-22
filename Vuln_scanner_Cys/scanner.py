import socket
import threading
from queue import Queue

def scan_port(target, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        if sock.connect_ex((target, port)) == 0:
            try:
                sock.send(b"Hello\r\n")
                banner = sock.recv(1024).decode(errors="ignore").strip()
            except:
                banner = "No banner"
            results.append({"port": port, "banner": banner})
        sock.close()
    except:
        pass

def worker(target, q, results):
    while True:
        port = q.get()
        scan_port(target, port, results)
        q.task_done()

def scan_ports(target):
    q = Queue()
    results = []

    for _ in range(200):  # 200 threads
        t = threading.Thread(target=worker, args=(target, q, results))
        t.daemon = True
        t.start()

    for port in range(1, 65536):  # full scan
        q.put(port)

    q.join()
    return results