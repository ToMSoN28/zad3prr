from multiprocessing.managers import BaseManager
from queue import Queue
import sys
from setWorker import SetWorker

class QueueManager(BaseManager): 
    pass

def main(ip, port, mode):
    QueueManager.register('in_queue')
    QueueManager.register('out_queue')
    m = QueueManager(address=(ip, int(port)), authkey=b'BostonCeltics')
    m.connect()
    in_queue = m.in_queue()
    out_queue = m.out_queue()
    setWorker = SetWorker()
    if mode == 'single':
        while (not in_queue.empty()):
            single_input = in_queue.get()
            single_ouptput = setWorker.calculate_single_set(single_input)
            out_queue.put(single_ouptput)
    elif mode == 'workers':
        multi_input = in_queue.get()
        multi_output = setWorker.calculate_n_set(multi_input)
        out_queue.put(multi_output)
    else:
        print('Wrong mode!!! Options: single, worker')
        
    return 0
        
        
        
        
        