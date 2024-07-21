# standard numerical library imports
import numpy as np
import re
import os
import numpy.ma as ma
import awkward as ak
import uproot
import matplotlib.pyplot as plt

# define local variables
# event_list = [['zp_4'], ['zp_5'], ['zp_10'], ['zp_20'], ['zp_30'], ['zp_40'], ['zp_50'], ['zp_60'], ['zp_75'],
#               ['lllv_signal'],
#               ['tt_bkg_1', 'tt_bkg_2', 'tt_bkg_3', 'tt_bkg_4', 'tt_bkg_5', 'tt_bkg_6', 'tt_bkg_7', 'tt_bkg_8',
#                'tt_bkg_9', 'tt_bkg_10',
#                'tt_bkg_11', 'tt_bkg_12', 'tt_bkg_13', 'tt_bkg_14', 'tt_bkg_15', 'tt_bkg_16', 'tt_bkg_17', 'tt_bkg_18',
#                'tt_bkg_19', 'tt_bkg_20',
#                'tt_bkg_21', 'tt_bkg_22', 'tt_bkg_23', 'tt_bkg_24', 'tt_bkg_25', 'tt_bkg_26', 'tt_bkg_27', 'tt_bkg_28',
#                'tt_bkg_29', 'tt_bkg_30',
#                'tt_bkg_31', 'tt_bkg_32', 'tt_bkg_33', 'tt_bkg_34', 'tt_bkg_35', 'tt_bkg_36', 'tt_bkg_37', 'tt_bkg_38',
#                'tt_bkg_39', 'tt_bkg_40',
#                'tt_bkg_41', 'tt_bkg_42', 'tt_bkg_43', 'tt_bkg_44', 'tt_bkg_45', 'tt_bkg_46', 'tt_bkg_47', 'tt_bkg_48',
#                'tt_bkg_49', 'tt_bkg_50'],
#               ['llll_bkg'],
#               ['lllv_large_bkg'],
#               ['lllv_small_bkg']]

event_list = [['zp_anomalous_4'], ['zp_anomalous_5'], ['zp_anomalous_10'], ['zp_anomalous_20'], ['zp_anomalous_30'],
              ['zp_anomalous_40'], ['zp_anomalous_50'], ['zp_anomalous_60'], ['zp_anomalous_75'],
              ['lllv_signal'],
              ['tt_bkg_1', 'tt_bkg_2', 'tt_bkg_3', 'tt_bkg_4', 'tt_bkg_5', 'tt_bkg_6', 'tt_bkg_7', 'tt_bkg_8',
               'tt_bkg_9', 'tt_bkg_10',
               'tt_bkg_11', 'tt_bkg_12', 'tt_bkg_13', 'tt_bkg_14', 'tt_bkg_15', 'tt_bkg_16', 'tt_bkg_17', 'tt_bkg_18',
               'tt_bkg_19', 'tt_bkg_20',
               'tt_bkg_21', 'tt_bkg_22', 'tt_bkg_23', 'tt_bkg_24', 'tt_bkg_25', 'tt_bkg_26', 'tt_bkg_27', 'tt_bkg_28',
               'tt_bkg_29', 'tt_bkg_30',
               'tt_bkg_31', 'tt_bkg_32', 'tt_bkg_33', 'tt_bkg_34', 'tt_bkg_35', 'tt_bkg_36', 'tt_bkg_37', 'tt_bkg_38',
               'tt_bkg_39', 'tt_bkg_40',
               'tt_bkg_41', 'tt_bkg_42', 'tt_bkg_43', 'tt_bkg_44', 'tt_bkg_45', 'tt_bkg_46', 'tt_bkg_47', 'tt_bkg_48',
               'tt_bkg_49', 'tt_bkg_50'],
              ['llll_bkg'],
              ['lllv_large_bkg'],
              ['lllv_small_bkg']]  # anomalous xs

