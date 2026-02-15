#!/usr/bin/env python3
"""
Auto-resize watcher for Ren'Py game images.
Watches game/images/ and resizes any new or modified image to 1920x1080.
Run:  source .venv/bin/activate && python watch_images.py
"""

import time
import sys
from pathlib import Path
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

TARGET_W, TARGET_H = 1920, 1080
WATCH_DIR = Path(__file__).resolve().parent / "game" / "images"
SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}

# Track files we just resized so we don't re-trigger on our own write
_just_resized = set()


def resize_if_needed(filepath: Path):
    if filepath.suffix.lower() not in SUPPORTED:
        return
    if str(filepath) in _just_resized:
        _just_resized.discard(str(filepath))
        return

    # Wait briefly for the file to finish writing
    time.sleep(0.5)

    try:
        with Image.open(filepath) as img:
            w, h = img.size

            if w == TARGET_W and h == TARGET_H:
                return

            # Skip portrait images (likely character sprites, not scenes)
            if h > w:
                print(f"  Skipped {filepath.name}: portrait orientation ({w}x{h})")
                return

            # Skip images smaller than the target (don't upscale)
            if w < TARGET_W and h < TARGET_H:
                print(f"  Skipped {filepath.name}: smaller than target ({w}x{h})")
                return

            print(f"  Resizing {filepath.name}: {w}x{h} -> {TARGET_W}x{TARGET_H}")
            _just_resized.add(str(filepath))
            resized = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
            resized.save(filepath)
            print(f"  Done: {filepath.name}")
    except Exception as e:
        print(f"  Skipped {filepath.name}: {e}")
        _just_resized.discard(str(filepath))


class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            resize_if_needed(Path(event.src_path))

    def on_modified(self, event):
        if not event.is_directory:
            resize_if_needed(Path(event.src_path))


if __name__ == "__main__":
    if not WATCH_DIR.exists():
        print(f"Error: {WATCH_DIR} does not exist.")
        sys.exit(1)

    print(f"Watching: {WATCH_DIR}")
    print(f"Target:   {TARGET_W}x{TARGET_H}")
    print(f"Press Ctrl+C to stop.\n")

    observer = Observer()
    observer.schedule(ImageHandler(), str(WATCH_DIR), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping watcher.")
        observer.stop()
    observer.join()
