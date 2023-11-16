import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def arithmetic_arranger(problems, solver=False):
    # Check problems does not exceed the given max(5)
    if len(problems) > 5:
        return "Error: Too many problems."
    toptier = ""
    bottomtier = ""
    lines = ""
    totals = ""
    for n in problems:
        fnumber = n.split()[0]
        operator = n.split()[1]
        snumber = n.split()[2]

        # Handle errors for input:
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if not fnumber.isdigit() or not snumber.isdigit():
            return "Error: Numbers must only contain digits."
        if len(fnumber) > 4 or len(snumber) > 4:
            return "Error: Numbers cannot be more than four digits"

        # Get total of correct function
        total = ops[operator](int(fnumber), int(snumber))
        # Get distance for longest operator
        operatorDistance = max(len(fnumber), len(snumber)) + 2

        snumber = operator + snumber.rjust(operatorDistance - 1)
        toptier = toptier + fnumber.rjust(operatorDistance) + (4 * " ")
        bottomtier = bottomtier + snumber + (4 * " ")
        lines = lines + len(snumber) * "_" + (4 * " ")
        totals = totals + str(total).rjust(operatorDistance) + (4 * " ")
    if solver:
        print(toptier)
        print(bottomtier)
        print(lines)
        print(totals)


if __name__ == "__main__":
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
import operator

from typing import Sequence, NamedTuple, Literal

ops = {"+": operator.add, "-": operator.sub}


class Problem(NamedTuple):
    x: int
    y: int
    op: Literal['+', '-']

    @classmethod
    def parse(cls, s: str) -> 'Problem':
        x, op, y = s.split()

        for n in (x, y):
            if not n.isdigit():
                raise ValueError('Error: Numbers must only contain digits.')

        return cls(x=int(x), y=int(y), op=op)

    def validate(self) -> None:
        for n in (self.x, self.y):
            if abs(n) >= 1e4:
                raise ValueError('Error: Number cannot be more than four digits.')

        if self.op not in ops:
            raise ValueError(
                'Error: Operator must be '
                + ' or '.join(f"'{o}'" for o in ops.keys())
            )

    def format_lines(self, solve: bool = False) -> tuple[str, ...]:
        longest = max(self.x, self.y)
        width = len(str(longest))
        lines = (
            f'{self.x:>{width + 2}}',
            f'{self.op} {self.y:>{width}}',
            f'{"":->{width+2}}',
        )
        if solve:
            lines += (
                f'{self.answer:>{width+2}}',
            )
        return lines

    @property
    def answer(self) -> int:
        return ops[self.op](self.x, self.y)


def arithmetic_arranger(problem_strings: Sequence[str], solve: bool = False) -> None:
    if len(problem_strings) > 5:
        print('Error: Too many problems.')
        return

    try:
        problems = [Problem.parse(s) for s in problem_strings]
        for problem in problems:
            problem.validate()
    except ValueError as e:
        print(e)
        return

    lines = zip(*(p.format_lines(solve) for p in problems))
    print(
        '\n'.join(
            '    '.join(groups) for groups in lines
        )
    )


if __name__ == "__main__":
    arithmetic_arranger((
        "32 + 698",
        "3801 - 2",
        "4 + 4553",
        "123 + 49",
        "1234 - 9876"
    ), solve=True)
