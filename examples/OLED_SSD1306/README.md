# OLED Display (SSD1306) Example

This example demonstrates how to use an OLED display (SSD1306) with the Raspberry Pi Pico RP2040. The OLED display is connected to the I2C bus (GPIO pins 4 and 5).

## Hardware Details

### Microcontroller: Raspberry Pi Pico RP2040

The Raspberry Pi Pico RP2040 is a versatile microcontroller designed for a wide range of applications. It features:
- **CPU**: Dual-core ARM Cortex-M0+ processor.
- **Memory**: 264 KB of SRAM, 2 MB of Flash memory.
- **Peripherals**: GPIO, PWM, ADC, I2C, SPI, UART, and more.
- **Package**: Available in a 40-pin DIP package.

### OLED Display (SSD1306)

The SSD1306 is a popular OLED display controller that supports I2C and SPI interfaces. It is commonly used for small monochrome displays.

## Software Details

### Prerequisites
- **Thonny IDE**: Download and install from [here](https://thonny.org/).
- **MicroPython**: Follow the instructions to set up [MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).
- **SSD1306 Library**: Install the SSD1306 library in Thonny.

### Instructions

1. **Hardware Setup**:
    - Connect the OLED display to the I2C bus:
        - SCL to GPIO pin 5
        - SDA to GPIO pin 4
        - VCC to 3.3V
        - GND to GND
2. **Open Thonny IDE**.
3. **Connect the Raspberry Pi Pico** to your computer via USB.
4. **Install the SSD1306 Library**:
    - Go to `Tools -> Manage Packages`.
    - Search for `micropython-ssd1306` and install it.
5. **Select the Raspberry Pi Pico interpreter** from the bottom-right corner in Thonny.
6. **Create a New File**:
    - Click `File -> New`.
    - Copy the content from the `main.py` provided in this folder.
    - Save the file as `main.py` on the Raspberry Pi Pico.
7. **Run the Program**:
    - The OLED display will show "Hello, World!" and other text, and then display the current time.

### Code Explanation

#### main.py
This code initializes the I2C bus on GPIO pins 4 (SDA) and 5 (SCL), and initializes the SSD1306 OLED display. It displays "Hello, World!" and other text, then shows the current time, updating every 2 seconds.

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
