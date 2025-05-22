+++
date = 2025-05-19
title = 'PEG Parsing Series Overview'
toc = false
draft = false
tags = ['programming languages']
+++

*by Guido van Rossum*

My series of blog posts about PEG parsing keeps expanding. Instead of updating each part to link to all other parts, here’s the table of content:

<!--more-->

1. [PEG Parsers](/posts/peg-parsers)
2. [Building a PEG Parser](/posts/peg-building)
3. [Generating a PEG Parser](/posts/peg-generate)
4. [Visualizing PEG Parsing](/posts/peg-visualize)
5. [Left-recursive PEG Grammars](/posts/peg-left-recur)
6. Adding Actions to a PEG Grammar
7. A Meta-Grammar for PEG Parsers
8. Implementing PEG Features
9. PEG at the Core Developer Sprint ([original](https://medium.com/@gvanrossum_83706/peg-at-the-core-developer-sprint-8b23677b91e6))

A video of a talk I gave about this topic at North Bay Python is up on YouTube:<br>
[Writing a PEG parser for fun and profit](https://www.youtube.com/watch?v=QppWTvh7_sI).

![screenshot of pegen viewer](/screens/peg/screenshot.webp)

> **Update:**
> April 2, 2020. In case you are wondering what’s happening, we now have
> [PEP 617](https://www.python.org/dev/peps/pep-0617/)
> up, which proposes to replace the current parser in CPython with a PEG-based parser.

© 2019, Guido van Rossum.<br>
License for this article, the series, and the code shown:
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> [!INFO]
> Source code for the examples is at <br>
> https://github.com/we-like-parsers/pegen_experiments<br>
> where [story1/](https://github.com/we-like-parsers/pegen_experiments/tree/2210f733afd0c5450a5a5ab6412d22dccade822b/story1) has the code for
> [Part 2](/posts/peg-building) and so on.
> 
> Guido van Rossum posted this series originally
> [on Medium.com](https://medium.com/@gvanrossum_83706/peg-parsing-series-de5d41b2ed60).
> Thanks to the Creative Commons license he chose,
> I can post the series here, and also on
> [Github](https://github.com/ramalho/ramalho.org/blob/3f0aaa6ed52710a16a78c1b52598a3641249e6df/blog/content/posts/peg-series/index.md),
> using Markdown format to make it easier for anyone to share,
> so that people can learn from Guido long after Medium.com is gone.
> — *LR*
