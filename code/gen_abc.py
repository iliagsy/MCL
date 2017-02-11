from numpy import *
from scipy.sparse import csr_matrix, find, hstack

from consts import SPECIES, FINAL_GRAPH, GRAPH_ABC


def gen_abc_graph(species, savefn=None):
    graph = csr_matrix(abs(FINAL_GRAPH(species)))
    graph_abc = vstack(find(graph)).T
    if savefn:
        with open(savefn, 'w') as fh:
            for i in range(graph_abc.shape[0]):
                ld = graph_abc[i].tolist()
                fh.write('%d %d %f\n' % tuple(ld))
    return graph_abc


if __name__ == '__main__':
    for sp in SPECIES:
        gen_abc_graph(sp, savefn=GRAPH_ABC(sp))
