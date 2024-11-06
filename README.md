# Video to Image Extractor

This Python script extracts images from a video file at specified intervals. It saves every nth frame as an image in a folder named "Images" in the current directory.

## Features

- Extracts images from any video file.
- Allows specifying the frame interval, so users can control how frequently frames are saved as images.

## Requirements

- Python 3.x
- OpenCV library (`cv2`)

## Installation

### 1. Install Python

Make sure Python 3 is installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### 2. Install OpenCV

Install the OpenCV library using `pip`:

```bash
pip install opencv-python
```

## Usage

```
python3 video_to_image.py <video_path> <frame_interval>
```
or 
```
./video_to_image.py <video_path> <frame_interval>
```

## Arguments 

- <video_path>: Path to the video file you want to process.
- <frame_interval>: The interval for frame extraction. For example, setting frame_interval to 5 saves every 5th frame.


## Example

bash

'''
python3 video_to_image.py sample_video.mp4 5
'''

This command processes sample_video.mp4, saves every 5th frame as an image, and stores the images in a folder named "Images" in the current directory.

## Output
- A folder named Images will be created in the current directory.
- Extracted frames will be saved as .jpg files in this folder with filenames like frame_0.jpg, frame_1.jpg, etc

## Author

Benedict Kipkoech

