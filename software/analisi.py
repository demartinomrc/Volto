import volto as V


class Analisi:
	
    def __init__(self,fname):
    	"""
    	Analyze a sound with the harmonic plus stochastic model
    	inputFile: input sound file (monophonic with sampling rate of 44100)
    	window: analysis window type (rectangular, hanning, hamming, blackman, blackmanharris)	
    	finestrainterna: analysis window size 
    	finestraesterna: fft size (power of two, bigger or equal than M)
    	threshold: magnitude threshold of spectral peaks 
    	minSineDur: minimum duration of sinusoidal tracks
    	maxharmonics: maximum number of harmonics
    	minf0: minimum fundamental frequency in sound
    	maxf0: maximum fundamental frequency in sound
    	f0et: maximum error accepted in f0 detection algorithm                                                                                            
    	harmDevSlope: allowed deviation of harmonic tracks, higher harmonics have higher allowed deviation
    	stocf: decimation factor used for the stochastic approximation
    	returns inputFile: input file name; fs: sampling rate of input file,
    	hfreq, hmag: harmonic frequencies, magnitude;
        mYst: stochastic residual
        fs: sampling frequencies
    	"""
        self.filename=fname
        self.window="blackman"
        self.finestrainterna=601
        self.finestraesterna=1024
        self.threshold=-100
        self.minSineDur=0.1
        self.maxharmonics=20
        self.maxf0=700
        self.minf0=20
        self.f0et=5 
        self.harmDevSlope= 0.01
        self.stocf= 0.1
        self.hfreq=self.hmag=self.hphase=self.mYst=[]
        self.set_file(self.filename)

    def set_file(self,fname):
        self.filename= fname
        (self.fs,self.signal) =V.UF.wavread(self.filename)
        
                
    def halfwin(self):
        return self.finestraesterna/2 
        
    def hopsize(self):
        return self.halfwin()/4
        
    def analyze(self):
        
      
        w = V.get_window(self.window,self.finestrainterna)
        
        self.hfreq,self.hmag,self.hphase,self.mYst= V.HPS.hpsModelAnal(self.signal, self.fs, w, self.finestraesterna, self.hopsize(), self.threshold, self.maxharmonics, self.minf0, self.maxf0, self.f0et, self.harmDevSlope, self.minSineDur, self.halfwin(), self.stocf)
        
        