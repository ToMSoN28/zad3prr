from multiprocessing.managers import BaseManager
from queue import Queue
import sys
from setCutter import SetCutter

class QueueManager(BaseManager): 
    pass

def main(ip, port, Afile, Xfile):
    A = read(Afile)
    X = read(Xfile)
    setCutter = SetCutter(A, X)
    set_0 = setCutter.get_set_id(0)
    print(set_0)
    # QueueManager.register('in_queue')
    # m = QueueManager(address=(ip, int(port)), authkey=b'BostonCeltics')
    # m.connect()
    # queue = m.in_queue()
    # queue.put('hello')
    # print( queue.get() )
    
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