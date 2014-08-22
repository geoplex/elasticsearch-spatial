# Introduction

Search has been typically poorly implemented in GIS systems. Many implementations provide interfaces to make structured queries over GIS data, but (I hope you agree) this approach has some serious limitations.

In my experience many GIS solutions do a great deal of things, some of these things they do very well and some things they do very poorly. I would hope they do the GIS bits well.

When designing a solution I rarely source all components from the same source. Search is a good example of this. A solution viewed by the end user is simply a facade over many moving parts, and each part should be selected for its ability to fulfill its respective responsibilities.

