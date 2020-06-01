import sys

def calculate(operator, value_1, value_2) -> int:
    param_1 = int(value_1)
    param_2 = int(value_2)

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
    if len(sys.argv) < 4:
        print("Missing Arguments To Calculator")
        return

    print(calculate(sys.argv[1], sys.argv[2], sys.argv[3]))
    return 

if __name__ == "__main__":
    main()