from utils import parser, CustomListener
import sys

with CustomListener(count_limit=1024) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        listener.stop()
        sys.exit(0)
