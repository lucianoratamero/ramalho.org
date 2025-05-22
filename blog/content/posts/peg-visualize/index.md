+++
date = '2019-08-11'
title = 'Visualizing PEG Parsing'
toc = false
draft = false
tags = ['programming languages']

+++

*by Guido van Rossum*

Last week I showed a simple PEG parser generator. This week I’ll show what the generated parser actually does when it’s parsing a program. I took a dive into the retro world of ASCII art, in particular a library named “curses” which is available in the Python standard library for Linux and Mac, and as an add-on for Windows.

[This is part 4 of my PEG series. See the 
[Series Overview](/posts/peg-series) for the rest.]

Let’s have a look at the visualization in progress. The screen is divided in three sections divided by that old standby of ASCII art, the line of hyphens:

* The top part shows the call stack of the parser, which as you may recall is a recursive descent parser with unlimited backtracking. I’ll explain how to read this below.

* The single-line section in the middle shows the contents of the token buffer, with a cursor pointing at the token that’s next under consideration.

* At the bottom we render the memoization cache used by the packrat parsing algorithm. Its entries are similar to some of the parser stack entries (the ones with results).

![Parsing a toy program with a toy grammar](/screens/peg/screenshot.webp)

The main thing to know to read this chart is that the indentation of lines in the top and bottom parts corresponds to the token buffer.

* The first two lines (starting with `statement` and `assignment`) represent parsing method calls that haven’t returned yet, and that were called when the token position was before the first token (`'aap'`).

* The next two lines (starting with `expr` and `term`) are aligned with the start of the token `'cat'`, which is where the corresponding parsing methods were called.

* The fifth and final line of the stack display shows an `expect('/')` call that is returning `None`. It was invoked at the position of the `'+'` token.

Indentation of items in the memoization cache also correspond to the token buffer position. For example, towards the bottom we find negative cache entries looking for the token `'if'` and the rule `if_statement` at the start of the token buffer. We also find successful cache entries for the token `'='` and for `NAME` (specifically `'cat'`) corresponding to further input positions.

In both the parser stack display and the cache display, calls that have returned are shown as `function(args) -> result`. Sometimes the parser stack shows several returned methods — I did this to reduce the “jumpiness” of the display.

(Speaking of “jumpiness”, the top of the parser stack display moves up when a call is added to the stack and it moves down when a call is popped from the stack. It seems our eyes don’t have too much of a problem following such moves— at least mine don’t. There’s probably a significant part of our brain devoted to tracking objects that move. :-)

The cache is visualized as an LRU cache, with the most recently used cache item at the top, and less used items dropping off towards the bottom of the screen. (The prototype packrat parser I showed in previous posts does not use LRU, but it would likely be a good strategy to improve its memory use.)

Let’s look at some more detail in the parsing stack display. The top four entries correspond to parsing methods that haven’t returned yet, each line showing the line from the grammar. The underlined item is the one that spawned the next call.

In this case we see that we’re on the second alternative for `statement`, namely `assignment`, and in that rule we’re on the third item, namely `expr`. In the `expr` rule we’re only at the first item of the first alternative (`term '+' expr`); and in the `term` rule we’re at the final alternative (`atom`).

Below that we see the result that caused the second alternative (`atom '/' term`) to fail: `expect('/') -> None` indented with the `'+'` token. When we move the visualization forward we’ll see it sink into the cache.

But surely you would rather see the animation for yourself! I’ve recorded the
[full parse of the canonical example program](/screens/peg/tty.gif). You can also play with the 
[code](https://github.com/we-like-parsers/pegen_experiments/tree/2210f733afd0c5450a5a5ab6412d22dccade822b/story3)
yourself, but note that this is a quick hack.

When you’re viewing the
[recorded GIF](/screens/peg/tty.gif),
it may feel a bit disorienting that sometimes the next token is not shown (e.g. at the very start, the stack grows several entries before the token `'aap'` is revealed). This is exactly what the parser sees though: the token buffer is filled lazily, and tokens are not scanned until the parser asks for them by calling `expect()`. Once the token is in the buffer, it stays there, even if the parser backtracks. Backtracking is shown by the cursor in the token buffer jumping left; the recording has numerous occurrences of this phenomenon. You can also observe cache fills in the recording, where the parser doesn’t make additional recursive calls. (I ought to highlight when this happens, but I ran out of time.)

Next week I’ll develop the parser further, probably adding my take on left recursive grammar rules. (They’re great!)

Acknowledgements: for the recording I used `ttygif` by Ilia Choly and `ttyrec` by Matthew Jording.

© 2019, Guido van Rossum.<br>
License for this article, the series, and the code shown:
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)