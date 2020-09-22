import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp
import scipy.io
from scipy.interpolate import interp1d
# dane
data13 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Dane/Dane energetyczne/data_98.mat',
                               squeeze_me=True).values())[3] # (dysk WAT)
# obliczenia
startp, starte, krok, rzad = 9750, 11000, 30, 6
n = np.arange(startp,starte,krok)
p = np.poly1d( np.polyfit(n,data13[n],rzad) ) # aproksymacja
y = np.polyval(p,n)     
fun = interp1d(n,data13[n],kind='cubic')      # interpolacja
plt.plot(n,data13[n],'ko',n,y,'g-',n,fun(n),'b')
plt.legend(('data','polynomial','interp'),loc='best') # legenda
