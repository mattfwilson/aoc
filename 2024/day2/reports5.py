inputs = []
safe_reports = []

with open('inputs.txt', 'r') as file:
    for line in file:
        levels = line.strip().split()
        inputs.append([int(n) for n in levels])

for report in inputs:
    if report == sorted(report) or report == sorted(report, reverse=True):
        diffs = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
        print(diffs)

        for num in diffs:
            if num > 1 and num <= 3:
                safe_reports.append(report)

print(len(safe_reports))
