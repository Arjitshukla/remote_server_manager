import paramiko

FORBIDDEN_COMMANDS = ["rm -rf", "shutdown", "reboot", ":(){"]

def execute_ssh_command(host, username, password, command, port=22):
    # Block dangerous commands
    for bad in FORBIDDEN_COMMANDS:
        if bad in command:
            raise Exception("Dangerous command blocked")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname=host,
        username=username,
        password=password,
        port=port,
        timeout=10
    )

    # Important: get_pty=True for proper output
    stdin, stdout, stderr = client.exec_command(command, get_pty=True)

    exit_status = stdout.channel.recv_exit_status()  # get exit code
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    client.close()

    return output, error, exit_status
