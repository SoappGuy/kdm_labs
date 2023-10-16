import itertools


def eval_expression(to_eval: str, values: dict) -> bool:
    global EXPRESSIONS

    for key in EXPRESSIONS.keys():
        to_eval = to_eval.replace(key, EXPRESSIONS[key])

    for key in values.keys():
        to_eval = to_eval.replace(key, str(values[key]))

    return eval(to_eval)


def generate_truth_table(expression: str) -> list:
    expression_strip = expression.replace("(", "")
    expression_strip = expression_strip.replace(")", "")
    values_list = expression_strip.split(" ")

    for key in EXPRESSIONS.keys():
        if key in values_list:
            values_list = [value for value in values_list if value != key]

    table = itertools.product(["True", "False"], repeat=len(values_list))

    to_return = [values_list]
    to_return[0].append(expression)

    for row in table:
        values_dict = dict(zip(values_list, row))
        row += (str(eval_expression(expression, values_dict)), )
        to_return.append(row)

    return to_return


def prettify(table: list) -> str:
    to_return = ""
    for row in table:
        for element in row:
            to_return += f"| {element:7} "
        to_return += "\n"

    return to_return


EXPRESSIONS: dict = {
        "AND": "and",
        "OR": "or",
        "NOT": "not",
    }

if __name__ == '__main__':

    # str_to_eval: str = "(A AND B) OR (NOT C)"
    # values_to_eval: dict = {
    #     "A": True,
    #     "B": False,
    #     "C": True,
    # }
    # print(eval_expression(str_to_eval, values_to_eval))

    str_to_eval: str = "(A AND B) OR C AND NOT GH"
    print(prettify(generate_truth_table(str_to_eval)))
