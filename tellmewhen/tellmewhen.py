import click
import subprocess
import sys
import time
from parse_tf_output import parse_tf_output
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('/home/marcysia/PycharmProjects/hackupc/tellmewhen/tellmewhen/tellmewhen-pk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tellmewhen-app.firebaseio.com'
})

ref = firebase_admin.db.reference('outputs')
 #replaces appending to events variable with firebase db call. #TODO


@click.command()
@click.argument('input_file')
@click.option('--tf', '-v', is_flag=True, help="Print more output.")
def get_stdout(input_file, tf):
    searched_term = "val_acc".encode()
    print(searched_term)
    p = subprocess.Popen([sys.executable or 'python'] + [input_file],
                         stdout=subprocess.PIPE)
    times = {}
    important_accuracy = None

    for line in iter(p.stdout.readline, b''):
        time.sleep(0.3)
        if (searched_term in line) & tf:
            print(line)
            important_accuracy = parse_tf_output(line)
            print(important_accuracy)
        print({time.ctime(): line})
        ref.push({time.ctime(): line.decode()})
        time.sleep(0.5)

    return times

if __name__ == '__main__':
    get_stdout()
