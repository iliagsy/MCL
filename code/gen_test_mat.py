from numpy import *
from scipy.sparse import block_diag, find, hstack
import string


nCl = 10
coos = random.randint(1, 10, size=nCl).tolist()
lob = map(lambda n: ones((n,n)), coos)
graph = block_diag(lob)
graph_abc = vstack(find(graph)).T
with open('graph_test.abc', 'w') as fh:
    for i in range(graph_abc.shape[0]):
        ld = graph_abc[i].tolist()
        ld[0] = string.printable[int(ld[0])]
        ld[1] = string.printable[int(ld[1])]
        fh.write('%s %s %.6f\n' % tuple(ld))
