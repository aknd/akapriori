# AKApriori
Python implementation of the Apriori Algorithm.

## Installation
    $ pip install akapriori

## Usage

```python
from akapriori import apriori

transactions = [
    ("apricot", "apple", "cherry", "plum", "banana"),
    ("strawberry", "plum", "cherry"),
    ("persimmon", "peach", "banana", "apple"),
    ("kiwi fruit", "apple", "pear"),
    ("cherry", "pear", "banana"),
    ("watermelon", "apple"),
    ("plum", "banana"),
    ("pear", "peach", "cherry", "banana", "apricot"),
    ("pineapple", "apple", "plum"),
    ("banana", "plum", "peach"),
    ("grape", "cherry"),
    ("mandarin", "plum"),
    ("melon", "apple", "persimmon", "plum"),
    ("peach", "cherry", "apple"),
    ("apple", "mandarin", "plum", "persimmon"),
]
```
If you want to extract rules that satisfy "support >= 0.05 and confidence >= 0.3 and lift > 2", implement as follows.
```python
rules = apriori(transactions, support=0.05, confidence=0.3, lift=2)
rules_sorted = sorted(rules, key=lambda x: (x[4], x[3], x[2]), reverse=True) # ORDER BY lift DESC, confidence DESC, support DESC

for r in rules_sorted:
    print(r)
```
```
(frozenset(['kiwi fruit']), frozenset(['pear']), 0.06666666666666667, 1.0, 5.0)
(frozenset(['melon']), frozenset(['persimmon']), 0.06666666666666667, 1.0, 5.0)
(frozenset(['pear']), frozenset(['kiwi fruit']), 0.06666666666666667, 0.3333333333333333, 5.0)
(frozenset(['persimmon']), frozenset(['melon']), 0.06666666666666667, 0.3333333333333333, 5.0)
(frozenset(['apricot']), frozenset(['banana']), 0.13333333333333333, 1.0, 2.5)
(frozenset(['apricot']), frozenset(['cherry']), 0.13333333333333333, 1.0, 2.5)
(frozenset(['grape']), frozenset(['cherry']), 0.06666666666666667, 1.0, 2.5)
(frozenset(['strawberry']), frozenset(['cherry']), 0.06666666666666667, 1.0, 2.5)
(frozenset(['apricot']), frozenset(['pear']), 0.06666666666666667, 0.5, 2.5)
(frozenset(['mandarin']), frozenset(['persimmon']), 0.06666666666666667, 0.5, 2.5)
(frozenset(['banana']), frozenset(['apricot']), 0.13333333333333333, 0.3333333333333333, 2.5)
(frozenset(['cherry']), frozenset(['apricot']), 0.13333333333333333, 0.3333333333333333, 2.5)
(frozenset(['pear']), frozenset(['apricot']), 0.06666666666666667, 0.3333333333333333, 2.5)
(frozenset(['persimmon']), frozenset(['mandarin']), 0.06666666666666667, 0.3333333333333333, 2.5)
```
