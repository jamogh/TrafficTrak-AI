# TrafficTrak-AI

TrafficTrak AI is a Python-based vehicle counting system using computer vision techniques. This project leverages OpenCV for vehicle detection and tracking in a video feed. It is designed to count the number of vehicles passing through a designated line, providing valuable data for traffic analysis and management.

![TrafficTrak AI in Action](https://github.com/kushalgupta1203/TrafficTrak-AI/blob/main/sample.gif)

## Features

- Real-time vehicle detection and counting
- Utilizes background subtraction and morphological operations for accurate detection
- Displays vehicle count on the video feed
- Customizable parameters for different use cases

## Installation

#### Clone the repository:
   ```bash
   git clone https://github.com/kushalgupta1203/TrafficTrak-AI.git
   cd TrafficTrak-AI
   ```
#### Create a virtual environment:

```bash
python -m venv venv
```

#### Activate the virtual environment:

###### Windows:
```bash
venv\Scripts\activate
```
###### macOS and Linux:
```bash
source venv/bin/activate
```
#### Install the required dependencies:

```bash
pip install -r requirements.txt
```
## Running the Application
Ensure the video file is in the correct directory:
Place your video file in the project directory. Update the video path in the code if necessary.

```bash
python main.py
```
## View the output:

#### The application will display two windows:

- Original Video: Shows the video feed with detected vehicles and the counting line.
- Detection: Displays the processed frame used for detection.

## How It Works
- The application uses a background subtractor to separate moving objects (vehicles) from the background.
- Morphological operations are applied to reduce noise and improve detection accuracy.
- Contours are detected and filtered based on size to identify valid vehicles.
- When a vehicle's center crosses the designated line, the vehicle count is incremented.

## Customization
- Minimum width and height of detected vehicles: Modify the min_width and min_height variables to adjust the size filter for vehicle detection.
- Counting line position: Change the line_position variable to move the counting line.
- FPS delay: Adjust the delay variable to change the frame processing speed.
