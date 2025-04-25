import os
from moviepy.editor import VideoFileClip

START = 9
END = 11

input_folder = "./video"
output_folder = "./trimmed"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with VideoFileClip(input_path) as clip:
            duration = clip.duration
            start = START
            end = duration - END
            if end > start:  # только если видео достаточно длинное
                trimmed = clip.subclip(start, end)
                trimmed.write_videofile(output_path, codec="libx264")
            else:
                print(f"Слишком короткое видео: {filename}")
