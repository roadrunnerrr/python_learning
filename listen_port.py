from argparse import ArgumentParser
import os
import subprocess

parser = argparse.ArgumentParser(description='check if port is available')
parser.add_argument('--port', '-p', type=int, help='port number')

args = parser.parse_args()

port = args.port
print(f'$ lsof -i :{args.port}')

cmd = subprocess.run(['lsof', '-i', f':{port}'], stdout=subprocess.PIPE)
out = cmd.stdout.decode().split()

if len(out) != 0:

    proc_name = out[9]
    proc_pid = out[10]

    print(f'Port {port} is listened by the process {proc_name} with PID {proc_pid}')

    kill = input('Show we kill this process? [y/n]: ')

    if kill is 'y':
        subprocess.run(['kill', '-9', f'{proc_pid}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f'Process {proc_pid} was killed')
    elif kill is 'n':
        print(f'Process {proc_pid} keeps running')

else:
    print(f'The port {port} is free')

