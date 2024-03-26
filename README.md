## Introduction
### What is Certissue?
Certissue is a Command-line interface program that saves effort and time of issuing certificates manually by automatically issuing certificates from .CSV files.
\
<br>
Please watch [this video](https://www.youtube.com/watch?v=Dp0G7kCMTjw) for detailed explanation.

### Advantages
- Open source
- One-time effort (Issuance of multiple certificates at once)
- Customizable
- Built using Python

### Modules
Certissue requires couple modules to run correctly, some of these modules are usually normally installed with Python, the other are not (see the [installation section](#installtion) for more details).
<br>
\
Modules used:
- PIL (PILLOW)
- os
- csv
- argparse
- sys

## Installation
### Cloning the repository
The code can be cloned using git tool. If you're confused, please watch [this video](https://www.youtube.com/watch?v=q9wc7hUrW8U) or simply copy and paste the code bellow in your shell:
```
git clone https://github.com/0xY43/certissue.git
```

### Installing requirements
After cloning the repository to your local machine, you might notice the (requirements.txt) text file, which includes all the required modules to run the script. These requirements can be installed using pip. Please copy and paste the following code in your shell:
```bash
pip install -r requirements.txt
```
### Finally, running the script
Finally, after cloning the repository and installing the required modules, you can run the script. The command for running the script can vary depending on the shell you're using. Example:
```bash
python3 certissue.py -x [x-axis] -y [y-axis] -i [Image.png] -fi [File.csv] -s [SIZE] -t [ON/OFF]
```
> [!NOTE]
> These arguments are the required ones only.
## Flags/Switches
- **-x***: x-axis point pixel coordinates (Integer since pixel coordinates cannot be float)
- **-y***: y-axis point pixel coordinates (Integer since pixel coordinates cannot be float)
- **-i***: Name of the certification image with the extension (the extension must be .PNG)
- **-fi***: Name of the .CSV file with the extension (the extension must be .CSV)
- **-fo**: Name of font with the extension (preferably .ttf), a custom font can be used by placing it in the /fonts/ directory
- **-s***: Size of the font used
- **-r**: Value of the red color must be in range of [0,255] (Since red is only 8 bits)
- **-g**: Value of the green color must be in range of [0,255] (Since green is only 8 bits)
- **-b**: Value of the blue color must be in range of [0,255] (Since blue is only 8 bits)
- **-t***: Test mode flag/switch, when ON the program will only issue ONE certificate (first row in the .CSV file), and when the switch is off the programm will issue all certificates for all rows.
> [!WARNING]
> The flags marked with (*) after the flag name means the flag is required and the script can't run with out it.

## Requirements
- Know where to place the typing cursor in advance by getting the coordinates of x,y points (If your image editor/viewer does not include this feature, [PixSpy](PixSpy.com) is a good enhanced pixel examination tool)
- Include the following within the tool folder:
    - Fonts folder (you can add and use your own font by adding it to this folder and passing it using the **-fo** switch)
    - Certification as image (.PNG extension)
    - Comma-Separated Value file (.CSV extension) with the columns "First name" and "Last name" for the first name and last name respectively

## Defense Mechanisms
- The program should exit using sys.exit() whenever:
    - Test switch (**-t**) string is neither ON nor OFF
    - Desired font is not in the /fonts/ path
    - Image extension is not .PNG
    - (x,y) coordinates pair is bigger than the width and/or height of the actual image (certificate)
    - File is not a .CSV file
    - Red value is lower than 0 or bigger than 255 (Red must be in the range of [0,255] since red is 8 bits)
    - Green value is lower than 0 or bigger than 255 (Green must be in the range of [0,255] since green is 8 bits)
    - Blue value is lower than 0 or bigger than 255 (Blue must be in the range of [0,255] since blue is 8 bits)