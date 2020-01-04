"""
The Witcher - Background running process
Run the observers in the background to know whenever a file is being saved.
"""

import time
import sys
import os
import shutil
from watchdog.observers import Observer #watches directories
from watchdog.events import PatternMatchingEventHandler # matching certain event patterms

sys.path.append('../handlers')

from handlers.video_handler import VideoHandler
from handlers.folder_handler import FolderHandler
from handlers.file_handler import FileHandler

class Witcher():
    def main(self):
        args = sys.argv[1:]
        observer = Observer()
        observer.schedule(VideoHandler(), path=args[0] if args else '.')
        observer.schedule(FolderHandler(), path=args[0] if args else '.')
        observer.schedule(FileHandler(), path=args[0] if args else '.')
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
