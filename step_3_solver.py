import math

def process_calc_statement(statement) -> int:
    [_, operator, param_string_1, param_string_2] = statement.split()

    param_1 = int(param_string_1)
    param_2 = int(param_string_2)

    if operator == '+':
        return param_1 + param_2
    elif operator == '-':
        return param_1 - param_2
    elif operator == 'x':
        return param_1 * param_2
    elif operator == '/':
        return param_1 / param_2
    else:
        raise Exception("Unexpected Operator!")

# Returns line number to goto
def process_goto_statement(statement) -> int:
    split_statement = statement.split()
    if split_statement[1] == 'calc':
        calc_statement = f"{split_statement[1]} {split_statement[2]} {split_statement[3]} {split_statement[4]}"
        return math.floor(process_calc_statement(calc_statement))
    else:
        return int(split_statement[1])

def main():
    with open("step_3.txt", mode='r') as f:
        file_by_lines = f.read().splitlines()
        lines_hit = set()
        line_number = 1
        while True:
            current_line = file_by_lines[line_number - 1]
            if current_line in lines_hit:
                break
            new_line_number = process_goto_statement(current_line)
            print(current_line)
            print(new_line_number)
            lines_hit.add(current_line)
            line_number = new_line_number
        print(f"Answer: Line {line_number} {current_line}")

if __name__ == "__main__":
    main()