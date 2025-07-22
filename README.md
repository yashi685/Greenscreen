🟢 Green Screen Remover (Image/Video) using OpenCV + FFmpeg
This project removes green screen backgrounds from videos or images, and replaces them with a custom background using OpenCV.
For videos, the original audio is retained using FFmpeg.

🎥 Features
✅ Replace green screen in videos

✅ Replace green screen in images

✅ Automatically resizes background to match subject

✅ Keeps original audio in videos using FFmpeg

✅ Easy command-line interface (CLI)

📁 Project Structure

green-screen-remover/
├── ffmpeg-7.1.1/              # FFmpeg folder (required for audio in video)
├── script.py                  # Main Python script
├── README.md                  # Project documentation
💻 Requirements
Python 3.x

OpenCV (cv2)

NumPy

FFmpeg (downloaded and referenced in code)

📦 Installation
Install dependencies

pip install opencv-python numpy
Download FFmpeg

Download FFmpeg

Extract it and update the ffmpeg_path in the script:


ffmpeg_path = r"C:\Users\YourName\Path\To\ffmpeg\bin\ffmpeg.exe"
▶️ How to Use
✅ 1. Run the script

python script.py
🟢 2. Choose mode:


1. Replace green screen in video
2. Replace green screen in image
💡 3. Provide file paths (examples):
Video with green screen:


C:/Users/yashi/Downloads/greenscreen_video.mp4
Background image:

C:/Users/yashi/Pictures/beach.jpg
📂 Output
For videos:

temp_output.mp4 – video with background replaced, no audio

final_output_with_audio.mp4 – final output with original audio

For images:

output_image.jpg – image with background replaced

🛠️ Customization
🎯 Adjust green range if needed:


lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])
🧠 Use your own ffmpeg_path if not in project folder
