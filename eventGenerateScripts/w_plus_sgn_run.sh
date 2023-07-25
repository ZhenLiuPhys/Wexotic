# W+ signal generation
generate p p > w+, w+ > l+ l+ l- vl @0
add process p p > w+ j, w+ > l+ l+ l- vl @1
output w_plus_sgn

# launch the run
launch w_plus_sgn
shower = Pythia8
detector = Delphes
analysis = ExRoot

# set parameters
update to_full
set run_tag w_plus_sgn
set nevents 20000 # this should be modified accordingly
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug

# set cuts
set ptj 20
set ptl 10
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 12
set JetMatching:qCut 20
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl


# W- signal generation
generate p p > w-, w- > l+ l+ l- vl @0
add process p p > w- j, w- > l+ l+ l- vl @1
output w_minus_signal

# launch the run
launch w_minus_signal
shower = Pythia8
detector = Delphes
analysis = ExRoot

# set parameters
update to_full
set run_tag signal1
set nevents 20000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug

# set cuts
set ptj 20
set ptl 10
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl