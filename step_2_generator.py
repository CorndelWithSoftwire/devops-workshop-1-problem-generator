import random

operators = ['+', '-', '*', '/']

def build_calc_statement(max) -> str:
    operator = operators[random.randint(0, len(operators) - 1)]
    parameter_1 = random.randint(1, max)
    parameter_2 = random.randint(1, max)
    return f"calc {operator} {parameter_1} {parameter_2}\n"

def process_calc_statement(statement) -> int:
    [_, operator, param_string_1, param_string_2] = statement.split()

    param_1 = int(param_string_1)
    param_2 = int(param_string_2)

    if operator == '+':
        return param_1 + param_2
    elif operator == '-':
        return param_1 - param_2
    elif operator == '*':
        return param_1 * param_2
    elif operator == '/':
        return param_1 / param_2
    else:
        raise Exception("Unexpected Operator!")

def main():
    with open("step_2.txt", mode='w') as f:
        for i in range(0, 1000):
            statement = build_calc_statement(100)
            f.write(statement)

    sum = 0
    with open("step_2.txt", mode='r') as f:
        with open("step_2_calculations.txt", mode='w') as f2:
            file_by_lines = f.read().splitlines()
            for line in file_by_lines:
                calc = process_calc_statement(line)
                f2.write(str(calc) + "\n")
                sum += calc
            print(sum)

if __name__ == "__main__":
    main()