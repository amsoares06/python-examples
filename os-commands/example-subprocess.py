import subprocess

def linebreak():
    print(f"----------------------------------------")

# Redirect stdout and sterr to VAR
process = subprocess.Popen(['uname', '-a'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
#stdout, stderr

print(f"process is type: {type(process)}") # var {process} is a subprocess.Popen object

# {stdout} and {stderr} vars are of type 'bytes'
print(f"stdout is type: {type(stdout)}")
print(f"stdout: {stdout.decode('utf-8')}") # Print as text instead of 'bytes'
print(f"stderr is type: {type(stderr)}")
print(f"stderr: {stderr}")

linebreak()

process = subprocess.Popen(['uname', '-a'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     universal_newlines=True) # get {stdout} and {stderr} as 'string'
stdout, stderr = process.communicate()
print(f"stdout is type: {type(stdout)}")
print(f"stdout: {stdout}")
print(f"stderr is type: {type(stderr)}")
print(f"stderr: {stderr}")

linebreak()

# Print command output in real time
process = subprocess.Popen(['ping', '-c 2', 'haas'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output
        for output in process.stdout.readlines():
            print(output.strip())
        break

# Redirect stdout to a file
with open('/tmp/stdout.txt', 'w') as f:
    process = subprocess.Popen(['ls', '-ld', '/tmp'], stdout=f)

# Redirect stderr to a file
with open('/tmp/stderr.txt', 'w') as f:
    process = subprocess.Popen(['ls', '-ld', '/non_existant_dir'], stderr=f)

linebreak()

# Get values of completed process
process = subprocess.run(['uname', '-a'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)

print(f"process is type: {type(process)}") # var {process} is a subprocess.CompletedProcess object
print(f"process: {process}")
print(f"stdout: {process.stdout}")

linebreak()

# Write to stdin
ssh = subprocess.Popen(["ssh", "osmc@haas"],
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        bufsize=0)

# Send ssh commands to stdin
ssh.stdin.write("uname -a\n")
ssh.stdin.write("uptime\n")
ssh.stdin.write("df -h")
ssh.stdin.close()

# Fetch output
for line in ssh.stdout:
    print(line.strip())
