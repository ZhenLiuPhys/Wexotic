# lllv bkg
import model sm-full
generate p p > l+ l- l+ vl 
add process p p > l+ l- l+ vl j 
add process p p > l+ l- l- vl~ 
add process p p > l+ l- l- vl~ j 
output lllv_small_bkg
# launch the run
launch lllv_small_bkg
shower = Pythia8
detector = Delphes
# set parameters
update to_full
set run_tag lllv_small_bkg
set nevents 500000
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
set mmnl 0
set mmnlmax 76.3
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl