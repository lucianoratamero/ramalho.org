+++
date = '2019-08-05'
title = 'Generating a PEG Parser'
toc = true
draft = false
tags = ['programming languages']
+++

*by Guido van Rossum*

Now that I’ve sketched the infrastructure for a parser and a simple hand-written parser in
[part 2](/posts/peg-building),
let’s turn to generating a parser from a grammar, as promised.
I’ll also show how to implement packrat parsing using a `@memoize` decorator.

<!--more-->

[This is part 3 of my PEG series. See the 
[Series Overview](/posts/peg-series) for the rest.]

Last time we ended with a hand-written parser.
With some limitations to the grammar, it’s easy to generate such parsers automatically from the grammar.
(We’ll lift those limitations later.)

We need two things: something that reads the grammar, constructing a data structure representing the grammar rules;
and something that takes that data structure and generates the parser.
We also need boring glue that I’ll omit.

So what we’re creating here is a simple compiler-compiler.
I’m simplifying the grammar notation a bit to the point where we just have rules and alternatives;
this is actually sufficient for the toy grammar I’ve been using in the previous parts of the series:

```
statement: assignment | expr | if_statement
expr: expr '+' term | expr '-' term | term
term: term '*' atom | term '/' atom | atom
atom: NAME | NUMBER | '(' expr ')'
assignment: target '=' expr
target: NAME
if_statement: 'if' expr ':' statement
```

Using the full notation we can write up the grammar for grammar files:

```
grammar: rule+ ENDMARKER
rule: NAME ':' alternative ('|' alternative)* NEWLINE
alternative: item+
item: NAME | STRING
```

Using a fancy word, this is our first meta-grammar (a grammar for grammars),
and our parser generator will be a meta-compiler
(a compiler is a program that translates programs from one language into another;
a meta-compiler is a compiler whose input is a grammar and whose output is a parser).

A simple way to represent the meta-grammar uses mostly built-in data types:
the right-hand-side of a rule is just a list of lists of items,
and the items can just be strings.
(Hack: we can tell `NAME` and `STRING` apart by checking whether the first character is a quote.)

For rules I am using a simple class, `Rule`, and the whole grammar is then a list of `Rule` objects.
Here’s the `Rule` class, leaving out `__repr__` and `__eq__`:

```python
class Rule:

    def __init__(self, name, alts):
        self.name = name
        self.alts = alts
```

And here’s the `GrammarParser` class that uses it
(for the `Parser` base class see my 
[previous post](/posts/peg-building)):

```python
class GrammarParser(Parser):
    def grammar(self):
        pos = self.mark()
        if rule := self.rule():
            rules = [rule]
            while rule := self.rule():
                rules.append(rule)
            if self.expect(ENDMARKER):
                return rules    # <------------- final result
        self.reset(pos)
        return None

    def rule(self):
        pos = self.mark()
        if name := self.expect(NAME):
            if self.expect(":"):
                if alt := self.alternative():
                    alts = [alt]
                    apos = self.mark()
                    while (self.expect("|")
                           and (alt := self.alternative())):
                        alts.append(alt)
                        apos = self.mark()
                    self.reset(apos)
                    if self.expect(NEWLINE):
                        return Rule(name.string, alts)
        self.reset(pos)
        return None

    def alternative(self):
        items = []
        while item := self.item():
            items.append(item)
        return items
    
    def item(self):
        if name := self.expect(NAME):
            return name.string
        if string := self.expect(STRING):
            return string.string
        return None

```

Note the use of `ENDMARKER` to make sure there isn’t anything left over after the last rule
(which there might be if there’s a typo in the grammar).
I’ve placed a primitive arrow pointing to the place where the `grammar()` method returns a list of `Rule`s.
The rest is very similar to the `ToyParser` class from the last episode,
so I won’t try to explain it.
Just observe that `item()` returns a string, `alternative()` returns a list of strings,
and the `alts` variable inside `rule()` collects a list of lists of strings.
The `rule()` method then combines the rule name (a string) and `alts` into a `Rule` object.

If we let this code loose on a file containing our toy grammar,
the `grammar()` method will return the following list of `Rule`s:

```python
[
  Rule('statement', [['assignment'], ['expr'], ['if_statement']]),
  Rule('expr', [['term', "'+'", 'expr'],
                ['term', "'-'", 'term'],
                ['term']]),
  Rule('term', [['atom', "'*'", 'term'],
                ['atom', "'/'", 'atom'],
                ['atom']]),
  Rule('atom', [['NAME'], ['NUMBER'], ["'('", 'expr', "')'"]]),
  Rule('assignment', [['target', "'='", 'expr']]),
  Rule('target', [['NAME']]),
  Rule('if_statement', [["'if'", 'expr', "':'", 'statement']]),
]
```

Now that we have the parsing part of our meta-compiler,
let’s make the code generator.
Together these form a rudimentary meta-compiler:

```python
def generate_parser_class(rules):
    print(f"class ToyParser(Parser):")
    for rule in rules:
        print()
        print(f"    @memoize")
        print(f"    def {rule.name}(self):")
        print(f"        pos = self.mark()")
        for alt in rule.alts:
            items = []
            print(f"        if (True")
            for item in alt:
                if item[0] in ('"', "'"):
                    print(f"            and self.expect({item})")
                else:
                    var = item.lower()
                    if var in items:
                        var += str(len(items))
                    items.append(var)
                    if item.isupper():
                        print("            " +
                              f"and ({var} := self.expect({item}))")
                    else:
                        print(f"            " +
                              f"and ({var} := self.{item}())")
            print(f"        ):")
            print(f"            " +
              f"return Node({rule.name!r}, [{', '.join(items)}])")
            print(f"        self.reset(pos)")
        print(f"        return None")
```

This code is pretty ugly, but it works (kind of),
and in a future episode I plan to rewrite it anyway.

A few details of the code inside the `for alt in rule.alts`
loop may require explanation: for each item in an alternative, we choose between three possibilities:

* if the item is a string literal, e.g. `'+'`, we generate `self.expect('+')`
* if the item is all upper case, e.g. NAME, we generate `(name := self.expect(NAME))`
* otherwise, e.g. if the item is `expr`, we generate `(expr := self.expr())`

If there are multiple items with the same item name in a single alternative
(e.g. `term '-' term`), we append a digit to the second one.
There’s also a small bug here which I’ll fix in a future episode.

Here’s a bit of its output (the whole class would be very boring).
Don’t worry about the odd, redundant `if (True and` … `)` idiom,
which I am using so every generated condition can start with and; Python’s bytecode compiler optimizes this out.

```python
class ToyParser(Parser):

    @memoize
    def statement(self):
        pos = self.mark()
        if (True
            and (assignment := self.assignment())
        ):
            return Node('statement', [assignment])
        self.reset(pos)
        if (True
            and (expr := self.expr())
        ):
            return Node('statement', [expr])
        self.reset(pos)
        if (True
            and (if_statement := self.if_statement())
        ):
            return Node('statement', [if_statement])
        self.reset(pos)
        return None
        
    ...
```

Note the `@memoize` decorator:
I smuggled that in so I can segue to a different topic:
using memoization to make the generated parser fast enough.

Here’s the memoize() function implementing this decorator:

```python
def memoize(func):
    def memoize_wrapper(self, *args):
        pos = self.mark()
        memo = self.memos.get(pos)
        if memo is None:
            memo = self.memos[pos] = {}
        key = (func, args)
        if key in memo:
            res, endpos = memo[key]
            self.reset(endpos)
        else:
            res = func(self, *args)
            endpos = self.mark()
            memo[key] = res, endpos
        return res
    return memoize_wrapper
```

As is typical for a decorator, it contains a nested function that
will replace (or *wrap*) the decorated function, for example the `statement()` method of the `ToyParser` class.
Because the wrapped function is a method,
the wrapper is also effectively a method:
its first argument is named `self` and refers to the `ToyParser` instance on which the decorated method is called.

The wrapper caches the result of calling the parsing method 
*at every input position* — that’s why it’s called packrat parsing!
The cache is a dict of dicts stored on the `Parser` instance.
The outer cache key is the input position;
I added `self.memos = {}` to `Parser.__init__()` to initialize it.
The inner dicts are added as needed; their keys consist of the method and its arguments.
(In the current design there are no arguments, but we could memoize `expect()`, which does have an argument,
and there’s little cost to this added generality.)

The result of a parsing method is represented as a tuple,
since parsing methods really have two results:
an explicit return value (for our generated parsers this is a `Node` representing the matched rule),
and a new input position, which we get from `self.mark()`.
After calling the parsing method, we store both its return value (`res`)
and the new input position (`endpos`) in the inner memoization dict.
Upon further calls of the same parsing method with the same arguments at the same input position,
we get both results from the cache, move the input position forward using `self.reset()`,
and return the cached return value.

It is important to cache negative results too — in fact most calls to parsing methods will be negative results.
In this case the return value is `None` and the input position is unchanged. You could add an `assert` to check this.

Note: A common memoization idiom in Python is to make the cache a local variable in the `memoize()` function.
That won’t do here: as I found out during a last-minute debug session, each `Parser`
instance *must* have its own cache.
However, you could get rid of the nested-dict design by using `(pos, func, args)` as the key.

Next week I will trace through the code to show how all this actually fits together when parsing an example program. I am still pulling my hair out over the best way to visualize how the tokenization buffer, the parser and the memoization cache work together. Maybe I’ll manage to produce animated ASCII art instead of just trace logging output.

© 2019, Guido van Rossum.<br>
License for this article, the series, and the code shown:
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)