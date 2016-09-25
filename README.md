# dux

This is my implementation of Redux in Python. There are many like it, but this
one is mine.

I wrote it primarily to better understand<super>†</super> Redux but I also plan
to experiment with ideas from other projects (of mine and others) which have
some conceptual overlap with Redux, for example
[Rev](https://github.com/jtauber/Rev).

Thanks to Flora Worley for getting my excited about Redux in the first place.


## Core implementation

Everything is pretty much just in `dux.py`.

There is also a `utils.py` with some helper functions for pure list
manipulations used so far (although you can just inline similar code in your
reducers if you want and I'm thinking of eliminating the module in favour of
documentation tips).


## Examples from egghead.io video series

The implementation and the usage examples so far are mostly based on [Dan
Abramov's video series](https://egghead.io/series/getting-started-with-redux).

See `egghead_examples/` for the code. Note these should be run with
`python -m`, e.g.

```
python -m egghead_examples.example3
```

## Examples from Redux docs

`redux_docs_basic_example/` contains a port of code from the
[Basics]((http://redux.js.org/docs/basics/)) section of the official Redux
docs. It doesn't really make sense to run because it's missing any of the
UI pieces but still might be useful to look at.


---
<super>†</super> what I cannot implement in Python, I do not understand
