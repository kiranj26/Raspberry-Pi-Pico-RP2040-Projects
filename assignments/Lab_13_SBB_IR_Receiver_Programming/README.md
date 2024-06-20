# Lab 13: SBB IR Receiver & Programming

This lab introduces students to the practical aspects of infrared (IR) communication through hands-on experience with the Raspberry Pi Pico and an IR receiver utilizing the Adafruit TSOP382. By incorporating the MicroPython library developed by Peter Hinch, students will explore how to set up a circuit for IR signal reception, decode NEC protocol frames, and apply this knowledge to control actions based on IR commands. The goal is to provide a foundational understanding of IR communication systems and their application in real-world scenarios, bridging the gap between theoretical knowledge and practical implementation.

## Table of Contents
- [Introduction](#introduction)
- [Learning Outcomes](#learning-outcomes)
- [Equipment & Materials](#equipment--materials)
- [Vocabulary](#vocabulary)
- [Hardware Setup](#hardware-setup)
- [Software Setup](#software-setup)
- [Software Implementation](#software-implementation)
- [Running and Verifying IR Signal Reception](#running-and-verifying-ir-signal-reception)
- [Lab Deliverables](#lab-deliverables)
- [Additional Resources](#additional-resources)

## Introduction
This lab provides step-by-step instructions for setting up an IR receiver circuit with the Raspberry Pi Pico, configuring it for signal detection, and decoding IR signals using the NEC protocol.

## Learning Outcomes
Upon completion of this lab, students will be able to:
- Understand the basic principles of IR communication, including signal modulation and demodulation.
- Set up an IR receiver circuit with the Raspberry Pi Pico and configure it for signal detection.
- Utilize programming techniques to interpret IR signals and translate them into actionable commands.
- Implement simple control logic to perform actions based on the decoded IR commands.

## Equipment & Materials
- Raspberry Pi Pico
- IR Receiver Module (TSOP382 from Adafruit)
- Breadboard
- Resistors (including a 10kΩ pull-up resistor if necessary)
- LED and suitable current-limiting resistor (220Ω to 1kΩ)
- Jumper wires
- USB Cable
- Visual Studio Code

## Vocabulary
- **Infrared (IR) Communication**: A form of wireless communication using infrared light waves.
- **NEC Protocol**: A popular protocol for IR communication, commonly used in remote control systems.
- **MicroPython**: A streamlined version of Python designed for microcontrollers and embedded systems.
- **Carrier Frequency**: The frequency of the infrared light wave that carries the encoded information.
- **Modulation/Demodulation**: The process of encoding and extracting data onto/from a carrier wave.
- **Breadboard**: A solderless device for prototyping electronic circuits.

## Hardware Setup
### Adafruit IR Receiver Specifications
The Adafruit IR Receiver (model 1528-157-ND) is designed for easy integration into projects involving IR signal reception. It is a 38kHz IR receiver module suitable for decoding signals from most remote controls.

- **Pinout**:
  - VCC (Power): Connect to 3.3V on the Raspberry Pi Pico.
  - GND (Ground): Connect to one of the ground pins on the Pico.
  - OUT (Signal Output): Connect to a GPIO pin (GPIO15) on the Pico for reading the IR signal.

### Breadboard Setup for IR Receiver
To facilitate an easy and reversible setup, we'll use a breadboard to connect the IR receiver to the Raspberry Pi Pico. This method allows for quick adjustments and troubleshooting.

#### Components:
- Raspberry Pi Pico
- Adafruit IR Receiver
- Breadboard
- Jumper wires

#### Connection Steps:
1. **Place the IR Receiver on the Breadboard**: Carefully insert the three pins of the IR receiver into three separate rows on the breadboard.
2. **Power Connection (VCC)**: Use a jumper wire to connect the VCC pin of the IR receiver to one of the 3.3V pins on the Raspberry Pi Pico.
3. **Ground Connection (GND)**: Use another jumper wire to connect the GND pin of the IR receiver to one of the ground (GND) pins on the Pico.
4. **Signal Connection (OUT)**: Use a jumper wire to connect the OUT pin of the IR receiver to GPIO15 on the Pico.

## Software Setup
### Importing IR Rx Library from Peter Hinch
To enable the Raspberry Pi Pico to decode infrared signals from remote controls, we'll utilize a dedicated library that simplifies the IR communication process. This section will guide you through the steps of downloading, installing, and utilizing the library for your project.

#### Downloading the Library
1. Visit the GitHub repository for the micropython-ir library: [micropython-ir on GitHub by Peter Hinch](https://github.com/peterhinch/micropython_ir/tree/master).
2. Locate the "Code" button and click on it to reveal the dropdown menu.
3. Select "Download ZIP" to download the library files to your computer.

#### Extracting the Library Files
1. Navigate to the downloaded ZIP file on your computer.
2. Right-click on the ZIP file and select "Extract All..." or use your preferred archive manager to extract the files.
3. After extraction, you will see a folder named `micropython_ir-master` containing various subfolders and files.

### Project Creation and Library Upload to Raspberry Pi Pico
Follow these steps to create a new project in Visual Studio Code for Lab 13 and upload the required IR receiver library to your Raspberry Pi Pico.

#### Step-by-Step Instructions:
1. **Open Visual Studio Code**: Launch Visual Studio Code on your computer.
2. **Create a New Project**:
    - Navigate to the 'File' menu and select 'New Folder'. This will be your project directory.
    - Name the folder `LAB13_PART1` or a name of your choosing that indicates it's for Lab 13.
3. **Set Up the Project for Raspberry Pi Pico**:
    - In Visual Studio Code, open the new folder you just created.
    - Configure the folder as a Pico project.
    - Your Explorer pane in Visual Studio Code should show the project directory with the `.vscode` and `micropico` files.
4. **Copy the IR Receiver Library Folder**:
    - Copy the `ir_rx` folder from the extracted `micropython-ir` library that you previously downloaded.
    - Paste the `ir_rx` folder into your `LAB13_PART1` project directory.
5. **Upload the Library to Raspberry Pi Pico**:
    - Connect your Raspberry Pi Pico to your computer via a USB cable.
    - In Visual Studio Code, right-click the project folder in the Explorer pane and select ‘Ctrl+Shift+P’ and type ‘>MicroPico:Upload project to Pico'.
    - Wait for the upload to complete. A notification should appear indicating that the project has been uploaded successfully.
6. **Create a New Python Script**:
    - Within the same project directory, create a new file by right-clicking and selecting 'New File'. Name this file `main.py`.
7. **Import the Library in Your Script**:
    - At the beginning of your Python script, add the following import statement to include the IR receiver library:
      ```python
      import ir_rx
      ```

## Software Implementation
### Script Implementation for IR Signal Reception
Once the `ir_rx` library has been successfully uploaded to your Raspberry Pi Pico, you're ready to start receiving and decoding IR signals. The following script uses the NEC protocol to interpret signals from a standard IR remote control.

#### Steps for Implementing the Script:
1. **Open Your Project Folder in Visual Studio Code**:
    - Navigate to the `LAB13_PART1` directory previously set up in Visual Studio Code.
2. **Create a New MicroPython Script**:
    - Right-click within the Explorer pane and select 'New File'.
    - Name the file something indicative of its function like `ir_receiver_script.py`.
3. **Copy the Provided Code**:
    - Open the `ir_receiver_script.py` file in Visual Studio Code and paste the provided code for receiving and decoding IR signals.
4. **Adjust the GPIO Pin Number if Necessary**:
    - If you've connected the IR receiver to a pin other than GPIO 16, update the `ir_pin` line with the correct GPIO number.
5. **Save the Script**:
    - Save the script by clicking 'File' > 'Save' or by pressing `Ctrl + S` on your keyboard.

## Running and Verifying IR Signal Reception
After setting up your Raspberry Pi Pico with the IR receiver library, it's time to test the reception with the assistance of your Teaching Assistant (TA). Here's how you can run your script and verify the reception of IR signals.

### Run the Script:
1. **Execute the Script**:
    - With the `ir_receiver_script.py` file open in Visual Studio Code, start the script by clicking on the 'Run' button located at the top-right of the editor or by pressing `F5`.
    - Alternatively, you can use the command palette with the shortcut `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS), type 'Run Python File' and hit `Enter`.

### Test with an IR Transmitter:
1. **Prepare for Testing**:
    - Ensure your Raspberry Pi Pico is connected and set up according to the previous steps with the `ir_rx` library uploaded and the script ready to run.
2. **TA Assistance for Signal Transmission**:
    - Your TA will use a standard IR transmitter to send various NEC commands toward your receiver setup.
    - Align the transmitter's IR LED with your Pico's IR receiver module for clear signal transmission.
3. **Observe Terminal Output**:
    - Watch the output in Visual Studio Code's integrated terminal.
    - A successful reception will display messages like "Received NEC command!" followed by specific data and address values from the received IR signal.
4. **Troubleshoot if Necessary**:
    - If the expected output isn't appearing, review the terminal for any error messages that might provide clues for debugging.
    - Double-check your hardware connections and ensure your IR receiver is correctly positioned to receive signals from the transmitter.

## Lab Deliverables
For Lab 13, students are expected to provide evidence of their work and understanding of IR communication using a Raspberry Pi Pico and an IR receiver. The following are the detailed deliverables each student must submit:

1. **IR Receiver Circuit Documentation**:
    - **Circuit Image**: A clear, well-lit photograph or a neatly drawn schematic of the completed IR receiver circuit.
      - The Raspberry Pi Pico and all connections, including power, ground, and signal wires to the IR receiver, should be visible and labeled.
    - **Circuit Description**: A brief description accompanying the image explaining the purpose of each component within the circuit.

2. **Data Sheet Analysis**:
    - **Forward Voltage and Current**: A written summary or a table extracted from the IR receiver's datasheet detailing the forward voltage (Vf) and the typical forward current (If) specifications.
    - **Explanation**: An explanation of how these values relate to the functionality of the IR receiver in the context of the lab.

3. **Circuit Measurement Documentation**:
    - **Multimeter Readings**: Document the measured forward voltage across the IR receiver when exposed to an IR signal.
    - **Current Measurement**: Record the current flowing through the IR receiver circuit when activated.
    - **Analysis**: Compare the measured values against the datasheet specifications. Discuss any discrepancies and their possible causes or implications on the circuit's performance.

4. **Script Execution and Output**:
    - **Script Code**: A copy of the final MicroPython script used for IR signal reception. Commented code explaining the function of critical lines or blocks of code.
    - **Terminal Output**: Screenshots or copied text from the Visual Studio Code terminal displaying the output of the script when IR signals are received.

5. **Reflection and Troubleshooting**:
    - **Lab Reflection**: A brief write-up reflecting on the lab experience, what was learned, and the practical skills gained.
    - **Troubleshooting Steps**: An account of any issues encountered during the lab and how they were resolved. This can include hardware setup challenges, software bugs, or understanding the datasheet.

### Submission Format:
- Compile all deliverables into a single PDF document, clearly sectioned and labeled.
- Ensure all images and screenshots are legible with appropriate captions or annotations.
- Submit the lab report by the deadline specified by the instructor. Reports should demonstrate a clear understanding of the lab's objectives and outcomes, reflecting the student's engagement with both the practical and theoretical aspects of IR communication.

## Additional Resources
- [Adafruit IR Receiver Datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5389/157_Web.pdf)
- [NEC IR Protocol Specification](https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol)
- [NEC Infrared Receiver Class Micropython](https://forum.micropython.org/viewtopic.php?t=671)

---

Happy coding!

**Kiran Jojare**  
*Embedded Software / Firmware Engineer*  
kijo7257@colorado.edu
