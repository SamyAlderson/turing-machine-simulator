class TuringMachine:
    """
    A basic implementation of a single-tape Turing machine simulator.

    This class encapsulates the Turing machine's state, tape, and behavior.
    It supports basic input/output operations and step-by-step execution.
    """

    def __init__(self, alphabet, states, transition_function):
        """
        Initialize the Turing machine with its alphabet, states, and transition function.

        Args:
            alphabet (list): The set of symbols the tape can hold.
            states (list): The set of states the Turing machine can be in.
            transition_function (dict): A dictionary mapping (state, symbol) pairs to new states and symbols.
        """
        self.alphabet = alphabet
        self.states = states
        self.transition_function = transition_function
        self.tape = []  # Initialize tape as a list of symbols
        self.state = None  # Initialize state to None

    def load_tape(self, tape):
        """
        Load the tape with the given symbols.

        Args:
            tape (list): A list of symbols to load onto the tape.
        """
        self.tape = tape[:]
        self.state = self.transition_function[("q0", tape[0])][0]  # Start in the initial state

    def step(self):
        """
        Execute one step of the Turing machine.

        This involves reading the current symbol, applying the transition function, and writing the new symbol.
        """
        if not self.tape:  # Check if the tape is empty
            raise ValueError("Tape is empty")

        current_symbol = self.tape.pop(0)  # Read the current symbol
        next_state, next_symbol = self.transition_function[(self.state, current_symbol)]
        self.tape.insert(0, next_symbol)  # Write the new symbol
        self.state = next_state  # Update the state

    def run(self, num_steps):
        """
        Run the Turing machine for the given number of steps.

        Args:
            num_steps (int): The number of steps to run the Turing machine.
        """
        for _ in range(num_steps):
            self.step()

    def __str__(self):
        """
        Return a string representation of the Turing machine's state.

        This includes the current state, tape, and number of steps executed.
        """
        return f"Turing machine in state {self.state} with tape {self.tape} after {self.tape.index(self.tape[0]) + 1} steps"


def create_turing_machine(alphabet, states, transition_function):
    """
    Create a Turing machine instance with the given parameters.

    Args:
        alphabet (list): The set of symbols the tape can hold.
        states (list): The set of states the Turing machine can be in.
        transition_function (dict): A dictionary mapping (state, symbol) pairs to new states and symbols.

    Returns:
        TuringMachine: A Turing machine instance with the given parameters.
    """
    return TuringMachine(alphabet, states, transition_function)


# Example usage:
alphabet = ["a", "b", "c"]
states = ["q0", "q1", "q2"]
transition_function = {
    ("q0", "a"): ("q1", "b"),
    ("q0", "b"): ("q2", "c"),
    ("q0", "c"): ("q2", "a"),
    ("q1", "a"): ("q2", "b"),
    ("q1", "b"): ("q0", "c"),
    ("q1", "c"): ("q0", "a"),
    ("q2", "a"): ("q0", "b"),
    ("q2", "b"): ("q1", "c"),
    ("q2", "c"): ("q1", "a")
}

turing_machine = create_turing_machine(alphabet, states, transition_function)
turing_machine.load_tape(["a", "b", "c"])
turing_machine.run(3)
print(turing_machine)