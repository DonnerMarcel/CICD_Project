import subprocess

def run_command(cmd):
    # This should trigger a security warning, or multiple
    return subprocess.call(cmd, shell=True)

def hardcoded_password():
    # ❗ Hardcoded credentials
    password = "SuperSecret123!"
    return password

def insecure_env_access():
    # ❗ Insecure use of environment variables (e.g., leaking secrets)
    print("Accessing AWS credentials...")
    print(f"AWS_SECRET_ACCESS_KEY: {os.environ.get('AWS_SECRET_ACCESS_KEY')}")
    