import csv


class InstantiateCSVError(Exception):

    def __str__(self):
        return 'Файл item.csv поврежден'