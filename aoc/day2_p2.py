#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three. 

def is_safe(report):
    increment = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    # < and > check for strict subsets.
    # {1, 2} <= {1, 2, 3} = True
    # {1, 3} <= {1, 2, 3} = True
    # {1, 4} <= {1, 2, 3} = False
    if set(increment) <= {1, 2, 3} or set(increment) <= {-1, -2, -3}:
        print('safe!')
        return True
    return False

with open('input.txt') as file:
    file = file.read()
    reports = [[int(level) for level in report.split()] for report in file.split('\n')]
    reports_to_check = [[row[:i] + row[i + 1:] for i in range(len(row))] for row in reports]
    num_safe = 0
    for report in reports_to_check:
        for sub_report in report:
            if is_safe(sub_report):
                num_safe += 1
                break
    print(num_safe)