import os

def linebreak():
    print(f"----------------------------------------")

# Run a command and print output
os.system('uname -a')
linebreak()

# Send output to a VAR
uname = os.popen('uname')
output = uname.read()
print(f"{output}")
linebreak()

# Send output to a VAR
output = os.popen('ls').read()
print(f"{output}")
linebreak()

# Read lines separately
output = os.popen('ls').readlines()
print(f"{output}")
