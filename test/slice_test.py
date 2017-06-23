import unittest
import test_helper
import volto
import analisi as A
import slice as S

class TestAnalisi(unittest.TestCase):

    def setUp(self):        
        self.env= A.Analisi("../suoni/Salvatore.wav")
        self.freq=261.6
        self.mag=-18
        self.column=5
        
        
    def test_creation(self):
        s= S.Slice(self.freq,self.mag,self.column,self.env)
        self.assertTrue(s)
        
    def test_dur(self):
        s= S.Slice(self.freq,self.mag,self.column,self.env)
        self.assertEqual(s.dur(),self.env.hopsize()/self.env.fs)
        
        
    def test_at(self):
        s= S.Slice(self.freq,self.mag,self.column,self.env)
        self.assertEqual(s.at(),(self.env.hopsize()/self.env.fs)*self.column)    
    
    
if __name__ == '__main__':
    unittest.main()
        
        