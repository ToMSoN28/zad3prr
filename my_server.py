from multiprocessing.managers import BaseManager
from queue import Queue
import sys


class QueueManager(BaseManager):
    pass


def main(ip, port):
    in_queue = Queue()
    out_queue = Queue()
    QueueManager.register('in_queue', callable=lambda:in_queue)
    QueueManager.register('out_queue', callable=lambda:out_queue)
    manager = QueueManager(address=(ip, int(port)), authkey=b'BostonCeltics')
    server = manager.get_server()
    server.serve_forever()


if __name__ == '__main__':
    main(*sys.argv[1:])
