# SPI Communication Example

This example demonstrates how to communicate with an SPI device using the Raspberry Pi Pico RP2040. The example reads data from an SPI flash memory (e.g., W25Q32) connected to the SPI bus.

## Hardware Details

### Microcontroller: Raspberry Pi Pico RP2040

The Raspberry Pi Pico RP2040 is a versatile microcontroller designed for a wide range of applications. It features:
- **CPU**: Dual-core ARM Cortex-M0+ processor.
- **Memory**: 264 KB of SRAM, 2 MB of Flash memory.
- **Peripherals**: GPIO, PWM, ADC, I2C, SPI, UART, and more.
- **Package**: Available in a 40-pin DIP package.

### SPI Flash Memory (W25Q32)

The W25Q32 is a 32 Mbit (4 MB) SPI flash memory. It communicates over SPI and is commonly used for data storage.

## Software Details

### Prerequisites
- **Thonny IDE**: Download and install from [here](https://thonny.org/).
- **MicroPython**: Follow the instructions to set up [MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).

### Instructions

1. **Hardware Setup**:
    - Connect the W25Q32 flash memory to the Raspberry Pi Pico:
        - W25Q32 VCC to Pico 3.3V
        - W25Q32 GND to Pico GND
        - W25Q32 CS to Pico GPIO 17
        - W25Q32 SCK to Pico GPIO 18
        - W25Q32 MOSI to Pico GPIO 19
        - W25Q32 MISO to Pico GPIO 16
2. **Open Thonny IDE**.
3. **Connect the Raspberry Pi Pico** to your computer via USB.
4. **Select the Raspberry Pi Pico interpreter** from the bottom-right corner in Thonny.
5. **Create a New File**:
    - Click `File -> New`.
    - Copy the content from the `main.py` provided in this folder.
    - Save the file as `main.py` on the Raspberry Pi Pico.
6. **Run the Program**:
    - Open the serial monitor in Thonny to see the flash ID readings from the W25Q32 memory.

### Code Explanation

#### main.py
This code initializes the SPI bus on GPIO pins 18 (SCK), 19 (MOSI), and 16 (MISO) and communicates with the W25Q32 flash memory. It sends a command to read the flash ID and prints the ID to the serial monitor every second.

### Additional Resources
- [Raspberry Pi Pico Datasheet](https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf)
- [Raspberry Pi Pico MicroPython Documentation](https://docs.micropython.org/en/latest/rp2/quickref.html)
- [Thonny IDE](https://thonny.org/)
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
- [Raspberry Pi Forums](https://www.raspberrypi.org/forums/)
- [MicroPython Forum](https://forum.micropython.org/)
- [Getting Started with MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
- [W25Q32 Datasheet](https://www.winbond.com/resource-files/w25q32jw%20revf%2003272018.pdf)
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
