r"""
A dictionary of predicates listing all possible relations between two intervals
\((x_1, x_2)\) and \((y_1, y_2)\).

..caution::
    This file was generated by
    [`make_compare_spans.py`](https://repo/helpers/make_compare_spans.py)
    on 2020-06-15 15:51:36.547396. Changes may cause incorrect behavior and will be lost if the
    code is regenerated.

Each predicate of the dictionary `compare_spans` is identified by a key of seven characters among
`"xy<≤="`, _e.g._ `"x=y≤x≤y"`. Several human-readable aliases are also provided:

- the 13 terms `"equals"`, `"starts"`, `"during"`, etc. introduced by James F. Allen in his seminal
  paper ([PDF](http://cse.unl.edu/~choueiry/Documents/Allen-CACM1983.pdf)) about temporal
  intervals[^Allen1983];
- some extra synonyms, _e.g._, `"in"` for `"during"` and `"is"` for `"equals"`.

[^Allen1983]:
    Allen, James F. (26 Nov. 1983). _Maintaining knowledge about temporal intervals_.
    Communications of the ACM. 26 (11): 832–843. doi:10.1145/182.358434
"""


compare_spans = {
    "x<x<y<y": lambda x, y: x[0] < x[1] < y[0] < y[1],
    "x<x<y≤y": lambda x, y: x[0] < x[1] < y[0] <= y[1],
    "x<x<y=y": lambda x, y: x[0] < x[1] < y[0] == y[1],
    "x<x≤y<y": lambda x, y: x[0] < x[1] <= y[0] < y[1],
    "x<x≤y≤y": lambda x, y: x[0] < x[1] <= y[0] <= y[1],
    "x<x≤y=y": lambda x, y: x[0] < x[1] <= y[0] == y[1],
    "x<x=y<y": lambda x, y: x[0] < x[1] == y[0] < y[1],
    "x<x=y≤y": lambda x, y: x[0] < x[1] == y[0] <= y[1],
    "x<x=y=y": lambda x, y: x[0] < x[1] == y[0] == y[1],
    "x≤x<y<y": lambda x, y: x[0] <= x[1] < y[0] < y[1],
    "x≤x<y≤y": lambda x, y: x[0] <= x[1] < y[0] <= y[1],
    "x≤x<y=y": lambda x, y: x[0] <= x[1] < y[0] == y[1],
    "x≤x≤y<y": lambda x, y: x[0] <= x[1] <= y[0] < y[1],
    "x≤x≤y≤y": lambda x, y: x[0] <= x[1] <= y[0] <= y[1],
    "x≤x≤y=y": lambda x, y: x[0] <= x[1] <= y[0] == y[1],
    "x≤x=y<y": lambda x, y: x[0] <= x[1] == y[0] < y[1],
    "x≤x=y≤y": lambda x, y: x[0] <= x[1] == y[0] <= y[1],
    "x≤x=y=y": lambda x, y: x[0] <= x[1] == y[0] == y[1],
    "x=x<y<y": lambda x, y: x[0] == x[1] < y[0] < y[1],
    "x=x<y≤y": lambda x, y: x[0] == x[1] < y[0] <= y[1],
    "x=x<y=y": lambda x, y: x[0] == x[1] < y[0] == y[1],
    "x=x≤y<y": lambda x, y: x[0] == x[1] <= y[0] < y[1],
    "x=x≤y≤y": lambda x, y: x[0] == x[1] <= y[0] <= y[1],
    "x=x≤y=y": lambda x, y: x[0] == x[1] <= y[0] == y[1],
    "x=x=y<y": lambda x, y: x[0] == x[1] == y[0] < y[1],
    "x=x=y≤y": lambda x, y: x[0] == x[1] == y[0] <= y[1],
    "x=x=y=y": lambda x, y: x[0] == x[1] == y[0] == y[1],
    "x<y<x<y": lambda x, y: x[0] < y[0] < x[1] < y[1],
    "x<y<x≤y": lambda x, y: x[0] < y[0] < x[1] <= y[1],
    "x<y<x=y": lambda x, y: x[0] < y[0] < x[1] == y[1],
    "x<y≤x<y": lambda x, y: x[0] < y[0] <= x[1] < y[1],
    "x<y≤x≤y": lambda x, y: x[0] < y[0] <= x[1] <= y[1],
    "x<y≤x=y": lambda x, y: x[0] < y[0] <= x[1] == y[1],
    "x<y=x<y": lambda x, y: x[0] < y[0] == x[1] < y[1],
    "x<y=x≤y": lambda x, y: x[0] < y[0] == x[1] <= y[1],
    "x<y=x=y": lambda x, y: x[0] < y[0] == x[1] == y[1],
    "x≤y<x<y": lambda x, y: x[0] <= y[0] < x[1] < y[1],
    "x≤y<x≤y": lambda x, y: x[0] <= y[0] < x[1] <= y[1],
    "x≤y<x=y": lambda x, y: x[0] <= y[0] < x[1] == y[1],
    "x≤y≤x<y": lambda x, y: x[0] <= y[0] <= x[1] < y[1],
    "x≤y≤x≤y": lambda x, y: x[0] <= y[0] <= x[1] <= y[1],
    "x≤y≤x=y": lambda x, y: x[0] <= y[0] <= x[1] == y[1],
    "x≤y=x<y": lambda x, y: x[0] <= y[0] == x[1] < y[1],
    "x≤y=x≤y": lambda x, y: x[0] <= y[0] == x[1] <= y[1],
    "x≤y=x=y": lambda x, y: x[0] <= y[0] == x[1] == y[1],
    "x=y<x<y": lambda x, y: x[0] == y[0] < x[1] < y[1],
    "x=y<x≤y": lambda x, y: x[0] == y[0] < x[1] <= y[1],
    "x=y<x=y": lambda x, y: x[0] == y[0] < x[1] == y[1],
    "x=y≤x<y": lambda x, y: x[0] == y[0] <= x[1] < y[1],
    "x=y≤x≤y": lambda x, y: x[0] == y[0] <= x[1] <= y[1],
    "x=y≤x=y": lambda x, y: x[0] == y[0] <= x[1] == y[1],
    "x=y=x<y": lambda x, y: x[0] == y[0] == x[1] < y[1],
    "x=y=x≤y": lambda x, y: x[0] == y[0] == x[1] <= y[1],
    "x=y=x=y": lambda x, y: x[0] == y[0] == x[1] == y[1],
    "x<y<y<x": lambda x, y: x[0] < y[0] < y[1] < x[1],
    "x<y<y≤x": lambda x, y: x[0] < y[0] < y[1] <= x[1],
    "x<y<y=x": lambda x, y: x[0] < y[0] < y[1] == x[1],
    "x<y≤y<x": lambda x, y: x[0] < y[0] <= y[1] < x[1],
    "x<y≤y≤x": lambda x, y: x[0] < y[0] <= y[1] <= x[1],
    "x<y≤y=x": lambda x, y: x[0] < y[0] <= y[1] == x[1],
    "x<y=y<x": lambda x, y: x[0] < y[0] == y[1] < x[1],
    "x<y=y≤x": lambda x, y: x[0] < y[0] == y[1] <= x[1],
    "x<y=y=x": lambda x, y: x[0] < y[0] == y[1] == x[1],
    "x≤y<y<x": lambda x, y: x[0] <= y[0] < y[1] < x[1],
    "x≤y<y≤x": lambda x, y: x[0] <= y[0] < y[1] <= x[1],
    "x≤y<y=x": lambda x, y: x[0] <= y[0] < y[1] == x[1],
    "x≤y≤y<x": lambda x, y: x[0] <= y[0] <= y[1] < x[1],
    "x≤y≤y≤x": lambda x, y: x[0] <= y[0] <= y[1] <= x[1],
    "x≤y≤y=x": lambda x, y: x[0] <= y[0] <= y[1] == x[1],
    "x≤y=y<x": lambda x, y: x[0] <= y[0] == y[1] < x[1],
    "x≤y=y≤x": lambda x, y: x[0] <= y[0] == y[1] <= x[1],
    "x≤y=y=x": lambda x, y: x[0] <= y[0] == y[1] == x[1],
    "x=y<y<x": lambda x, y: x[0] == y[0] < y[1] < x[1],
    "x=y<y≤x": lambda x, y: x[0] == y[0] < y[1] <= x[1],
    "x=y<y=x": lambda x, y: x[0] == y[0] < y[1] == x[1],
    "x=y≤y<x": lambda x, y: x[0] == y[0] <= y[1] < x[1],
    "x=y≤y≤x": lambda x, y: x[0] == y[0] <= y[1] <= x[1],
    "x=y≤y=x": lambda x, y: x[0] == y[0] <= y[1] == x[1],
    "x=y=y<x": lambda x, y: x[0] == y[0] == y[1] < x[1],
    "x=y=y≤x": lambda x, y: x[0] == y[0] == y[1] <= x[1],
    "x=y=y=x": lambda x, y: x[0] == y[0] == y[1] == x[1],
    "y<x<x<y": lambda x, y: y[0] < x[0] < x[1] < y[1],
    "y<x<x≤y": lambda x, y: y[0] < x[0] < x[1] <= y[1],
    "y<x<x=y": lambda x, y: y[0] < x[0] < x[1] == y[1],
    "y<x≤x<y": lambda x, y: y[0] < x[0] <= x[1] < y[1],
    "y<x≤x≤y": lambda x, y: y[0] < x[0] <= x[1] <= y[1],
    "y<x≤x=y": lambda x, y: y[0] < x[0] <= x[1] == y[1],
    "y<x=x<y": lambda x, y: y[0] < x[0] == x[1] < y[1],
    "y<x=x≤y": lambda x, y: y[0] < x[0] == x[1] <= y[1],
    "y<x=x=y": lambda x, y: y[0] < x[0] == x[1] == y[1],
    "y≤x<x<y": lambda x, y: y[0] <= x[0] < x[1] < y[1],
    "y≤x<x≤y": lambda x, y: y[0] <= x[0] < x[1] <= y[1],
    "y≤x<x=y": lambda x, y: y[0] <= x[0] < x[1] == y[1],
    "y≤x≤x<y": lambda x, y: y[0] <= x[0] <= x[1] < y[1],
    "y≤x≤x≤y": lambda x, y: y[0] <= x[0] <= x[1] <= y[1],
    "y≤x≤x=y": lambda x, y: y[0] <= x[0] <= x[1] == y[1],
    "y≤x=x<y": lambda x, y: y[0] <= x[0] == x[1] < y[1],
    "y≤x=x≤y": lambda x, y: y[0] <= x[0] == x[1] <= y[1],
    "y≤x=x=y": lambda x, y: y[0] <= x[0] == x[1] == y[1],
    "y=x<x<y": lambda x, y: y[0] == x[0] < x[1] < y[1],
    "y=x<x≤y": lambda x, y: y[0] == x[0] < x[1] <= y[1],
    "y=x<x=y": lambda x, y: y[0] == x[0] < x[1] == y[1],
    "y=x≤x<y": lambda x, y: y[0] == x[0] <= x[1] < y[1],
    "y=x≤x≤y": lambda x, y: y[0] == x[0] <= x[1] <= y[1],
    "y=x≤x=y": lambda x, y: y[0] == x[0] <= x[1] == y[1],
    "y=x=x<y": lambda x, y: y[0] == x[0] == x[1] < y[1],
    "y=x=x≤y": lambda x, y: y[0] == x[0] == x[1] <= y[1],
    "y=x=x=y": lambda x, y: y[0] == x[0] == x[1] == y[1],
    "y<x<y<x": lambda x, y: y[0] < x[0] < y[1] < x[1],
    "y<x<y≤x": lambda x, y: y[0] < x[0] < y[1] <= x[1],
    "y<x<y=x": lambda x, y: y[0] < x[0] < y[1] == x[1],
    "y<x≤y<x": lambda x, y: y[0] < x[0] <= y[1] < x[1],
    "y<x≤y≤x": lambda x, y: y[0] < x[0] <= y[1] <= x[1],
    "y<x≤y=x": lambda x, y: y[0] < x[0] <= y[1] == x[1],
    "y<x=y<x": lambda x, y: y[0] < x[0] == y[1] < x[1],
    "y<x=y≤x": lambda x, y: y[0] < x[0] == y[1] <= x[1],
    "y<x=y=x": lambda x, y: y[0] < x[0] == y[1] == x[1],
    "y≤x<y<x": lambda x, y: y[0] <= x[0] < y[1] < x[1],
    "y≤x<y≤x": lambda x, y: y[0] <= x[0] < y[1] <= x[1],
    "y≤x<y=x": lambda x, y: y[0] <= x[0] < y[1] == x[1],
    "y≤x≤y<x": lambda x, y: y[0] <= x[0] <= y[1] < x[1],
    "y≤x≤y≤x": lambda x, y: y[0] <= x[0] <= y[1] <= x[1],
    "y≤x≤y=x": lambda x, y: y[0] <= x[0] <= y[1] == x[1],
    "y≤x=y<x": lambda x, y: y[0] <= x[0] == y[1] < x[1],
    "y≤x=y≤x": lambda x, y: y[0] <= x[0] == y[1] <= x[1],
    "y≤x=y=x": lambda x, y: y[0] <= x[0] == y[1] == x[1],
    "y=x<y<x": lambda x, y: y[0] == x[0] < y[1] < x[1],
    "y=x<y≤x": lambda x, y: y[0] == x[0] < y[1] <= x[1],
    "y=x<y=x": lambda x, y: y[0] == x[0] < y[1] == x[1],
    "y=x≤y<x": lambda x, y: y[0] == x[0] <= y[1] < x[1],
    "y=x≤y≤x": lambda x, y: y[0] == x[0] <= y[1] <= x[1],
    "y=x≤y=x": lambda x, y: y[0] == x[0] <= y[1] == x[1],
    "y=x=y<x": lambda x, y: y[0] == x[0] == y[1] < x[1],
    "y=x=y≤x": lambda x, y: y[0] == x[0] == y[1] <= x[1],
    "y=x=y=x": lambda x, y: y[0] == x[0] == y[1] == x[1],
    "y<y<x<x": lambda x, y: y[0] < y[1] < x[0] < x[1],
    "y<y<x≤x": lambda x, y: y[0] < y[1] < x[0] <= x[1],
    "y<y<x=x": lambda x, y: y[0] < y[1] < x[0] == x[1],
    "y<y≤x<x": lambda x, y: y[0] < y[1] <= x[0] < x[1],
    "y<y≤x≤x": lambda x, y: y[0] < y[1] <= x[0] <= x[1],
    "y<y≤x=x": lambda x, y: y[0] < y[1] <= x[0] == x[1],
    "y<y=x<x": lambda x, y: y[0] < y[1] == x[0] < x[1],
    "y<y=x≤x": lambda x, y: y[0] < y[1] == x[0] <= x[1],
    "y<y=x=x": lambda x, y: y[0] < y[1] == x[0] == x[1],
    "y≤y<x<x": lambda x, y: y[0] <= y[1] < x[0] < x[1],
    "y≤y<x≤x": lambda x, y: y[0] <= y[1] < x[0] <= x[1],
    "y≤y<x=x": lambda x, y: y[0] <= y[1] < x[0] == x[1],
    "y≤y≤x<x": lambda x, y: y[0] <= y[1] <= x[0] < x[1],
    "y≤y≤x≤x": lambda x, y: y[0] <= y[1] <= x[0] <= x[1],
    "y≤y≤x=x": lambda x, y: y[0] <= y[1] <= x[0] == x[1],
    "y≤y=x<x": lambda x, y: y[0] <= y[1] == x[0] < x[1],
    "y≤y=x≤x": lambda x, y: y[0] <= y[1] == x[0] <= x[1],
    "y≤y=x=x": lambda x, y: y[0] <= y[1] == x[0] == x[1],
    "y=y<x<x": lambda x, y: y[0] == y[1] < x[0] < x[1],
    "y=y<x≤x": lambda x, y: y[0] == y[1] < x[0] <= x[1],
    "y=y<x=x": lambda x, y: y[0] == y[1] < x[0] == x[1],
    "y=y≤x<x": lambda x, y: y[0] == y[1] <= x[0] < x[1],
    "y=y≤x≤x": lambda x, y: y[0] == y[1] <= x[0] <= x[1],
    "y=y≤x=x": lambda x, y: y[0] == y[1] <= x[0] == x[1],
    "y=y=x<x": lambda x, y: y[0] == y[1] == x[0] < x[1],
    "y=y=x≤x": lambda x, y: y[0] == y[1] == x[0] <= x[1],
    "y=y=x=x": lambda x, y: y[0] == y[1] == x[0] == x[1],
}

