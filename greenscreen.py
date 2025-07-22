import cv2
import numpy as np
import os

# FFmpeg path (adjust if needed)
ffmpeg_path = r"C:\Users\yashi\greenscreen\ffmpeg-7.1.1\bin\ffmpeg.exe"

def replace_green_screen_video(video_path, bg_image_path, temp_output="temp_output.mp4", final_output="final_output_with_audio.mp4"):
    cap = cv2.VideoCapture(video_path)
    bg = cv2.imread(bg_image_path)

    if bg is None:
        print(f"\n❌ Couldn't load background image: {bg_image_path}")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        bg_resized = cv2.resize(bg, (frame.shape[1], frame.shape[0]))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_green = np.array([35, 40, 40])
        upper_green = np.array([85, 255, 255])
        mask = cv2.inRange(hsv, lower_green, upper_green)
        mask_inv = cv2.bitwise_not(mask)

        fg_subject = cv2.bitwise_and(frame, frame, mask=mask_inv)
        bg_masked = cv2.bitwise_and(bg_resized, bg_resized, mask=mask)
        final_frame = cv2.add(fg_subject, bg_masked)

        if out is None:
            out = cv2.VideoWriter(temp_output, fourcc, 20.0, (frame.shape[1], frame.shape[0]))

        out.write(final_frame)

    cap.release()
    if out:
        out.release()

    print(f"\n✅ Video without green screen saved as: {temp_output}")

    # Add original audio
    command = f'"{ffmpeg_path}" -y -i "{temp_output}" -i "{video_path}" -c:v copy -map 0:v:0 -map 1:a:0 -shortest "{final_output}"'
    os.system(command)

    print(f"✅ Final video with audio saved as: {final_output}")


def replace_green_screen_image(image_path, bg_path, output_path="output_image.jpg"):
    image = cv2.imread(image_path)
    bg = cv2.imread(bg_path)

    if image is None or bg is None:
        print("❌ Error loading image or background.")
        return

    bg_resized = cv2.resize(bg, (image.shape[1], image.shape[0]))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)

    fg_subject = cv2.bitwise_and(image, image, mask=mask_inv)
    bg_masked = cv2.bitwise_and(bg_resized, bg_resized, mask=mask)
    final_image = cv2.add(fg_subject, bg_masked)

    cv2.imwrite(output_path, final_image)
    print(f"✅ Green screen removed from image. Saved as: {output_path}")


def main():
    print("🎬 Green Screen Remover")
    print("1. Replace green screen in video")
    print("2. Replace green screen in image")

    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        video = input("Enter path to green screen video: ").strip().strip('"')
        bg = input("Enter path to background image: ").strip().strip('"')
        replace_green_screen_video(video, bg)
    elif choice == '2':
        image = input("Enter path to green screen image: ").strip().strip('"')
        bg = input("Enter path to background image: ").strip().strip('"')
        replace_green_screen_image(image, bg)
    else:
        print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
