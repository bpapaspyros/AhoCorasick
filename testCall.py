#!/usr/bin/env python
from AhoCorasick import AhoCorasick

# sample AhoCorasick call
patterns = 'GAATG,CTA,CCGT,AC,ATG,TGTOC'.split(',')
text = 'CTAATGTTGAATGGCCACTACCGTGAATGCCGTGTGAATGCTA'

ac = AhoCorasick(patterns, text)
ac.run()
ac.printResults()
