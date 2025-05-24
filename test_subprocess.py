import subprocess

p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

output = p.communicate()
print(output)              # Output is a tuple
print(output[0])           # First item is stdout in bytes

# Decode and clean up the output
stdout = output[0].decode('utf-8').strip()
print(stdout)
