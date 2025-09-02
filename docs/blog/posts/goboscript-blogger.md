---
date: 2025-07-26
authors:
    - faretek1
---

# What is goboscript actually useful for?
Perhaps i would say that the reason why i use goboscript (gs) is because the scratch editor was lagging too much. But there are a couple of other things that are really nice about goboscript.

- abstractions like functions, macros and structs
- git(hub)
- being able to handle tons of variables/lists without the block palette becoming clogged

But perhaps my favourite feature of them all, is the  %include <path> statement.

This is because it opens up the door for library development in scratch. Library development in scratch would allow you to use other people's code easier. And being able to use other people's code without having to drag-and-drop out of your backpack is a wonder for the soul.

Just a simple  %include <path> statement is all you need.

And of course, this is not limited to other people's code. The  %include statement simple copy-pastes another goboscript file into another within the preprocessing for compilation. 

- For example, the goboscript standard library's testing script makes use of   %include to separate testing scripts for different submodules into different files. i.e., the `math.gs` module is tested by the `test/lib/test_math.gs` instead of being bundled with other testing scripts, like `test/lib/test_string.gs`.

holy yap