# A Quantum Programming Roadmap

## Overview

This repository contains a structured roadmap of **Quantum Programming and Quantum Machine Learning**, designed to guide learners from fundamental concepts to advanced quantum computing techniques. Each project focuses on a key aspect of Qiskit’s SDK, enabling us to; Build a solid foundation in quantum circuits and algorithms and; Develop device-level understanding using transpilation, mitigation, and pulse control.

---
## What is Qiskit?

- Developed by IBM, Qiskit is the most widely used open-source quantum framework with excellent documentation and community support.  
- It supports a full-stack workflow: from high-level circuits and algorithms to low-level pulse control.  
- Qiskit includes domain libraries (Finance, Nature, Machine Learning) that link quantum computing to real-world use cases.
---
## What is Cirq?
- An open source quantum framework developed by Google. It's designed for "NISQ" (Noisy Intermediate-Scale Quantum) devices, meaning it gives you fine-grained control over gate placement and timing, which is crucial for experimenting with current quantum hardware.

- Building Quantum Circuits: Cirq lets you design quantum circuits from scratch, choosing specific quantum gates (like Hadamard, CNOT, Rx) and applying them to individual qubits.
- Simulating Quantum Programs: You can run your quantum circuits on a simulator right on your own computer, allowing you to test and debug your quantum algorithms before trying them on actual quantum hardware.

- Running on Quantum Hardware: Cirq integrates with Google's quantum processors (like Sycamore), enabling you to execute your designed circuits on real quantum computers.

---
## Sequential Project List

1. **“Hello World” & Bell State**
   - Create and run a 2-qubit entanglement circuit on simulator and real QPU.
2. **Single‑Qubit Superposition & RNG**
   - Use Hadamard gates to generate random bits; build an RNG service.
3. **Grover’s Search Algorithm**
   - Design oracle and diffuser to implement Grover’s search on small datasets.
4. **Shor’s Algorithm (Small Integers)**
   - Factor a small integer (e.g., 15) using QFT and phase estimation.
5. **VQE for Simple Molecule**
   - Compute ground-state energy of H₂ or LiH via VQE hybrid workflow.
6. **Error Correction: Repetition Code**
   - Build logical qubits using repetition encoding and decode against noise.
7. **QAOA for 3‑Node Max‑Cut**
   - Solve a Max‑Cut problem using QAOA with cost and mixer circuits.
8. **Portfolio Optimization**
   - Map 3–8 stock portfolios to QAOA or amplitude estimation tasks.
9. **Circuit Transpilation & Error Mitigation**
   - Optimize circuits for target backend and apply mitigation techniques.
10. **Qiskit Pulse & Hardware Calibration**
    - Explore pulse-level control, backend characteristics, and custom gate generation.

---

## Learning Outcomes

- **Circuit fundamentals** (gates, measurement, entanglement, sampling)
- **Core quantum algorithms** (Grover’s, Shor’s, QAOA, VQE)
- **Practical application domains**: chemistry, portfolio finance, and error correction
- **Hardware awareness**: transpilation, error mitigation, and pulse programming
- **Public teaching materials**: templates, documentation, and demo code for training

---

## Teaching Framework

Each project includes:

- A clear problem statement explaining relevance and context.
- Code templates and Jupyter notebooks with annotated explanations.
- Data visualization (plots, Bloch spheres, performance graphs).

---
## Github Repos You Should Check out
- https://github.com/BrianOtieno/quantum-computing/tree/main
- https://github.com/MonitSharma/Learn-Quantum-Computing-with-Qiskit
- https://github.com/quantumlib/Cirq
- https://github.com/PennyLaneAI/qml
- https://github.com/joydeb1729/Quantum-Computing-With-Cirq
---
## Foundational QC Textbooks
- https://files.batistalab.com/teaching/attachments/chem584/Mosca.pdf ; An Introduction to Quantum Computing
- https://profmcruz.wordpress.com/wp-content/uploads/2017/08/quantum-computation-and-quantum-information-nielsen-chuang.pdf  ; Quantum Computation and Quantum Information" by Nielsen & Chuang (2000, 2nd ed. 2010)
- https://arxiv.org/pdf/quant-ph/9812037 ; Quantum Computation by Dorit Aharonov
---
## Some Insightful Research Papers
Introductory Principles
- https://arxiv.org/pdf/quant-ph/9809016 ; An Introduction to Quantum Computing for Non‑Physicists
- https://arxiv.org/pdf/2310.10315 ; A Survey on Quantum Machine Learning: Basics, Current Trends, Challenges, Opportunities, and the Road Ahead
- https://quantum-journal.org/papers/q-2018-08-06-79/pdf/ ; Quantum Computing in the NISQ era and beyond


Further Concepts
- https://link.springer.com/article/10.1007/s11569-022-00424-z ; Historical Roots and Seminal Papers of Quantum Technology 2.0
- https://arxiv.org/abs/1411.4028 ; A Quantum Approximate Optimization Algorithm
- https://arxiv.org/pdf/1810.03787 ; Quantum Convolutional Neural Networks
- https://arxiv.org/pdf/2011.01938 ; Power of data in quantum machine learning
- https://arxiv.org/pdf/1509.04279 ; The theory of variational hybrid quantum-classical algorithms

---
## Getting Started

1. Clone this repo.
2. `pip install qiskit` (ensure latest 2.x version) along with optional extras (`qiskit-aer`, `qiskit-ibm-runtime`, etc.).
3. Load your IBM Quantum account token via `IBMQ.save_account(...)`.
4. Launch notebooks sequentially, adapting and extending code for learning and demonstration.

---



