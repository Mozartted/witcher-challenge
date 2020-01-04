from watchdog.events import PatternMatchingEventHandler
import shutil
import os
import getpass

class FileHandler (PatternMatchingEventHandler):
    patterns = ["pdf", "txt", "html", "jpg", "png", "jpeg"]
    currentUser = getpass.getuser()
    destination = '/Users/'+currentUser+'/My Documents/Downloads/Files'

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print(event.src_path, event.event_type, self.currentUser)  # print now only for debug
        # locate the file system to use

        if event.is_directory == True:
            explodedString = event.src_path.split("/")
            print(explodedString)
            shutil.move(event.src_path, self.destination+'/'+explodedString[-1])
        else:
            explodedString = event.src_path.split("/")
            print('... processed directories 🔥')
            shutil.move(event.src_path, self.destination+'/'+explodedString[-1])

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)
