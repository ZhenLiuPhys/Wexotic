import model Z_mutau_anomaly
generate p p > w+, ( w+ > l+ vl zp , zp > mu+ mu- )
add process p p > w+ j, ( w+ > l+ vl zp , zp > mu+ mu- )
add process p p > w-, ( w- > l- vl~ zp , zp > mu+ mu- )
add process p p > w- j, ( w- > l- vl~ zp , zp > mu+ mu- )
output zp_signal_anomalous_atlas

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 4.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_4
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 5.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_5
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 10.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_10
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 20.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_20
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 30.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_30
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 40.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_40
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 50.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_50
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 60.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_60
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl

launch zp_signal_anomalous_atlas
shower = Pythia8
detector = Delphes
analysis = OFF
set mass 233 75.0
set width 233 Auto
update to_full
set run_tag zp_anomalous_atlas_75
set nevents 100000
set ebeam1 6500
set ebeam2 6500
set cut_decays True
set use_syst False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 2.5
set ickkw 1
set xqcut 15
./delphes_card_ATLAS_update.tcl
