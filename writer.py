import datetime as dt
import os
import csv


class DataWriter:
    DATA_FOLDER = "./.data"
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self):
        self.init_folders()
        
    def _create_folder_if_not_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
    
    def init_folders(self):
        self._create_folder_if_not_exists(self.DATA_FOLDER)
        
    def _get_today_folder_path(self):
        today = dt.date.today().strftime(self.DATE_FORMAT)
        path = f"{self.DATA_FOLDER}/{today}"
        return path

    def init_today_flder(self):
        path = self._get_today_folder_path()
        self._create_folder_if_not_exists(path)
        
    def write_date(self, interval, data):
        path = f"{self._get_today_folder_path()}/{interval}.csv"
        if not os.path.exists(path):
            with open(path, "w") as f:
                csv_writer = csv.DictWriter(f, fieldnames=list(data.keys()))
                csv_writer.writeheader()

        with open(path, "a") as f:
            csv_writer = csv.DictWriter(f, fieldnames=list(data.keys()))
            csv_writer.writerow(data)
