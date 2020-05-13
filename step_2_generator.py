import random

operators = ['+', '-', 'x', '/']

def build_calc_statement(max) -> str:
    operator = operators[random.randint(0, len(operators) - 1)]
    parameter_1 = random.randint(1, max)
    parameter_2 = random.randint(1, max)
    return f"calc {operator} {parameter_1} {parameter_2}\n"

def main():
    with open("step_2.txt", mode='w') as f:
        for i in range(0, 1000):
            statement = build_calc_statement(100)
            f.write(statement)

if __name__ == "__main__":
    main()