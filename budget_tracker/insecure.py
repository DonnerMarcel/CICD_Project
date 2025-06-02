import subprocess

def run_command(cmd):
    # This should trigger a security warning, or multiple
    return subprocess.call(cmd, shell=True)
