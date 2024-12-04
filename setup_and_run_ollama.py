import os
import subprocess

def install_ollama():
    """Installs the Ollama CLI and Python bindings."""
    try:
        # Install Ollama CLI using the curl command
        subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, check=True)
        print("Ollama CLI installed successfully.")
        
        # Install Python bindings for Ollama
        subprocess.run("pip install ollama", shell=True, check=True)
        print("Ollama Python bindings installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during installation: {e}")
        exit(1)

def run_ollama_serve():
    """Runs the Ollama serve command."""
    try:
        # Start the Ollama server
        subprocess.run("ollama serve", shell=True, check=True)
        print("Ollama server is running.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Ollama server: {e}")
        exit(1)

if __name__ == "__main__":
    # Install Ollama and start the server
    install_ollama()
    run_ollama_serve()
