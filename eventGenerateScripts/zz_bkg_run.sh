# ZZ bkg
generate p p > z z, z > l+ l-, z > l+ l-
add process p p > z z j, z > l+ l-, z > l+ l-
output zz_bkg
# launch the run
launch zz_bkg
shower = Pythia8
detector = Delphes
# set parameters
update to_full
set run_tag zz_bkg
set nevents 50000
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