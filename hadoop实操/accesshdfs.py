import subprocess
cat = subprocess.Popen(["/usr/local/hadoop","fs","-cat", "xx.part-0000"],stdout=subprocess.PIPE)
for line in cat.stdout:
    print(line)