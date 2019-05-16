---
date: "2019-05-16T22:48:10+02:00"
title: "Python, debugging, print, and context managers"
categories:
  - Software
tags:
  - python
  - python3
  - debug
  - programming
---

I've been recently working on some big changes to a big module in a big Python application. For this precise module,
there are 1019 unit tests, most of them auto-generated from a few (big) data files. The tests are run using [pytest][],
and usually take about 7 seconds to run on my laptop.

My changes caused a single test to fail. One out of 1019. Yay? Well, time to debug that: let's add some `print()` in a
few functions, and run just that test using `pytest path/to/file.py -k test_name`... And now it takes 35 seconds to run,
and prints thouands and thousands of messages. WTF? Well, turns out that one of the functions in which I added `print()`
is used to parse the data files during the collection phase, so all my `print()`s are called many, many, many times...

A perfect solution to this would be to have something that works just like `print()`, but actually does nothing most of
the time, and only does when it's explicitely enabled. And that's actually pretty easy to do in Python using a context
manager :slightly_smiling_face:

Without further ado, here it is:

{{< code "boom.py" py >}}

That's it. No dependency, less than 20 lines of code, works with Python 2 and 3. Just copy-paste it in any of your
files. Then, instead of using `print()`, use `boom()`. And when you want to enable printing with `boom`, just use it as
a context manager:

```python
def foo(arg):
   boom(arg)

foo("not displayed")
foo("still not displayed")
with boom:
    foo("this is displayed!")
```

For extra fun, I added a calls counter. Know I know that in my case, collecting the test cases + running a single tests
caused `boom()` to be called 1,125,545 times :sweat_smile:
