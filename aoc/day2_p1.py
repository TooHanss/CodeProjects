#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three. 

with open('input.txt') as file:
    file = file.read()
    reports = [report.split() for report in file.split('\n')]   
    num_unsafe = 0
    for report in reports:
        num_items = len(report)-1
        print(report)
        if int(report[0]) < int(report[1]):
            increasing = True
        else:
            increasing = False
        for i in range(num_items):
            if not increasing:
                if 1 <= (int(report[i]) - int(report[i+1])) <= 3:
                    print('safe')
                else:
                    print('unsafe!')
                    num_unsafe += 1
                    break
            else:
                if 1 <= (int(report[i+1]) - int(report[i])) <= 3:
                    print('safe')
                else:
                    print('unsafe!')
                    num_unsafe += 1
                    break
    
    num_safe = len(reports) - num_unsafe
    print(num_safe)    