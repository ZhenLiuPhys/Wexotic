# standard numerical library imports
import numpy as np
import re
import numpy.ma as ma
import awkward as ak
import uproot
import matplotlib.pyplot as plt

##############################################################
# read in the data from csv and convert them to numpy arrays
#############################################################
# define local variables
# event_list = ['w_plus_sgn', 'w_plus_z_bkg', 'tt_bkg', 'zz_bkg', 'h_bkg']
# event_list = ['w_plus_sgn']
# event_list = ['w_sgn_1', 'w_sgn_2', 'w_sgn_3', 'w_sgn_4', 'w_sgn_5', 'w_sgn_6',
#               'w_z_bkg_1', 'w_z_bkg_2', 'w_z_bkg_3', 'w_z_bkg_4', 'w_z_bkg_5', 'w_z_bkg_6']
event_list = ['lllv_signal',
              'tt_bkg_1', 'tt_bkg_2', 'tt_bkg_3', 'tt_bkg_4', 'tt_bkg_5', 'tt_bkg_6', 'tt_bkg_7', 'tt_bkg_8',
              'tt_bkg_9', 'tt_bkg_10',
              'tt_bkg_11', 'tt_bkg_12', 'tt_bkg_13', 'tt_bkg_14', 'tt_bkg_15', 'tt_bkg_16', 'tt_bkg_17', 'tt_bkg_18',
              'tt_bkg_19', 'tt_bkg_20',
              'tt_bkg_21', 'tt_bkg_22', 'tt_bkg_23', 'tt_bkg_24', 'tt_bkg_25', 'tt_bkg_26', 'tt_bkg_27', 'tt_bkg_28',
              'tt_bkg_29', 'tt_bkg_30',
              'tt_bkg_31', 'tt_bkg_32', 'tt_bkg_33', 'tt_bkg_34', 'tt_bkg_35', 'tt_bkg_36', 'tt_bkg_37', 'tt_bkg_38',
              'tt_bkg_39', 'tt_bkg_40',
              'tt_bkg_41', 'tt_bkg_42', 'tt_bkg_43', 'tt_bkg_44', 'tt_bkg_45', 'tt_bkg_46', 'tt_bkg_47', 'tt_bkg_48',
              'tt_bkg_49', 'tt_bkg_50',
              'llll_bkg',
              'lllv_large_bkg',
              'lllv_small_bkg']
event_list_atlas = ['lllv_signal_atlas',
                    'tt_bkg_atlas_1', 'tt_bkg_atlas_2', 'tt_bkg_atlas_3', 'tt_bkg_atlas_4', 'tt_bkg_atlas_5',
                    'tt_bkg_atlas_6', 'tt_bkg_atlas_7', 'tt_bkg_atlas_8', 'tt_bkg_atlas_9', 'tt_bkg_atlas_10',
                    'tt_bkg_atlas_11', 'tt_bkg_atlas_12', 'tt_bkg_atlas_13', 'tt_bkg_atlas_14', 'tt_bkg_atlas_15',
                    'tt_bkg_atlas_16', 'tt_bkg_atlas_17', 'tt_bkg_atlas_18', 'tt_bkg_atlas_19', 'tt_bkg_atlas_20',
                    'tt_bkg_atlas_21', 'tt_bkg_atlas_22', 'tt_bkg_atlas_23', 'tt_bkg_atlas_24', 'tt_bkg_atlas_25',
                    'tt_bkg_atlas_26', 'tt_bkg_atlas_27', 'tt_bkg_atlas_28', 'tt_bkg_atlas_29', 'tt_bkg_atlas_30',
                    'tt_bkg_atlas_31', 'tt_bkg_atlas_32', 'tt_bkg_atlas_33', 'tt_bkg_atlas_34', 'tt_bkg_atlas_35',
                    'tt_bkg_atlas_36', 'tt_bkg_atlas_37', 'tt_bkg_atlas_38', 'tt_bkg_atlas_39', 'tt_bkg_atlas_40',
                    'tt_bkg_atlas_41', 'tt_bkg_atlas_42', 'tt_bkg_atlas_43', 'tt_bkg_atlas_44', 'tt_bkg_atlas_45',
                    'tt_bkg_atlas_46', 'tt_bkg_atlas_47', 'tt_bkg_atlas_48', 'tt_bkg_atlas_49', 'tt_bkg_atlas_50',
                    'llll_bkg_atlas',
                    'lllv_large_bkg_atlas',
                    'lllv_small_bkg_atlas']
