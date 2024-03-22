from multiprocessing.managers import BaseManager
from queue import Queue
import sys
from setCutter import SetCutter
from setWorker import SetWorker
from setSumer import SetSumer

class QueueManager(BaseManager): 
    pass

def main(ip, port, Afile, Xfile, mode, worker_n=0):
    A = read(Afile)
    X = read(Xfile)
    setCutter = SetCutter(A, X)
    setSumer = SetSumer(len(A[0]))

    
    QueueManager.register('in_queue')
    QueueManager.register('out_queue')
    m = QueueManager(address=(ip, int(port)), authkey=b'BostonCeltics')
    m.connect()
    in_queue = m.in_queue()
    out_queue = m.out_queue()
    if mode == 'single':
        counter = len(X)
        for i in range(len(X)):
            in_queue.put(setCutter.get_set_id(i))
    elif mode == 'worker':
        if worker_n == 0:
            print ('wrong worker number')
        else:
            counter = worker_n
            for i in range (worker_n):
                in_queue.put(setCutter.get_set_worker_id(worker_n, i))
    else:
        print('Wrong mode!!! Options: single, worker')
        
    # teraz już jesrt git i będzie na spojkojnie czekał
    # doda wszyskie rzecy bo liczy i czeka na wszyskie odpowiedzi
    
    while(True):
        if (not out_queue.empty()):
            setSumer.add(out_queue.get())
            counter -= 1
            if counter == 0:
                break
    
    print(setSumer.result)
            
    
    
def read(fname):
	f = open(fname, "r")
	nr = int(f.readline())
	nc = int(f.readline())

	A = [[0] * nc for x in range(nr)]
	r = 0
	c = 0
	for i in range(0,nr*nc):
		A[r][c] = float(f.readline())
		c += 1
		if c == nc:
			c = 0
			r += 1

	return A
    
if __name__ == '__main__':
    main(*sys.argv[1:])