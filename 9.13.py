from collections import OrderedDict

glossary = OrderedDict()

glossary['print'] = 'print text'
glossary['lower'] = 'make all capital letters lower letters'
glossary['for'] = 'used to iterate over lists'
glossary['if/elif'] = 'used to sort options'
glossary['range'] = 'listing a set of numbers'
glossary['set'] = 'only tracks unique terms'
glossary['{}'] = 'a dictionary'
glossary['[]'] = 'a list'
glossary['()'] = 'a tuple'
glossary['sorted'] = 'alphabetizes'

for key, value in glossary.items():
    print("\nTerm: " + key)
    print("Definition: " + value)