event_label_list = [1,
                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    2,
                    2,
                    2]
                    
muon_mass = 0.1056583745  # GeV
electron_mass = 0.0005109989461  # GeV

information_list = ['Electron.PT', 'Electron.Eta', 'Electron.Phi', 'Electron.Charge', 'Muon.PT',
                    'Muon.Eta', 'Muon.Phi', 'Muon.Charge', 'Jet.PT', 'Jet.Eta', 'Jet.Phi', 'Jet.BTag']
data = {}


def extract_data(dataSet: str):
    global event_list, event_list_atlas
    # extraction_table_data = []
    # extraction_table_data.append(extraction_table_title)

    # decide which event list to use
    if 'atlas' in dataSet:
        event_list = event_list_atlas

    for event in event_list:

        # extraction_table_row = []
        information = {}

        file = uproot.open('./root_file/' + event + '_delphes_events.root')
        delphes_tree = file['Delphes;1']

        # lepton size should be 3
        event_lepton_size = np.asarray(delphes_tree['Muon_size'].array() + delphes_tree['Electron_size'].array())
        for i in information_list:
            full_event = ak.to_numpy(ak.pad_none(delphes_tree[i].array(), 20))
            if 'tt_bkg' in event:
                information[i] = full_event[event_lepton_size == 2]
                continue
            information[i] = full_event[event_lepton_size == 3]

        # cut the event with more than 2 jets
        event_jet_size = np.ma.count(information['Jet.PT'], axis=1)
        event_BTag_size = np.ma.count(information['Jet.BTag'], axis=1)
        event_Btag_size = np.count_nonzero(information['Jet.BTag'], axis=1)
        # event_jet_PT = np.min(information['Jet.PT'], axis=1)
        for i in information_list:
            if 'tt_bkg' in event:
                condition = np.logical_and(event_jet_size <= 3, event_BTag_size >= 1)
                condition = np.logical_and(event_jet_size >= 1, condition)
                condition = np.logical_and(event_Btag_size >= 1, condition)
                information[i] = information[i][condition]
                continue
            information[i] = information[i][event_jet_size <= 2]
        # if not extraction_table_regex.match(event):
            # extraction_table_row.append(str(information['Electron.PT'].shape[0] * event_count) + ' ({:.1%})'.format(
            #     information['Electron.PT'].shape[0] / event_lepton_size.shape[0]))

        # fill data for machine learning
        mass_bool = ~ma.masked_invalid(information['Muon.PT']).mask
        mass = mass_bool.astype(int)

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
        information['Jet.PT'] = information['Jet.PT'][:, :3]
        information['Jet.Eta'] = information['Jet.Eta'][:, :3]
        information['Jet.Phi'] = information['Jet.Phi'][:, :3]
        information['Jet.BTag'] = information['Jet.BTag'][:, :3]

        # cut the data array to 3
        mass = mass[:, :3]
        for i in information_list:
            information[i] = information[i][:, :3]

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

        # fill the data array
        pt, eta, phi, charge, PID = np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float), \
            np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float)
        for i in ['PT', 'Eta', 'Phi', 'Charge', 'PID']:
            for j in range(mass.shape[0]):
                value = np.zeros(mass.shape[1], dtype=float)
                for k in range(mass.shape[1]):

                    if information['Muon.' + i][j][k] is not ma.masked:
                        value[k] = information['Muon.' + i][j][k]
                    else:
                        for l in range(mass.shape[1]):
                            if information['Electron.' + i][j][l] is not ma.masked:
                                value[k] = information['Electron.' + i][j][l]
                                k = k + 1
                        break
                if i == 'PT':
                    pt[j] = value
                elif i == 'Eta':
                    eta[j] = value
                elif i == 'Phi':
                    phi[j] = value
                elif i == 'Charge':
                    charge[j] = value
                elif i == 'PID':
                    PID[j] = value
        # derive mass array from PID
        mass_array = np.where(np.abs(PID) == 11, electron_mass, muon_mass)
        energy = np.sqrt(pt ** 2 * np.cosh(eta) ** 2 + mass_array ** 2)

        # fill jet information
        jet_pt, jet_eta, jet_phi, jet_btag = np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float), \
            np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float)
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
        jet_pt = jet_pt[bool_product]
        jet_eta = jet_eta[bool_product]
        jet_phi = jet_phi[bool_product]
        jet_PID = jet_PID[bool_product]
        energy = energy[bool_product]

        # ptl should be larger than 5
        ptl_bool = np.all(pt >= 5, axis=1)
        pt = pt[ptl_bool]
        eta = eta[ptl_bool]
        phi = phi[ptl_bool]
        charge = charge[ptl_bool]
        PID = PID[ptl_bool]
        mass = mass[ptl_bool]
        jet_pt = jet_pt[ptl_bool]
        jet_eta = jet_eta[ptl_bool]
        jet_phi = jet_phi[ptl_bool]
        jet_PID = jet_PID[ptl_bool]
        energy = energy[ptl_bool]

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
            PID = PID[ptl_bool]
            mass = mass[ptl_bool]
            jet_pt = jet_pt[ptl_bool]
            jet_eta = jet_eta[ptl_bool]
            jet_phi = jet_phi[ptl_bool]
            jet_PID = jet_PID[ptl_bool]
            energy = energy[ptl_bool]

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
                                                                                                           0], energy[:,
                                                                                                               1]

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
        pt = pt[~ll_invariant_mass_mask_condition.any(axis=1)]
        eta = eta[~ll_invariant_mass_mask_condition.any(axis=1)]
        phi = phi[~ll_invariant_mass_mask_condition.any(axis=1)]
        charge = charge[~ll_invariant_mass_mask_condition.any(axis=1)]
        PID = PID[~ll_invariant_mass_mask_condition.any(axis=1)]
        mass = mass[~ll_invariant_mass_mask_condition.any(axis=1)]
        energy = energy[~ll_invariant_mass_mask_condition.any(axis=1)]
        jet_pt = jet_pt[~ll_invariant_mass_mask_condition.any(axis=1)]
        jet_eta = jet_eta[~ll_invariant_mass_mask_condition.any(axis=1)]
        jet_phi = jet_phi[~ll_invariant_mass_mask_condition.any(axis=1)]
        jet_PID = jet_PID[~ll_invariant_mass_mask_condition.any(axis=1)]
        # extraction_table_row[7] = extraction_table_row[7] + pt.shape[0]
        
        # mlll < 80 GeV
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
        lll_invariant_mass_bool_80 = np.all(lll_invariant_mass < 80, axis=1)
        pt = pt[lll_invariant_mass_bool_80]
        eta = eta[lll_invariant_mass_bool_80]
        phi = phi[lll_invariant_mass_bool_80]
        charge = charge[lll_invariant_mass_bool_80]
        PID = PID[lll_invariant_mass_bool_80]
        jet_pt = jet_pt[lll_invariant_mass_bool_80]
        jet_eta = jet_eta[lll_invariant_mass_bool_80]
        jet_phi = jet_phi[lll_invariant_mass_bool_80]
        jet_PID = jet_PID[lll_invariant_mass_bool_80]
        lll_invariant_mass = lll_invariant_mass[lll_invariant_mass_bool_80]

        # # add row to data
        # if not extraction_table_regex.match(event):
        #     extraction_table_data.append(extraction_table_row)

        # stack pt, eta, phi, charge, PID together
        pt_particles = np.hstack((pt, jet_pt))
        eta_particles = np.hstack((eta, jet_eta))
        phi_particles = np.hstack((phi, jet_phi))
        PID_particles = np.hstack((PID, jet_PID))

        data[event + '_data'] = np.stack((pt_particles, eta_particles, phi_particles, PID_particles), axis=-1)
        np.save('./data/' + event + '_data.npy', data[event + '_data'])
        data[event + '_label'] = np.full(data[event + '_data'].shape[0], event_label_list[event_list.index(event)])
        np.save('./data/' + event + '_label.npy', data[event + '_label'])
        print(event + ' data and label saved')


if __name__ == '__main__':
    # extract_data('hllhc')
    extract_data('atlas')
