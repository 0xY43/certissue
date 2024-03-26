import argparse
import os
import sys
import csv
from PIL import Image, ImageDraw, ImageFont

def main():

    # REQUIRED: -x, -y, -i, -s, -fi, -t
    # OPTIONAL: -fo, -r, -g, -b
    args = parse_arguments()
    validate_test_mode(args.t) # -t
    validate_font(args.fo) # -fo
    validate_image_extension(args.i) # -i
    validate_coordinates(args.x, args.y, args.i) # -x, -y
    validate_csv_extension(args.fi) # -fi
    validate_rgb_colors(args.r, args.g, args.b) # -r, -g, -b
    names_list, rows_count = get_full_name(args.fi)
    issue_certificates(names_list, rows_count, args.x, args.y, args.i, args.fi, args.fo, args.s, args.t, args.r, args.g, args.b)






def parse_arguments():
    """
    Parses the Command-Line Interface arguments.

    :return: Parsed arguments
    :rtype: Object
    """
    parser = argparse.ArgumentParser(
        prog="Certissue",
        description="Program that saves the effort of issuing certificates manually",
        epilog="https://github.com/0xY43"
    )
    parser.add_argument("-x", help="x-axis point", type=int, required=True, metavar="Integer")
    parser.add_argument("-y", help="y-axis point", type=int, required=True, metavar="Integer")
    parser.add_argument("-i", help="Name of the certification file with the extension (.PNG)", type=str, required=True, metavar="String")
    parser.add_argument("-fo", help="Name of the built-in font with the extension (You can add your own in fonts/)", required=False, metavar="String", default="FreeMono.ttf")
    parser.add_argument("-s", help="Font size", type=int, required=True, metavar="Integer")
    parser.add_argument("-fi", help="Name of the CSV file with the extension (.CSV)", type=str, required=True, metavar="String")
    parser.add_argument("-t", help="Test mode (Either ON or OFF)", type=str, required=False, metavar="String", default="ON")
    parser.add_argument("-r", help="Red color value, default is 0 (Minimum is 0, Maximum is 255)", type=int, required=False, metavar="Integer", default=0)
    parser.add_argument("-g", help="Green color value, default is 0 (Minimum is 0, Maximum is 255)", type=int, required=False, metavar="Integer", default=0)
    parser.add_argument("-b", help="Blue color value, default is 0 (Minimum is 0, Maximum is 255)", type=int, required=False, metavar="Integer", default=0)
    args = parser.parse_args()
    return args


def validate_test_mode(test_mode):
    """
    Validates whether -t is either ON or OFF

    :param test_mode: Test mode
    :type test_mode: str
    :return: True
    """

    if (test_mode.lower() != "on" and test_mode.lower() != "off"):
        sys.exit("Test mode must either be ON or OFF")
    return True


def validate_font(font_name):
    """
    Validates whether the requested font exists or not

    :param font_name: Name of the requested font (.ttf)
    :type font_name: str
    :return: True
    :rtype: Boolean
    """
    fonts_list = os.listdir("fonts")
    if (font_name not in fonts_list):
        print("Available fonts:")
        for fonts in fonts_list:
            print(fonts)
        sys.exit()
    return True


def validate_image_extension(certification):
    """
    Validates whether the extension of the image is .PNG or not

    :param certification: Name of the certification file with the extension (.PNG)
    :type certification: str
    :return: True
    :rtype: Boolean
    """
    name_and_extension = os.path.splitext(certification)
    extension = name_and_extension[1].lower()
    if (extension.lower() == ".png"):
        return True
    sys.exit("Certification is not a .PNG file")


def validate_coordinates(x,y,certification):
    """
    Validates if the (x,y) coordinates of the provided certification are correct or not.

    :param x: x-axis point
    :type x: int
    :param y: y-axis point
    :type y: int
    :param certification: Name of the certification file with the extension (.PNG)
    :type certification: str
    :return: True
    :rtype: Boolean
    """
    img = Image.open(certification)
    width = img.width
    height = img.height
    # print(f"{width}. {height}")
    if (x > width or x < 0 or y < 0 or y > height):
        sys.exit("Invalid (x,y) coordinates")
    return True


def validate_csv_extension(csv_file):
    """
    Validates whether the extension of the CSV file is .csv or not

    :param csv_file: Name of the CSV file with the extension (.CSV)
    :type csv_file: str
    :return: True
    :rtype: Boolean
    """
    name_and_extension = os.path.splitext(csv_file)
    extension = name_and_extension[1].lower()
    if (extension == ".csv"):
        return True
    sys.exit("CSV file is not a .csv file")


def validate_rgb_colors(red, green, blue):
    """
    Validates whether the RGB colors have a valid value or not

    :param red: Red color value
    :type red: int
    :param green: Green color value
    :type green: int
    :param blue: Blue color value
    :type blue: int
    :return: True
    :rtype: Boolean
    """
    if (red > 255 or red < 0):
        sys.exit("Red must have value of range [0,255]")
    if (green > 255 or green < 0):
        sys.exit("Green must have value of range [0,255]")
    if (blue > 255 or blue < 0):
        sys.exit("Blue must have value of range [0,255]")
    return True


def get_full_name(csv_file):
    """
    Get full name and number of people registered

    :param csv_file: Name of the CSV file with the extension (.CSV)
    :type csv_file: str
    :return: ([],Number)
    :rtype: (list,int)
    """
    names = []
    number_of_rows = 0
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append({"first_name":row["First name"], "last_name":row["Last name"]})
            number_of_rows += 1

    return (names,number_of_rows)


def issue_certificates(names_list, number_of_rows, x, y, certification, csv_file, font_name, font_size, mode, red, green, blue):

    # When test mode is ON
    if (mode.lower() == "on"):
        with Image.open(certification).convert("RGBA") as base:

            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255,255,255, 0))

            # get a font (from fonts/ directory)
            fnt = ImageFont.truetype(f"fonts/{font_name}", font_size)

            # get a drawing context
            d = ImageDraw.Draw(txt)

            # draw text
            d.text((x,y),
            f"{names_list[0]['first_name']} {names_list[0]['last_name']}",
            font=fnt, fill=(red,green,blue,255))

            # output as .PDF and .PNG
            output = Image.alpha_composite(base, txt)
            rgb_output = output.convert("RGB")
            rgb_output.save("TEST.pdf", format="PDF", resoultion=100.0)
            output.save("TEST.png", format="PNG", resolution=100.0)
            sys.exit("TEST certificates created successfully")

    # When test mode is OFF
    for i in range(number_of_rows):
        with Image.open(certification).convert("RGBA") as base:

            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255,255,255, 0))

            # get a font (from fonts/ directory)
            fnt = ImageFont.truetype(f"fonts/{font_name}", font_size)

            # get a drawing context
            d = ImageDraw.Draw(txt)

            # draw text
            d.text((x,y), f"{names_list[i]['first_name']} {names_list[i]['last_name']}",
            font=fnt, fill=(red,green,blue,255))

            # output as .PDF and .PNG
            output = Image.alpha_composite(base, txt)
            rgb_output = output.convert("RGB")
            rgb_output.save(f"{names_list[i]['first_name']} {names_list[i]['last_name']}.pdf", format="PDF", resoultion=100.0)
            output.save(f"{names_list[i]['first_name']} {names_list[i]['last_name']}.PNG", format="PNG", resolution=100.0)

    sys.exit("Certificates created successfully")


if __name__ == "__main__":
    main()