import numpy as np

def run_simulation(n_tosses=10000):
    print(f"--- Running Monte Carlo Simulation with {n_tosses:,} tosses ---")
    
    # Simulate coin tosses (0 = Tails, 1 = Heads)
    tosses = np.random.randint(0, 2, size=n_tosses)
    
    # Calculate statistics
    n_heads = np.sum(tosses == 1)
    n_tails = np.sum(tosses == 0)
    
    prob_heads = n_heads / n_tosses
    prob_tails = n_tails / n_tosses
    
    print(f"Heads: {n_heads} (Probability: {prob_heads:.4f})")
    print(f"Tails: {n_tails} (Probability: {prob_tails:.4f})")
    print(f"Difference from theoretical 0.5: {abs(prob_heads - 0.5):.6f}")

if __name__ == "__main__":
    run_simulation()
