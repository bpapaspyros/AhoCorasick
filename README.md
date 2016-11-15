# Aho-Corasick pattern-matching algorithm implementation

#### Included source files

- AhoCorasick.py
- testCall.py

#### Summary

In this repository you will find a pattern-matching implementation as explained in [Efficient String Matching: An Aid to Bibliographic Search](http://cr.yp.to/bib/1975/aho.pdf). testCall.py containts a sample call and run of the algorithm (e.g `./testCall.py`).

* Tested on python2.7 and python3.5

#### Use AhoCorasick in other projects

```python
from AhoCorasick import AhoCorasick
                    ...
    patterns = ... # comma separated, no spaces (unless part of text)
    text     = ...
                    ...
    ac = AhoCorasick(paterns, text)
    ac.run()
    ac.printResults()
                    ...
```

### MIT License

Copyright (c) 2016 Vaios Papaspyros

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
