#!/usr/bin/python3

import cv2
import os
import argparse

"""
function to extract every n images from a video

author:
    Benedict Kipkoech
"""

def extract_images_from_video(video_path, frame_interval, output_folder='Images'):
    os.makedirs(output_folder, exist_ok=True)

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
