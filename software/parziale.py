import numpy as np

class Parziale:
    
    def __init__(self,k):
        self.slices=np.array([])
        self.index=k
        
        
    def slice_append(self,s):
        self.slices= np.append(self.slices,[s]) 
            
         