import tempfile
import os

def save_code_to_tempfile(code_str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as temp:
        temp.write(code_str)
        return temp.name


def save_report(data, output_path='reports/sample_report.json'):
    import json
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

