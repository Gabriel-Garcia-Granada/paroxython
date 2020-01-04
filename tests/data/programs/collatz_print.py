def print_collatz(n):  # paroxython: added_block_label...
    while n != 1:
        print(n)
        if n % 2 == 0:  # paroxython: added_label_on_line_4
            n = n // 2  # paroxython: -literal:Num -binary_operator:FloorDiv
        else:  # paroxython: if
            n = 3 * n + 1
    print(n)  # paroxython: ...added_block_label