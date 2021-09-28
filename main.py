from Calculator import Calculator
from EquationSimplifiers.StrengthBasedEquationSimplifier import StrengthBasedEquationSimplifier
from SymbolToCalculatorResolver.SymbolToCalculatorResolver import SymbolToCalculatorResolver
from OperationCalculators.BinaryOperationCalculator import BinaryOperationCalculator
from OperationCalculators.OnarOperationCalculator import OnarOperationCalculator

from Operators.binaryOperators import Addition, Subtraction, Multiplication, Maximum
from Operators.OnarOperations import SquareRoot, Factorial


def create_calculator():
    """operations"""
    addition = Addition.Addition()
    subtraction = Subtraction.Subtraction()
    multiplication = Multiplication.Multiplication()
    maximum = Maximum.Maximum()
    square_root = SquareRoot.SquareRoot()
    factorial = Factorial.Factorial()

    """binary operation calculators"""
    addition_calculator = BinaryOperationCalculator(addition)
    subtraction_calculator = BinaryOperationCalculator(subtraction)
    multiplication_calculator = BinaryOperationCalculator(multiplication)
    maximum_calculator = BinaryOperationCalculator(maximum)

    """onar operation calculators"""
    square_root_calculator = OnarOperationCalculator(square_root)
    factorial_calculator = OnarOperationCalculator(factorial)

    """operator list"""
    operator_list = [addition, subtraction, multiplication, maximum, square_root, factorial]

    """symbol to calculator resolver"""
    symbol_to_calculator_resolver = SymbolToCalculatorResolver({
        addition.symbol: addition_calculator,
        subtraction.symbol: subtraction_calculator,
        multiplication.symbol: multiplication_calculator,
        maximum.symbol: maximum_calculator,
        square_root.symbol: square_root_calculator,
        factorial.symbol: factorial_calculator
    })

    """equation simplifier"""
    equation_simplifier = StrengthBasedEquationSimplifier(operator_list, symbol_to_calculator_resolver)

    """calculator"""
    calculator = Calculator(equation_simplifier)

    return calculator


def main(equation: str):
    calculator = create_calculator()

    for step in calculator.calculate(equation):
        print(step)


if __name__ == '__main__':
    main("(1 + 2*2) * (v4 * 3 @ 8)")
