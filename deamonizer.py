from daemonize import Daemonize
import sys
from pathlib import Path
sys.path.append('./witcher/witcher')

pid = "/tmp/witcher.pid"

from witcher.witcher import Witcher

def main():
    witcher = Witcher()
    witcher.main()

# if __name__ == '__main__' and __package__ is None:
#     file = Path(__file__).resolve()
#     parent, top = file.parent, file.parents[3]
#
#     sys.path.append(str(top))
#     try:
#         sys.path.remove(str(parent))
#     except ValueError: # Already removed
#         pass
#
#     import package.subpackage.subsubpackage
#     __package__ = 'witcher-challenge.witcher.witcher'
#
#
daemon = Daemonize(app="witcher", pid=pid, action=main)
daemon.start()

# from ... import module # N = 3