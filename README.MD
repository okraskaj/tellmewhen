# tellmewhen

Tellmewhen is a tool to help you control your long-lasting commands away
 from your computer 

## Architecture
As this is an alpha version this repository contains both server component,
 and console tool `tellmewhen`. They should be treated as separate modules.

## Installation

To install the console tool just clone this repo...
```bash
git clone https://github.com/okraskaj/tellmewhen.git
```
 install it with pip (preferably in a virtualenv)
```bash
mkvirtualenv tellmewhen
cd tellmewhen
pip install -e 
```

## Usage

You can use the tool with any python tool that prints to the standard output:

```bash
tellmewhen sample_mnist.py

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
