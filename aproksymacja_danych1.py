# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:45:29 2020

@author: figonpiot
"""

# inicjacja danych
import matplotlib.pyplot as plt
import numpy as np
import scipy.io 
mat = list(scipy.io.loadmat('G:/Czarny Pendrive/Szary Komputer/2/Doktorat/ss/ss/GIHA/Rejestracje/R5uF_mat.mat',squeeze_me=True).values())[3]
N_mat = len(mat)
n = np.arange(0,int(N_mat/2),1,dtype=np.int)
u = mat[0:int(N_mat/2)]
u = u/u.max()
i = mat[int(N_mat/2):int(N_mat)]
i = i/i.max()
# wykresy
fig = plt.figure(figsize=(7.5,5),facecolor='white')
ax = fig.gca()
ax.plot(n,u,n,i)
ax.set_xlim(179e3,180e3)
tin = 179200
u1, i1 = u[int(101e3):int(101300)], i[int(101e3):int(101300)]
#############################################################################
### wlasciwa czesc programu ###
# aproksymacja funkcji wielomianem rzedu _rzad_wielomianu
# u1 to dane wejsciowe uzyskane np. z mat-pliku procedura
# mat = scipy.io.loadmat(sciezka_dostepu,squeeze_me=True).values())[3] # rownoczesnie konwertuje liste do np.array
N_mat = len(mat)
rzad_wielomianu = 3
z = np.polyfit(np.arange(0,len(u1),1),u1,rzad_wielomianu)        # generowanie wspolczynnikow wielomianu
p = np.poly1d(z)                                                 # konwersja do klasy poly1d
y = np.polyval(p,np.arange(0,len(u1),1))                         # generowanie wartosci funkcji aproksymujacej
plt.plot(np.arange(0,len(u1),1),y,np.arange(0,len(u1),1),u1)     # wykres
### koniec wlasciwej czesci programu ###
#############################################################################
