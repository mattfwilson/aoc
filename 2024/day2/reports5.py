inputs = []
safe_reports = []
diffs = []

with open('inputs.txt', 'r') as file:
    for line in file:
        levels = line.strip().split()
        inputs.append([int(n) for n in levels])

for report in inputs:
    if report == sorted(report) or report == sorted(report, reverse=True):
        diffs = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]

    for num in diffs:
        if num >= 1 and num <= 3:
            safe_reports.append(report)

                
print(safe_reports)
print(f'safe reports: {len(safe_reports)}')
