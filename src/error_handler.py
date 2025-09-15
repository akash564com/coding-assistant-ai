import io
import sys
import traceback
import subprocess

def extract_code(code: str) -> str:
    """Extract clean Python code from markdown blocks if present."""
    if "```" in code:
        parts = code.split("```")
        for p in parts:
            if p.strip().startswith("python"):
                return p.replace("python", "", 1).strip()
            elif not p.strip().startswith("`") and len(p.strip()) > 0:
                return p.strip()
    return code


def run_code(code: str):
    """Safely execute Python code in a subprocess."""
    clean_code = extract_code(code)

    with open("temp.py", "w") as f:
        f.write(clean_code)

    try:
        result = subprocess.run(
            ["python", "temp.py"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return {"status": "success", "output": result.stdout.strip()}
        else:
            return {"status": "error", "output": result.stderr.strip()}
    except Exception as e:
        return {"status": "error", "output": str(e)}
