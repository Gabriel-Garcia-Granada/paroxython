[
    {
        "operation": "impart",
        "data": [
            "01_hello_world.py",
            "02_input_name.py",
            "subroutine/procedure",
            "call/function",
            "flow",
        ],
    },
    {
        "operation": "exclude",
        "data": [
            "03_friends.py",
        ],
    },
    {
        "operation": "exclude",
        "data": [
            "type/number/floating_point/literal",
            ("type/sequence/tuple", "is not", "variable/assignment/parallel"),
        ],
    },
    {
        "operation": "include",
        "data": [
            "variable/assignment",
        ],
    },
    {
        "operation": "hide",
        "data": [
            "io",
        ],
    },
]
