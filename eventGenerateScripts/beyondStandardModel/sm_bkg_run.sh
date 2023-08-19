import model sm-full
generate p p > w+, w+ > l+ l- l+ vl
add process p p > w+ j, w+ > l+ l- l+ vl
add process p p > w-, w- > l+ l- l- vl~
add process p p > w- j, w- > l+ l- l- vl~
add process p p > w+, w+ > ta+ ta- l+ vl
add process p p > w+ j, w+ > ta+ ta- l+ vl
add process p p > w-, w- > ta+ ta- l- vl~
add process p p > w- j, w- > ta+ ta- l- vl~
add process p p > w+, w+ > l+ l- ta+ vt
add process p p > w+ j, w+ > l+ l- ta+ vt
add process p p > w-, w- > l+ l- ta- vt~
add process p p > w- j, w- > l+ l- ta- vt~
add process p p > w+, w+ > ta+ ta- ta+ vt
add process p p > w+ j, w+ > ta+ ta- ta+ vt
add process p p > w-, w- > ta+ ta- ta- vt~
add process p p > w- j, w- > ta+ ta- ta- vt~
output sm_bkg

# launch the run
launch sm_bkg -n sm_bkg
shower = Pythia8
detector = Delphes
analysis = ExRoot

# set parameters
update to_full
set run_tag sm_bkg
set nevents 100000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False 

# set cuts
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
set JetMatching:qCut -1
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

