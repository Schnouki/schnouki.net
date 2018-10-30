---
date: "2018-10-30T11:23:00+01:00"
title: "Remove the last page of a PDF if empty"
categories:
  - Software
tags:
  - howto
  - pdf
  - LaTeX
  - makefile
---

A small but common issue… My CV is written with `\LaTeX`[^1], and in France, CVs are expected to be 1 page long (unless
you have a *lot* of experience). This can be quite challenging.

When reducing the length of my CV to 1 page, I often end with a 2-page PDF with a completely blank second page. I then
use [stapler][] to remove this empty page. But doing this every time quickly gets annoying! So I need a way to do this
automatically when I update my CV. And it needs to be smart: it must remove the second page, but *only* if it's empty,
so I can check what overflowed if there's more than one page.

I found a way to do all of this in my Makefile:

```Makefile

all: path/to/cv.pdf

%.pdf: %.tex
	latexmk -xelatex -cd $<
	if [ $$(pdfinfo $@ | awk -F: '$$1 == "Pages" {print $$2}') -gt 1 ] \
	&& [ -z "$$(pdftotext -f 2 $@ - | tr -d '[:space:]')" ]; then \
	    echo "Cutting to 1 page"; \
	    stapler cat $@ 1 $@-1page; \
	    mv $@-1page $@; \
	fi

.PHONY: clean mrproper
clean:
	find . -name '*.tex' -exec latexmk -c -cd {} \;

mrproper:
	find . -name '*.tex' -exec latexmk -C -cd {} \;
	find -type d -name auto -exec rm -rf {} +
```

This uses `stapler`, `awk`, `tr`, `pdfinfo` and `pdftotext`. On Arch Linux, you can find them with the `coreutils`,
`gawk`, `poppler` and `aur/stapler` packages.

[^1]: I mean, LaTeX, or <span class="latex">L<sup>a</sup>T<sub>e</sub>X</span>, or whatever.
[stapler]: https://github.com/hellerbarde/stapler
