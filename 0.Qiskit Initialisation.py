# Qiskit Initialization: 

# 1. CORE CIRCUITS
# QuantumCircuit is the central object to build quantum algorithms
from qiskit import QuantumCircuit, transpile, assemble

#2. EXECUTION 
# Aer provides simulators for testing quantum circuits locally
from qiskit.providers.aer import AerSimulator

# IBMQ is used for running circuits on actual quantum devices
from qiskit_ibm_provider import IBMProvider  # Uncomment when using IBM Quantum devices

#3. VISUALIZATION TOOLS
# Tools to visualize circuits and results (like measurement histograms)
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt

# 4. STATEVECTOR SIMULATION
# Used for inspecting quantum state (amplitudes) at any point
from qiskit.quantum_info import Statevector

#5. OTHER 
import numpy as np


# Create a simple quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply gates
qc.h(0)                 # Hadamard gate on qubit 0
qc.cx(0, 1)             # CNOT gate from qubit 0 to 1 (entanglement)
qc.measure([0,1], [0,1])# Measure both qubits

# Draw the circuit
print("Quantum Circuit:")
print(qc.draw())

# Use AerSimulator to simulate
sim = AerSimulator()

# Transpile the circuit (optimization step tailored to the backend)
compiled_qc = transpile(qc, sim)

# Run the circuit and get results
job = sim.run(compiled_qc, shots=1024)
result = job.result()
counts = result.get_counts()

# Show the results as histogram
print("Measurement Counts:", counts)
plot_histogram(counts)
plt.show()

#Visualize statevector before measurement
# Reset circuit to exclude measurement and inspect state
qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0, 1)

# Get the statevector
sv = Statevector.from_instruction(qc2)
print("Statevector:", sv)
sv.draw('latex')  # Requires LaTeX or Jupyter support
