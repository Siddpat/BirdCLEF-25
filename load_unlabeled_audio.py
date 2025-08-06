import os
import re
from datetime import datetime

AUDIO_DIR = "/media/siddhantp/TOSHIBA EXT/birdclef-2025 (1)/train_soundscapes/"

FILENAME_PATTERN = re.compile(r"(?P<site>[A-Z0-9]+)_(?P<date>\d{8})_(?P<time>\d{6})\.ogg$")

audio_files_info = []

def get_unlabeled_audio_data(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".ogg"):
            match = FILENAME_PATTERN.match(filename)
            if match:
                site = match.group("site")
                date = match.group("date")
                time = match.group("time")
                timestamp = datetime.strptime(f"{date}_{time}", "%Y%m%d_%H%M%S")

                audio_files_info.append({
                    "filename": filename,
                    "site": site,
                    "datetime": timestamp,
                    "path": os.path.join(directory, filename)
                })

    return audio_files_info


if __name__ == "__main__":
    data = get_unlabeled_audio_data(AUDIO_DIR)
    print(f"Found {len(data)} audio files.")
    for item in data[:5]:  
        print(item)
