# lllv bkg
import model sm-full
generate p p > l+ l- l+ vl 
add process p p > l+ l- l+ vl j 
add process p p > l+ l- l- vl~ 
add process p p > l+ l- l- vl~ j 
output lllv_signal_atlas
# launch the run
launch lllv_signal_atlas
shower = Pythia8
detector = Delphes
# set parameters
update to_full
set run_tag lllv_signal_atlas
set nevents 500000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst False # avoid delphes bug
# set cuts
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set mmnl 76.3
set mmnlmax 84.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl