import argparse
from src.turing_machine import TuringMachine

def main():
    parser = argparse.ArgumentParser(description="Turing machine simulator")
    parser.add_argument("tape", type=str, help="Initial tape contents")
    parser.add_argument("--steps", type=int, default=100, help="Maximum number of steps")
    args = parser.parse_args()

    try:
        tm = TuringMachine(args.tape)
        tm.execute(args.steps)
        tm.print_tape()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()