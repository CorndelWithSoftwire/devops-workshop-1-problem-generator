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
    sum = 0
    with open("step_2.txt", mode='r') as f:
        with open("step_2_calculations.txt", mode='w') as f2:
            file_by_lines = f.read().splitlines()
            for line in file_by_lines:
                calc = process_calc_statement(line)
                f2.write(str(calc) + "\n")
                sum += calc
            print(f"Answer: {sum}")

if __name__ == "__main__":
    main()