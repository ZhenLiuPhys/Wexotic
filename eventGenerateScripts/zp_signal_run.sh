import model Z_mutau
generate p p > w+, ( w+ > l+ vl zp , zp > mu+ mu- )
add process p p > w+ j, ( w+ > l+ vl zp , zp > mu+ mu- )
add process p p > w-, ( w- > l- vl~ zp , zp > mu+ mu- )
add process p p > w- j, ( w- > l- vl~ zp , zp > mu+ mu- )
add process p p > w+, ( w+ > ta+ vt zp , zp > mu+ mu- )
add process p p > w+ j, ( w+ > ta+ vt zp , zp > mu+ mu- )
add process p p > w-, ( w- > ta- vt~ zp , zp > mu+ mu- )
add process p p > w- j, ( w- > ta- vt~ zp , zp > mu+ mu- )
add process p p > w+, ( w+ > l+ vl zp , zp > ta+ ta- )
add process p p > w+ j, ( w+ > l+ vl zp , zp > ta+ ta- )
add process p p > w-, ( w- > l- vl~ zp , zp > ta+ ta- )
add process p p > w- j, ( w- > l- vl~ zp , zp > ta+ ta- )
add process p p > w+, ( w+ > ta+ vt zp , zp > ta+ ta- )
add process p p > w+ j, ( w+ > ta+ vt zp , zp > ta+ ta- )
add process p p > w-, ( w- > ta- vt~ zp , zp > ta+ ta- )
add process p p > w- j, ( w- > ta- vt~ zp , zp > ta+ ta- )
output zp_signal

# launch the run
# Mzp=1
launch zp_signal -n zp_1
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 1.0
set width 233 Auto
update to_full
set run_tag zp_1
set nevents 100000
set ebeam1 7000
set ebeam2 7000
set cut_decays True
set use_syst=False
# set cuts
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

# Mzp=2
launch -n zp_2
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 2.0
set width 233 Auto
set run_tag zp_2
set use_syst=False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

# Mzp=5
launch -n zp_5
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 5.0
set width 233 Auto
set run_tag zp_5
set use_syst=False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

# Mzp=10
launch -n zp_10
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 10.0
set width 233 Auto
set run_tag zp_10
set use_syst=False # avoid delphes bug

# Mzp=20
launch -n zp_20
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 20.0
set width 233 Auto
set run_tag zp_20
set use_syst=False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

# Mzp=30
launch -n zp_30
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 30.0
set width 233 Auto
set run_tag zp_30
set use_syst=False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

# Mzp=40
launch -n zp_40
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 40.0
set width 233 Auto
set run_tag zp_40
set use_syst=False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

# Mzp=50
launch -n zp_50
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 50.0
set width 233 Auto
set run_tag zp_50
set use_syst=False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

# Mzp=60
launch -n zp_60
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 60.0
set width 233 Auto
set run_tag zp_60
set use_syst=False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl

# Mzp=80
launch -n zp_80
shower = Pythia8
detector = Delphes
analysis = ExRoot
# set parameters
set mass 233 80.0
set width 233 Auto
set run_tag zp_80
set use_syst=False
set ptj 20
set ptl 3
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl
