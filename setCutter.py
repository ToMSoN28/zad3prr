class SetCutter:
    
    def __init__(self, A, X):
        self.A = A
        self.X = X
        
    def get_set_id(self, set_id):
        output = []
        x = self.X[set_id][0]
        a = []
        for i in range(len(self.A[0])):
            a.append(self.A[set_id][i])
        output.append(set_id)
        output.append(x)
        output.append(a)
        return output
    
    def get_set_worker_id(self, worker_number, worker_id):
        n = int(len(self.A[0])/worker_number)
        output = []
        for i in range(n*worker_id, n*(worker_id+1)):
            output.append(self.get_set_id(i))
        return output