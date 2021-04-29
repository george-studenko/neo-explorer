"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional),
    diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, name=None, diameter=None,
                 hazardous='N', approaches=[]):
        """Create a new `NearEarthObject`.

        :param designation: The primary designation for this NearEarthObject.
        :param name: The IAU name for this NearEarthObject.
        :param diameter: The diameter, in kilometers, of this NearEarthObject.
        :param hazardous: Whether or not this NearEarthObject is potentially
        hazardous.
        :param approaches: A collection of this NearEarthObjects close
        approaches to Earth.
        """
        self.designation = designation
        self.name = name
        if name == '':
            self.name = None
        self.diameter = float('nan')
        if diameter:
            self.diameter = float(diameter)
        hazardous_dict = {'Y': True, 'N': False}
        self.hazardous = hazardous_dict.get(hazardous, False)

        # Create an empty initial collection of linked approaches.
        self.approaches = approaches

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f'{self.name} {self.designation}'

    def __str__(self):
        """Return `str(self)`."""
        hazardous_classification = {True: 'has', False: 'has not'}
        return f"A NearEarthObject named {self.fullname} with diameter of " \
               f"{self.diameter:.3f} km. {self.name} " \
               f"{hazardous_classification[self.hazardous]} " \
               f"been classified as hazardous by the NASA and had " \
               f"{len(self.approaches)} approaches to earth"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of
         this object."""
        return (f"NearEarthObject(designation={self.designation!r}, "
                f"name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach
    to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.
    def __init__(self, des, time, distance: float, velocity: float, neo=None):
        """Create a new `CloseApproach`.
        :param time: The date and time, in UTC, at which the NEO passes closest
         to Earth.
        :param distance: The nominal approach distance, in astronomical units,
         of the NEO to Earth at the closest point.
        :param velocity: The velocity, in kilometers per second, of the NEO
        relative to Earth at the closest point.
        :param neo: The NearEarthObject that is making a close approach to
         Earth.
        """
        self._designation = des
        if neo:
            self._designation = neo.designation
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach
         time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # build a formatted representation of the approach time.
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"A Close approach to earth happened at {self.time_str} " \
               f"with a distance of {self.distance} au and a velocity of " \
               f"{self.velocity:} km/h"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of
         this object."""
        return (
            f"CloseApproach(time={self.time_str!r}, distance={self.distance} "
            f"velocity={self.velocity}, neo={self.neo})")
