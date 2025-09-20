# Quantum Computing and QML; a Comprehensive Roadmap

![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)


## Overview:

This repository contains a structured roadmap of **Quantum Computing and Quantum Machine Learning**, designed to guide learners from fundamental concepts to advanced quantum computing techniques. Each project focuses on a key aspect of Qiskit and Cirq, enabling us to build a solid foundation in quantum circuits and algorithms and develop device-level understanding using transpilation, mitigation, and pulse control.

All you need is a fundamental understanding of Python to get started!

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
## Sequential Project List:

- *0_InitialisingQiskit.ipynb* ;

Introduction to setting up and initializing the Qiskit framework for quantum computing.

- *1__Intro_to_Cirq.ipynb* ;

Introduction to Cirq, a framework for quantum computing developed by Google.

- *2_QiskitRNG.ipynb* ;

Building a random number generator using Qiskit and quantum principles.

- *3_Grovers_Search_Algorithm_and_Applications.ipynb* ;
  
Implementation of Grover's search algorithm and its applications in database searching.

- *4_UnderstandingShorsAlgo_inCirq.ipynb* ;

Understanding and implementing Shor's algorithm for integer factorization using Cirq.

- *4_UnderstandingShorsAlgo_inQiskit.ipynb* ;
  
Understanding and implementing Shor's algorithm for integer factorization using Qiskit.

- 5.*VQE and its applications.ipynb* ;

Variational Quantum Eigensolver (VQE) and its applications in quantum chemistry.

- *6_LogicalQubits.ipynb* ;

Construction of logical qubits using quantum error correction techniques.

- *7_Solving_MaxCut_using_QAOA.ipynb* ;
  
Solving the Max-Cut problem using the Quantum Approximate Optimization Algorithm (QAOA).

- *8_Portfolio_Optimization_with_QAOA.ipynb* ;
  
Application of QAOA for optimizing stock portfolios in finance.

- *9_Cirq_Circuit_Transpilation_and_Error_Mitigation.ipynb* ;
  
Techniques for circuit transpilation and error mitigation in Cirq.

- *10_BB84Algo_Quantum_Key_Distribution.ipynb* ;

Implementation of the BB84 protocol for secure quantum key distribution.

- *11_Intro to TensorFlowQuantum.ipynb* ;
  
Overview of TensorFlow Quantum and its integration with quantum machine learning.

- *12_Intro_To_PennyLane.ipynb* ;
  
Introduction to PennyLane, a library for quantum machine learning and differentiable programming.

- *13_Quantum_Machine_Learning_A_Basic_Pipeline.ipynb* ;

A basic pipeline for implementing quantum machine learning algorithms.
---

## Learning Outcomes:

- **Circuit fundamentals** (quantum gates, measurement, entanglement, sampling)
- **Core quantum algorithms** (Grover’s, Shor’s, QAOA, VQE)
- **Practical application domains**: chemistry, portfolio finance, and error correction
- **Hardware awareness**: transpilation, error mitigation, and pulse programming
- **Public teaching materials**: templates, documentation, and demo code for training

---

## Learning Framework

Each project includes:

- A clear problem statement explaining relevance and context.
- Jupyter notebooks with annotated explanations.
- Data visualization (plots, Bloch spheres, performance graphs).

---
## Github Repos You Should Check out:
- https://github.com/BrianOtieno/quantum-computing/tree/main
- https://github.com/MonitSharma/Learn-Quantum-Computing-with-Qiskit
- https://github.com/quantumlib/Cirq
- https://github.com/PennyLaneAI/qml
- https://github.com/joydeb1729/Quantum-Computing-With-Cirq
---
## Foundational QC Textbooks:
- https://files.batistalab.com/teaching/attachments/chem584/Mosca.pdf ; An Introduction to Quantum Computing
- https://profmcruz.wordpress.com/wp-content/uploads/2017/08/quantum-computation-and-quantum-information-nielsen-chuang.pdf  ; Quantum Computation and Quantum Information" by Nielsen & Chuang (2000, 2nd ed. 2010)
- https://arxiv.org/pdf/quant-ph/9812037 ; Quantum Computation by Dorit Aharonov
---
## Some Insightful Research Papers:
Introductory Principles
- https://arxiv.org/pdf/quant-ph/9809016 ; An Introduction to Quantum Computing for Non‑Physicists
- https://arxiv.org/pdf/2310.10315 ; A Survey on Quantum Machine Learning: Basics, Current Trends, Challenges, Opportunities, and the Road Ahead
- https://quantum-journal.org/papers/q-2018-08-06-79/pdf/ ; Quantum Computing in the NISQ era and beyond


Further Concepts
- https://arxiv.org/abs/1304.3061 ; A variational eigenvalue solver on a quantum processor
- https://link.springer.com/article/10.1007/s11569-022-00424-z ; Historical Roots and Seminal Papers of Quantum Technology 2.0
- https://arxiv.org/abs/1411.4028 ; A Quantum Approximate Optimization Algorithm
- https://arxiv.org/pdf/1810.03787 ; Quantum Convolutional Neural Networks
- https://arxiv.org/pdf/2011.01938 ; Power of data in quantum machine learning
- https://arxiv.org/pdf/1509.04279 ; The theory of variational hybrid quantum-classical algorithms

---
## Getting Started:

To begin your journey into Quantum Programming and Quantum Machine Learning, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Symbiosis-Quantum-Club/Quantum-Computing-and-QML-a-Comprehensive-Roadmap
   cd Quantum-Computing-and-QML-a-Comprehensive-Roadmap
2. `pip install qiskit` (ensure latest 2.x version) along with optional extras (`qiskit-aer`, `qiskit-ibm-runtime`, etc.).
3. Launch notebooks sequentially, adapting and extending code for learning and demonstration.

---



