class SetWorker:
    
    def calculate_single_set(self, set):
        set_id = set[0]
        x = set[1]
        a = set[2]
        
        a = [ai * x for ai in a]
        return a
    
    def calculate_n_set(self, set):
        output = [0]*len(set[0][2])
        for i in range(len(set)):
            a = self.calculate_single_set(i)
            output += a #na nunpy prezrzucic
        return output