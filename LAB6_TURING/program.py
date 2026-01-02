import sys
from collections import deque

def read_transitions(file_path):
    transitions = {}
    with open(file_path) as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            state, symbol, new_symbol, direction, new_state = parts
            transitions.setdefault((state, symbol), []).append((new_symbol, direction, new_state))
    return transitions

def print_tape(tape, head, state):
    print(''.join(tape), state)
    print(' ' * head + '^')

def run_turing_machine(tape_str, transitions, transitions_file_name):
    tape = list(tape_str)
    initial_state = 'init'
    queue = deque()
    queue.append((tape, 0, initial_state, []))

    while queue:
        tape, head, state, history = queue.popleft()
        history = history + [(list(tape), head, state)]

        if state.startswith('halt'):
            for t, h, s in history:
                print_tape(t, h, s)
            # po osiągnięciu halt: liczenie jedynek jeśli plik ma "count1" w nazwie
            if "count1" in transitions_file_name:
                ones_count = tape.count('1')
                print(f"Liczba jedynek na taśmie: {ones_count}")
            return

        symbol = tape[head] if 0 <= head < len(tape) else '_'
        key = (state, symbol)
        if key not in transitions:
            continue

        for new_symbol, direction, new_state in transitions[key]:
            new_tape = tape.copy()
            new_head = head

            # rozszerzanie taśmy w razie potrzeby
            if new_head < 0:
                new_tape = ['_'] * (-new_head) + new_tape
                new_head = 0
            if new_head >= len(new_tape):
                new_tape += ['_'] * (new_head - len(new_tape) + 1)

            new_tape[new_head] = new_symbol
            if direction == 'L':
                new_head -= 1
            elif direction == 'R':
                new_head += 1

            queue.append((new_tape, new_head, new_state, history))

    print("Maszyna nie osiągnęła stanu halt")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Użycie: python program.py <tape> <transitions_file>")
        sys.exit(1)

    tape_str = sys.argv[1]
    transitions_file = sys.argv[2]
    transitions = read_transitions(transitions_file)
    run_turing_machine(tape_str, transitions, transitions_file)