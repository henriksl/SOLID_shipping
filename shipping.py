"""Concrete classes for shipping module."""

from abstract import FileParser, ItemRegister, ShippingSolver


class TextParser(FileParser):
    """Parser reading items from text file where initial item is container"""

    def read_item_numbers(self):
        """File reading method with text input"""
        with open(self.file_name, encoding="utf-8") as f:
            for line in f:
                self.item_numbers.append(int(line))


class ParserFactory:
    """Method used to create file parser based on file extension."""

    @staticmethod
    def create_parser(file_name: str) -> FileParser:
        """Factory method for concrete file parser classes."""
        if file_name.endswith(".txt"):
            return TextParser(file_name)

        raise NameError("Input error: input file needs to have .txt extension")


class TextItemRegister(ItemRegister):
    """
    Item register based on single 4 column text file
    with item numbers, names, value and volume.
    """

    def read_item_name_data_base(self):
        """Method used to load register, specific to text file."""
        with open(self.data_base_name, encoding="utf-8") as f:
            for line in f:
                split_line = line.split()
                self.data_base[int(split_line[0])] = {
                    "name": split_line[1],
                    "value": split_line[2],
                    "volume": split_line[3],
                }


class RegisterFactory:
    """Method used to create item register based on data base name extension."""

    @staticmethod
    def create_item_register(item_numbers: list, data_base_name: str) -> ItemRegister:
        """Factory method to create item retrievers dynamically"""
        if data_base_name.endswith(".txt"):
            return TextItemRegister(item_numbers, data_base_name)

        raise NameError("Input error: input data base needs to have .txt extension")


class TrivialSolver(ShippingSolver):
    """Solver which only returns provided data."""

    def solve(self):
        """Trivial solver"""
        self.item_data = self.item_data_initial

class SolverFactory:
    """Method used to create solver instances based on specified solver type"""

    @staticmethod
    def create_solver(solver_type: str, container, item_data) -> ShippingSolver:
        """Factory method for concrete file parser classes."""
        if solver_type == "trivial":
            return TrivialSolver(container, item_data)

        raise NameError("Input error: solver type needs to equal trivial.")

