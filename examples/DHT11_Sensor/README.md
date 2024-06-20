# DHT11 Temperature and Humidity Sensor Example

This example demonstrates how to use the DHT11 temperature and humidity sensor with the Raspberry Pi Pico RP2040. The DHT11 sensor is connected to GPIO pin 16.

## Hardware Details

### Microcontroller: Raspberry Pi Pico RP2040

The Raspberry Pi Pico RP2040 is a versatile microcontroller designed for a wide range of applications. It features:
- **CPU**: Dual-core ARM Cortex-M0+ processor.
- **Memory**: 264 KB of SRAM, 2 MB of Flash memory.
- **Peripherals**: GPIO, PWM, ADC, I2C, SPI, UART, and more.
- **Package**: Available in a 40-pin DIP package.

### DHT11 Sensor

The DHT11 is a basic, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air and provides a digital signal on the data pin.

## Software Details

### Prerequisites
- **Thonny IDE**: Download and install from [here](https://thonny.org/).
- **MicroPython**: Follow the instructions to set up [MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).
- **DHT Library**: Install the DHT library in Thonny.

### Instructions

1. **Hardware Setup**:
    - Connect the DHT11 sensor to GPIO pin 16.
    - Connect the DHT11 sensor's VCC to 3.3V and GND to GND.
    - Connect the data pin of the DHT11 to GPIO pin 16.
2. **Open Thonny IDE**.
3. **Connect the Raspberry Pi Pico** to your computer via USB.
4. **Install the DHT Library**:
    - Go to `Tools -> Manage Packages`.
    - Search for `micropython-dht` and install it.
5. **Select the Raspberry Pi Pico interpreter** from the bottom-right corner in Thonny.
6. **Create a New File**:
    - Click `File -> New`.
    - Copy the content from the `main.py` provided in this folder.
    - Save the file as `main.py` on the Raspberry Pi Pico.
7. **Run the Program**:
    - The temperature and humidity will be printed every 2 seconds.

### Code Explanation

#### main.py
This code initializes the DHT11 sensor on GPIO pin 16 and reads the temperature and humidity values every 2 seconds. The values are printed to the console.

### Additional Resources
- [Raspberry Pi Pico Datasheet](https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf)
- [RP2040 Datasheet](https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf)
- [Raspberry Pi Pico MicroPython Documentation](https://docs.micropython.org/en/latest/rp2/quickref.html)
- [Thonny IDE](https://thonny.org/)
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
- [Raspberry Pi Forums](https://www.raspberrypi.org/forums/)
- [MicroPython Forum](https://forum.micropython.org/)
- [Getting Started with MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
- [Raspberry Pi YouTube Channel](https://www.youtube.com/user/RaspberryPiBeginners)

## Contributing
Contributions are welcome! If you have a project or example you'd like to share, please fork the repository, create a new branch, and submit a pull request. Make sure to follow the coding standards and include a detailed description of your project.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Happy coding!

**Kiran Jojare**  
*Embedded Software / Firmware Engineer*  
kijo7257@colorado.edu
