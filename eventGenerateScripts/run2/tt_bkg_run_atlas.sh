# TTbar bkg
import model sm-full
generate p p > t t~
add process p p > t t~ j
output tt_bkg_atlas

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_1
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_2
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_3
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_4
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_5
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_6
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_7
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_8
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_9
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_atlas_10
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_11
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_12
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_13
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_14
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_15
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_16
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_17
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_18
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_19
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_20
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_21
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_22
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_23
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_24
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_25
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_26
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_27
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_28
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_29
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_30
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_31
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_32
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_33
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_34
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_35
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_36
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_37
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_38
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_39
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_40
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_41
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_42
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_43
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_44
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_45
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_46
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_47
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_48
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_49
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

# launch the run
launch tt_bkg_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_atlas_50
set nevents 200000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

