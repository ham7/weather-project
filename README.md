# Weather station project

## Installation
To get this working you first need to install a library that can read the DHT22
sensor.
For this execute the following commands:

    git submodule update --init --recursive

Followed by:

    cd Adafruit_Python_DHT
    sudo python3 setup.py install

Then you can test if the board is setup well by executing, where 6 is your GPIO
number:

    cd examples
    python3 AdafruitDHT.py 22 6

From here you can get temperature and humidity in the main app.
