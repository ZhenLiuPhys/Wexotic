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