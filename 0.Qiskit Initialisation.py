# Qiskit Initialization

# Step 1: Install Qiskit if not already installed
# !pip install qiskit --upgrade

# Step 2: Import the core Qiskit modules
from qiskit import QuantumCircuit, transpile, assemble, execute
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram

# Step 3: Initialize a simple quantum program
# Create a 2-qubit, 2-classical-bit circuit
qc = QuantumCircuit(2, 2)

# Apply some gates
qc.h(0)           # Hadamard gate on qubit 0
qc.cx(0, 1)       # CNOT gate between qubit 0 and qubit 1
qc.measure([0, 1], [0, 1])  # Measure qubits into classical bits

# Step 4: Run the program on local simulator
simulator = AerSimulator()
compiled = transpile(qc, simulator)
qobj = assemble(compiled)
result = simulator.run(qobj).result()
counts = result.get_counts()

# Step 5: Display the result
print("Counts:", counts)
plot_histogram(counts).show()
