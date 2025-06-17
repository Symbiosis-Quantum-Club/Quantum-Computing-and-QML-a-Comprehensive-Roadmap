# Qiskit Project Roadmap

## Overview

This repository contains a structured roadmap of **Qiskit projects**, designed to guide learners from fundamental concepts to advanced quantum computing techniques. Each project focuses on a key aspect of Qiskit’s SDK, enabling us to; Build a solid foundation in quantum circuits and algorithms and; Develop device-level understanding using transpilation, mitigation, and pulse control.

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

## 🏆 Learning Outcomes

- **Circuit fundamentals** (gates, measurement, entanglement, sampling)
- **Core quantum algorithms** (Grover’s, Shor’s, QAOA, VQE)
- **Practical application domains**: chemistry, portfolio finance, and error correction
- **Hardware awareness**: transpilation, error mitigation, and pulse programming
- **Public teaching materials**: templates, documentation, and demo code for training

---

## 📚 Teaching Framework

Each project includes:

- A clear problem statement explaining relevance and context.
- Code templates and Jupyter notebooks with annotated explanations.
- An example of execution on both simulator and quantum backend.
- Data visualization (plots, Bloch spheres, performance graphs).
- “Show your work” content suitable for Twitter/X threads and blog posts.

---

## 🔗 Getting Started

1. Clone this repo.
2. `pip install qiskit` (ensure latest 2.x version) along with optional extras (`qiskit-aer`, `qiskit-ibm-runtime`, etc.).
3. Load your IBM Quantum account token via `IBMQ.save_account(...)`.
4. Launch notebooks sequentially, adapting and extending code for learning and demonstration.

---

## 🧠 Why Qiskit?

- Developed by IBM, Qiskit is the most widely used open-source quantum framework with excellent documentation and community support.  
- It supports a full-stack workflow: from high-level circuits and algorithms to low-level pulse control.  
- Qiskit includes domain libraries (Finance, Nature, Machine Learning) that link quantum computing to real-world use cases.

---

## ✅ Contribution

We welcome contributions:

- Bug fixes, optimizations, documentation improvements
- New teaching modules or problem variants
- Interfaces to other quantum devices or frameworks

See [CONTRIBUTING.md] for guidelines.

---

## 📖 References

Key resources that inspired this roadmap:

- Qiskit official tutorials and guides – foundational learning :contentReference[oaicite:1]{index=1}  
- Qiskit Machine Learning tutorials – for hybrid quantum approaches :contentReference[oaicite:2]{index=2}  
- Community tutorials and cookbook – real-world examples :contentReference[oaicite:3]{index=3}

---

> **Team Quantum Club** – Building India’s next generation of quantum leaders 🧩