# event_list_atlas = [['zp_atlas_4'], ['zp_atlas_5'], ['zp_atlas_10'], ['zp_atlas_20'], ['zp_atlas_30'], ['zp_atlas_40'], ['zp_atlas_50'],
#                     ['zp_atlas_60'], ['zp_atlas_75'],
#                     ['lllv_signal_atlas'],
#                     ['tt_bkg_atlas_1', 'tt_bkg_atlas_2', 'tt_bkg_atlas_3', 'tt_bkg_atlas_4', 'tt_bkg_atlas_5',
#                      'tt_bkg_atlas_6', 'tt_bkg_atlas_7', 'tt_bkg_atlas_8', 'tt_bkg_atlas_9', 'tt_bkg_atlas_10',
#                      'tt_bkg_atlas_11', 'tt_bkg_atlas_12', 'tt_bkg_atlas_13', 'tt_bkg_atlas_14', 'tt_bkg_atlas_15',
#                      'tt_bkg_atlas_16', 'tt_bkg_atlas_17', 'tt_bkg_atlas_18', 'tt_bkg_atlas_19', 'tt_bkg_atlas_20',
#                      'tt_bkg_atlas_21', 'tt_bkg_atlas_22', 'tt_bkg_atlas_23', 'tt_bkg_atlas_24', 'tt_bkg_atlas_25',
#                      'tt_bkg_atlas_26', 'tt_bkg_atlas_27', 'tt_bkg_atlas_28', 'tt_bkg_atlas_29', 'tt_bkg_atlas_30',
#                      'tt_bkg_atlas_31', 'tt_bkg_atlas_32', 'tt_bkg_atlas_33', 'tt_bkg_atlas_34', 'tt_bkg_atlas_35',
#                      'tt_bkg_atlas_36', 'tt_bkg_atlas_37', 'tt_bkg_atlas_38', 'tt_bkg_atlas_39', 'tt_bkg_atlas_40',
#                      'tt_bkg_atlas_41', 'tt_bkg_atlas_42', 'tt_bkg_atlas_43', 'tt_bkg_atlas_44', 'tt_bkg_atlas_45',
#                      'tt_bkg_atlas_46', 'tt_bkg_atlas_47', 'tt_bkg_atlas_48', 'tt_bkg_atlas_49', 'tt_bkg_atlas_50'],
#                     ['llll_bkg_atlas'],
#                     ['lllv_large_bkg_atlas'],
#                     ['lllv_small_bkg_atlas']]

event_list_atlas = [['zp_anomalous_atlas_4'], ['zp_anomalous_atlas_5'], ['zp_anomalous_atlas_10'],
                    ['zp_anomalous_atlas_20'], ['zp_anomalous_atlas_30'], ['zp_anomalous_atlas_40'],
                    ['zp_anomalous_atlas_50'],
                    ['zp_anomalous_atlas_60'], ['zp_anomalous_atlas_75'],
                    ['lllv_signal_atlas'],
                    ['tt_bkg_atlas_1', 'tt_bkg_atlas_2', 'tt_bkg_atlas_3', 'tt_bkg_atlas_4', 'tt_bkg_atlas_5',
                     'tt_bkg_atlas_6', 'tt_bkg_atlas_7', 'tt_bkg_atlas_8', 'tt_bkg_atlas_9', 'tt_bkg_atlas_10',
                     'tt_bkg_atlas_11', 'tt_bkg_atlas_12', 'tt_bkg_atlas_13', 'tt_bkg_atlas_14', 'tt_bkg_atlas_15',
                     'tt_bkg_atlas_16', 'tt_bkg_atlas_17', 'tt_bkg_atlas_18', 'tt_bkg_atlas_19', 'tt_bkg_atlas_20',
                     'tt_bkg_atlas_21', 'tt_bkg_atlas_22', 'tt_bkg_atlas_23', 'tt_bkg_atlas_24', 'tt_bkg_atlas_25',
                     'tt_bkg_atlas_26', 'tt_bkg_atlas_27', 'tt_bkg_atlas_28', 'tt_bkg_atlas_29', 'tt_bkg_atlas_30',
                     'tt_bkg_atlas_31', 'tt_bkg_atlas_32', 'tt_bkg_atlas_33', 'tt_bkg_atlas_34', 'tt_bkg_atlas_35',
                     'tt_bkg_atlas_36', 'tt_bkg_atlas_37', 'tt_bkg_atlas_38', 'tt_bkg_atlas_39', 'tt_bkg_atlas_40',
                     'tt_bkg_atlas_41', 'tt_bkg_atlas_42', 'tt_bkg_atlas_43', 'tt_bkg_atlas_44', 'tt_bkg_atlas_45',
                     'tt_bkg_atlas_46', 'tt_bkg_atlas_47', 'tt_bkg_atlas_48', 'tt_bkg_atlas_49', 'tt_bkg_atlas_50'],
                    ['llll_bkg_atlas'],
                    ['lllv_large_bkg_atlas'],
                    ['lllv_small_bkg_atlas']]  # anomalous xs

muon_mass = 0.1056583745  # GeV
electron_mass = 0.0005109989461  # GeV

information_list = ['Electron.PT', 'Electron.Eta', 'Electron.Phi', 'Electron.Charge', 'Muon.PT',
                    'Muon.Eta', 'Muon.Phi', 'Muon.Charge', 'Jet.PT', 'Jet.Eta', 'Jet.Phi', 'Jet.BTag']
