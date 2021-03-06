class Range:
    def __init__(self, low, high):
        self._low = low
        self._high = high
    def __iter__(self):
        return self._generate()
    def _generate(self):
        i = self._low
        while i < self._high:
            yield i
            i += 1

class LetterIter:
    """An iterator over letters.

    >>> a_to_c = LetterIter('a', 'c')
    >>> next(a_to_c)
    'a'
    >>> next(a_to_c)
    'b'
    >>> next(a_to_c)
    Traceback (most recent call last):
        ...
    StopIteration
    """

    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end

    def __next__(self):
        if self.next_letter >= self.end:
            raise StopIteration
        result = self.next_letter
        self.next_letter = chr(ord(result)+1)
        return result

class Letters:
    """An implicit sequence of letters.

    >>> b_to_k = Letters('b', 'k')
    >>> first_iterator = b_to_k.__iter__()
    >>> next(first_iterator)
    'b'
    >>> next(first_iterator)
    'c'
    >>> second_iterator = iter(b_to_k)
    >>> second_iterator.__next__()
    'b'
    >>> first_iterator.__next__()
    'd'
    >>> first_iterator.__next__()
    'e'
    >>> second_iterator.__next__()
    'c'
    >>> second_iterator.__next__()
    'd'
    """

    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end

    def __iter__(self):
        return LetterIter(self.start, self.end)

def letters_generator(next_letter, end):
    """A generator function that returns an iterator over letters.

    >>> for letter in letters_generator('a', 'e'):
    ...     print(letter)
    a
    b
    c
    d
    """
    while next_letter < end:
        yield next_letter
        next_letter = chr(ord(next_letter)+1)

def fib_generator():
    """A generator function for Fibonacci numbers.

    >>> fg = fib_generator()
    >>> [(i, n) for i, n in zip(range(1, 9), fg)]
    [(1, 0), (2, 1), (3, 1), (4, 2), (5, 3), (6, 5), (7, 8), (8, 13)]
    """
    yield 0
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev+curr

def all_pairs(s):
    """Yield pairs of elements from iterable s.

    >>> list(all_pairs([1, 2, 3]))
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    """
    for item1 in s:
        for item2 in s:
            yield (item1, item2)

class LettersWithYield:
    """The Letters class implemented with a yield statement.

    >>> a_to_c = LettersWithYield('a', 'c')
    >>> list(all_pairs(a_to_c))
    [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]
    """
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end
    def __iter__(self):
        next_letter = self.start
        while next_letter < self.end:
            yield next_letter
            next_letter = chr(ord(next_letter)+1)

def powerset(s):
    """Yield all subsets of iterator t.

    >>> for s in powerset(LetterIter('a', 'd')):
    ...     print(s)
    []
    ['a']
    ['b']
    ['a', 'b']
    ['c']
    ['a', 'c']
    ['b', 'c']
    ['a', 'b', 'c']
    """
    try:
        first = next(s)
        for suffix in powerset(s):
            yield suffix
            yield [first] + suffix
    except StopIteration:
        yield []
