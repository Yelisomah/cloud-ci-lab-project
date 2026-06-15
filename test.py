import subprocess
import sys

def test_app():
    result = subprocess.run([sys.executable, 'app.py'], capture_output=True, text=True)
    assert result.returncode == 0, "App did not run successfully"
    assert "Hello, welcome to CICD pipeline project!" in result.stdout, "wrong output"
    
if __name__ == "__main__":
    test_app()
    print("Tests passed!")