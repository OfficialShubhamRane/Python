#!/usr/bin/python
import concurrent.futures
from datetime import datetime
import os
import string
import time
from FileManager import FileManager
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.utils.dirsnapshot import DirectorySnapshot
from winotify import Notification
import threading

from icecream import ic


class Watcher:
    # DIRECTORY_TO_WATCH = "E:\\DirectoryMonitorTestDirectory"
    directories_to_watch = None
    directory_to_watch = None

    def __init__(self):
        self.observer = Observer()
        fm = FileManager()

        while (True):
            directories_to_watch = fm.readTobeMonitoredDirectories()
            self.run(directories_to_watch, fm)
            time.sleep(10)

    def run(self, directories_to_watch, fm):
        # print("directories to monitor: ", directories_to_watch)
        global last_modified_of_directory_datetime
        directory_to_m_datetime_map_string = ""
        if os.path.isfile(os.getcwd() + "\\modifiedDateTimeHolder.txt"):
            for directory_to_watch in directories_to_watch:
                print("....working on: ", directory_to_watch)

                # read last known modified of the file that is previously known
                last_known_modified_of_directory_str = fm.read_modified_datetime(directory_to_watch)
                print("    last_known_modified_of_directory of", directory_to_watch, " is [",
                      last_known_modified_of_directory_str, "]")
                last_modified_of_directory_datetime = datetime.strptime(last_known_modified_of_directory_str,
                                                                        "%m/%d/%Y %H:%M:%S")

                # gets current last modified date
                modify_time = os.path.getmtime(directory_to_watch)
                current_modify_date = datetime.fromtimestamp(modify_time)
                current_modify_date_str = datetime.strftime(current_modify_date, "%m/%d/%Y %H:%M:%S")
                print("    current_modify_date_str of         ", directory_to_watch, " is [",
                      current_modify_date_str, "]")
                current_modify_date_datetime = datetime.strptime(current_modify_date_str, "%m/%d/%Y %H:%M:%S")

                if os.path.isfile(os.getcwd() + "\\modifiedDateTimeHolder.txt"):
                    # comparison
                    if current_modify_date_datetime != last_modified_of_directory_datetime:
                        print("    changes in directory " + directory_to_watch)
                        # notification creator
                        toast = Notification(app_id='DiriMon', title=directory_to_watch, msg="Modified",
                                             duration="short")
                        # toast.add_actions(label="Go to Directory", launch=directory_to_watch)
                        toast.show()

                var = directory_to_m_datetime_map_string + "\n" + directory_to_watch + "|" + current_modify_date_str
                directory_to_m_datetime_map_string = var
        else:
            for directory_to_watch in directories_to_watch:
                # gets current last modified date
                modify_time = os.path.getmtime(directory_to_watch)
                current_modify_date = datetime.fromtimestamp(modify_time)
                current_modify_date_str = datetime.strftime(current_modify_date, "%m/%d/%Y %H:%M:%S")
                print("    current_modify_date_str of         ", directory_to_watch, " is [",
                      current_modify_date_str, "]")
                current_modify_date_datetime = datetime.strptime(current_modify_date_str, "%m/%d/%Y %H:%M:%S")

                var = directory_to_m_datetime_map_string + "\n" + directory_to_watch + "|" + current_modify_date_str
                directory_to_m_datetime_map_string = var

        # creates write lines for modified file
        fm.write_modified_datetime(directory_to_m_datetime_map_string)


if __name__ == '__main__':
    w = Watcher()
