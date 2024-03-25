from multiprocessing.managers import BaseManager
from queue import Queue

class QueueManager():
    manager : BaseManager

    def __init__(self):
        self.manager = None

    def create_manager(self, ip : str, port : int, authkey : bytearray):
        self.manager = BaseManager(address=(ip, port), authkey=authkey)

    def in_queue(self) -> Queue:
        return self.manager.in_queue()

    def out_queue(self) -> Queue:
        return self.manager.out_queue()

class QueueManagerServer(QueueManager):
    def __init__(self, ip : str, port : int, authkey : bytearray):
        super().__init__()

        self.inqueue = Queue()
        self.outqueue = Queue()

        BaseManager.register('in_queue', callable=lambda:self.inqueue)
        BaseManager.register('out_queue', callable=lambda:self.outqueue)

        self.create_manager(ip, port, authkey)

    def run_server(self):
        server = self.manager.get_server()
        server.serve_forever()

class QueueManagerClient(QueueManager):
    def __init__(self, ip : str, port : int, authkey : bytearray):
        super().__init__()

        BaseManager.register('in_queue')
        BaseManager.register('out_queue')

        self.create_manager(ip, port, authkey)

    def connect(self):
        self.manager.connect()