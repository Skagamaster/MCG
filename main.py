from MC_glauber import *
import time
import numpy as np

# Imports the main library file

# DisplayData()

N = 100
Particle1 = '197Au'
Particle2 = '197Au'
A1 = 197
A2 = 197
Energy = 14.5  # GeV
bRange = 1.1
model1 = '2pF'
model2 = '2pF'
Range = 2
Bins = 100

time_start = time.perf_counter()
# help(Collider)  # Shows the documentation for the Collider function
b, Nucleus1, Nucleus2, Npart, Ncoll, Maxr, Rp1, Rp2 = Collider(N, Particle1, A1, Particle2, A2, model1, model2,
                                                               Energy, bRange, Range, Bins)

np.save(r"C:\Users\dansk\Documents\Thesis\Tristan\Ncoll_14.npy", Ncoll)
np.save(r"C:\Users\dansk\Documents\Thesis\Tristan\Npart_14.npy", Npart)
np.save(r"C:\Users\dansk\Documents\Thesis\Tristan\b_14.npy", b)

time_stamp_1 = time.perf_counter()
print("Collider run time:", time.perf_counter()-time_start)

# help(PlotNuclei)
PlotNuclei(Nucleus1, Nucleus2, Particle1, Particle2, model1, model2, Rp1, Rp2, Range, Bins)

# help(ShowCollision)
ShowCollision(N, Particle1, A1, Particle2, A2, Rp1, Rp2, Nucleus1, Nucleus2, b, Npart, Ncoll, Maxr)

# help(PlotResults)
PlotResults(b, Npart, Ncoll, Particle1, Particle2, N, Energy, 100)

'''
N = 100
Particle1 = '63Cu'
Particle2 = '63Cu'
A1 = 63
A2 = 63
Energy = 200
bRange = 1.1
model1 = '2pF'
model2 = '2pF'
Range = 2
Bins = 100
b, Nucleus1, Nucleus2, Npart, Ncoll, Maxr, Rp1, Rp2 = Collider(N, Particle1, A1, Particle2, A2, model1, model2, Energy,
                                                               bRange, Range, Bins)
PlotResults(b, Npart, Ncoll, Particle1, Particle2, N, Energy, 22)
'''
