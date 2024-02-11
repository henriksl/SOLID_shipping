"""
Application used to test the container module and more generally to practice SOLID.
The file parser, item register and solvers are all open-closed, Liskov is enforced 
through inheritance, and dependency inversion through relatively clean interfaces.
More work could have more clearly defined objects with clear responsibilities.
The application can be run after adjusting below __directory__ to appropriate folder.
python3 tester.py itemNumbers.txt itemRegister.txt trivial
"""


import sys
import shipping

__directory__ = "/home/henrik/Development/privateProjects/py_dev/ContainerProject/"
 
def get_path(name):
    """Path getter in set directory and given name."""
    return __directory__ + name

if __name__ == "__main__":

    try:
        __file_path__ = get_path(sys.argv[1])
        __data_base_path__ = get_path(sys.argv[2])
        __solver_type__ = sys.argv[3]

        # Parse file
        file_parser = shipping.ParserFactory.create_parser(__file_path__)
        file_parser.read_item_numbers()

        # Retrieve item data from specified items
        item_register = shipping.RegisterFactory.create_item_register(
            file_parser.get_item_numbers(), __data_base_path__
        )
        item_register.convert_item_numbers_to_data()

        # Create solver for specified type, initialise data and solve shipping problem.
        solver = shipping.SolverFactory.create_solver(
            __solver_type__, item_register.get_container(), item_register.get_item_data()
        )
        solver.solve()

        # Display results - below is one specific display type. Could be generalised as above.
        print(solver.get_results())

    except NameError as err:
        print(err)
