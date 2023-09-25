# WZ bkg
import model sm-full
generate p p > w+ z , w+ > l+ vl , z > l+ l-
add process p p > w+ z j , w+ > l+ vl , z > l+ l-
add process p p > w- z , w- > l- vl~ , z > l+ l-
add process p p > w- z j , w- > l- vl~ , z > l+ l-
add process p p > w+ z, w+ > ta+ vt, z > l+ l-
add process p p > w+ z j, w+ > ta+ vt, z > l+ l-
add process p p > w- z, w- > ta- vt~, z > l+ l-
add process p p > w- z j, w- > ta- vt~, z > l+ l-
add process p p > w+ z, w+ > l+ vl, z > ta+ ta-
add process p p > w+ z j, w+ > l+ vl, z > ta+ ta-
add process p p > w- z, w- > l- vl~, z > ta+ ta-
add process p p > w- z j, w- > l- vl~, z > ta+ ta-
add process p p > w+ z, w+ > ta+ vt, z > ta+ ta-
add process p p > w+ z j, w+ > ta+ vt, z > ta+ ta-
add process p p > w- z, w- > ta- vt~, z > ta+ ta-
add process p p > w- z j, w- > ta- vt~, z > ta+ ta-
output wz_bkg
# launch the run
launch wz_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag wz_bkg
set nevents 180000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst False # avoid delphes bug
# set cuts
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl
