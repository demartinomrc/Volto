import unittest
import test_helper
import volto
import parziale as P

class TestParziale(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(P.Parziale(100,20))
        
        
    def test_get(self):
        p = P.Parziale(100,20)
        self.assertEqual(p.freq,100)
        self.assertEqual(p.mag,20)
        
        
    def test_set(self):
        p = P.Parziale(100,20)
        p.freq=300
        p.mag= -20
        self.assertEqual(p.freq,300)
        self.assertEqual(p.mag,-20)
        
        
    
if __name__ == '__main__':
    unittest.main()
    
    
    