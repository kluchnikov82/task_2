from dirsync import sync
import logging, time, sys


source_path = sys.argv[1]
target_path = sys.argv[2]
delay = sys.argv[3]
log_file = sys.argv[4]
logging.basicConfig(filename=log_file, level=logging.DEBUG)
my_log = logging.getLogger('dirsync')


def sync_func():
    sync(source_path, target_path, 'sync', logger=my_log) #for syncing one way

while True:
    time.sleep(5)
    sync_func()