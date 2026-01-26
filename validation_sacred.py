import sys

try:
    import yaml
    import numpy as np
    from sacred import Experiment
    print("--> All core dependencies imported.")
except ImportError as e:
    print(f"CRITICAL: Missing dependency: {e}")
    sys.exit(1)

ex = Experiment("AURA_Sacred_Test")

@ex.config
def config():
    seed = 42

@ex.main
def main(_run, seed):
    print(f"--> Experiment running with seed: {seed}")
    arr = np.array([1, 2, 3])
    return "SUCCESS"

if __name__ == "__main__":
    print("--- Starting Sacred Smoke Test ---")
    try:
        # Test 1: Config Parsing (YAML check)
        cfg = yaml.safe_load("seed: 100")
        
        # Test 2: Execution (Wrapt/Decorator check)
        run = ex.run(config_updates=cfg)
        
        if run.status == "COMPLETED":
            print("--- SMOKE TEST PASSED ---")
        else:
            sys.exit(1)
    except Exception as e:
        print(f"FAILURE: {e}")
        sys.exit(1)