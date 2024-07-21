# standard numerical library imports
import numpy as np
import re
import os
import numpy.ma as ma
import awkward as ak
import uproot
import matplotlib.pyplot as plt

# define local variables
event_list = [['lllv_signal'],
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
              ['lllv_small_bkg']]
event_list_atlas = [['lllv_signal_atlas'],
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
                    ['lllv_small_bkg_atlas']]
# event count !!

muon_mass = 0.1056583745  # GeV
electron_mass = 0.0005109989461  # GeV

# extraction_table_regex = re.compile(r"^(?!.*_1$)(.*_)([2-9]|\d{2,})$")

information_list = ['Electron.PT', 'Electron.Eta', 'Electron.Phi', 'Electron.Charge', 'Muon.PT',
                    'Muon.Eta', 'Muon.Phi', 'Muon.Charge', 'Jet.PT', 'Jet.Eta', 'Jet.Phi', 'Jet.BTag']
data = {}

extraction_table_title = ['event', 'cross section', 'merged event number', 'Lepton = 3',
                          'Lepton Charge not same',
                          'PTL >= 5 GeV',
                          'PTL1 >= 20 GeV, PTL2 >= 10 GeV (RUN2)',
                          'M(ll) > 4 (GeV)',
                        #   '4 < M(ll) < 85 (GeV)',
                          # '1.5 < M(ll) < 2.8 | M(ll) > 4 (GeV)',
                          'Jet <= 2',
                          'M(lll) < 80 GeV',
                          'M(lll) < 60 GeV']


