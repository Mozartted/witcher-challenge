from watchdog.events import PatternMatchingEventHandler
import shutil
import getpass

class VideoHandler (PatternMatchingEventHandler):
    patterns = ["*.mkv", "*.mp4", "*.avi"]
    currentUser = getpass.getuser()
    destination = '/Users/' + currentUser + '/My Documents/Downloads/Folders'

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