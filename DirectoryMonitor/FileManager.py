import os


class FileManager:
    def __init__(self):
        pass

    def run(self):
        print("file manager run")

    def readTobeMonitoredDirectories(self):

        f = open(os.getcwd() + "\\folder_paths.txt", "r")
        directories_list = []
        for x in f:
            if not x.startswith("#"):
                # print(x)
                directories_list.append((x).strip())

        f.close()
        # print(set(directories_list))
        return set(directories_list)

    def write_modified_datetime(self, content):
        f = open(os.getcwd() + "\\modifiedDateTimeHolder.txt", "w")
        f.write(content)
        f.close()

    def read_modified_datetime(self, directory_to_get_data_for):
        f = open(os.getcwd() + "\\modifiedDateTimeHolder.txt", "r")
        modified_date_time = ""
        for line in f:
            if directory_to_get_data_for in line:
                split_str = line.split("|", 2)
                # print("modified date for ", directory_to_get_data_for, " is ", split_str[1])
                modified_date_time = split_str[1]
        f.close()
        return modified_date_time.strip()


if __name__ == '__main__':
    w = FileManager()
