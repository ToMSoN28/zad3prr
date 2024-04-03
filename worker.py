from queue_manager import QueueManagerClient
from queue import Queue
import sys
from setWorker import SetWorker

def main(ip : str, port : str, auth_key : str, mode : str):
    port_int = int(port)
    manager = QueueManagerClient(ip, port_int, bytearray(auth_key, 'utf-8'))
    manager.connect()
    setWorker = SetWorker()
    if mode == 'single':
        while (True):
            if not manager.in_queue().empty():
                single_input = manager.in_queue().get()
                single_ouptput = setWorker.calculate_single_set(single_input)
                manager.out_queue().put(single_ouptput)
    elif mode == 'worker':
        while (True):
            if not manager.in_queue().empty():
                multi_input = manager.in_queue().get()
                multi_output = setWorker.calculate_n_set(multi_input)
                manager.out_queue().put(multi_output)
                break
    else:
        print('Wrong mode!!! Options: single, worker')
        
    return 0

if __name__ == '__main__':
    main(*sys.argv[1:])