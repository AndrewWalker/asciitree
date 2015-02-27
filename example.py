from asciitree import ascii_tree
from collections import OrderedDict as OD
from copy import deepcopy


# a basic tree
# OrderedDict is used in some places where node order is important, otherwise
# a normal dict is used for the sake of readabilitiy
tree = {
    'asciitree': OD([
        ('sometimes',
            {'you': {}}),
        ('just',
            {'want': OD([
                ('to', {}),
                ('draw', {}),
            ])}),
        ('trees', {}),
        ('in', {
            'your': {
                'terminal': {}
            }
        })
    ])
}

print ascii_tree(tree)
print


# construct a more complex tree by copying the tree and grafting it onto itself
tree2 = deepcopy(tree)
tree2['asciitree']['trees'] = deepcopy(tree2['asciitree'])

print ascii_tree(tree2)