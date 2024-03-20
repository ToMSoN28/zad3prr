import numpy as np

class SetSumer:
    
    def __init__(self, n):
        self.result = np.array([0.0]*n)
        
    def add(self, o_set):
        self.result += np.array(o_set)
        
    