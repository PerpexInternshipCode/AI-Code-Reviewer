import subprocess

def check_flake8(file_path):
    """Check for style issues using flake8."""
    try:
        result = subprocess.run(["flake8", file_path], capture_output=True, text=True, check=True)
        return result.stdout.strip() or "✅ No style issues found."
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() or "⚠️ flake8 returned an error."
    except FileNotFoundError:
        return "❌ flake8 is not installed or not found in PATH."

def check_black(file_path):
    """Check if the file is formatted according to black."""
    try:
        result = subprocess.run(["black", "--check", file_path], capture_output=True, text=True, check=True)
        return result.stdout.strip() or "✅ Code is properly formatted."
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() or "⚠️ Formatting issues found by black."
    except FileNotFoundError:
        return "❌ black is not installed or not found in PATH."

def auto_format_black(file_path):
    """Auto-format the file using black."""
    try:
        result = subprocess.run(["black", file_path], capture_output=True, text=True, check=True)
        return result.stdout.strip() or "✅ Code formatted successfully."
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() or "⚠️ Could not format the code."
    except FileNotFoundError:
        return "❌ black is not installed or not found in PATH."
