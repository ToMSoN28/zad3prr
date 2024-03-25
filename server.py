from queue_manager import QueueManagerServer
from queue import Queue
import sys


def main(ip : str, port : str, auth_key : str):
    port_int = int(port)
    manager = QueueManagerServer(ip, port_int, bytearray(auth_key, 'utf-8'))
    print(f"Server is running at {ip}:{port}")
    manager.run_server()


if __name__ == '__main__':
    main(*sys.argv[1:])