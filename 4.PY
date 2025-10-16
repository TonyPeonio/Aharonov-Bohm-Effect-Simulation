#Created using qutip

from qutip import qeye, sigmax, sigmay, sigmaz, tensor, expect, sigmap, sigmam, basis
import matplotlib.pyplot as plt
import numpy as np

#Let J=1

phi = 0
eigen_output_file = open("eigen_file.txt", 'w')

for i in range(0, 5):
    Hamiltonian = -1*(tensor(sigmap(), sigmam())*np.exp(1j*phi) + tensor(sigmam(), sigmap())*np.exp(-1j*phi))

    eigen_output_file.write("Curernt Phi: ")
    print(str(phi) + "\n\n")
    print("Hamiltonian with Current Phi: " )
    print(str(Hamiltonian) + "\n")
    print("Hamiltonian Eigenenergies (Eigenvalues): ")
    print(str(Hamiltonian.eigenenergies()) + "\n")
    print("Hamiltonian Eigenstates (Eigenvectors): ")
    print(str(Hamiltonian.eigenstates()) + "\n")
    print("\n\n\n")
    phi+=np.pi/4


