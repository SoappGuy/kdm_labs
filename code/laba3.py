import itertools


def evaluate_expression(expression: str, values: dict) -> str:

    for key in operators.keys():
        expression = expression.replace(key, operators[key])

    for key in values.keys():
        expression = expression.replace(key, values[key])

    return str(eval(expression))


def generate_table(expression: str):
    values = expression
    for key in operators.keys():
        values = values.replace(key, "")

    values = values.split(" ")
    # values = [item for item in values if item != ""]

    while "" in values:
        values.remove("")

    table = itertools.product(["True", "False"], repeat=len(values))

    result_table = list([tuple(value for value in values) + (expression, )])
    result_table.append(["-" * len(str(result_table[0]))])
    for row in table:
        expr_dict = dict(zip(values, row))
        result = evaluate_expression(expression, expr_dict)
        row += (result, )
        result_table.append(row)

    for row in result_table:
        string = ""
        for column in row:
            string += f"|{column:7}"
        print(string)


operators = {
        "AND": "and",
        "OR": "or",
        "NOT": "not",
        "(": "(",
        ")": ")",
    }

if __name__ == "__main__":

    expr: str = "(A AND B) OR (NOT C)"
    values_dict: dict = {
        "A": "True",
        "B": "False",
        "C": "True",
    }

    print(evaluate_expression(expr, values_dict))

    expr: str = "(A AND B) OR C"
    generate_table(expr)
