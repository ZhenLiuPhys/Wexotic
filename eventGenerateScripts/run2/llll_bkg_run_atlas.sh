# llll bkg
import model sm-full
generate p p > l+ l- l+ l- 
add process p p > l+ l- l+ l- j 
output llll_bkg_atlas
# launch the run
launch llll_bkg_atlas
shower = Pythia8
detector = Delphes
# set parameters
update to_full
set run_tag llll_bkg_atlas
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
set bwcutoff 2.0
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl