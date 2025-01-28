from input_parser import InputParser

class Report():
    def __init__(self, levels):
        self.levels = levels
        self.is_safe = "Indeterminate"

def make_reports(input):
    
    reports = [Report(x) for x in input]

    return reports

def evaluate_reports_state(reports):

    for report_index in range(len(reports)):

        levels = reports[report_index].levels    
        
        report_is_ascending = is_ascending(levels)

        if not report_is_ascending:          
            levels = [x * -1 for x in levels]      
   
        reports[report_index].is_safe = check_if_report_is_safe(levels)

        if not reports[report_index].is_safe:

            for i in range(len(levels) - 1):

                reports[report_index].is_safe = check_if_report_is_safe(levels[:i] + levels[i + 1:])

                if reports[report_index].is_safe:
                    break
            
            if not reports[report_index].is_safe:
                reports[report_index].is_safe = check_if_report_is_safe(levels[:-1])
            
    return reports

def is_ascending(levels):
    
    direction = 0

    for i in range(1, len(levels)):

        difference = levels[i] - levels[i - 1]

        if difference > 0:
            direction += 1
        
        elif difference < 0:
            direction -= 1
        
    if direction > 0:
        return True
    
    return False

def check_if_report_is_safe(levels):
        
    for i in range(1, len(levels)):

        report_difference = levels[i] - levels[i - 1]

        if report_difference not in [1, 2, 3]:
            
            return False
    
    return True

if __name__ == "__main__":

    input_parser = InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_2\input.txt")

    reports = make_reports(input_parser.parsed_input)

    reports = evaluate_reports_state(reports)


    safe_report_counter = 0

    for report in reports:
        if report.is_safe == True:
            safe_report_counter += 1
    
    print(safe_report_counter)
