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

if __name__ == "__main__":
    main()