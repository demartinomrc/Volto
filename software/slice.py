class Slice:
    
    
    def __init__(self,freq,mag,column,env):
        self.freq=freq
        self.mag=mag
        self.column=column
        self.env=env
        
    def dur(self):
        return self.env.hopsize()/self.env.fs    
        
        
    def at(self):
        return self.dur()*self.column
            
        