from typing import List, Tuple


def run_code(commands: List[str]) -> Tuple[str, int]:
    call_count = {}
    acc = 0
    i = 0
    status = ""
    while True:
        if i in call_count:
            status = "error"
            break
        elif i >= len(commands):
            status = "ok"
            break
        else:
            call_count[i] = 1
        command = commands[i]

        operation, args = command.split(" ")
        sign = args[0]
        value = int(args[1:])

        if operation == "nop":
            i += 1
        elif operation == "acc":
            if sign == "-":
                acc -= value
            elif sign == "+":
                acc += value
            i += 1
        elif operation == "jmp":
            if sign == "-":
                i -= value
            elif sign == "+":
                i += value
    return status, acc


def fix_program(commands: List[str]) -> List[str]:
    positions = set()
    for i, command in enumerate(commands):
        if "nop" in command:
            original_command = command
            commands[i] = command.replace("nop", "jmp")
            status, acc = run_code(commands)
            if status == "ok":
                return status, acc
            else:
                commands[i] = original_command
        if "jmp" in command:
            original_command = command
            commands[i] = command.replace("jmp", "nop")
            status, acc = run_code(commands)
            if status == "ok":
                return status, acc
            else:
                commands[i] = original_command
    return "error", 0


if __name__ == "__main__":
#     commands = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6""".split("\n")

    with open("input/day8.txt", "r") as f:
        commands = f.read().splitlines()

    _, acc = run_code(commands)
    print(acc)

    status, acc = fix_program(commands)
    print(status, acc)