# Watchdog Timer Example

This example demonstrates how to use the Watchdog Timer on the Raspberry Pi Pico RP2040. The watchdog timer is set up to reset the system if it is not fed within a certain period.

## Hardware Details

### Microcontroller: Raspberry Pi Pico RP2040

The Raspberry Pi Pico RP2040 is a versatile microcontroller designed for a wide range of applications. It features:
- **CPU**: Dual-core ARM Cortex-M0+ processor.
- **Memory**: 264 KB of SRAM, 2 MB of Flash memory.
- **Peripherals**: GPIO, PWM, ADC, I2C, SPI, UART, and more.
- **Package**: Available in a 40-pin DIP package.

### Onboard LED
The Raspberry Pi Pico includes a built-in LED connected to GPIO pin 25.

## Software Details

### Prerequisites
- **Thonny IDE**: Download and install from [here](https://thonny.org/).
- **MicroPython**: Follow the instructions to set up [MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).

### Instructions

1. **Open Thonny IDE**.
2. **Connect the Raspberry Pi Pico** to your computer via USB.
3. **Select the Raspberry Pi Pico interpreter** from the bottom-right corner in Thonny.
4. **Create a New File**:
    - Click `File -> New`.
    - Copy the content from the `main.py` provided in this folder.
    - Save the file as `main.py` on the Raspberry Pi Pico.
5. **Run the Program**:
    - The onboard LED should toggle every second, and the message "System running normally, feeding the watchdog..." should be printed.
    - Uncomment the lines simulating a system hang to observe the watchdog reset after 5 seconds.

### Code Explanation

#### main.py
This code initializes the Watchdog Timer (WDT) with a timeout of 5 seconds. In the main loop, the watchdog is fed every second to prevent a system reset. The LED is toggled to indicate normal operation. By uncommenting the lines simulating a system hang, the watchdog timer will reset the system after 5 seconds of inactivity.

### Additional Resources
- [Raspberry Pi Pico Datasheet](https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf)
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
