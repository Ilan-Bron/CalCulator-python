from string import digits


def find_operation_border(equation: str, operator_index: int):
    non_operand_characters = digits + ". "

    current_index = operator_index - 1
    while current_index >= 0 and equation[current_index] in non_operand_characters:
        current_index -= 1

    starting_index = current_index + 1

    current_index = operator_index + 1
    while current_index < len(equation) and equation[current_index] in non_operand_characters:
        current_index += 1

    end_index = current_index - 1

    return starting_index, end_index