data = {}

extraction_table_title = ['event', 'cross section', 'merged event number', 'Muon= 3',
                          'Jet <= 2',
                          'Muon Charge not same',
                          'PTL >= 5 GeV',
                          'PTL1 >= 20 GeV, PTL2 >= 10 GeV (RUN2)',
                          'M(ll) > 4 (GeV)',
                          'M(lll) < 80 GeV']


def data_cutflow(dataSet: str, fake: bool = False):
    global event_list, event_list_atlas
    extraction_table_data = []
    extraction_table_data.append(extraction_table_title)

    # decide which event list to use
    if 'atlas' in dataSet:
        event_list = event_list_atlas

    for event_batch in event_list:
        extraction_table_row = [0 for _ in range(len(extraction_table_title))]
        mlll_list: np.ndarray = np.array([])
        for event in event_batch:
            information = {}

            relative_location = os.readlink('./root_file/' + event + '_delphes_events.root')
            exact_location = os.path.abspath(relative_location)
            file = uproot.open(exact_location)
            delphes_tree = file['Delphes;1']
            extraction_table_row[0] = event
            # # delphes_tree['Event/Event.Weight'].array()
            # print(delphes_tree.keys())
            # make the last cross section the cross section needed
            # print(np.asarray(delphes_tree['Event.CrossSection'].array())[-1][0])
            extraction_table_row[1] = extraction_table_row[1] + delphes_tree['Event.CrossSection'].array()[-1][0]
            # print(np.asarray(delphes_tree['Muon_size'].array()))

            # lepton size should be 3
            event_muon_size = np.asarray(delphes_tree['Muon_size'].array())
            extraction_table_row[2] = extraction_table_row[2] + event_muon_size.shape[0]
            for i in information_list:
                full_event = ak.to_numpy(ak.pad_none(delphes_tree[i].array(), 20))
                if ('tt_bkg' in event) and fake:
                    information[i] = full_event[event_muon_size == 2]
                    continue
                information[i] = full_event[event_muon_size == 3]
            extraction_table_row[3] = extraction_table_row[3] + information['Electron.PT'].shape[0]

            # cut the event with more than 2 jets
            event_jet_size = np.ma.count(information['Jet.PT'], axis=1)
            event_BTag_size = np.ma.count(information['Jet.BTag'], axis=1)
            event_Btag_size = np.count_nonzero(information['Jet.BTag'], axis=1)
            # event_jet_PT = np.min(information['Jet.PT'], axis=1)
            for i in information_list:
                if fake:
                    if 'tt_bkg' in event:
                        condition = np.logical_and(event_jet_size <= 3, event_BTag_size >= 1)
                        condition = np.logical_and(event_jet_size >= 1, condition)
                        condition = np.logical_and(event_Btag_size >= 1, condition)
                        information[i] = information[i][condition]
                        continue
                information[i] = information[i][event_jet_size <= 2]
            extraction_table_row[4] = extraction_table_row[4] + information['Electron.PT'].shape[0]

            # fill data
            lepton_mass_bool = ~ma.masked_invalid(information['Muon.PT']).mask
            mass = lepton_mass_bool.astype(float) * muon_mass

            # construct PID
            # electron
            electron_masked = information['Electron.PT'].mask
            muon_masked = np.ma.getmaskarray(information['Muon.PT'])
            information['Electron.PID'] = np.where(electron_masked, information['Electron.PT'], -11)
            information['Electron.PID'] = np.ma.masked_where(np.isnan(information['Electron.PID']),
                                                             information['Electron.PID'])
            information['Electron.PID'] = information['Electron.PID'] * information['Electron.Charge']
            # muon
            information['Muon.PID'] = np.where(muon_masked, information['Muon.PT'], -13)
            information['Muon.PID'] = np.ma.masked_where(np.isnan(information['Muon.PID']), information['Muon.PID'])
            information['Muon.PID'] = information['Muon.PID'] * information['Muon.Charge']

            # jet
            information['Jet.PT'] = information['Jet.PT']
            information['Jet.Eta'] = information['Jet.Eta']
            information['Jet.Phi'] = information['Jet.Phi']
            information['Jet.BTag'] = information['Jet.BTag']

            # cut the data array to 3
            mass = mass[:, :3]

            if fake:
                if 'tt_bkg' in event:
                    # print(information['Jet.PT'].shape)
                    # fake the last btagged jet as an electron, maintaining the charge requirements before the lepton pt cut
                    for row_idx in range(information['Jet.PT'].shape[0]):
                        last_value_idx = np.ma.count(information['Jet.PT'][row_idx]) - 1
                        electron_value_idx = np.ma.count(information['Electron.PT'][row_idx])
                        last_value = information['Jet.PT'][row_idx, last_value_idx]
                        information['Jet.PT'][row_idx, last_value_idx] = ma.masked
                        information['Electron.PT'][row_idx, electron_value_idx] = last_value
                    for row_idx in range(information['Jet.Eta'].shape[0]):
                        last_value_idx = np.ma.count(information['Jet.Eta'][row_idx]) - 1
                        electron_value_idx = np.ma.count(information['Electron.Eta'][row_idx])
                        last_value = information['Jet.Eta'][row_idx, last_value_idx]
                        information['Jet.Eta'][row_idx, last_value_idx] = ma.masked
                        information['Electron.Eta'][row_idx, electron_value_idx] = last_value
                    for row_idx in range(information['Jet.Phi'].shape[0]):
                        last_value_idx = np.ma.count(information['Jet.Phi'][row_idx]) - 1
                        electron_value_idx = np.ma.count(information['Electron.Phi'][row_idx])
                        last_value = information['Jet.Phi'][row_idx, last_value_idx]
                        information['Jet.Phi'][row_idx, last_value_idx] = ma.masked
                        information['Electron.Phi'][row_idx, electron_value_idx] = last_value
                    for row_idx in range(information['Jet.BTag'].shape[0]):
                        last_value_idx = np.ma.count(information['Jet.BTag'][row_idx]) - 1
                        electron_value_idx = np.ma.count(information['Electron.PID'][row_idx])
                        # last_value = information['Jet.BTag'][row_idx, last_value_idx]
                        if electron_value_idx == 0:
                            last_value = (information['Muon.Charge'][row_idx, 0]) * (11)
                            last_value_charge = - (information['Muon.Charge'][row_idx, 0])
                        else:
                            last_value = (information['Electron.Charge'][row_idx, electron_value_idx - 1]) * (11)
                            last_value_charge = - (information['Electron.Charge'][row_idx, electron_value_idx - 1])
                        information['Jet.BTag'][row_idx, last_value_idx] = ma.masked
                        information['Electron.PID'][row_idx, electron_value_idx] = last_value
                        information['Electron.Charge'][row_idx, electron_value_idx] = last_value_charge

            for i in information:
                information[i] = information[i][:, :3]
            # fill the data array
            pt, eta, phi, charge, PID, energy = np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float), \
                np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float), np.empty_like(mass,
                                                                                                  dtype=float), np.empty_like(
                mass, dtype=float)
            # fill the data array
            pt = information['Muon.PT']
            eta = information['Muon.Eta']
            phi = information['Muon.Phi']
            charge = information['Muon.Charge']
            PID = information['Muon.PID']

            # derive mass array from PID
            mass_array = np.where(np.abs(PID) == 11, electron_mass, muon_mass)
            energy = np.sqrt(pt ** 2 * np.cosh(eta) ** 2 + mass_array ** 2)

            # fill jet information
            jet_pt = information['Jet.PT'].filled(0)
            jet_eta = information['Jet.Eta'].filled(0)
            jet_phi = information['Jet.Phi'].filled(0)
            jet_PID = information['Jet.BTag'].filled(0)

            # charges should not be same
            product_charge = np.sum(charge, axis=1)
            bool_product = ((product_charge != 3) & (product_charge != -3))
            pt = pt[bool_product]
            eta = eta[bool_product]
            phi = phi[bool_product]
            charge = charge[bool_product]
            PID = PID[bool_product]
            mass = mass[bool_product]
            energy = energy[bool_product]
            jet_pt = jet_pt[bool_product]
            jet_eta = jet_eta[bool_product]
            jet_phi = jet_phi[bool_product]
            jet_PID = jet_PID[bool_product]
            extraction_table_row[5] = extraction_table_row[5] + pt.shape[0]

            # ptl should be larger than 5
            ptl_bool = np.all(pt >= 5, axis=1)
            pt = pt[ptl_bool]
            eta = eta[ptl_bool]
            phi = phi[ptl_bool]
            charge = charge[ptl_bool]
            PID = PID[ptl_bool]
            mass = mass[ptl_bool]
            energy = energy[ptl_bool]
            jet_pt = jet_pt[ptl_bool]
            jet_eta = jet_eta[ptl_bool]
            jet_phi = jet_phi[ptl_bool]
            jet_PID = jet_PID[ptl_bool]
            extraction_table_row[6] = extraction_table_row[6] + pt.shape[0]

            # for atlas the leading lepton pt should be larger than 20
            # subleading lepton pt should be larger than 10
            if 'atlas' in dataSet:
                ptl_max = np.max(pt, axis=1)
                ptl_subleading = np.partition(pt, -2, axis=1)[:, -2]
                ptl_bool = np.where((ptl_max >= 20) & (ptl_subleading >= 10), True, False)
                pt = pt[ptl_bool]
                eta = eta[ptl_bool]
                phi = phi[ptl_bool]
                charge = charge[ptl_bool]
                mass = mass[ptl_bool]
                energy = energy[ptl_bool]
                PID = PID[ptl_bool]
                jet_pt = jet_pt[ptl_bool]
                jet_eta = jet_eta[ptl_bool]
                jet_phi = jet_phi[ptl_bool]
                jet_PID = jet_PID[ptl_bool]

            extraction_table_row[7] = extraction_table_row[7] + pt.shape[0]

            # two same flavor, opposite charge leptons, their invariant mass should be
            # larger than 4 GeV
            # shuffle the index to 1, 2, 0
            pt_shuffle = np.zeros_like(pt, dtype=float)
            eta_shuffle = np.zeros_like(eta, dtype=float)
            phi_shuffle = np.zeros_like(phi, dtype=float)
            PID_shuffle = np.zeros_like(charge, dtype=int)
            energy_shuffle = np.zeros_like(energy, dtype=float)

            # shuffle the index to 2, 0, 1
            pt_shuffle_third = np.zeros_like(pt, dtype=float)
            eta_shuffle_third = np.zeros_like(eta, dtype=float)
            phi_shuffle_third = np.zeros_like(phi, dtype=float)
            PID_shuffle_third = np.zeros_like(charge, dtype=int)
            energy_shuffle_third = np.zeros_like(energy, dtype=float)

            # calculate the invariant mass of the muon pair
            px = pt * np.cos(phi)
            py = pt * np.sin(phi)
            pz = pt * np.sinh(eta)

            pt_shuffle[:, 0], pt_shuffle[:, 1], pt_shuffle[:, 2] = pt[:, 1], pt[:, 2], pt[:, 0]
            pt_shuffle_third[:, 0], pt_shuffle_third[:, 1], pt_shuffle_third[:, 2] = pt[:, 2], pt[:, 0], pt[:, 1]
            eta_shuffle[:, 0], eta_shuffle[:, 1], eta_shuffle[:, 2] = eta[:, 1], eta[:, 2], eta[:, 0]
            eta_shuffle_third[:, 0], eta_shuffle_third[:, 1], eta_shuffle_third[:, 2] = eta[:, 2], eta[:, 0], eta[:, 1]
            phi_shuffle[:, 0], phi_shuffle[:, 1], phi_shuffle[:, 2] = phi[:, 1], phi[:, 2], phi[:, 0]
            phi_shuffle_third[:, 0], phi_shuffle_third[:, 1], phi_shuffle_third[:, 2] = phi[:, 2], phi[:, 0], phi[:, 1]
            PID_shuffle[:, 0], PID_shuffle[:, 1], PID_shuffle[:, 2] = PID[:, 1], PID[:, 2], PID[:, 0]
            PID_shuffle_third[:, 0], PID_shuffle_third[:, 1], PID_shuffle_third[:, 2] = PID[:, 2], PID[:, 0], PID[:, 1]
            energy_shuffle[:, 0], energy_shuffle[:, 1], energy_shuffle[:, 2] = energy[:, 1], energy[:, 2], energy[:, 0]
            energy_shuffle_third[:, 0], energy_shuffle_third[:, 1], energy_shuffle_third[:, 2] = energy[:, 2], energy[:,
                                                                                                               0], energy[
                                                                                                                   :, 1]

            px_shuffle = pt_shuffle * np.cos(phi_shuffle)
            py_shuffle = pt_shuffle * np.sin(phi_shuffle)
            pz_shuffle = pt_shuffle * np.sinh(eta_shuffle)

            ll_px_sum = px + px_shuffle
            ll_py_sum = py + py_shuffle
            ll_pz_sum = pz + pz_shuffle
            ll_energy_sum = energy + energy_shuffle

            # muon pair should have opposite charge
            ll_PID_sum = PID + PID_shuffle

            ll_px_sum = np.ma.masked_where(ll_PID_sum != 0, ll_px_sum)
            ll_py_sum = np.ma.masked_where(ll_PID_sum != 0, ll_py_sum)
            ll_pz_sum = np.ma.masked_where(ll_PID_sum != 0, ll_pz_sum)

            # calculate the invariant mass of two leptons should close to 0 GeV
            ll_invariant_mass = np.sqrt(ll_energy_sum ** 2 - ll_px_sum ** 2 - ll_py_sum ** 2 - ll_pz_sum ** 2)

            # also two lepton and anti-lepton pairs' invariant mass should be 
            # larger than 4 GeV
            ll_invariant_mass_mask_condition = ~(ll_invariant_mass > 4)
            ll_invariant_mass = ll_invariant_mass[~ll_invariant_mass_mask_condition.any(axis=1)]
            pt_shuffle_third = pt_shuffle_third[~ll_invariant_mass_mask_condition.any(axis=1)]
            pt = pt[~ll_invariant_mass_mask_condition.any(axis=1)]
            eta = eta[~ll_invariant_mass_mask_condition.any(axis=1)]
            phi = phi[~ll_invariant_mass_mask_condition.any(axis=1)]
            charge = charge[~ll_invariant_mass_mask_condition.any(axis=1)]
            PID = PID[~ll_invariant_mass_mask_condition.any(axis=1)]
            mass = mass[~ll_invariant_mass_mask_condition.any(axis=1)]
            jet_pt = jet_pt[~ll_invariant_mass_mask_condition.any(axis=1)]
            jet_eta = jet_eta[~ll_invariant_mass_mask_condition.any(axis=1)]
            jet_phi = jet_phi[~ll_invariant_mass_mask_condition.any(axis=1)]
            jet_PID = jet_PID[~ll_invariant_mass_mask_condition.any(axis=1)]

            # remove rows with all masked values
            masked_condition = np.all(np.ma.getmaskarray(ll_invariant_mass), axis=1)
            # if 'tt' in event:
            #     # if masked_condition.max not all False:
            #     if masked_condition.any():
            #         print(""")
            ll_invariant_mass = ll_invariant_mass[~masked_condition]
            # print(ll_invariant_mass)
            pt = pt[~masked_condition]
            eta = eta[~masked_condition]
            phi = phi[~masked_condition]
            charge = charge[~masked_condition]
            PID = PID[~masked_condition]
            mass = mass[~masked_condition]
            jet_pt = jet_pt[~masked_condition]
            jet_eta = jet_eta[~masked_condition]
            jet_phi = jet_phi[~masked_condition]
            jet_PID = jet_PID[~masked_condition]
            extraction_table_row[8] = extraction_table_row[8] + pt.shape[0]

            # mlll <= 80 GeV
            energy = np.sqrt(pt ** 2 * np.cosh(eta) ** 2 + mass ** 2)
            # to compute mlll, first shuffle pt as [0,1,2], [1,2,0], [2,0,1]
            pt_shuffle_1 = np.zeros_like(pt, dtype=float)
            eta_shuffle_1 = np.zeros_like(eta, dtype=float)
            phi_shuffle_1 = np.zeros_like(phi, dtype=float)
            energy_shuffle_1 = np.zeros_like(energy, dtype=float)
            pt_shuffle_2 = np.zeros_like(pt, dtype=float)
            eta_shuffle_2 = np.zeros_like(eta, dtype=float)
            phi_shuffle_2 = np.zeros_like(phi, dtype=float)
            energy_shuffle_2 = np.zeros_like(energy, dtype=float)

            pt_shuffle_1[:, [0, 1, 2]] = pt[:, [1, 2, 0]]
            pt_shuffle_2[:, [0, 1, 2]] = pt[:, [2, 0, 1]]
            eta_shuffle_1[:, [0, 1, 2]] = eta[:, [1, 2, 0]]
            eta_shuffle_2[:, [0, 1, 2]] = eta[:, [2, 0, 1]]
            phi_shuffle_1[:, [0, 1, 2]] = phi[:, [1, 2, 0]]
            phi_shuffle_2[:, [0, 1, 2]] = phi[:, [2, 0, 1]]
            energy_shuffle_1[:, [0, 1, 2]] = energy[:, [1, 2, 0]]
            energy_shuffle_2[:, [0, 1, 2]] = energy[:, [2, 0, 1]]

            px = pt * np.cos(phi)
            py = pt * np.sin(phi)
            pz = pt * np.sinh(eta)
            px_shuffle_1 = pt_shuffle_1 * np.cos(phi_shuffle_1)
            py_shuffle_1 = pt_shuffle_1 * np.sin(phi_shuffle_1)
            pz_shuffle_1 = pt_shuffle_1 * np.sinh(eta_shuffle_1)
            px_shuffle_2 = pt_shuffle_2 * np.cos(phi_shuffle_2)
            py_shuffle_2 = pt_shuffle_2 * np.sin(phi_shuffle_2)
            pz_shuffle_2 = pt_shuffle_2 * np.sinh(eta_shuffle_2)

            lll_px_sum = px + px_shuffle_1 + px_shuffle_2
            lll_py_sum = py + py_shuffle_1 + py_shuffle_2
            lll_pz_sum = pz + pz_shuffle_1 + pz_shuffle_2
            lll_energy_sum = energy + energy_shuffle_1 + energy_shuffle_2

            lll_invariant_mass = np.sqrt(lll_energy_sum ** 2 - lll_px_sum ** 2 - lll_py_sum ** 2 - lll_pz_sum ** 2)

            mlll_list = np.concatenate([mlll_list, lll_invariant_mass[:, 0]], axis=0)

            lll_invariant_mass_bool_80 = np.all(lll_invariant_mass < 80, axis=1)
            pt = pt[lll_invariant_mass_bool_80]
            eta = eta[lll_invariant_mass_bool_80]
            phi = phi[lll_invariant_mass_bool_80]
            charge = charge[lll_invariant_mass_bool_80]
            energy = energy[lll_invariant_mass_bool_80]
            PID = PID[lll_invariant_mass_bool_80]
            jet_pt = jet_pt[lll_invariant_mass_bool_80]
            jet_eta = jet_eta[lll_invariant_mass_bool_80]
            jet_phi = jet_phi[lll_invariant_mass_bool_80]
            jet_PID = jet_PID[lll_invariant_mass_bool_80]
            lll_invariant_mass = lll_invariant_mass[lll_invariant_mass_bool_80]
            extraction_table_row[9] = extraction_table_row[9] + pt.shape[0]

            # select muon pair invariant mass close to zp mass
            # shuffle the index to 1, 2, 0
            pt_shuffle = np.zeros_like(pt, dtype=float)
            eta_shuffle = np.zeros_like(eta, dtype=float)
            phi_shuffle = np.zeros_like(phi, dtype=float)
            charge_shuffle = np.zeros_like(charge, dtype=int)
            energy_shuffle = np.zeros_like(energy, dtype=float)

            # shuffle the index to 2, 0, 1
            pt_shuffle_third = np.zeros_like(pt, dtype=float)
            eta_shuffle_third = np.zeros_like(eta, dtype=float)
            phi_shuffle_third = np.zeros_like(phi, dtype=float)
            charge_shuffle_third = np.zeros_like(charge, dtype=int)
            energy_shuffle_third = np.zeros_like(energy, dtype=float)

            # calculate the invariant mass of the muon pair
            px = pt * np.cos(phi)
            py = pt * np.sin(phi)
            pz = pt * np.sinh(eta)

            pt_shuffle[:, 0], pt_shuffle[:, 1], pt_shuffle[:, 2] = pt[:, 1], pt[:, 2], pt[:, 0]
            pt_shuffle_third[:, 0], pt_shuffle_third[:, 1], pt_shuffle_third[:, 2] = pt[:, 2], pt[:, 0], pt[:, 1]
            eta_shuffle[:, 0], eta_shuffle[:, 1], eta_shuffle[:, 2] = eta[:, 1], eta[:, 2], eta[:, 0]
            eta_shuffle_third[:, 0], eta_shuffle_third[:, 1], eta_shuffle_third[:, 2] = eta[:, 2], eta[:, 0], eta[:, 1]
            phi_shuffle[:, 0], phi_shuffle[:, 1], phi_shuffle[:, 2] = phi[:, 1], phi[:, 2], phi[:, 0]
            phi_shuffle_third[:, 0], phi_shuffle_third[:, 1], phi_shuffle_third[:, 2] = phi[:, 2], phi[:, 0], phi[:, 1]
            charge_shuffle[:, 0], charge_shuffle[:, 1], charge_shuffle[:, 2] = charge[:, 1], charge[:, 2], charge[:, 0]
            charge_shuffle_third[:, 0], charge_shuffle_third[:, 1], charge_shuffle_third[:, 2] = charge[:, 2], charge[:,
                                                                                                               0], charge[
                                                                                                                   :, 1]
            energy_shuffle[:, 0], energy_shuffle[:, 1], energy_shuffle[:, 2] = energy[:, 1], energy[:, 2], energy[:, 0]
            energy_shuffle_third[:, 0], energy_shuffle_third[:, 1], energy_shuffle_third[:, 2] = energy[:, 2], energy[:,
                                                                                                               0], energy[
                                                                                                                   :, 1]

            px_shuffle = pt_shuffle * np.cos(phi_shuffle)
            py_shuffle = pt_shuffle * np.sin(phi_shuffle)
            pz_shuffle = pt_shuffle * np.sinh(eta_shuffle)

            ll_px_sum = px + px_shuffle
            ll_py_sum = py + py_shuffle
            ll_pz_sum = pz + pz_shuffle
            ll_energy_sum = energy + energy_shuffle

            # muon pair should have opposite charge
            ll_charge_sum = charge + charge_shuffle

            ll_px_sum = np.ma.masked_where(ll_charge_sum != 0, ll_px_sum)
            ll_py_sum = np.ma.masked_where(ll_charge_sum != 0, ll_py_sum)
            ll_pz_sum = np.ma.masked_where(ll_charge_sum != 0, ll_pz_sum)

            # calculate the invariant mass of two leptons should close to 0 GeV
            ll_invariant_mass = np.sqrt(ll_energy_sum ** 2 - ll_px_sum ** 2 - ll_py_sum ** 2 - ll_pz_sum ** 2)
            # change to min and max instead of close
            zp_mass_difference = np.abs(ll_invariant_mass)
            closest_mass_indices = np.argmin(zp_mass_difference, axis=1)

            # invariant mass of two leptons and the third lepton's pt
            ll_pt_close_third = np.asarray(pt_shuffle_third[np.arange(pt_shuffle_third.shape[0]), closest_mass_indices])
            ll_invariant_mass_close = np.asarray(
                ll_invariant_mass[np.arange(ll_invariant_mass.shape[0]), closest_mass_indices])

            if fake:
                np.save('./hist_cut/ll_data/' + event + '_ll_invariant_mass_close.npy', ll_invariant_mass_close)
                np.save('./hist_cut/ll_data/' + event + '_ll_pt_close_third.npy', ll_pt_close_third)

            print(event + ' cutflow done')

        # add row to data
        extraction_table_row[1] = "{:.4g}".format(extraction_table_row[1] / len(event_batch))
        merged_event_number = extraction_table_row[2]
        extraction_table_row[2] = "{:.0f}".format(extraction_table_row[2]) + "(100%)"
        for i in range(3, len(extraction_table_row)):
            extraction_table_row[i] = "{:.0f}".format(extraction_table_row[i]) + "({:.2g}%)".format(
                extraction_table_row[i] * 100 / merged_event_number)
        extraction_table_data.append(extraction_table_row)

        # plot the mlll histogram
        # output histogram height data of mlll, with x = 0-300, bin width = 6 GeV, probablity density = True
        heights, _ = np.histogram(mlll_list, bins=50, range=(0, 300), density=True)
        # output heights to a csv
        if 'atlas' in dataSet:
            np.savetxt('./csvData/atlas/' + event_batch[-1] + '_bsmfake_mlll_atlas.csv', heights, delimiter=',')
        else:
            np.savetxt('./csvData/hllhc/' + event_batch[-1] + '_bsmfake_mlll.csv', heights, delimiter=',')

    # remove the run2 column for HLLHC
    if 'atlas' not in dataSet:
        extraction_table_data = np.delete(extraction_table_data, 7, axis=1)

    if 'atlas' in dataSet:
        plt.figure(figsize=(20, 5))
    else:
        plt.figure(figsize=(15, 5))

    plt.axis('off')

    extraction_table = plt.table(cellText=extraction_table_data, loc='center', cellLoc='center', colLabels=None)

    extraction_table.auto_set_font_size(False)
    extraction_table.set_fontsize(10)

    extraction_table.scale(1, 1.5)
    extraction_table.auto_set_column_width(range(len(extraction_table_title)))
    # plt.text(0.05, 0.1, 'For ttbar events, lepton size = 2, 1 <= jet size <= 3 w/ btag >=1, and fake the last
    # btagged jet as an electron,\n maintaining the charge requirements before the lepton pt cut.')
    if 'atlas' in dataSet:
        # old title
        plt.title('BSM {} Cutflow Table RUN2'.format("Faked" if fake else "Original"))
        plt.savefig(
            './hist_cut/atlas/bsm_anomalous{}_cutflow_table_4_run2.png'.format("_fake" if fake else ""))  # anomalous xs
        # plt.savefig('./hist_cut/atlas/bsm{}_cutflow_table_4_run2.png'.format("_fake" if fake else ""))
    else:
        plt.title('BSM {} Cutflow Table HLLHC'.format("Faked" if fake else "Original"))
        plt.savefig(
            './hist_cut/hllhc/bsm_anomalous{}_cutflow_table_4.png'.format("_fake" if fake else ""))  # anomalous xs
        # plt.savefig('./hist_cut/hllhc/bsm{}_cutflow_table_4.png'.format("_fake" if fake else ""))
    # plt.show()
    plt.close()
    print('All done.')


if '__main__' == __name__:
    data_cutflow('hllhc')
    data_cutflow('hllhc', fake=True)
    data_cutflow('atlas')
    data_cutflow('atlas', fake=True)
