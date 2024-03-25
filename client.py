import sys
from setCutter import SetCutter
from setWorker import SetWorker
from setSumer import SetSumer
from queue_manager import QueueManagerClient

def main(ip, port, auth_key, Afile, Xfile, mode, worker_n=0):
    worker_n_int = int(worker_n)
    port_int = int(port)
    manager = QueueManagerClient(ip, port_int, bytearray(auth_key, 'utf-8'))
    manager.connect()

    A = read(Afile)
    X = read(Xfile)
    setCutter = SetCutter(A, X)
    setSumer = SetSumer(len(A[0]))

    if mode == 'single':
        counter = len(X)
        for i in range(len(X)):
            manager.in_queue().put(setCutter.get_set_id(i))
    elif mode == 'worker':
        if worker_n_int == 0:
            print ('wrong worker number')
            return 1
        else:
            counter = worker_n_int
            for i in range (worker_n_int):
                manager.in_queue().put(setCutter.get_set_worker_id(worker_n_int, i))
    else:
        print('Wrong mode!!! Options: single, worker')
        return 1
        
    # teraz już jesrt git i będzie na spojkojnie czekał
    # doda wszyskie rzecy bo liczy i czeka na wszyskie odpowiedzi
    
    while(True):
        if (not manager.out_queue().empty()):
            setSumer.add(manager.out_queue().get())
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