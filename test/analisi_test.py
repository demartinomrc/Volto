import unittest
import test_helper
import volto
import analisi as A

class TestAnalisi(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(A.Analisi("../suoni/Salvatore.wav"))
        
           
    def test_analisi(self):
        a = A.Analisi("../suoni/Salvatore.wav")
        a.analyze()
        self.assertEqual(type(a.hfreq).__name__,"ndarray")
        self.assertTrue(len(a.hfreq) > 0)
        self.assertEqual(len(a.hfreq),3232)
    
if __name__ == '__main__':
    unittest.main()
    
    