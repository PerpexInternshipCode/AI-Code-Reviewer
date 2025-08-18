# import subprocess

# def check_radon(file_path):
#     result = subprocess.run(["radon", "cc", file_path, "-s", "-a"], capture_output=True, text=True)
#     return result.stdout.strip()

# def get_complexity(code_path):
#     result = subprocess.run(["radon", "cc", code_path, "-s", "-a"], capture_output=True, text=True)
#     return result.stdout

import subprocess

def check_radon(file_path):
    """Run radon to check code complexity."""
    try:
        result = subprocess.run(
            ["radon", "cc", file_path, "-s", "-a"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip() or "✅ No complexity issues found."
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() or "⚠️ Radon returned an error."
    except FileNotFoundError:
        return "❌ Radon is not installed or not found in PATH."
