import random, math

operators = ['+', '-', 'x', '/']

def build_calc_statement(max) -> str:
    operator = operators[random.randint(0, len(operators) - 1)]
    parameter_1 = random.randint(1, max)
    parameter_2 = random.randint(1, math.ceil(math.sqrt(max)))
    return f"calc {operator} {parameter_1} {parameter_2}"

def build_goto_statement(max) -> str:
    line = random.randint(1, max)
    return f"goto {line}"

def build_remove_statement(max) -> str:
    line = random.randint(1, max)
    return f"remove {line}"

def build_replace_statement(max) -> str:
    line_1 = random.randint(1, max)
    line_2 = random.randint(1, max)
    return f"replace {line_1} {line_2}"

def build_goto_calc_statement(line_total) -> str:
    while True:
        calc_statement = build_calc_statement(line_total)
        value = process_calc_statement(calc_statement)
        if value < line_total:
            break
    return f"goto {calc_statement}"

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
    with open("step_4.txt", mode='w') as f:
        line_total = 10000

        for i in range(0, line_total):
            statement_dice_roll = random.randint(0, 3)
            if statement_dice_roll == 0:
                statement = build_goto_calc_statement(line_total)
            elif statement_dice_roll == 1:
                statement = build_goto_statement(line_total)
            elif statement_dice_roll == 2:
                statement = build_remove_statement(line_total)
            elif statement_dice_roll == 3:
                statement = build_replace_statement(line_total)
            statement += "\n"
            f.write(statement)

    with open("step_4.txt", mode='r') as f:
        file_by_lines = f.read().splitlines()
        lines_hit = set()
        line_number = 1
        while True:
            current_line = file_by_lines[line_number - 1]
            new_line_number = process_statement(current_line, line_number, file_by_lines)
            print(current_line)
            print(new_line_number)
            if new_line_number in lines_hit:
                line_number = new_line_number
                break
            lines_hit.add(new_line_number)
            line_number = new_line_number
        print(line_number)

if __name__ == "__main__":
    main()