def data_cutflow(dataSet: str):
    global event_list, event_list_atlas
    extraction_table_data = []
    extraction_table_data.append(extraction_table_title)

    # decide which event list to use
    if 'atlas' in dataSet:
        event_list = event_list_atlas

    for event_batch in event_list:
        extraction_table_row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
            event_lepton_size = np.asarray(delphes_tree['Muon_size'].array() + delphes_tree['Electron_size'].array())
            extraction_table_row[2] = extraction_table_row[2] + event_lepton_size.shape[0]
            for i in information_list:
                full_event = ak.to_numpy(ak.pad_none(delphes_tree[i].array(), 20))
                information[i] = full_event[event_lepton_size == 3]
            extraction_table_row[3] = extraction_table_row[3] + information['Electron.PT'].shape[0]

            # # cut the event with more than 2 jets
            # event_jet_size = np.ma.count(information['Jet.PT'], axis=1)
            # for i in information_list:
            #     information[i] = information[i][event_jet_size <= 2]
            # extraction_table_row[4] = extraction_table_row[4] + information['Electron.PT'].shape[0]

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
            for i in information_list:
                information[i] = information[i][:, :3]
            # fill the data array
            pt, eta, phi, charge, PID, energy = np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float), \
                np.empty_like(mass, dtype=float), np.empty_like(mass, dtype=float), np.empty_like(mass,
                                                                                                  dtype=float), np.empty_like(
                mass, dtype=float)
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
            extraction_table_row[4] = extraction_table_row[4] + pt.shape[0]

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
            extraction_table_row[5] = extraction_table_row[5] + pt.shape[0]

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

            extraction_table_row[6] = extraction_table_row[6] + pt.shape[0]

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

            # also two lepton and anti-lepton pairs' invariant mass should be from 1.5 GeV to 2.8 GeV
            # or larger than 4 GeV
            # ll_invariant_mass_mask_condition = (
            #         ~((1.5 <= ll_invariant_mass) & (ll_invariant_mass <= 2.8)) & ~(ll_invariant_mass > 4))
            # ll_invariant_mass_mask_condition = ~((4 <= ll_invariant_mass) & (ll_invariant_mass <= 85))
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
            extraction_table_row[7] = extraction_table_row[7] + pt.shape[0]

            # cut the event with more than 2 jets
            jet_size_bool = (jet_pt != 0).all(axis=1)
            pt = pt[~jet_size_bool]
            eta = eta[~jet_size_bool]
            phi = phi[~jet_size_bool]
            charge = charge[~jet_size_bool]
            PID = PID[~jet_size_bool]
            mass = mass[~jet_size_bool]
            jet_pt = jet_pt[~jet_size_bool]
            jet_eta = jet_eta[~jet_size_bool]
            jet_phi = jet_phi[~jet_size_bool]
            jet_PID = jet_PID[~jet_size_bool]
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
            PID = PID[lll_invariant_mass_bool_80]
            jet_pt = jet_pt[lll_invariant_mass_bool_80]
            jet_eta = jet_eta[lll_invariant_mass_bool_80]
            jet_phi = jet_phi[lll_invariant_mass_bool_80]
            jet_PID = jet_PID[lll_invariant_mass_bool_80]
            lll_invariant_mass = lll_invariant_mass[lll_invariant_mass_bool_80]
            extraction_table_row[9] = extraction_table_row[9] + pt.shape[0]

            lll_invariant_mass_bool_60 = np.all(lll_invariant_mass < 60, axis=1)
            pt = pt[lll_invariant_mass_bool_60]
            eta = eta[lll_invariant_mass_bool_60]
            phi = phi[lll_invariant_mass_bool_60]
            charge = charge[lll_invariant_mass_bool_60]
            PID = PID[lll_invariant_mass_bool_60]
            jet_pt = jet_pt[lll_invariant_mass_bool_60]
            jet_eta = jet_eta[lll_invariant_mass_bool_60]
            jet_phi = jet_phi[lll_invariant_mass_bool_60]
            jet_PID = jet_PID[lll_invariant_mass_bool_60]
            lll_invariant_mass = lll_invariant_mass[lll_invariant_mass_bool_60]
            extraction_table_row[10] = extraction_table_row[10] + pt.shape[0]


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
            np.savetxt('./csvData/atlas/' + event_batch[-1] + '_mlll_atlas.csv', heights, delimiter=',')
        else:
            np.savetxt('./csvData/hllhc/' + event_batch[-1] + '_mlll.csv', heights, delimiter=',')

    # remove the run2 column for HLLHC
    if 'atlas' not in dataSet:
        extraction_table_data = np.delete(extraction_table_data, 6, axis=1)

    # 创建一个图形和坐标轴
    if 'atlas' in dataSet:
        plt.figure(figsize=(21, 3))
    else:
        plt.figure(figsize=(16, 3))
    # 关闭坐标轴
    plt.axis('off')
    # 创建表格
    extraction_table = plt.table(cellText=extraction_table_data, loc='center', cellLoc='center', colLabels=None)
    # 设置表格字体大小
    extraction_table.auto_set_font_size(False)
    extraction_table.set_fontsize(10)
    # 调整表格布局
    extraction_table.scale(1, 1.5)
    extraction_table.auto_set_column_width(range(len(extraction_table_title)))
    # plt.text(0.05, 0.1, 'For ttbar events, lepton size = 2, 1 <= jet size <= 3 w/ btag >=1, and fake the last
    # btagged jet as an electron,\n maintaining the charge requirements before the lepton pt cut.')
    if 'atlas' in dataSet:
        plt.title('SM Cutflow Table RUN2')
        # old title
        plt.savefig('./hist_cut/atlas/sm_cutflow_table_4_run2.png')
        # plt.savefig('./hist_cut/atlas/sm_cutflow_table_85_run2.png')
        # plt.savefig('./hist_cut/atlas/sm_cutflow_table_run2.png')

    else:
        plt.title('SM Cutflow Table HLLHC')
        plt.savefig('./hist_cut/hllhc/sm_cutflow_table_4.png')
    # plt.show()
    plt.close()
    print('All done.')

if '__main__' == __name__:
    # data_cutflow('hllhc')
    data_cutflow('atlas')
