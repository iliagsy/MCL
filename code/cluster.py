from os import system as _ss
import os

from consts import SPECIES, BASE_DIR_MCL, GRAPH_ABC

middir = BASE_DIR_MCL + '/mid'
outdir = BASE_DIR_MCL + '/out'
for dir_ in (middir, outdir):
    try:
        os.mkdir(dir_)
    except OSError:
        pass

for sp in SPECIES:
    tabfn = '{middir}/{sp}.tab'.format(middir=middir, sp=sp)
    ntvfn = '{middir}/{sp}.mci'.format(middir=middir, sp=sp)

    _ss(
        'mcxload -abc {fn} --stream-mirror -write-tab {tabfn} -o {ntvfn}'.format(
            fn=GRAPH_ABC(sp), tabfn=tabfn, ntvfn=ntvfn
        ))
    for infl in (1.4, 2., 4.):
        outfn = '{outdir}/out.{sp}.I{infl10}.mci'.format(
            outdir=outdir, sp=sp, infl10=int(infl*10)
        )
        dpfn = outfn.replace('out.', 'dump.').replace('.mci', '')

        _ss('mcl {ntvfn} -I {infl} -o {outfn}'.format(
            ntvfn=ntvfn, infl=infl, outfn=outfn
        ))
        _ss('mcxdump -icl {outfn} -tabr {tabfn} -o {dpfn}'.format(
            outfn=outfn, tabfn=tabfn, dpfn=dpfn
        ))
