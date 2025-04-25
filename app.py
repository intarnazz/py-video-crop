import os
import logging
from moviepy.editor import VideoFileClip

# Настройка логирования в файл (ASCII, без кириллицы)
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

START = 9
END = 11

input_folder = "./video"
output_folder = "./trimmed"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with VideoFileClip(input_path) as clip:
                duration = clip.duration
                start = START
                end = duration - END
                if end > start:
                    trimmed = clip.subclip(start, end)
                    trimmed.write_videofile(output_path, codec="libx264")
                    logging.info(f"|success| {filename}")
                else:
                    logging.info(f"|skip| {filename} (too short)")
                    print(f"Skipped (too short): {filename}")
        except Exception as e:
            logging.error(f"|error| {filename} - {e}")
            print(f"Error processing {filename}: {e}")
