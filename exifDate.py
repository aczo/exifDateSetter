# Import modules
import os
import sys
import datetime
import argparse
from PIL import Image, ExifTags

parser = argparse.ArgumentParser(description='Change OS image creation/modification date to the ones present in EXIF data.')
parser.add_argument('directory', help='directory containing files')

args = parser.parse_args()

print(args.directory)

process_dir = args.directory

# Loop through all JPG files in the current directory
for file in os.listdir(process_dir):
    if file.lower().endswith(".jpg"):
        # Get the full path of the file
        file_path = os.path.join(process_dir, file)
        # Open the file as an image
        image = Image.open(file_path)
        # Get the exif data of the image
        exif_data = image.getexif()
        if ExifTags.Base.DateTime.value in exif_data:
            # Get the date and time of the image as a string
            date_time_str = exif_data[ExifTags.Base.DateTime.value]
            # Convert the date and time string to a datetime object
            date_time_obj = datetime.datetime.strptime(date_time_str, "%Y:%m:%d %H:%M:%S")
            # Convert the datetime object to a timestamp
            timestamp = date_time_obj.timestamp()
            # Set the creation and modification date of the file to the timestamp
            os.utime(file_path, (timestamp, timestamp))
            # Print a message
            print(f"Set the date and time of {file} to {date_time_str}")
        else:
            # Print a message
            print(f"No exif data found for {file}")
