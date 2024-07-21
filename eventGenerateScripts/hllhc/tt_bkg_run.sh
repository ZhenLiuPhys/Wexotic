# TTbar bkg
import model sm-full
generate p p > t t~
add process p p > t t~ j
output tt_bkg

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_1
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_2
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_3
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_4
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_5
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_6
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_7
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_8
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_9
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# analysis = ExRoot
# set parameters
update to_full
set run_tag tt_bkg_10
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_11
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_12
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_13
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_14
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_15
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_16
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_17
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_18
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_19
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_20
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_21
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_22
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_23
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_24
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_25
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_26
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_27
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_28
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_29
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_30
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_31
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_32
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_33
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_34
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_35
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_36
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_37
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_38
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_39
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_40
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_41
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_42
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_43
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_44
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_45
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_46
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_47
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_48
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_49
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

# launch the run
launch tt_bkg
shower = Pythia8
detector = Delphes
analysis = OFF
# set parameters
update to_full
set run_tag tt_bkg_50
set nevents 200000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set hard_survey=1
set sde_strategy=1
set use_syst=False # avoid delphes bug
# set cuts
set ptj 20
set etaj 5
set ickkw 1
set xqcut 15
./delphes_card_HLLHC_update.tcl

