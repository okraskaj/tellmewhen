from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="tellmewhen",
    version="2016.12.24",
    description="",
    long_description=readfile('README.md'),
    author="Marcjanna J",
    author_email="marcjedrychg@gmail.com",
    url="",
    py_modules=['tellmewhen'],
    license=readfile('LICENSE'),
    entry_points={
        'console_scripts': [
            'tellmewhen = tellmewhen:get_stdout'
        ]
    },
)
