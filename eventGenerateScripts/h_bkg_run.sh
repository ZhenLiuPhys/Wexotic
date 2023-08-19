# h bkg
# convert model /root/MG5_aMC_v3_4_2/models/heft
set auto_convert_model T
import model heft-full
generate p p > h, h > l+ l- l+ l-
output h_bkg
# launch the run
launch h_bkg
shower = Pythia8
detector = Delphes
# set parameters
update to_full
set run_tag h_bkg
set nevents 10000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptl 10
set etal 5
set drll 0.2
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl