# I2C Communication Example

This example demonstrates how to communicate with an I2C device using the Raspberry Pi Pico RP2040. The example reads data from an I2C temperature sensor (e.g., TMP102) connected to the I2C bus.

## Hardware Details

### Microcontroller: Raspberry Pi Pico RP2040

The Raspberry Pi Pico RP2040 is a versatile microcontroller designed for a wide range of applications. It features:
- **CPU**: Dual-core ARM Cortex-M0+ processor.
- **Memory**: 264 KB of SRAM, 2 MB of Flash memory.
- **Peripherals**: GPIO, PWM, ADC, I2C, SPI, UART, and more.
- **Package**: Available in a 40-pin DIP package.

### I2C Temperature Sensor (TMP102)

The TMP102 is a digital temperature sensor that communicates over I2C. It provides temperature readings with high accuracy.

## Software Details

### Prerequisites
- **Thonny IDE**: Download and install from [here](https://thonny.org/).
- **MicroPython**: Follow the instructions to set up [MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).

### Instructions

1. **Hardware Setup**:
    - Connect the TMP102 sensor to the Raspberry Pi Pico:
        - TMP102 VCC to Pico 3.3V
        - TMP102 GND to Pico GND
        - TMP102 SDA to Pico GPIO 16
        - TMP102 SCL to Pico GPIO 17
2. **Open Thonny IDE**.
3. **Connect the Raspberry Pi Pico** to your computer via USB.
4. **Select the Raspberry Pi Pico interpreter** from the bottom-right corner in Thonny.
5. **Create a New File**:
    - Click `File -> New`.
    - Copy the content from the `main.py` provided in this folder.
    - Save the file as `main.py` on the Raspberry Pi Pico.
6. **Run the Program**:
    - Open the serial monitor in Thonny to see the temperature readings from the TMP102 sensor.

### Code Explanation

#### main.py
This code initializes the I2C bus on GPIO pins 16 (SDA) and 17 (SCL) and communicates with the TMP102 temperature sensor. It reads the temperature data from the sensor and prints it to the serial monitor every second.

### Additional Resources
- [Raspberry Pi Pico Datasheet](https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf)
- [Raspberry Pi Pico MicroPython Documentation](https://docs.micropython.org/en/latest/rp2/quickref.html)
- [Thonny IDE](https://thonny.org/)
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
- [Raspberry Pi Forums](https://www.raspberrypi.org/forums/)
- [MicroPython Forum](https://forum.micropython.org/)
- [Getting Started with MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
- [TMP102 Datasheet](https://www.ti.com/lit/ds/symlink/tmp102.pdf)
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
