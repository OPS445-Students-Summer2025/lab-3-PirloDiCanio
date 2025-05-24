import os

# Launching commands with os.popen()
ls_return = os.popen('ls')
print('The contents of ls_return:', ls_return)

whoami_return = os.popen('whoami')
print('The contents of whoami_return:', whoami_return)

# Reading actual contents
whoami_contents = whoami_return.read()
print('whoami_contents:', whoami_contents)

# Trying an invalid command
ipconfig_return = os.popen('ipconfig')
ipconfig_contents = ipconfig_return.read()
print('The contents of ipconfig_return:', ipconfig_contents)
