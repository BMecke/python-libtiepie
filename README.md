# ⚠️ Warning: This software is no longer under development⚠️

This is a fork of the no longer available python-libtiepie library from Tiepie Engineering, extended with the libtiepie binaries and udev rules.

To get back to the original version, the project can be reset to the last commit of the manufacturer.

```
git checkout d47dd20fd2adf67bf41ab541ffb319c4fe502962 
```

## As an alternative I recommend the actively developed library ["handyscope"](https://github.com/emtpb/handyscope).

# python-libtiepie
[![PyPI](https://img.shields.io/pypi/v/python-libtiepie.svg)](https://pypi.org/project/python-libtiepie/)
[![License](https://img.shields.io/github/license/tiepie/python-libtiepie.svg)](LICENSE)

Python bindings for [LibTiePie SDK](https://www.tiepie.com/node/930). The LibTiePie SDK is a library to easily interface with TiePie engineering [USB oscilloscopes](https://www.tiepie.com/node/4). Using the LibTiePie SDK the user has full control over all aspects of the USB oscilloscope and can perform measurements easily on Windows and Linux. Examples for different measurements are available to get started easily.

## Installation

### Windows

To install the Python bindings for LibTiePie and examples on Windows:

1. Install the Python bindings by executing `pip install python-libtiepie`
2. Download the [python-libtiepie examples](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/TiePie/python-libtiepie/tree/master/examples).
3. Unpack them using an extractor.
4. Connect your [USB oscilloscope](https://www.tiepie.com/node/4).
5. Run an example by executing e.g. `python OscilloscopeBlock.py`

### Linux

To install the Python bindings for LibTiePie and examples on Linux:

1. Copy the udev rules to /etc/udev/rules.d by executing
```curl -fsSL https://raw.githubusercontent.com/TiePie/python-libtiepie/master/45-tiepie.rules | sudo tee /etc/udev/rules.d/45-tiepie.rules```
2. Install the Python bindings by executing
```pip install python-libtiepie```
3. Download the [python-libtiepie examples](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/TiePie/python-libtiepie/tree/master/examples).
4. Unpack them using an extractor, or run in the console using `unzip`.
5. Connect your [USB oscilloscope](https://www.tiepie.com/node/4).
6. Run an example by executing e.g. `python OscilloscopeBlock.py`

## Examples

See the [examples directory](examples).
