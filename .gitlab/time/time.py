import os
import csv
import sqlite3
import argparse


def convert_to_hours(time):
    time = time.split()
    time_in_hours = 0
    for entry in time:
        last_char = entry[-1]
        entry = entry[:-1]
        if last_char == 'd':
            time_in_hours += float(entry) * 8
        if last_char == 'h':
            time_in_hours += float(entry)
        if last_char == 'm':
            time_in_hours += 1. / 60. * float(entry)
    return time_in_hours


def convert_to_date(date):
    date = date.split()
    date, time = date[0], date[1]
    date = date.split(".")
    date = date[2] + '-' + date[1] + '-' + date[0] + ' ' + time
    return date


def read_issues(issues_file):
    with open(issues_file, 'r') as file:
        dict_reader = csv.DictReader(file)
        issues = [{
            "iid": entry['iid'],
            "title": entry['title'],
            "spent": convert_to_hours(entry['spent']),
            "total_estimate": convert_to_hours(entry['total_estimate'])
        } for entry in
            dict_reader]
    return issues


def write_issues(issues, issues_file):
    with open(issues_file, "w") as file:
        writer = csv.DictWriter(
            file, ["iid", "title", "spent", "total_estimate"])
        writer.writeheader()
        writer.writerows(issues)


def read_records(records_file):
    with open(records_file, 'r') as file:
        dict_reader = csv.DictReader(file)
        records = [{
            "user": entry['user'],
            "date": convert_to_date(entry['date']),
            "type": entry['type'],
            "iid": entry['iid'],
            "time": convert_to_hours(entry['time'])
        } for entry in dict_reader]
    return records


def write_records(records, records_file):
    with open(records_file, "w") as file:
        writer = csv.DictWriter(
            file, ["user", "date", "type", "iid", "time"])
        writer.writeheader()
        writer.writerows(records)


def check_file(file_path):
    assert os.path.exists(
        file_path), 'File {} does not exist!'.format(file_path)


def main_function():
    parser = argparse.ArgumentParser(
        description='gitlab-time-tracker CSV files to SQLite file.', )
    parser.add_argument('-i', '--issues', dest='issues',
                        help='CSV file with issues', required=True)
    parser.add_argument('-r', '--records', dest='records',
                        help='CSV file with records', required=True)
    parser.add_argument('-p', '--print', dest='output',
                        help='Print', action='store_true')
    args = parser.parse_args()
    
    check_file(args.issues)
    issues = read_issues(args.issues)
    write_issues(issues, args.issues)
    
    check_file(args.records)
    records = read_records(args.records)
    write_records(records, args.records)


if __name__ == "__main__":
    main_function()
