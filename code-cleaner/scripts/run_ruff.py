import subprocess
import sys
import shutil
import os

def check_ruff():
    """Ensure ruff is installed in the current environment."""
    if not shutil.which("ruff"):
        print("Installing ruff...")
        subprocess.run([sys.executable, "-m", "pip", "install", "ruff"], check=True)

def clean_target(target_dir="."):
    """Run rigorous linting and formatting."""
    print(f"🧹 Janitor running on: {os.path.abspath(target_dir)}")
    
    # 1. Remove unused imports (F401) and variables (F841)
    subprocess.run(["ruff", "check", "--select", "F401,F841", "--fix", target_dir], check=False)
    
    # 2. Standardize formatting (Black-compatible)
    subprocess.run(["ruff", "format", target_dir], check=False)
    print("✨ Automated hygiene complete.")

if __name__ == "__main__":
    target = sys.argv[12] if len(sys.argv) > 1 else "."
    check_ruff()
    clean_target(target)

