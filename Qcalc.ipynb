#correct adder, multiplier is not good
from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister



def cp_gate(qc,phi, control, target):
    # Apply P(ϕ/2) to target
    qc.p(phi/2, target)
    # Apply CNOT (control -> target)
    qc.cx(control, target)
    # Apply P(-ϕ/2) to target
    qc.p(-phi/2, target)
    # Apply CNOT again (control -> target)
    qc.cx(control, target)
    # Apply P(ϕ/2) to control (critical for correct phase!)
    qc.p(phi/2, control)

def qft(qc, qubits):
    """Quantum Fourier Transform on given qubits"""
    n = len(qubits)
    for i in reversed(range(n)):
        qc.h(qubits[i])
        for j in reversed(range(i)):
            angle = np.pi/(2**(i-j))
            cp_gate(qc, angle, qubits[j], qubits[i])

def iqft(qc, qubits):
    """Inverse Quantum Fourier Transform on given qubits"""
    n = len(qubits)
    for i in range(n):
        for j in range(i):
            angle = -np.pi/(2**(i-j))
            cp_gate(qc, angle, qubits[j], qubits[i])

        qc.h(qubits[i])
        qc.p(np.pi/2,qubits[i])

def adder(qc,d,a,b):
    """QFT adder with all phase corrections"""
    # QFT on b register
    qft(qc,b)

    # Controlled addition with phase compensation
    for i in reversed(range(d)):
        for j in reversed(range(i+1)):
            angle = np.pi/(2**(i-j))
            cp_gate(qc,angle,a[j],b[i])
            #qc.cp(angle, a[j], b[i])
            qc.p(-angle/2, a[j])  # Phase compensation
    
    # Exact inverse QFT
    iqft(qc,b)

def controlled_adder(qc, d, a, b, z, ancilla):
    """Controlled adder (when z=0)"""
    # QFT on target register
    qft(qc, b)
    
    # Perform controlled addition
    for i in reversed(range(d)):
        for j in reversed(range(i+1)):
            angle = np.pi/(2**(i-j))
            # Implement controlled phase operation (when z=0)
            qc.x(z)
            qc.ccx(z, a[j], ancilla)
            cp_gate(qc, angle, ancilla, b[i])
            qc.p(-angle/2, ancilla)
            qc.ccx(z, a[j], ancilla)
            qc.x(z)
    
    # IQFT on target register
    iqft(qc, b)



def qcalc(d):
    # Create registers
    x = QuantumRegister(d, 'x')
    y = QuantumRegister(d, 'y')
    z = QuantumRegister(1, 'z')
    result = QuantumRegister(d, 'result')
    ancilla = AncillaRegister(1, 'ancilla')  # Only need 1 ancilla
    
    # Create circuit
    qc = QuantumCircuit(result,z,y,x, ancilla)
    qc.x(x[0])  # LSB
    qc.x(x[1])  # Middle bit
    qc.x(y[1])  # y = 2 (|010⟩)
    qc.x(z)     # Enable multiplier (z=1)
    # Copy y to result (initial value for addition)
    for i in range(d):
        qc.cx(y[i], result[i])
    qc.barrier()
    # Implement controlled operations based on z
    controlled_adder(qc, d, x, result,z,ancilla)


    #adder(qc,d,x,result)
    qc.barrier()
    
    # Reset the result register for multiplication
    #for i in range(d):
    #    qc.cx(y[i], result[i])  # Undo the initial copy
    #qc.barrier()
    
    # Implement controlled multiplication
    controlled_multiplier(qc, d, x,y, result, z,ancilla)
    #qc.barrier()
    
    return qc


d=2
qc=qcalc(d)
qc.draw(output="text", style="bw")#,fold=-1
state=Statevector(qc)
state.draw('latex')
