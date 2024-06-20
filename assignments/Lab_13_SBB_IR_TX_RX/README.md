# Lab 13: SBB IR Transmitter & Receiver

This lab builds upon the foundational knowledge of infrared (IR) communication introduced in the previous lab. Students will explore both transmission and reception of IR signals using the Raspberry Pi Pico, an IR transmitter, and an IR receiver. The lab will focus on setting up a complete IR communication system, encoding and sending IR signals using an IR LED transmitter, and receiving and decoding these signals with an IR receiver. This comprehensive approach aims to deepen students' understanding of IR communication mechanisms, protocols, and practical applications in real-world scenarios.

## Table of Contents
- [Introduction](#introduction)
- [Learning Outcomes](#learning-outcomes)
- [Equipment & Materials](#equipment--materials)
- [Vocabulary](#vocabulary)
- [Hardware Setup](#hardware-setup)
- [Software Setup for IR Transmission](#software-setup-for-ir-transmission)
- [Software Setup for IR Reception](#software-setup-for-ir-reception)
- [Software Implementation](#software-implementation)
  - [Script Implementation for IR Signal Transmission](#script-implementation-for-ir-signal-transmission)
  - [Script Implementation for IR Signal Reception](#script-implementation-for-ir-signal-reception)
- [Running and Verifying IR Signal Reception and Transmission](#running-and-verifying-ir-signal-reception-and-transmission)
- [Lab Deliverables](#lab-deliverables)
- [Additional Resources](#additional-resources)

## Introduction
This lab provides step-by-step instructions for setting up an IR transmission and reception system with the Raspberry Pi Pico, configuring it for signal detection, and decoding IR signals using the NEC protocol.

## Learning Outcomes
Upon completion of the lab, students will be able to:
- Design and Build an IR Transmission System: Construct a circuit using the Raspberry Pi Pico that can transmit IR signals.
- Encode IR Signals: Learn to encode data into IR signals using NEC protocols.
- Transmit and Receive IR Signals: Successfully transmit IR signals from the IR transmitter setup and receive them using the IR receiver setup.
- Apply IR Signals: Implement simple control logic to perform actions based on the decoded IR commands, simulating real-world IR application scenarios.

## Equipment & Materials
- Raspberry Pi Pico
- IR Receiver Module (TSOP382 from Adafruit)
- IR Transmitter (TSAL6400)
- Breadboard
- Resistors
- LED
- Jumper Wires
- USB Cable
- Visual Studio Code

## Vocabulary
- **Infrared (IR) Communication**: A form of wireless communication that uses infrared light waves to transmit data over short distances. Commonly used in remote controls, IR communication allows for the control of various devices without the need for physical connections.
- **NEC Protocol**: A popular protocol for IR communication, particularly in remote control systems. It outlines a specific set of rules for encoding and transmitting data over infrared signals, including data structure, bit length, and timing for signals.
- **MicroPython**: A streamlined version of the Python 3 programming language designed to run on microcontrollers and embedded systems. It enables programming microcontrollers in Python, making it accessible for rapid prototyping and development.
- **Carrier Frequency**: In the context of IR communication, it refers to the frequency of the infrared light wave that carries the encoded information. The most common carrier frequency for IR remote controls is 38 kHz, allowing the receiver to filter out signals from other sources.
- **Modulation/Demodulation**: The process by which data is encoded onto a carrier wave (modulation) for transmission and subsequently extracted from the carrier wave by the receiver (demodulation). In IR communication, modulation involves varying the pulse width of the IR signal to encode data.
- **Breadboard**: A solderless device for prototyping electronic circuits. It allows for the insertion of components and jumper wires into connected sockets to build and test circuit designs without permanent soldering, facilitating easy adjustments and experimentation.

## Hardware Setup
### TSAL 6400 IR Emitter
The TSAL6400 is an infrared 940 nm emitting diode in GaAlAs multi-quantum well (MQW) technology with high radiant power and high speed.

#### Pinout
- **Cathode (-)**
- **Anode (+)**

### Breadboard Setup for IR Emitter
Note: Use separate breadboards for the IR Transmission circuit and the IR Receiver circuit as detailed in the following section. The transmission circuit should be assembled on one breadboard and tested with a Raspberry Pi belonging to one of the team members. Meanwhile, the receiver circuit should be set up on another breadboard and programmed using a different laptop.

#### Components:
- Raspberry Pi Pico
- NPN Transistor (e.g., 2N2222)
- IR Transmitter LED (TSAL6400)
- Current-limiting resistor for the IR LED
- Base resistor for the NPN transistor
- Jumper wires

#### Connection Steps:
1. **Connect GPIO Pin 17 of the Raspberry Pi Pico to the base of the NPN transistor through a suitable base resistor (1kΩ in our case)**.
2. **Connect the emitter of the NPN transistor directly to the ground (GND) on the Raspberry Pi Pico**.
3. **Connect the collector of the NPN transistor to the cathode (negative side) of the IR LED through a suitable resistor (47Ω in our case)**.
4. **Connect the anode (positive side) of the IR LED to the VSYS pin of the Raspberry Pi. The VSYS pin provides 5 volts which is suitable for powering the IR LED**.
5. **Use VBUS or VSYS to power the breadboard and connect GND to ground the breadboard**.

### Adafruit IR Receiver Specifications
The Adafruit IR Receiver (Adafruit model 1528-157-ND) is designed for easy integration into projects involving IR signal reception. It's a 38kHz IR receiver module suitable for decoding signals from most remote controls.

#### Pinout
- **VCC (Power)**: Connect to 3.3V on the Raspberry Pi Pico.
- **GND (Ground)**: Connect to one of the ground pins on the Pico.
- **OUT (Signal Output)**: Connect to a GPIO pin (GPIO16) on the Pico for reading the IR signal.

### Breadboard Setup for IR Receiver
To facilitate an easy and reversible setup, we'll use a breadboard to connect the IR receiver to the Raspberry Pi Pico. This method allows for quick adjustments and troubleshooting. The receiver side of the lab is designed to receive four distinct commands from the IR transmitter. Upon successful reception of each command, a different LED (LED1 to LED4) will blink.

#### Components:
- Raspberry Pi Pico
- Adafruit IR Receiver
- LEDs
- 64 Ohm Resistors
- Breadboard
- Jumper wires

#### Connection Steps:
1. **Place the IR Receiver on the Breadboard**: Carefully insert the three pins of the IR receiver into three separate rows on the breadboard. Ensure there's no short circuit between the pins.
2. **Power Connection (VCC)**: Use a jumper wire to connect the VCC pin of the IR receiver to one of the 3.3V pins on the Raspberry Pi Pico. This supplies power to the IR receiver.
3. **Ground Connection (GND)**: Use another jumper wire to connect the GND pin of the IR receiver to one of the ground (GND) pins on the Pico. It's crucial to establish a common ground for all components.
4. **Signal Connection (OUT)**: Finally, use a jumper wire to connect the OUT pin of the IR receiver to a chosen GPIO pin on the Pico (e.g., GPIO15). This pin will be used to read the IR signals.
5. **Connect GPIO Pins 18 to 21 of the Raspberry Pi Pico to the anodes (positive sides) of LED1 to LED4 respectively through a 64 Ohm resistor each**.
6. **Connect the cathodes (negative sides) of LED1 to LED4 directly to the ground (GND) on the Raspberry Pi Pico**.

## Software Setup for IR Transmission
### Importing IR Tx Library from Peter Hinch
To enable the Raspberry Pi Pico to send infrared signals, we'll utilize a dedicated library that simplifies the IR communication process. This section will guide you through the steps of downloading, installing, and utilizing the library for your project.

#### Downloading the Library
1. Visit the GitHub repository for the micropython-ir library: [micropython-ir on GitHub by Peter Hinch](https://github.com/peterhinch/micropython_ir/tree/master).
2. Locate the "Code" button and click on it to reveal the dropdown menu.
3. Select "Download ZIP" to download the library files to your computer.

### Project Creation and Library Upload to Raspberry Pi Pico
Note: Use two distinct laptops. Set up the Transmission project on one laptop and the Reception project on another.

#### Step-by-Step Instructions:
1. **Open Visual Studio Code**: Launch Visual Studio Code on your computer.
2. **Create a New Project**: Navigate to the 'File' menu and select 'New Folder'. This will be your project directory. Name the folder `IR_TX` or a name of your choosing that indicates it's for Lab 13.
3. **Set Up the Project for Raspberry Pi Pico**: In Visual Studio Code, open the new folder you just created. Configure the folder as a Pico project. Your Explorer pane in Visual Studio Code should show the project directory with the `.vscode` and `micropico` files.
4. **Copy the IR Receiver Library Folder**: Copy the `ir_tx` folder from the extracted `micropython-ir` library that you previously downloaded. Paste the `ir_tx` folder into your `IR_TX` project directory.
5. **Upload the Library to Raspberry Pi Pico**: Connect your Raspberry Pi Pico to your computer via a USB cable. In Visual Studio Code, right-click the project folder in the Explorer pane and select ‘Ctrl+Shift+P’ and type ‘>MicroPico:Upload project to Pico'. Wait for the upload to complete. A notification should appear indicating that the project has been uploaded successfully.
6. **Create a New Python Script**: Within the same project directory, create a new file by right-clicking and selecting 'New File'. Name this file `main.py`.
7. **Import the Library in Your Script**: At the beginning of your Python script, add the following import statement to include the IR receiver library:
    ```python
    import ir_tx
    ```

### Test The Library
Run your script by pressing the run button in Visual Studio Code. If no errors occur, it confirms that the `ir_tx` library is successfully imported and ready for use in your project. You can now proceed to utilize the library's functionality to develop your IR transmitter application.

## Software Setup for IR Reception
Note: Use two different Laptops. Create a Transmission project in one laptop. Create a Reception project in another.

### Importing IR Rx Library from Peter Hinch
To enable the Raspberry Pi Pico to decode infrared signals from remote controls, we'll utilize a dedicated library that simplifies the IR communication process. This section will guide you through the steps of downloading, installing, and utilizing the library for your project.

#### Downloading the Library
1. Visit the GitHub repository for the micropython-ir library: [micropython-ir on GitHub by Peter Hinch](https://github.com/peterhinch/micropython_ir/tree/master).
2. Locate the "Code" button and click on it to reveal the dropdown menu.
3. Select "Download ZIP" to download the library files to your computer.

### Extracting the Library Files
1. Navigate to the downloaded ZIP file on your computer.
2. Right-click on the ZIP file and select "Extract All..." or use your preferred archive manager to extract the files.
3. After extraction, you will see a folder named `micropython_ir-master` containing various subfolders and files.

### Project Creation and Library Upload to Raspberry Pi Pico
Follow these steps to create a new project in Visual Studio Code for Lab 13 and upload the required IR receiver library to your Raspberry Pi Pico.

#### Step-by-Step Instructions:
1. **Open Visual Studio Code**: Launch Visual Studio Code on your computer.
2. **Create a New Project**: Navigate to the 'File' menu and select 'New Folder'. This will be your project directory. Name the folder `IR_RX` or a name of your choosing that indicates it's for Lab 13.
3. **Set Up the Project for Raspberry Pi Pico**: In Visual Studio Code, open the new folder you just created. Configure the folder as a Pico project. Your Explorer pane in Visual Studio Code should show the project directory with the `.vscode` and `micropico` files.
4. **Copy the IR Receiver Library Folder**: Copy the `ir_rx` folder from the extracted `micropython-ir` library that you previously downloaded. Paste the `ir_rx` folder into your `IR_RX` project directory.
5. **Upload the Library to Raspberry Pi Pico**: Connect your Raspberry Pi Pico to your computer via a USB cable. In Visual Studio Code, right-click the project folder in the Explorer pane and select ‘Ctrl+Shift+P’ and type ‘>MicroPico:Upload project to Pico'. Wait for the upload to complete. A notification should appear indicating that the project has been uploaded successfully.
6. **Create a New Python Script**: Within the same project directory, create a new file by right-clicking and selecting 'New File'. Name this file `main.py`.
7. **Import the Library in Your Script**: At the beginning of your Python script, add the following import statement to include the IR receiver library:
    ```python
    import ir_rx
    ```

### Test The Library
Run your script by pressing the run button in Visual Studio Code. If no errors occur, it confirms that the `ir_rx` library is successfully imported and ready for use in your project. You can now proceed to utilize the library's functionality to develop your IR receiver application.

## Software Implementation

### Script Implementation for IR Signal Transmission
Now that you have set up your Raspberry Pi Pico for IR transmission, use this script to send commands to the IR receiver. Make sure you have connected your IR LED to the Raspberry Pi Pico as detailed in the hardware setup instructions.

#### Steps for Implementing the IR Transmission Script:
1. **Open Your Project Folder in Visual Studio Code**: Navigate to the directory for the IR transmission project you have created in Visual Studio Code.
2. **Create a New MicroPython Script for Transmission named `main.py`**:
    - Right-click within the Explorer pane and select 'New File'.
    - Name the file `main.py`.
3. **Copy the Transmission Code with Comments**:
    ```python
    from machine import Pin
    import uasyncio as asyncio
    from ir_tx.nec import NEC

    # Define an asynchronous function to handle IR transmission
    async def transmit_ir():
        ir_transmitter = NEC(Pin(17, Pin.OUT, value=0))  # Initialize IR transmitter on Pin 17
        addr = 0x01  # Example device address

        commands = [0x01, 0x02, 0x03, 0x04]  # List of commands to send

        while True:
            for command in commands:
                ir_transmitter.transmit(addr, command)  # Send each command
                print(f"IR signal transmitted: Addr {addr} Command {command}")
                await asyncio.sleep(3)  # Wait for 3 seconds before sending the next command

    # Main function to run the transmitter
    async def main():
        await transmit_ir()  # Call the transmit function

    if __name__ == "__main__":
        asyncio.run(main())  # Start the asynchronous event loop
    ```
4. **Save the Script**: Save the script by clicking 'File' > 'Save' or pressing `Ctrl + S`.

### Script Implementation for IR Signal Reception
Once the `ir_rx` library has been successfully uploaded to your Raspberry Pi Pico, you're ready to start receiving and decoding IR signals. The following script uses the NEC protocol to interpret signals from a standard IR remote control.

#### Steps for Implementing the Script:
1. **Open Your Project Folder in Visual Studio Code**: Navigate to the IR reception directory previously set up in Visual Studio Code.
2. **Create a New MicroPython Script**: Right-click within the Explorer pane and select 'New File'. Name the file something indicative of its function like `main.py`.
3. **Copy the following Code**:
    ```python
    from machine import Pin
    import uasyncio as asyncio
    from ir_rx.nec import NEC_8  # Use the NEC 8-bit class

    # Initialize GPIO pins for LEDs with corresponding command codes
    led_pins = {
       0x01: Pin(18, Pin.OUT),  # Command 0x01 associated with LED on Pin 18
       0x02: Pin(19, Pin.OUT),  # Command 0x02 associated with LED on Pin 19
       0x03: Pin(20, Pin.OUT),  # Command 0x03 associated with LED on Pin 20
       0x04: Pin(21, Pin.OUT)   # Command 0x04 associated with LED on Pin 21
    }

    # Asynchronous function to turn off LED after a delay
    async def turn_off_led(led_pin):
       await asyncio.sleep(2)  # Non-blocking wait for 2 seconds
       led_pin.value(0)  # Turn off LED

    # Callback function triggered when an IR code is received
    async def ir_callback(data, addr, _):
       print(f"Received NEC command! Data: 0x{data:02X} Addr: 0x{addr:02X}")
       if data in led_pins:  # If the command is one of the known commands
           led_pin = led_pins[data]  # Get the corresponding LED Pin object
           led_pin.value(1)  # Turn on the LED
           asyncio.create_task(turn_off_led(led_pin))  # Schedule turning off the LED

    # Initialize and set up the IR receiver
    ir_pin = Pin(16, Pin.IN, Pin.PULL_UP)  # IR receiver on GPIO Pin 16
    ir_receiver = NEC_8(ir_pin, callback=ir_callback)  # Setup IR receiver with the callback function `ir_callback`.

    # Optional use print_error for debugging if necessary
    ir_receiver.error_function(print_error)

    # Asynchronous main loop to keep the script running
    async def main():
        while True:
            await asyncio.sleep_ms(100)  # Sleep for 100 ms

    # Run the asynchronous event loop
    if __name__ == "__main__":
        asyncio.run(main())
    ```
4. **Save the Script**: Save the script by clicking 'File' > 'Save' or by pressing `Ctrl + S` on your keyboard.

## Running and Verifying IR Signal Reception and Transmission
Once you have programmed both Raspberry Pi Picos with their respective IR transmission (IR_TX) and IR reception (IR_RX) scripts, it's time to test the complete setup. This process will allow you to verify the correct functionality of both the transmission and reception of IR signals.

### Uploading the Scripts to Raspberry Pi Pico:
#### Uploading IR_TX Script:
1. **Open Visual Studio Code** and navigate to the project directory containing the `main.py` for IR transmission.
2. **Connect your Raspberry Pi Pico (designated as the transmitter) to your computer via USB**.
3. **Access the command palette with `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) and type `>MicroPico: Upload project to Raspberry Pi Pico`**. This will upload the `main.py` script to the transmitter Pico.

#### Uploading IR_RX Script:
1. **Repeat the process for the Raspberry Pi Pico designated as the receiver**, ensuring that its `main.py` script is the one used for IR reception.

### Running the Scripts:
#### Transmitter Pico:
- **Once the IR_TX script is uploaded**, as soon as the transmitter Pico is powered up, it will start sending the NEC messages.

#### Receiver Pico:
- **Similarly, once the IR_RX script is uploaded and the receiver Pico is powered**, it will automatically start listening for NEC signals.

### Testing the Transmission and Reception:
#### Verification Process:
- **Upon successful transmission, the receiver Pico should detect the NEC signals and the corresponding LEDs should blink according to the transmitted IR NEC codes**.

#### Terminal Output:
- **Observe the terminal output in Visual Studio Code**. You should see printed messages indicating that NEC commands have been received with the data and address values from the transmitted IR signal.

#### Troubleshooting:
- **It's common to encounter some missed or unknown frames due to the presence of other IR signals in the environment**.
- **Ensure the main four codes sent by the transmitter are consistently being received by the receiver**.
- **If the expected codes are not received, check for errors in the terminal, review the hardware connections, and confirm the proper alignment of the IR transmitter and receiver**.

### Expected Outcome:
#### Successful Reception:
- **A successful test is indicated by the receiver Pico consistently identifying the main four codes transmitted by the transmitter Pico and blinking the corresponding LEDs**.

#### Handling Ambient IR Signals:
- **Some interference from ambient IR signals is expected. However, the system should reliably recognize and respond to the signals transmitted by the IR_TX setup**.

## Lab Deliverables
For this lab, students will document the process and results of building and testing an IR communication system with both a transmitter and a receiver using the Raspberry Pi Pico.

### IR Receiver and Transmitter Circuit Documentation:
#### Circuit Images:
- **Provide clear, well-lit photographs or neatly drawn schematics of both the completed IR transmitter and receiver circuits**.
- **The Raspberry Pi Pico and all connections for each circuit, including power, ground, signal wires, and LEDs, should be visible and labeled**.

#### Circuit Descriptions:
- **Include a brief description for each image outlining the purpose and function of each component within both the transmitter and receiver circuits**.

### Circuit Measurement Documentation:
#### Multimeter Readings:
- **Record and document the forward voltage across the IR LED and IR receiver when in operation**.
- **Measure and record the current flowing through both the IR transmitter and receiver circuits**.

#### Analysis:
- **Compare the measurements against the datasheet specifications**.
- **Analyze any discrepancies and discuss potential reasons and impacts on circuit functionality**.

### Script Execution and Output:
#### Script Code:
- **A copy of the final MicroPython script used for IR signal transmission and reception**.
- **Commented code explaining the function of critical lines or blocks of code**.

#### Terminal Output:
- **Screenshots or copied text from the Visual Studio Code terminal displaying the output of the script when IR signals are transmitted and received**.

### Reflection and Troubleshooting:
#### Lab Reflection:
- **A brief write-up reflecting on the lab experience, what was learned, and the practical skills gained**.

#### Troubleshooting Steps:
- **An account of any issues encountered during the lab and how they were resolved**.
- **This can include hardware setup challenges, software bugs, or understanding the datasheet**.

### Submission Format:
- **Compile all deliverables into a single PDF document, clearly sectioned and labeled**.
- **Ensure all images and screenshots are legible with appropriate captions or annotations**.
- **Students must submit their lab report by the deadline specified by the instructor. Reports should demonstrate a clear understanding of the lab's objectives and outcomes, reflecting the student's engagement with both the practical and theoretical aspects of IR communication**.

## Additional Resources
- [Adafruit 1528-157-ND IR receiver datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5389/157_Web.pdf)
- [TSAL 6400 IR Emitter](https://www.vishay.com/docs/81011/tsal6400.pdf)
- [NEC IR protocol specification](https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol)
- [NEC Infrared receiver class Micropython](https://forum.micropython.org/viewtopic.php?t=671)

---

Happy coding!

**Kiran Jojare**  
*Embedded Software / Firmware Engineer*  
kijo7257@colorado.edu
