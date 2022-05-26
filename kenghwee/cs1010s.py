from clrprint import *
from random import choice

txt, color = choice([
    ['https://github.com/cs1010s', 'y'],
    ["""Traceback (most recent call last):\n  File "<pyshell#0>", line 1, in <module>\n    from kenghwee import cs1010s\nImportError: cannot import name 'cs1010s' from 'kenghwee'""", 'r'],
    ["""Traceback (most recent call last):\n  File "<pyshell#0>", line 1, in <module>\n    import kenghwee.cs1010s\nModuleNotFoundError: No module named 'kenghwee.cs1010s'""", 'r'],
    ["""Traceback (most recent call last):\n  File "<pyshell#1>", line 1, in <module>\n    print('Keng Hwee is the best!')\n  File "<pyshell#0>", line 2, in print\n    print('Keng Hwee is the best!')\n  File "<pyshell#0>", line 2, in print\n    print('Keng Hwee is the best!')\n  File "<pyshell#0>", line 2, in print\n    print('Keng Hwee is the best!')\n  [Previous line repeated 1022 more times]\nRecursionError: maximum recursion depth exceeded""", 'r']
])

clrprint(txt, clr=color)