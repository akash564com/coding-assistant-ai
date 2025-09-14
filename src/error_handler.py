import subprocess

def run_code(code: str):
    with open("temp.py", "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["python", "temp.py"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return {"status": "success", "output": result.stdout}
        else:
            return {"status": "error", "output": result.stderr}
    except Exception as e:
        return {"status": "error", "output": str(e)}
