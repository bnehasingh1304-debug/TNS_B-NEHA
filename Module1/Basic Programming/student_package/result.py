def calculate_total(marks1, marks2, marks3):
    return marks1 + marks2 + marks3


def calculate_average(total):
    return total / 3


def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"
