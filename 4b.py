#Created using qutip

from qutip import qeye, sigmax, sigmay, sigmaz, tensor, expect, sigmap, sigmam, basis
import matplotlib.pyplot as plt
import numpy as np

#Let J=1
#Let 1 = |0>
#Let 2 = |1>
#Let 3 = |2>
#Let 4 = |3>

#Begin with phi = 0
phi = 0

one_state = basis(4, 0)
two_state = basis(4, 1)
three_state = basis(4, 2)
four_state = basis(4, 3)


for i in range(0, 5):
    #Create blank lists for each loop
    xs = []
    one = []
    two = []
    three = []
    four = []

    #Set the hamiltonian equal to the equation (phi dependent)
    Hamiltonian = two_state*one_state.dag()*np.exp(-1j*phi) + one_state*two_state.dag()*np.exp(1j*phi) + three_state*two_state.dag() + two_state*three_state.dag() + four_state*three_state.dag() + three_state*four_state.dag() + one_state*four_state.dag() + four_state*one_state.dag()

    current_state = one_state

    xs.append(0)
    one.append(abs(one_state.overlap(current_state))**2)
    two.append(abs(two_state.overlap(current_state))**2)
    three.append(abs(three_state.overlap(current_state))**2)
    four.append(abs(four_state.overlap(current_state))**2)

    dt = 0.1
    for t in range(1, 81):
        current_state = (-1j * Hamiltonian * dt).expm() * current_state
        current_state = current_state.unit()
        xs.append(t/10)
        one.append(abs(one_state.overlap(current_state))**2)
        two.append(abs(two_state.overlap(current_state))**2)
        three.append(abs(three_state.overlap(current_state))**2)
        four.append(abs(four_state.overlap(current_state))**2)
        
    plt.plot(xs, one, label = "|0>")
    #Added slight offset to two because it was invisible in some of the graphs behind other lines
    plt.plot(xs, np.array(two) + 0.005, label = "|1>")
    plt.plot(xs, three, label = "|2>")
    plt.plot(xs, four, label = "|3>")
    plt.legend()
    if(i == 0):
        plt.savefig("4b1.png")
    if(i == 1):
        plt.savefig("4b2.png")
    if(i == 2):
        plt.savefig("4b3.png")
    if(i == 3):
        plt.savefig("4b4.png")
    else:
        plt.savefig("4b5.png")

    plt.clf()

    phi+=np.pi/4



