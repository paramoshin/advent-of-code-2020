if __name__ == "__main__":
#     s = """abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b"""

    with open("input/day6.txt", "r") as f:
        s = f.read()

    groups = [g.replace("\n", "") for g in s.split("\n\n")]
    count_any = 0
    for group in groups:
        answers = {char for char in group}
        count_any += len(answers)
    print(count_any)

    groups = [g.split("\n") for g in s.split("\n\n")]
    count_all = 0
    for group in groups:
        answers = set(group[0])
        for i in range(1, len(group)):
            answers &= set(group[i])
        count_all += len(answers)
    print(count_all)
