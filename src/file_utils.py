# Utility methods
import os


def parse_records(file):
    """
    Get records from a file as lists of words
    :param file: path to a file where data in a record is separated with spaces
    :return: lists of words which represent each record
    """
    file_path = os.path.join(os.getcwd(), file)
    records = list()
    with open(file_path) as f:
        for raw_line in f:
            records.append(raw_line.strip().split(" "))
    return records
