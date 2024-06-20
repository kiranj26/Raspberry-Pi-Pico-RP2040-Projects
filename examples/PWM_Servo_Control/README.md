# PWM Servo Control Example

This example demonstrates how to use PWM to control a servo motor on the Raspberry Pi Pico RP2040. The servo is connected to GPIO pin 15.

## Hardware Details

### Microcontroller: Raspberry Pi Pico RP2040

The Raspberry Pi Pico RP2040 is a versatile microcontroller designed for a wide range of applications. It features:
- **CPU**: Dual-core ARM Cortex-M0+ processor.
- **Memory**: 264 KB of SRAM, 2 MB of Flash memory.
- **Peripherals**: GPIO, PWM, ADC, I2C, SPI, UART, and more.
- **Package**: Available in a 40-pin DIP package.

### Servo Motor

A servo motor is connected to GPIO pin 15. Servos are used for precise control of angular or linear position, velocity, and acceleration.

## Software Details

### Prerequisites
- **Thonny IDE**: Download and install from [here](https://thonny.org/).
- **MicroPython**: Follow the instructions to set up [MicroPython on the Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).

### Instructions

1. **Hardware Setup**:
    - Connect the servo motor to GPIO pin 15.
    - Connect the servo's VCC to 5V (if your servo operates at 5V) or 3.3V (if your servo operates at 3.3V).
    - Connect the servo's GND to the Raspberry Pi Pico's GND.
2. **Open Thonny IDE**.
3. **Connect the Raspberry Pi Pico** to your computer via USB.
4. **Select the Raspberry Pi Pico interpreter** from the bottom-right corner in Thonny.
5. **Create a New File**:
    - Click `File -> New`.
    - Copy the content from the `main.py` provided in this folder.
    - Save the file as `main.py` on the Raspberry Pi Pico.
6. **Run the Program**:
    - The servo motor should sweep back and forth from 0 to 180 degrees.

### Code Explanation

#### main.py
This code initializes GPIO pin 15 as a PWM output pin for controlling a servo motor. It sets the PWM frequency to 50 Hz, which is standard for servo control. The `set_servo_angle` function maps the desired angle (0-180 degrees) to the corresponding PWM duty cycle. The servo is then swept from 0 to 180 degrees and back in a loop.

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
