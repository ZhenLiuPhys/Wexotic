generate p p > w+ @0
add process p p > w+ j @1
output xqcut12_qcut_10_50
launch xqcut12_qcut_10_50
shower = Pythia8
analysis = OFF
set ickkw 1
set xqcut 12
set nevents 100000
# run1
set run_tag xqcut12_qcut10
set JetMatching:qCut 10
0
# run2
launch
set run_tag xqcut12_qcut15
set JetMatching:qCut 15
0
# run3
launch
set run_tag xqcut12_qcut20
set JetMatching:qCut 20
0
# run4
launch
set run_tag xqcut12_qcut25
set JetMatching:qCut 25
0
# run5
launch
set run_tag xqcut12_qcut30
set JetMatching:qCut 30
0
# run6
launch
set run_tag xqcut12_qcut40
set JetMatching:qCut 40
0
# run7
launch
set run_tag xqcut12_qcut50
set JetMatching:qCut 50
0