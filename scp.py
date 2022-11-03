import os
import subprocess

print(os.getcwd)

file = "/home/user/Temp/file.txt"

try:
    p = subprocess.Popen(["scp", file, "jenkins@127.0.0.1:/home/jenkins/Temp"])
    sts = os.waitpid(p.pid, 0)
except Exception as e:
    print(repr(e))

print("Done.")
