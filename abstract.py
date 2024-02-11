"""Module containing abstract classes for shipping module."""

from abc import ABC, abstractmethod


class FileParser(ABC):
    """Abstract file parser class."""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "read_item_numbers")
            and callable(subclass.read_item_numbers)
            or NotImplemented
        )

    def __init__(self, file_name):
        self.file_name = file_name
        self.item_numbers = []

    @abstractmethod
    def read_item_numbers(self):
        """Method used to perform file reading."""
        raise NotImplementedError

    def get_item_numbers(self) -> list:
        """Method used to return list of item numbers."""
        return self.item_numbers


class ItemRegister(ABC):
    """Abstract item retriever class."""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "read_item_name_data_base")
            and callable(subclass.read_item_name_data_base)
            or NotImplemented
        )

    def __init__(self, item_numbers, data_base_name):
        self.item_numbers = item_numbers
        self.data_base_name = data_base_name
        self.data_base = {}
        self.item_data = []
        # Read in current data base of available items.
        self.read_item_name_data_base()

    @abstractmethod
    def read_item_name_data_base(self):
        """Method used to read given data base to memory."""
        raise NotImplementedError

    def convert_item_numbers_to_data(self):
        """Convert item number to data and add to item_data member."""
        for item in self.item_numbers:
            if item in self.data_base.keys():
                self.item_data.append(self.data_base[item])

    def get_item_data(self) -> list:
        """Method used to return list of item data. item data is given as
        a dict with name, value and volume entries."""
        return self.item_data[1:]

    def get_container(self):
        """Method used to get container."""
        return self.item_data[0]


class ShippingSolver(ABC):
    """Abstract shipping solver, which solves specific
    shipping problem given item_data and solver type."""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "solve")
            and callable(subclass.solve)
            or NotImplemented
        )

    def __init__(self, container, item_data):
        self.container = container
        self.item_data_initial = item_data
        self.item_data = []

    @abstractmethod
    def solve(self):
        """Method which reduces item_data for given problem and solver"""
        raise NotImplementedError

    def get_results(self):
        """Returns item data after solving."""
        return self.item_data
