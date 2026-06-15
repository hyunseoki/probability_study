# 💻 Probability Simulation Codes

This directory is set up for running code exercises and simulations from the textbook. The book contains dedicated chapters on simulating random variables and systems:
* **Chapter 12:** Simulation using MATLAB
* **Chapter 13:** Simulation using R
* **Chapter 14:** Simulation using Python

---

## 🐍 Python Setup (Recommended)

To run Python simulations, we recommend setting up a virtual environment and installing standard scientific packages like `numpy`, `scipy`, and `matplotlib`.

### 1. Create a Virtual Environment
Run the following commands in your terminal:
```bash
python3 -m venv .venv
source .venv/activate
```

### 2. Install Required Libraries
```bash
pip install numpy scipy matplotlib jupyter
```

---

## 🚀 Example: Monte Carlo Simulation
You can create a script `coin_toss_simulation.py` to run a basic simulation:
```python
import numpy as np

# Simulate 10,000 coin tosses
n_tosses = 10000
results = np.random.choice(['Heads', 'Tails'], size=n_tosses, p=[0.5, 0.5])

# Calculate fraction of Heads
n_heads = np.sum(results == 'Heads')
fraction_heads = n_heads / n_tosses

print(f"Number of Heads: {n_heads}")
print(f"Fraction of Heads: {fraction_heads:.4f} (Theoretical: 0.5000)")
```
