import click
import subprocess
import sys
import time

@click.command()
@click.argument('input_file')

def get_stdout(input_file):
    print(input_file)
    p = subprocess.Popen([sys.executable or 'python'] + [input_file],
                         stdout=subprocess.PIPE)
    times = {}

    for line in iter(p.stdout.readline, b''):
        print(line.rstrip())
        times[time.ctime()] = line
        time.sleep(0.2)

if __name__ == '__main__':
    get_stdout()
