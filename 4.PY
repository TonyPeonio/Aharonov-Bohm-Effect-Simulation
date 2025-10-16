#Created using qutip

from qutip import qeye, sigmax, sigmay, sigmaz, tensor, expect, sigmap, sigmam, basis
import matplotlib.pyplot as plt
import numpy as np

#Let J=1

phi = 0

for i in range(0, 5):
    phi+=np.pi/4
    Hamiltonian = -1*(tensor(sigmap(), sigmam())*np.exp(1j*phi) + tensor(sigmam(), sigmap())*np.exp(-1j*phi))
    print(phi)
    print(Hamiltonian)
    print(Hamiltonian.eigenenergies())
    print(Hamiltonian.eigenstates())
    print("\n\n")
