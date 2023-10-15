from laba1 import AwesomeSet


def cartesian_product(set_a, set_b):
    result = AwesomeSet()
    for elementA in set_a:
        for elementB in set_b:
            result.add(AwesomeSet(elementA, elementB))

    return result


def is_relation_valid(relation, set_a, set_b):
    cartesian = cartesian_product(set_a, set_b)

    for element in relation:
        if element not in cartesian:
            return False

    return True


def find_relations(set_a, func):
    relations = AwesomeSet()
    for element1 in set_a:
        for element2 in set_a:
            if func(element1, element2) and element1 != element2:
                relations.add((element1, element2))
    return relations


def filtered_cartesian_product(set_a, set_b, func):
    result = AwesomeSet()
    for elementA in set_a:
        for elementB in set_b:
            if func(elementA, elementB) and elementA != elementB:
                result.add((elementA, elementB))

    return result


set1 = AwesomeSet(1, 2)
set2 = AwesomeSet("a", "b")
print(cartesian_product(set1, set2))


set1 = AwesomeSet(1, 2)
set2 = AwesomeSet("a", "b")
relation = AwesomeSet(AwesomeSet(1, "a"), AwesomeSet(2, "b"))
print(is_relation_valid(relation, set1, set2))


set1 = AwesomeSet(1, 2, 3, 4, 6)
is_divisible = lambda a, b: a % b == 0
print(find_relations(set1, is_divisible))


set1 = AwesomeSet(1, 2, 3)
set2 = AwesomeSet(3, 4, 5)
is_less = lambda a, b: a < b
wtf = lambda el_a, el_b: (el_a % 2 == 0 and el_b % 2 != 0) or (el_a % 2 != 0 and el_b % 2 == 0)
print(filtered_cartesian_product(set1, set2, wtf))

