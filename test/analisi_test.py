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
        
    def test_set_file(self):           
         a = A.Analisi("../suoni/Salvatore.wav")
         self.assertEqual(a.fs,44100)
         a.set_file("../suoni/test44100.wav")
         self.assertEqual(a.fs,44100)
               
        # questo test non si pu ancora fare perch sms tools non vede file diversi da 44100
        #a = A.Analisi("../suoni/test48000.wav")
        #self.assertEqual(self.fs,48000)
        #a.set_file("../suoni/test96000.wav")
        #self.assertEqual(self.fs,96000)
        
        
    def test_halfwin(self):
        a = A.Analisi("../suoni/Salvatore.wav")
        self.assertEqual(a.halfwin(),a.finestraesterna/2)
        
    def test_hopsize(self):
        a = A.Analisi("../suoni/Salvatore.wav")
        self.assertEqual(a.hopsize(),a.finestraesterna/8)
            
        
        
            
if __name__ == '__main__':
    unittest.main()
    
    