# The 13 Allen's interval algebra relations, with all inequalities regarded as inclusive.

compare_spans.update(
    {  #                                              Allen's symbols
        "equals": compare_spans["x=y≤x=y"],  #             =
        "starts": compare_spans["x=y≤x≤y"],  #             s
        "during": compare_spans["y≤x≤x≤y"],  #             d
        "finishes": compare_spans["y≤x≤x=y"],  #           f
        "before": compare_spans["x≤x≤y≤y"],  #             <
        "meets": compare_spans["x≤x=y≤y"],  #              m
        "overlaps": compare_spans["x≤y≤x≤y"],  #           o
        "started by": compare_spans["y=x≤y≤x"],  #         si
        "contains": compare_spans["x≤y≤y≤x"],  #           di
        "finished by": compare_spans["x≤y≤y=x"],  #        fi
        "after": compare_spans["y≤y≤x≤x"],  #              >
        "met by": compare_spans["y≤y=x≤x"],  #             mi
        "overlapped by": compare_spans["y≤x≤y≤x"],  #      oi
    }
)

# Some extra synonyms.

compare_spans.update(
    {
        "ended by": compare_spans["finished by"],
        "ends": compare_spans["finishes"],
        "equal": compare_spans["equals"],
        "in": compare_spans["during"],
        "inside": compare_spans["during"],
        "is": compare_spans["equals"],
    }
)
