import click
import datetime
import subprocess
import sys
import time

@click.command()
@click.argument('input_file')

def hello(input_file):
    print(input_file)
    p = subprocess.Popen([sys.executable or 'python'] + [input_file], stdout=subprocess.PIPE)
    times = {}

    for line in iter(p.stdout.readline, b''):
        print(line.rstrip())
        times[line] = line
        time.sleep(0.2)

    print(datetime.datetime.date())

if __name__ == '__main__':
    hello()
