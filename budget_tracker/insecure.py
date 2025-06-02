import subprocess

def run_command(cmd):
    # This should trigger a security warning, or multiple
    return subprocess.call(cmd, shell=True)

def hardcoded_password():
    # ❗ Hardcoded credentials
    password = "SuperSecret123!"
    return password
