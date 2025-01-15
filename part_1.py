from input_parser import InputParser

class Report():
    def __init__(self, levels):
        self.levels = levels
        self.state = None

def make_reports(input):
    
    reports = [Report(x) for x in input]

    return reports

def evaluate_reports_state(reports):

    for report in range(len(reports)):
        reports[report].state = check_if_report_is_safe(reports[report])
    
    return reports

def check_if_report_is_safe(report):

    report_length = len(report.levels)

    if report.levels[0] < report.levels[1]:
        
        for level in range(report_length - 1):

            report_difference = report.levels[level] - report.levels[level + 1]

            if report_difference not in [-1, -2, -3]:
                return "Unsafe"
    
    elif report.levels[0] > report.levels[1]:

        for level in range(report_length - 1):

            report_difference = report.levels[level] - report.levels[level + 1]

            if report_difference not in [1, 2, 3]:
                return "Unsafe"                   
    else:
        return "Unsafe"
    
    return "Safe"

if __name__ == "__main__":

    input_parser = InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_2\input.txt")

    reports = make_reports(input_parser.parsed_input)

    reports = evaluate_reports_state(reports)

    safe_report_counter = 0

    for report in reports:
        if report.state == "Safe":
            safe_report_counter += 1
    
    print(safe_report_counter)
