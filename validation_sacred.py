import sys
from sacred import Experiment
import yaml
import numpy as np

# Create a dummy experiment
ex = Experiment("AURA_Test")

@ex.config
def config():
    seed = 42
    params = {"lr": 0.01, "batch_size": 32}

@ex.main
def main(_run, seed, params):
    print(f"--> Running experiment with seed {seed}")
    # Verify numpy integration
    arr = np.array([1, 2, 3])
    print(f"--> Numpy array: {arr}")
    return "SUCCESS"

def test_sacred_lifecycle():
    print("--- Starting Sacred Research Smoke Test ---")
    try:
        # 1. Test YAML config parsing
        print("--> Testing PyYAML integration...")
        cfg_data = "seed: 123\nparams: {lr: 0.001}"
        parsed = yaml.safe_load(cfg_data)
        
        # 2. Test Function Wrapping (The 'wrapt' dependency check)
        print("--> Testing experiment execution...")
        run = ex.run(config_updates=parsed)
        
        if run.status == "COMPLETED" and run.result == "SUCCESS":
            print("--- SMOKE TEST PASSED ---")
        else:
            raise RuntimeError(f"Experiment failed with status: {run.status}")
            
    except Exception as e:
        print(f"CRITICAL VALIDATION FAILURE: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_sacred_lifecycle()