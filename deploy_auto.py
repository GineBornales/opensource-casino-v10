import os
import datetime
import subprocess

project_dir = "/data/data/com.termux/files/home/storage/downloads/opensource-casino-v10"
log_file = "/data/data/com.termux/files/home/deploy_log.txt"

def log(text):
    with open(log_file, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {text}\n")

def deploy():
    try:
        os.chdir(project_dir)

        log("1. Installing dependencies...")
        subprocess.run(["composer", "install"], check=True)

        log("2. Git add...")
        subprocess.run(["git", "add", "."], check=True)

        log("3. Git commit...")
        subprocess.run(["git", "commit", "-m", "Auto deploy from Termux"], check=True)

        log("4. Git push...")
        subprocess.run(["git", "push"], check=True)

        log("5. Done! Auto deploy complete.")
    except Exception as e:
        log(f"ERROR: {str(e)}")

if __name__ == "__main__":
    deploy()
