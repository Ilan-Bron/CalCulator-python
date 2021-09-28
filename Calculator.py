from EquationSimplifiers.IOneStepEquationSimplifier import IOneStepEquationSimplifier


def find_closing_bracket(equation: str) -> int:
    return equation.find(")")


class Calculator:

    def __init__(self, simplifier: IOneStepEquationSimplifier):
        self.simplifier = simplifier

    def solve_equation(self, equation):
        new_equation = self.simplifier.simplify(equation)

        while new_equation != equation:
            yield equation
            equation = new_equation
            new_equation = self.simplifier.simplify(equation)

        yield new_equation

    def calculate(self, equation: str) -> str:
        simplified_equation = equation.replace(" ", "")

        open_bracket_index = simplified_equation.find("(")

        while open_bracket_index != -1:

            close_bracket_index = find_closing_bracket(simplified_equation)

            sub_equation = simplified_equation[open_bracket_index + 1: close_bracket_index]
            rest_of_equation = simplified_equation[close_bracket_index + 1:]

            all_steps = list(self.solve_equation(sub_equation))
            for step in all_steps:
                step_in_whole_equation = f"{simplified_equation[0: open_bracket_index]}"\
                                      f"({step})"\
                                      f"{rest_of_equation}"

                yield step_in_whole_equation

            simplified_equation = f"{simplified_equation[0: open_bracket_index]}"\
                                  f"{all_steps[-1]}"\
                                  f"{rest_of_equation}"

            open_bracket_index = simplified_equation.find("(")

        for step in self.solve_equation(simplified_equation):
            yield step
