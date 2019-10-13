import click
import subprocess
import sys
import time
from parse_tf_output import parse_tf_output, get_epoch
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import psutil

cred = credentials.Certificate('/home/marcysia/PycharmProjects/hackupc/tellmewhen/tellmewhen/tellmewhen-pk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tellmewhen-app.firebaseio.com'
})

ref = firebase_admin.db.reference('outputs')


@click.command()
@click.argument('input_file')
@click.option('--tf', '-v', is_flag=True, help="Print more output.")
def get_stdout(input_file, tf):
    ref.push({'date': time.ctime(),
              'file_name': input_file})
    searched_term = "val_accuracy".encode()
    searched_epoch = 'Epoch'.encode()
    print(searched_term)
    p = subprocess.Popen([sys.executable or 'python'] + [input_file],
                         stdout=subprocess.PIPE)

    epoch_nb = 0
    important_accuracy = None

    for line in iter(p.stdout.readline, b''):
        if (searched_epoch in line) & tf:
            epoch_nb = get_epoch(line)
        if (searched_term in line) & tf:
            important_accuracy = parse_tf_output(line)
            important_accuracy['epoch'] = epoch_nb
        ref.push({'date': time.ctime(),
                  'outputs': line.decode(),
                  'metrics': important_accuracy,
                  'cpu_use': psutil.cpu_percent(),
                  'RAM': psutil.virtual_memory()})
        time.sleep(0.5)

    return

if __name__ == '__main__':
    get_stdout()
