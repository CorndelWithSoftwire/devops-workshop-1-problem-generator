import random, math

operators = ['+', '-', 'x', '/']

def build_calc_statement(max) -> str:
    operator = operators[random.randint(0, len(operators) - 1)]
    parameter_1 = random.randint(1, max)
    parameter_2 = random.randint(1, max) // 100 + 1
    return f"calc {operator} {parameter_1} {parameter_2}"

def build_goto_statement(max) -> str:
    line = random.randint(1, max)
    return f"goto {line}"

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

def main():
    with open("step_3.txt", mode='w') as f:
        line_total = 10000

        for i in range(0, line_total):
            coin_toss = random.randint(0, 1)
            if coin_toss == 1:
                statement = build_goto_calc_statement(line_total)
            else:
                statement = build_goto_statement(line_total)
            statement += "\n"
            f.write(statement)

    sum = 0
    with open("step_3.txt", mode='r') as f:
        file_by_lines = f.read().splitlines()
        lines_hit = set()
        line_number = 1
        while True:
            current_line = file_by_lines[line_number]
            new_line_number = process_goto_statement(current_line)
            print(new_line_number)
            if new_line_number in lines_hit:
                line_number = new_line_number
                break
            lines_hit.add(new_line_number)
            line_number = new_line_number
        print(line_number)

if __name__ == "__main__":
    main()