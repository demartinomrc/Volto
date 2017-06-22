import unittest
import test_helper
import volto
import parziale as P
import slice as S

class TestParziale(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(P.Parziale(1))
        
        
    def test_get(self):
        p = P.Parziale(1)
        self.assertEqual(p.index,1)
        
        
        
    def test_slice_append(self):
        
        p = P.Parziale(1)
        s= S.Slice(300,-20,3,1)
        p.slice_append(s)
        self.assertEqual(p.slices.size,1)
        self.assertEqual(p.slices[0].freq,s.freq)
        self.assertEqual(p.slices[0].mag,s.mag)     
        
           
        
    
if __name__ == '__main__':
    unittest.main()
    
    
    