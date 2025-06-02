# %%
#final circuit, fully working
from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister
import numpy as np

def cp_gate(qc,phi, control, target):
    qc.p(phi/2, target)
    qc.cx(control, target)
    qc.p(-phi/2, target)
    qc.cx(control, target)
    qc.p(phi/2, control)



def qft(qc, qubits):
    n = len(qubits)
    for i in reversed(range(n)):
        qc.h(qubits[i])
        for j in reversed(range(i)):
            angle = np.pi/(2**(i-j))
            cp_gate(qc, angle, qubits[j], qubits[i])

def iqft(qc, qubits):
    n = len(qubits)
    for i in range(n):
        for j in range(i):
            angle = -np.pi/(2**(i-j))
            cp_gate(qc, angle, qubits[j], qubits[i])

        qc.h(qubits[i])
        qc.p(np.pi/2,qubits[i])


def controlled_adder(qc, d, a, b, z, ancilla):
    #based on Draper (2000)
    qft(qc, b)
    qc.barrier()
    for i in reversed(range(d)):
        for j in reversed(range(i+1)):
            angle = np.pi/(2**(i-j))
            qc.x(z)
            qc.ccx(z, a[j], ancilla)
            cp_gate(qc, angle, ancilla, b[i])
            qc.p(-angle/2, ancilla)
            qc.ccx(z, a[j], ancilla)
            qc.x(z)
    qc.barrier()
    iqft(qc, b)


def controlled_multiplier(qc,d,x,y,z,result):
    #based on 
    ancilla_1 = AncillaRegister(d, 'anc_1')
    ancilla_2 = AncillaRegister(1, 'anc_2')
    qc.add_register(ancilla_1)
    qc.add_register(ancilla_2)
    
    # Initialize result to 0 (for addition, y gets copied over but we do not want that during multiplication)
    for i in range(d):
        qc.cx(y[i], result[i])
    
    qft(qc, result)

    qc.barrier()

    for i in range(d):
        qc.ccx(z,y[i],ancilla_1[0])

        for j in range(d):
            qc.ccx(x[j],ancilla_2[0],ancilla_1[j])

        for j in range(d): #shift and add multiplication
            for k in range(d):
                if j+k<d:
                    angle=np.pi/(2**k)
                    cp_gate(qc,angle,ancilla_1[j],result[j+k])

        for j in reversed(range(d)):
            qc.ccx(x[j],ancilla_2[0],ancilla_1[j])

        qc.ccx(z,y[i],ancilla_1[0])

    qc.barrier()

    iqft(qc,result)




def Qcalc(d):
    # Create registers
    x = QuantumRegister(d, 'x')
    y = QuantumRegister(d, 'y')
    z = QuantumRegister(1, 'z')
    result = QuantumRegister(d, 'result')
    ancilla = AncillaRegister(1, 'ancilla')  
    
    qc = QuantumCircuit(result,z,y,x, ancilla)

    # Copy y to result (initial value for addition)
    for i in range(d):
        qc.cx(y[i], result[i])
    qc.barrier()


    controlled_adder(qc, d, x, result,z,ancilla)

    qc.barrier()
    
    controlled_multiplier(qc,d,x,y,z,result)
    qc.barrier()
    
    return qc


d=2
qc=Qcalc(d)
qc.draw(output="mpl", style="bw",fold=-1)





# %%
#gate count
qc.count_ops()


# %%
#gate depth
qc.depth()


# %%
#number of qubits
qc.num_qubits


