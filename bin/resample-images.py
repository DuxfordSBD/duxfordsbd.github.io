#!/usr/bin/env python3

import argparse
import os
import sys
from PIL import Image

def resample_image(input_path, output_path, percentage):
    """
    Resamples a single image file to a specified percentage of its original size.

    Args:
        input_path (str): Path to the source image file.
        output_path (str): Path where the resampled image will be saved.
        percentage (int): The resampling percentage.
    """
    try:
        # Open the image file
        img = Image.open(input_path)

        # Retrieve the DPI from the original image's info dictionary
        # If no DPI info exists, it will be None
        dpi = img.info.get('dpi')

        # Calculate new dimensions based on the percentage
        width, height = img.size
        new_width = int(width * (percentage / 100))
        new_height = int(height * (percentage / 100))

        # Resample the image using a high-quality filter
        new_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Save the new image, preserving the original DPI if it was available
        if dpi:
            new_img.save(output_path, "JPEG", dpi=dpi)
        else:
            new_img.save(output_path, "JPEG")
        
        print(f"Successfully resampled '{os.path.basename(input_path)}' to '{output_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while processing '{input_path}': {e}")
        sys.exit(1)

def main():
    """
    Main function to parse command-line arguments and process images.

    Requires you to install pillow
    """
    parser = argparse.ArgumentParser(
        description="Resample one or more JPEG images and save them to a new location."
    )
    
    # Argument for input files or directories
    parser.add_argument(
        "input",
        nargs='+',
        help="A list of one or more file paths or a single directory path to process."
    )

    # Argument for output directory
    parser.add_argument(
        "-d", "--output-dir",
        required=True,
        help="The directory where the resampled images will be saved."
    )

    # Optional flag to allow overwriting
    parser.add_argument(
        "-o", "--overwrite",
        action="store_true",
        help="If set, existing files in the output directory will be overwritten."
    )
    
    # Optional argument for resampling percentage, defaults to 15
    parser.add_argument(
        "-p", "--percentage",
        type=int,
        default=15,
        help="The percentage to resample the image by (default: 15)."
    )

    args = parser.parse_args()

    # Step 1: Collect all image files to process
    files_to_process = []
    for path in args.input:
        if os.path.isdir(path):
            # If the path is a directory, get all JPEG files inside
            for filename in os.listdir(path):
                if filename.lower().endswith(('.jpeg', '.jpg')):
                    files_to_process.append(os.path.join(path, filename))
        elif os.path.isfile(path):
            # If the path is a file, check if it's a JPEG and add it
            if path.lower().endswith(('.jpeg', '.jpg')):
                files_to_process.append(path)
            else:
                print(f"Skipping non-JPEG file: '{path}'")
        else:
            print(f"Warning: Path not found or is not a file/directory: '{path}'")

    if not files_to_process:
        print("No JPEG images found to process. Exiting.")
        sys.exit(0)

    # Step 2: Check for existing files in the output directory if overwriting is not enabled
    if os.path.exists(args.output_dir) and not args.overwrite:
        for file_path in files_to_process:
            output_filename = os.path.basename(file_path)
            full_output_path = os.path.join(args.output_dir, output_filename)
            if os.path.exists(full_output_path):
                print(
                    f"Error: File '{output_filename}' already exists in the output directory '{args.output_dir}'. "
                    "Use the --overwrite flag to proceed. Exiting."
                )
                sys.exit(1)

    # Step 3: Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Step 4: Process each image
    for file_path in files_to_process:
        output_filename = os.path.basename(file_path)
        full_output_path = os.path.join(args.output_dir, output_filename)
        resample_image(file_path, full_output_path, args.percentage)

if __name__ == "__main__":
    main()
