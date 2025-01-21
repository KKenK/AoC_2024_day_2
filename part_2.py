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

    report_indexs = len(report.levels) - 1

    levels = report.levels

    i = 0

    bad_level_counter = 0

    if levels[0] < levels[1]:
        
        while i < report_indexs:

            report_difference = levels[i] - levels[i + 1]

            if report_difference not in [-1, -2, -3]:
                
                bad_level_counter += 1

                if bad_level_counter > 1:
                    return "Unsafe"

                levels.pop(i + 1)
          
                report_indexs -= 1
                                                     
                continue

            i += 1
        
    elif levels[0] > levels[1]:

       while i < report_indexs:

            report_difference = levels[i] - levels[i + 1]

            if report_difference not in [1, 2, 3]:
                
                bad_level_counter += 1

                if bad_level_counter > 1:
                    return "Unsafe"

                levels.pop(i + 1)

                report_indexs -= 1

                continue
            
            i += 1
                                   
    else:
        return "Unsafe"
    
    return "Safe"

if __name__ == "__main__":

    input_parser = InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_2\test.txt")

    reports = make_reports(input_parser.parsed_input)

    reports = evaluate_reports_state(reports)


    safe_report_counter = 0

    for report in reports:
        if report.state == "Safe":
            safe_report_counter += 1
    
    print(safe_report_counter)
