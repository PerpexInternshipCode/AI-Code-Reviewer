import subprocess

def run_flake8(file_path):
    result = subprocess.run(['flake8', file_path], capture_output=True, text=True)
    return result.stdout.strip()

def run_black(file_path):
    result = subprocess.run(['black', '--check', file_path], capture_output=True, text=True)
    return result.stdout.strip()

def run_radon(file_path):
    result = subprocess.run(['radon', 'cc', file_path, '-s', '-a'], capture_output=True, text=True)
    return result.stdout.strip()
