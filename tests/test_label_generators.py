from pathlib import Path

import pytest

import context
from paroxython.label_generators import (
    generate_labeled_sources,
    generate_programs_labels,
)
from paroxython.program_generator import generate_programs

programs = list(generate_programs("tests/data/programs"))


def test_generate_labeled_sources():
    result = generate_labeled_sources(programs)

    assert "assignment.py" in next(result)
    assert next(result).strip() == "a = b # assignment, global_variable_definition"

    assert "collatz_print.py" in next(result)
    assert next(result).strip() == "\n".join(
        [
            "def print_collatz(n): # added_block_label (-> +7), function:print_collatz (-> +7)",
            "    while n != 1: # comparison_operator:NotEq, evolve_state (-> +5), literal:Num",
            "        print(n) # function_call:print",
            "        if n % 2 == 0: # added_label_on_line_4, binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_else (-> +3), literal:Num, suggest_conditional_expression (-> +3)",
            "            n = n // 2 # assignment, suggest_augmented_assignment",
            "        else: # if",
            "            n = 3 * n + 1 # assignment, binary_operator:Add, binary_operator:Mult, literal:Num, suggest_constant_definition",
            "    print(n) # function_call:print",
        ]
    )

    assert "function_definition.py" in next(result)
    assert next(result).strip() == "\n".join(
        [
            "def succ(n): # function:succ (-> +1)",
            "    return a + b + 1 # binary_operator:Add, literal:Num",
        ]
    )

    assert "loop.py" in next(result)
    assert next(result).strip() == "\n".join(
        [
            "while input(): # function_call:input",
            '    print("foobar") # function_call:print, literal:Str',
        ]
    )


def test_generate_programs_labels():
    result = list(generate_programs_labels(programs))
    expected = [
        (
            Path("tests/data/programs/assignment.py"),
            {"assignment": [(1, 1)], "global_variable_definition": [(1, 1)]},
        ),
        (
            Path("tests/data/programs/collatz_print.py"),
            {
                "added_block_label": [(1, 8)],
                "added_label_on_line_4": [(4, 4)],
                "assignment": [(5, 5), (7, 7)],
                "binary_operator:Add": [(7, 7)],
                "binary_operator:Mod": [(4, 4)],
                "binary_operator:Mult": [(7, 7)],
                "comparison_operator:Eq": [(4, 4)],
                "comparison_operator:NotEq": [(2, 2)],
                "divisibility_test:2": [(4, 4)],
                "evolve_state": [(2, 7)],
                "function:print_collatz": [(1, 8)],
                "function_call:print": [(3, 3), (8, 8)],
                "if": [(4, 7), (6, 6)],
                "if_else": [(4, 7)],
                "literal:Num": [(2, 2), (4, 4), (4, 4), (7, 7), (7, 7)],
                "suggest_augmented_assignment": [(5, 5)],
                "suggest_conditional_expression": [(4, 7)],
                "suggest_constant_definition": [(7, 7)],
            },
        ),
        (
            Path("tests/data/programs/function_definition.py"),
            {
                "binary_operator:Add": [(2, 2), (2, 2)],  # the construct appears twice
                "function:succ": [(1, 2)],
                "literal:Num": [(2, 2)],
            },
        ),
        (
            Path("tests/data/programs/loop.py"),
            {
                "function_call:input": [(1, 1)],
                "function_call:print": [(2, 2)],
                "literal:Str": [(2, 2)],
            },
        ),
    ]
    print(result)
    for (rk, rv), (ek, ev) in zip(result, expected):
        assert rk == ek
        for (label, spans) in rv:
            assert ev[label] == [span.to_couple() for span in spans]


pytest.main(args=["-q"])
