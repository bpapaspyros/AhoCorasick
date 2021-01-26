# MIT License
#
# Copyright (c) 2016 Vaios Papaspyros
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math

class AhoCorasick:
    # initialize class vars
    def __init__(self, patterns, text):
        self.patterns = patterns
        self.text = text
        self.g = {}
        self.f = {}
        self.output = {}
        self.occurences = {}
        self.comparisons = 0
        self.skipcount = 0

    # run the algorithm in steps
    def run(self):
        self._goto(self.patterns)
        self._failure()
        self._match()

    # actual searching/matching
    def _match(self):
        state = 0
        for i in range(len(self.text)):
            while not (state, self.text[i]) in self.g:
                state = self.f[state]
                self.comparisons += 1 # updating the comparison counter
                self.skipcount += 1   # updating the skip count counter

            state = self.g[state, self.text[i]]
            if state in self.output:
                l = list(self.output[state])
                for p in l:
                    self.occurences[p] += 1 # updating the occurrence counter

            self.comparisons += 1 # updating the comparison counter

    # builds the "tree" for the given patterns
    def _goto(self, patterns):
        newstate = 0
        for pattern in patterns:
            state = 0
            j = 0

            # walking an existing path
            while j<len(pattern) and (state, pattern[j]) in self.g.keys():
                state = self.g[(state, pattern[j])]
                j += 1

            # creating the necessary new nodes
            for p in range(j, len(pattern)):
                newstate += 1
                self.g[(state, pattern[p])] = newstate
                state = newstate

            # set the last state as an output
            self.output[state] = [str(pattern)]

            # initializing the occurrence dictionary for later use
            self.occurences[pattern] = 0

        # when in state 0 every non existent transition returns to 0
        for pattern in patterns:
            for p in range(len(pattern)):
                if not (0, pattern[p]) in self.g:
                    self.g[(0, pattern[p])] = 0

    # builds the failure transitions
    def _failure(self):
        queue = []

        # initialize the failure list with the depth 1 nodes
        for k, v in self.g.items():
            if (0, k[1]) in self.g and self.g[(0, k[1])] == v and v != 0:
                queue.append(v)
                self.f[v] = 0

        # filling in the rest of the transitions on level at a time
        while queue:
            r = queue.pop(0)
            for k, v in self.g.items():
                if ((r, k[1]) in self.g) and (self.g[(r, k[1])] != v):
                    s = self.g[(r, k[1])]
                    queue.append(s)
                    state = self.f[r]

                    # fall back to a valid node
                    while (state, k[1]) not in self.g:
                        state = self.f[state]
                    self.f[s] = self.g[(state, k[1])]

                    # update the output dictionary removing duplicates
                    if s and self.f[s] in self.output:
                            self.output[s] += self.output[self.f[s]]
                            self.output[s] = list(set(self.output[s]))

    def getPatternOccurences(self):
        return self.occurences

    def getComparisons(self):
        return self.comparisons

    def printResults(self):
        print('\n')
        print('- Patterns inputed   : ' + str(self.patterns))
        print('- Text inputed       : ' + str(self.text))
        print('\n\t ---------------------- \n')
        print('- Skip count         : ' + str(self.skipcount))
        print('- Comparisons counted: ' + str(self.comparisons))
        print('- Pattern occurrences : ' + str(self.occurences))
        print('\n')
