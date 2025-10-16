#Created using qutip

from qutip import qeye, sigmax, sigmay, sigmaz, tensor, expect, sigmap, sigmam, basis
import matplotlib.pyplot as plt
import numpy as np

#Let J=1

phi = 0
eigen_output_file = open("eigen_file.txt", 'w')

one_state = (basis(4, 0))
two_state = (basis(4, 1))
three_state = (basis(4, 2))
four_state = (basis(4, 3))

for i in range(0, 5):
    Hamiltonian = two_state*one_state.dag()*np.exp(-1j*phi) + one_state*two_state.dag()*np.exp(1j*phi) + three_state*two_state.dag() + two_state*three_state.dag() + four_state*three_state.dag() + three_state*four_state.dag() + one_state*four_state.dag() + four_state*one_state.dag()

    eigen_output_file.write("Curernt Phi: ")
    eigen_output_file.write(str(phi) + "\n\n")
    eigen_output_file.write("Hamiltonian with Current Phi: " )
    eigen_output_file.write(str(Hamiltonian) + "\n")
    eigen_output_file.write("Hamiltonian Eigenenergies (Eigenvalues): ")
    eigen_output_file.write(str(Hamiltonian.eigenenergies()) + "\n")
    eigen_output_file.write("Hamiltonian Eigenstates (Eigenvectors): ")
    eigen_output_file.write(str(Hamiltonian.eigenstates()) + "\n")
    eigen_output_file.write("\n\n\n")
    phi+=np.pi/4


