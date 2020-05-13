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

def process_goto_statement(statement) -> int:
    split_statement = statement.split()
    if split_statement[1] == 'calc':
        calc_statement = f"{split_statement[1]} {split_statement[2]} {split_statement[3]} {split_statement[4]}"
        return math.floor(process_calc_statement(calc_statement))
    else:
        return int(split_statement[1])

def process_remove_statement(statement, current_line, file_by_lines) -> int:
    split_statement = statement.split()
    line_to_remove = int(split_statement[1])
    if line_to_remove <= current_line:
        line_to_process_next = current_line
    else:
        line_to_process_next = current_line + 1
    file_by_lines.pop(line_to_remove)
    return line_to_process_next

def process_replace_statement(statement, current_line, file_by_lines) -> int:
    split_statement = statement.split()
    line_number_to_replace = int(split_statement[1])
    line_number_to_copy = int(split_statement[2])
    copied_line = file_by_lines[line_number_to_copy - 1]
    file_by_lines.pop(line_number_to_replace - 1)
    file_by_lines.insert(line_number_to_replace - 1, copied_line)
    return current_line + 1

def process_statement(statement, current_line, file_by_lines):
    split_statement = statement.split()
    instruction = split_statement[0]

    if instruction == "goto":
        return process_goto_statement(statement)
    elif instruction == "remove":
        return process_remove_statement(statement, current_line, file_by_lines)
    elif instruction == "replace":
        return process_replace_statement(statement, current_line, file_by_lines)
    else:
        raise Exception("Unexpected Instruction!")

def main():
    with open("step_4.txt", mode='r') as f:
        file_by_lines = f.read().splitlines()
        lines_hit = set()
        line_number = 1
        while True:
            current_line = file_by_lines[line_number - 1]
            print(current_line)
            if current_line in lines_hit:
                break
            new_line_number = process_statement(current_line, line_number, file_by_lines)
            print(new_line_number)
            lines_hit.add(current_line)
            line_number = new_line_number
        print(f"Answer: Line {line_number} {current_line}")


if __name__ == "__main__":
    main()