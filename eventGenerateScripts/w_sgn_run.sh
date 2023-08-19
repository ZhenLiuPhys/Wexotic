# W+ signal generation
generate p p > w+, w+ > l+ l+ l- vl @0
add process p p > w+ j, w+ > l+ l+ l- vl @1
add process p p > w-, w- > l- l- l+ vl~ @2
add process p p > w- j, w- > l+ l- l- vl~ @3
output w_sgn

# launch the run
launch w_sgn
shower = Pythia8
detector = Delphes

# set parameters
update to_full
set run_tag w_sgn_1
set nevents 50000 # this should be modified accordingly
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

# launch the run
launch w_sgn
shower = Pythia8
detector = Delphes

# set parameters
update to_full
set run_tag w_sgn_2
set nevents 50000 # this should be modified accordingly
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

# launch the run
launch w_sgn
shower = Pythia8
detector = Delphes

# set parameters
update to_full
set run_tag w_sgn_3
set nevents 50000 # this should be modified accordingly
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

# launch the run
launch w_sgn
shower = Pythia8
detector = Delphes

# set parameters
update to_full
set run_tag w_sgn_4
set nevents 50000 # this should be modified accordingly
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

# launch the run
launch w_sgn
shower = Pythia8
detector = Delphes

# set parameters
update to_full
set run_tag w_sgn_5
set nevents 50000 # this should be modified accordingly
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

# launch the run
launch w_sgn
shower = Pythia8
detector = Delphes

# set parameters
update to_full
set run_tag w_sgn_6
set nevents 50000 # this should be modified accordingly
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