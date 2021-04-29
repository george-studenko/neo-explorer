"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json

from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output
    row
    corresponds to the information in a single close approach from the
    `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
    saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name',
        'diameter_km', 'potentially_hazardous')
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            row = get_csv_row(result)
            writer.writerow(row)


def get_csv_row(result):
    """Format a row to export to csv."""
    row = dict()
    row['datetime_utc'] = datetime_to_str(result.time)
    row['distance_au'] = result.distance
    row['velocity_km_s'] = result.velocity
    row['designation'] = result.neo.designation
    row['name'] = result.neo.name
    row['diameter_km'] = result.neo.diameter
    row['potentially_hazardous'] = result.neo.hazardous
    return row


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is
     a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
     saved.
    """
    with open(filename, 'w') as file:
        rows = [get_json_row(result) for result in results]
        json.dump(rows, file, indent=2)


def get_json_row(result):
    """Format a row to export to JSON."""
    approach = dict()
    neo = dict()
    approach['datetime_utc'] = datetime_to_str(result.time)
    approach['distance_au'] = result.distance
    approach['velocity_km_s'] = result.velocity
    neo['designation'] = result.neo.designation
    neo['name'] = result.neo.name
    neo['diameter_km'] = result.neo.diameter
    neo['potentially_hazardous'] = result.neo.hazardous
    approach['neo'] = neo

    return approach
