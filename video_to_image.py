#!/usr/bin/python3

import cv2
import os
import argparse

"""
function to extract every n images from a video

author:
    Benedict Kipkoech
"""

def get_unique_output_folder(base_folder_name):
    """
    Generates a unique folder name by appending a number if a folder with the same name exists.

    Parameters:
    - base_folder_name (str): The base name of the folder.

    Returns:
    - str: A unique folder name.
    """
    folder_name = base_folder_name
    counter = 1

    # Loop until a unique folder name is found
    while os.path.exists(folder_name):
        folder_name = f"{base_folder_name}({counter})"
        counter += 1

    return folder_name


def extract_images_from_video(video_path, frame_interval, output_folder='Images'):
    """
    Extracts every nth frame from a video file and saves it as an image.

    Parameters:
    - video_path (str): Path to the input video file.
    - frame_interval (int): Interval at which frames are saved (e.g., 5 means every 5th frame).
    - output_folder (str): Directory where extracted images will be saved. Defaults to 'Images'.

    Returns:
    - None
    """
    if not isinstance(frame_interval, int) or frame_interval <=0:
        raise ValueError("frame_interval must be a positive integer.")
    
    output_folder = get_unique_output_folder(output_folder)
    os.makedirs(output_folder)

    # Load the video
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_frame_count = 0

    if not cap.isOpened():
        print("Error: Could not open Video.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frame_interval == 0:
            filename = os.path.join(output_folder, f"frame_{saved_frame_count}.jpg")
            cv2.imwrite(filename, frame)
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_frame_count} frames to {output_folder}")


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Extract images from video every n frames.")
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    parser.add_argument("frame_interval", type=int, help="Number of frames to skip between saved images.")

    args = parser.parse_args()

    # Call the function with the provided arguments
    extract_images_from_video(args.video_path, args.frame_interval)
