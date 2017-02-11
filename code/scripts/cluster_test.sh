# 文档：clmprotocols(5)

mcxload -abc graph_test.abc --stream-mirror -write-tab graph_test.tab -o graph_test.mci

# output:
# [mclIO] writing <graph_test.mci>
# .................................
# [mclIO] wrote native interchange 67x67 matrix with 493 entries to stream <graph_test.mci>
# [mclIO] wrote 67 tab entries to stream <graph_test.tab>
# [mcxload] tab has 67 entries


mcl graph_test.mci -I 1.4
mcl graph_test.mci -I 2
mcl graph_test.mci -I 4

# output:
# [mclIO] reading <graph_test.mci>
# .................................
# [mclIO] read native interchange 67x67 matrix with 493 entries
# [mcl] pid 13490
#  ite ----------------  chaos  time hom(avg,lo,hi) m-ie m-ex i-ex fmv
#   1  ................   0.00  0.00 1.00/1.00/1.00 1.00 1.00 1.00 100
# [mcl] jury pruning marks: <100,100,100>, out of 100
# [mcl] jury pruning synopsis: <100.0 or really really really good> (cf -scheme, -do log)
# [mclIO] writing <out.graph_test.mci.I14>
# ..........
# [mclIO] wrote native interchange 67x10 matrix with 67 entries to stream <out.graph_test.mci.I14>
# [mcl] 10 clusters found
# [mcl] output is in out.graph_test.mci.I14


mcxdump -icl out.graph_test.mci.I14 -tabr graph_test.tab -o dump.graph_test.mci.I14
mcxdump -icl out.graph_test.mci.I20 -tabr graph_test.tab -o dump.graph_test.mci.I20
mcxdump -icl out.graph_test.mci.I40 -tabr graph_test.tab -o dump.graph_test.mci.I40

# output:
# [mclIO] reading <out.graph_test.mci.I14>
# ..........
# [mclIO] read native interchange 67x10 matrix with 67 entries
