import numpy as np

class SetWorker:
    def __init__(self):
        pass
    
    def calculate_single_set(self, set):
        set_id = set[0]
        x = set[1]
        a = np.array(set[2])
        
        a *= x
        return a
    
    def calculate_n_set(self, set):
        output = np.array([0.0]*len(set[0][2]))
        for i in range(len(set)):
            a = self.calculate_single_set(set[i])
            output += a
        return output