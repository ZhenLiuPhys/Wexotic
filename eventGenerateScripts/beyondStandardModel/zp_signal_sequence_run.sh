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
output w_lllvl_zp_withtau_signal

# launch the run
launch w_lllvl_zp_withtau_signal
shower = Pythia8
detector = Delphes
analysis = ExRoot

# set parameters
set mass 233 1.0
set width 233 Auto
update to_full
set run_tag signal1
set nevents 100000
set ebeam1 7000
set ebeam2 7000
set cut_decays False
set use_syst=False # avoid delphes bug

# set cuts
set ptj 20
set ptl 10
set drll 0.2
set etaj 5
set etal 5
set ickkw 1
set xqcut 15
../MG5_aMC_v3_4_2/Delphes/cards/delphes_card_HLLHC.tcl