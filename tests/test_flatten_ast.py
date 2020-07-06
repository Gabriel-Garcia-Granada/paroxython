import pytest
import regex
from typed_ast import ast3 as ast

import context
from paroxython.flatten_ast import flatten_ast, pseudo_hash

sources = r"""
<<< Examples of _type, _length, _pos and _hash (full output)
42
---
/_type=Module # Any node has a type, stored under _type
/body/_length=1 # Any sequence has a length, stored under _length
/body/1/_type=Expr # The first line of a body is numbered 1
/body/1/_pos=1:1- # _pos consists in the line number, followed by the path from the AST root
/body/1/value/_type=Num
/body/1/value/_hash=0x0001 # Each expression has a unique identifier, stored in _hash
/body/1/value/_pos=1:1-0-
/body/1/value/n=42
/type_ignores/_length=0
>>>

<<< Example of function
def foo():
    bar()
    buz()
---
/body/1/_type=FunctionDef
/body/1/_pos=1:1-
/body/1/name=foo
/body/1/args/_type=arguments
/body/1/args/args/_length=0
/body/1/args/vararg=None
/body/1/args/kwonlyargs/_length=0
/body/1/args/kw_defaults/_length=0
/body/1/args/kwarg=None
/body/1/args/defaults/_length=0
/body/1/decorator_list/_length=0 # moved before the body of the function
/body/1/returns=None # moved before the body of the function
/body/1/type_comment=None
/body/1/body/_length=2 # start of the body of the function
>>>

<<< Example of conditional else
if c:
    pass
else:
    pass
---
/body/1/_type=If
/body/1/_pos=1:1-
/body/1/test/_type=Name
/body/1/test/_hash=0x0001
/body/1/test/_pos=1:1-0-
/body/1/test/id=c
/body/1/test/ctx/_type=Load
/body/1/body/_length=1
/body/1/body/1/_type=Pass
/body/1/body/1/_pos=2:1-1-1-
/body/1/orelse/_length=1
/body/1/orelse/1/_type=Pass
/body/1/orelse/1/_pos=4:1-2-1-
>>>

<<< Example of loop else
while c:
    pass
else:
    pass
---
/body/1/_type=While
/body/1/_pos=1:1-
/body/1/test/_type=Name
/body/1/test/_hash=0x0001
/body/1/test/_pos=1:1-0-
/body/1/test/id=c
/body/1/test/ctx/_type=Load
/body/1/body/_length=1
/body/1/body/1/_type=Pass
/body/1/body/1/_pos=2:1-1-1-
/body/1/loopelse/_length=1 # renamed from "orelse" to "loopelse"
/body/1/loopelse/1/_type=Pass
/body/1/loopelse/1/_pos=4:1-2-1-
>>>

<<< Example of assignement
a = 1
---
/body/1/_type=Assign
/body/1/_pos=1:1-
/body/1/assigntargets/_length=1 # renamed from "targets" to "assigntargets"
/body/1/assigntargets/1/_type=Name
/body/1/assigntargets/1/_hash=0x0001
/body/1/assigntargets/1/_pos=1:1-0-1-
/body/1/assigntargets/1/id=a
/body/1/assigntargets/1/ctx/_type=Store
/body/1/assignvalue/_type=Num # renamed from "value" to "assignvalue"
/body/1/assignvalue/_hash=0x0002
/body/1/assignvalue/_pos=1:1-1-
/body/1/assignvalue/n=1
>>>

<<< Example of augmented assignement
a += 1
---
/body/1/_type=AugAssign
/body/1/_pos=1:1-
/body/1/assigntarget/_type=Name # renamed from "target" to "assigntarget"
/body/1/assigntarget/_hash=0x0001
/body/1/assigntarget/_pos=1:1-0-
/body/1/assigntarget/id=a
/body/1/assigntarget/ctx/_type=Store
/body/1/op/_type=Add
/body/1/assignvalue/_type=Num # renamed from "value" to "assignvalue"
/body/1/assignvalue/_hash=0x0002
/body/1/assignvalue/_pos=1:1-2-
/body/1/assignvalue/n=1
>>>

<<< Example of deletion
del a
---
/body/1/_type=Delete
/body/1/_pos=1:1-
/body/1/targets/_length=1 # note the use of "targets"
/body/1/targets/1/_type=Name
/body/1/targets/1/_hash=0x0001
/body/1/targets/1/_pos=1:1-0-1-
/body/1/targets/1/id=a
/body/1/targets/1/ctx/_type=Del
>>>

<<< Example of comprehension
[x for x in s]
---
/body/1/value/_type=ListComp # note the use of "value"
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/elt/_type=Name
/body/1/value/elt/_hash=0x0002
/body/1/value/elt/_pos=1:1-0-0-
/body/1/value/elt/id=x
/body/1/value/elt/ctx/_type=Load
/body/1/value/generators/_length=1
/body/1/value/generators/1/_type=comprehension
/body/1/value/generators/1/target/_type=Name # note the use of "target"
/body/1/value/generators/1/target/_hash=0x0002
/body/1/value/generators/1/target/_pos=1:1-0-1-1-0-
/body/1/value/generators/1/target/id=x
/body/1/value/generators/1/target/ctx/_type=Store
>>>

<<< Examples of importation
from m import f1
from . import f2
---
/body/1/_type=ImportFrom
/body/1/_pos=1:1-
/body/1/module=m # no quotes
/body/1/names/_length=1
/body/1/names/1/_type=alias
/body/1/names/1/name=f1
/body/1/names/1/asname=None
/body/1/level=0
/body/2/_type=ImportFrom
/body/2/_pos=2:2-
/body/2/module=None # no problem, since "from None import f" would raise a syntax error
/body/2/names/_length=1
/body/2/names/1/_type=alias
/body/2/names/1/name=f2
/body/2/names/1/asname=None
/body/2/level=1
>>>

<<< Examples of strings
"hello world"
""
"\n"
---
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=Str
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/s=hello world # stripped from its quote delimiters
/body/1/value/kind=
/body/2/_type=Expr
/body/2/_pos=2:2-
/body/2/value/_type=Str
/body/2/value/_hash=0x0002
/body/2/value/_pos=2:2-0-
/body/2/value/s= # an empty string is followed by an \n
/body/2/value/kind=
/body/3/_type=Expr
/body/3/_pos=3:3-
/body/3/value/_type=Str
/body/3/value/_hash=0x0003
/body/3/value/_pos=3:3-0-
/body/3/value/s=\n # which is distinct from the string "\n"
/body/3/value/kind=
>>>

<<< Examples of function call (full output)
print("hello, world")
---
/_type=Module
/body/_length=1
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=Call
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/func/_type=Name
/body/1/value/func/_hash=0x0002
/body/1/value/func/_pos=1:1-0-0-
/body/1/value/func/id=print
/body/1/value/func/ctx/_type=Load
/body/1/value/args/_length=1
/body/1/value/args/1/_type=Str
/body/1/value/args/1/_hash=0x0003
/body/1/value/args/1/_pos=1:1-0-1-1-
/body/1/value/args/1/s=hello, world
/body/1/value/args/1/kind=
/body/1/value/keywords/_length=0
/type_ignores/_length=0
>>>

<<< Example of negative literal
-42
---
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=Num
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/n=-42
>>>

<<< Example of complete program (full output)
def fibonacci(n):
    result = []
    (a, b) = (0, 1)
    while a < n:
        result.append(a)
        (a, b) = (b, a + b)
    return result
---
/_type=Module
/body/_length=1
/body/1/_type=FunctionDef
/body/1/_pos=1:1-
/body/1/name=fibonacci
/body/1/args/_type=arguments
/body/1/args/args/_length=1
/body/1/args/args/1/_type=arg
/body/1/args/args/1/_pos=1:1-1-0-1-
/body/1/args/args/1/arg=n
/body/1/args/args/1/annotation=None
/body/1/args/args/1/type_comment=None
/body/1/args/vararg=None
/body/1/args/kwonlyargs/_length=0
/body/1/args/kw_defaults/_length=0
/body/1/args/kwarg=None
/body/1/args/defaults/_length=0
/body/1/decorator_list/_length=0
/body/1/returns=None
/body/1/type_comment=None
/body/1/body/_length=4
/body/1/body/1/_type=Assign
/body/1/body/1/_pos=2:1-5-1-
/body/1/body/1/assigntargets/_length=1
/body/1/body/1/assigntargets/1/_type=Name
/body/1/body/1/assigntargets/1/_hash=0x0001
/body/1/body/1/assigntargets/1/_pos=2:1-5-1-0-1-
/body/1/body/1/assigntargets/1/id=result
/body/1/body/1/assigntargets/1/ctx/_type=Store
/body/1/body/1/assignvalue/_type=List
/body/1/body/1/assignvalue/_hash=0x0002
/body/1/body/1/assignvalue/_pos=2:1-5-1-1-
/body/1/body/1/assignvalue/elts/_length=0
/body/1/body/1/assignvalue/ctx/_type=Load
/body/1/body/1/type_comment=None
/body/1/body/2/_type=Assign
/body/1/body/2/_pos=3:1-5-2-
/body/1/body/2/assigntargets/_length=1
/body/1/body/2/assigntargets/1/_type=Tuple
/body/1/body/2/assigntargets/1/_hash=0x0003
/body/1/body/2/assigntargets/1/_pos=3:1-5-2-0-1-
/body/1/body/2/assigntargets/1/elts/_length=2
/body/1/body/2/assigntargets/1/elts/1/_type=Name
/body/1/body/2/assigntargets/1/elts/1/_hash=0x0004
/body/1/body/2/assigntargets/1/elts/1/_pos=3:1-5-2-0-1-0-1-
/body/1/body/2/assigntargets/1/elts/1/id=a
/body/1/body/2/assigntargets/1/elts/1/ctx/_type=Store
/body/1/body/2/assigntargets/1/elts/2/_type=Name
/body/1/body/2/assigntargets/1/elts/2/_hash=0x0005
/body/1/body/2/assigntargets/1/elts/2/_pos=3:1-5-2-0-1-0-2-
/body/1/body/2/assigntargets/1/elts/2/id=b
/body/1/body/2/assigntargets/1/elts/2/ctx/_type=Store
/body/1/body/2/assigntargets/1/ctx/_type=Store
/body/1/body/2/assignvalue/_type=Tuple
/body/1/body/2/assignvalue/_hash=0x0006
/body/1/body/2/assignvalue/_pos=3:1-5-2-1-
/body/1/body/2/assignvalue/elts/_length=2
/body/1/body/2/assignvalue/elts/1/_type=Num
/body/1/body/2/assignvalue/elts/1/_hash=0x0007
/body/1/body/2/assignvalue/elts/1/_pos=3:1-5-2-1-0-1-
/body/1/body/2/assignvalue/elts/1/n=0
/body/1/body/2/assignvalue/elts/2/_type=Num
/body/1/body/2/assignvalue/elts/2/_hash=0x0008
/body/1/body/2/assignvalue/elts/2/_pos=3:1-5-2-1-0-2-
/body/1/body/2/assignvalue/elts/2/n=1
/body/1/body/2/assignvalue/ctx/_type=Load
/body/1/body/2/type_comment=None
/body/1/body/3/_type=While
/body/1/body/3/_pos=4:1-5-3-
/body/1/body/3/test/_type=Compare
/body/1/body/3/test/_hash=0x0009
/body/1/body/3/test/_pos=4:1-5-3-0-
/body/1/body/3/test/left/_type=Name
/body/1/body/3/test/left/_hash=0x0004
/body/1/body/3/test/left/_pos=4:1-5-3-0-0-
/body/1/body/3/test/left/id=a
/body/1/body/3/test/left/ctx/_type=Load
/body/1/body/3/test/ops/_length=1
/body/1/body/3/test/ops/1/_type=Lt
/body/1/body/3/test/comparators/_length=1
/body/1/body/3/test/comparators/1/_type=Name
/body/1/body/3/test/comparators/1/_hash=0x000a
/body/1/body/3/test/comparators/1/_pos=4:1-5-3-0-2-1-
/body/1/body/3/test/comparators/1/id=n
/body/1/body/3/test/comparators/1/ctx/_type=Load
/body/1/body/3/body/_length=2
/body/1/body/3/body/1/_type=Expr
/body/1/body/3/body/1/_pos=5:1-5-3-1-1-
/body/1/body/3/body/1/value/_type=Call
/body/1/body/3/body/1/value/_hash=0x000b
/body/1/body/3/body/1/value/_pos=5:1-5-3-1-1-0-
/body/1/body/3/body/1/value/func/_type=Attribute
/body/1/body/3/body/1/value/func/_hash=0x000c
/body/1/body/3/body/1/value/func/_pos=5:1-5-3-1-1-0-0-
/body/1/body/3/body/1/value/func/value/_type=Name
/body/1/body/3/body/1/value/func/value/_hash=0x0001
/body/1/body/3/body/1/value/func/value/_pos=5:1-5-3-1-1-0-0-0-
/body/1/body/3/body/1/value/func/value/id=result
/body/1/body/3/body/1/value/func/value/ctx/_type=Load
/body/1/body/3/body/1/value/func/attr=append
/body/1/body/3/body/1/value/func/ctx/_type=Load
/body/1/body/3/body/1/value/args/_length=1
/body/1/body/3/body/1/value/args/1/_type=Name
/body/1/body/3/body/1/value/args/1/_hash=0x0004
/body/1/body/3/body/1/value/args/1/_pos=5:1-5-3-1-1-0-1-1-
/body/1/body/3/body/1/value/args/1/id=a
/body/1/body/3/body/1/value/args/1/ctx/_type=Load
/body/1/body/3/body/1/value/keywords/_length=0
/body/1/body/3/body/2/_type=Assign
/body/1/body/3/body/2/_pos=6:1-5-3-1-2-
/body/1/body/3/body/2/assigntargets/_length=1
/body/1/body/3/body/2/assigntargets/1/_type=Tuple
/body/1/body/3/body/2/assigntargets/1/_hash=0x0003
/body/1/body/3/body/2/assigntargets/1/_pos=6:1-5-3-1-2-0-1-
/body/1/body/3/body/2/assigntargets/1/elts/_length=2
/body/1/body/3/body/2/assigntargets/1/elts/1/_type=Name
/body/1/body/3/body/2/assigntargets/1/elts/1/_hash=0x0004
/body/1/body/3/body/2/assigntargets/1/elts/1/_pos=6:1-5-3-1-2-0-1-0-1-
/body/1/body/3/body/2/assigntargets/1/elts/1/id=a
/body/1/body/3/body/2/assigntargets/1/elts/1/ctx/_type=Store
/body/1/body/3/body/2/assigntargets/1/elts/2/_type=Name
/body/1/body/3/body/2/assigntargets/1/elts/2/_hash=0x0005
/body/1/body/3/body/2/assigntargets/1/elts/2/_pos=6:1-5-3-1-2-0-1-0-2-
/body/1/body/3/body/2/assigntargets/1/elts/2/id=b
/body/1/body/3/body/2/assigntargets/1/elts/2/ctx/_type=Store
/body/1/body/3/body/2/assigntargets/1/ctx/_type=Store
/body/1/body/3/body/2/assignvalue/_type=Tuple
/body/1/body/3/body/2/assignvalue/_hash=0x000d
/body/1/body/3/body/2/assignvalue/_pos=6:1-5-3-1-2-1-
/body/1/body/3/body/2/assignvalue/elts/_length=2
/body/1/body/3/body/2/assignvalue/elts/1/_type=Name
/body/1/body/3/body/2/assignvalue/elts/1/_hash=0x0005
/body/1/body/3/body/2/assignvalue/elts/1/_pos=6:1-5-3-1-2-1-0-1-
/body/1/body/3/body/2/assignvalue/elts/1/id=b
/body/1/body/3/body/2/assignvalue/elts/1/ctx/_type=Load
/body/1/body/3/body/2/assignvalue/elts/2/_type=BinOp
/body/1/body/3/body/2/assignvalue/elts/2/_hash=0x000e
/body/1/body/3/body/2/assignvalue/elts/2/_pos=6:1-5-3-1-2-1-0-2-
/body/1/body/3/body/2/assignvalue/elts/2/left/_type=Name
/body/1/body/3/body/2/assignvalue/elts/2/left/_hash=0x0004
/body/1/body/3/body/2/assignvalue/elts/2/left/_pos=6:1-5-3-1-2-1-0-2-0-
/body/1/body/3/body/2/assignvalue/elts/2/left/id=a
/body/1/body/3/body/2/assignvalue/elts/2/left/ctx/_type=Load
/body/1/body/3/body/2/assignvalue/elts/2/op/_type=Add
/body/1/body/3/body/2/assignvalue/elts/2/right/_type=Name
/body/1/body/3/body/2/assignvalue/elts/2/right/_hash=0x0005
/body/1/body/3/body/2/assignvalue/elts/2/right/_pos=6:1-5-3-1-2-1-0-2-2-
/body/1/body/3/body/2/assignvalue/elts/2/right/id=b
/body/1/body/3/body/2/assignvalue/elts/2/right/ctx/_type=Load
/body/1/body/3/body/2/assignvalue/ctx/_type=Load
/body/1/body/3/body/2/type_comment=None
/body/1/body/3/loopelse/_length=0
/body/1/body/4/_type=Return
/body/1/body/4/_pos=7:1-5-4-
/body/1/body/4/value/_type=Name
/body/1/body/4/value/_hash=0x0001
/body/1/body/4/value/_pos=7:1-5-4-0-
/body/1/body/4/value/id=result
/body/1/body/4/value/ctx/_type=Load
/type_ignores/_length=0
>>>
"""
source_rex = regex.compile(r"(?ms)^<<< ([^\n]+)\n(.+?)\n---\n(.*?)\n>>>")
examples = [m for m in source_rex.findall(sources)]


@pytest.mark.parametrize("title, source, expected", examples)
def test_flatten_ast(title, source, expected):
    expected = regex.sub(r" +# .+", "", expected)
    pseudo_hash.reset()
    print(title)
    print("-" * len(title))
    result = flatten_ast(ast.parse(source)).strip()
    print(result)
    assert expected in result


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
