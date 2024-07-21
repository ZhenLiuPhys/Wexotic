# standard numerical library imports
import numpy as np
import numpy.ma as ma
import awkward as ak
import uproot
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Tuple
import re
import copy


# sgn_list: List[str] = ['zp_4', 'zp_5', 'zp_10', 'zp_20', 'zp_30', 'zp_40', 'zp_50', 'zp_60', 'zp_75']
# sgn_list_atlas: List[str] = ['zp_atlas_4', 'zp_atlas_5', 'zp_atlas_10', 'zp_atlas_20', 'zp_atlas_30', 'zp_atlas_40', 'zp_atlas_50',
#                              'zp_atlas_60',
#                              'zp_atlas_75']

sgn_list: List[str] = ['zp_anomalous_4', 'zp_anomalous_5', 'zp_anomalous_10', 'zp_anomalous_20',
                             'zp_anomalous_30', 'zp_anomalous_40', 'zp_anomalous_50',
                             'zp_anomalous_60',
                             'zp_anomalous_75']  # anomalous xs

sgn_list_atlas: List[str] = ['zp_anomalous_atlas_4', 'zp_anomalous_atlas_5', 'zp_anomalous_atlas_10', 'zp_anomalous_atlas_20',
                             'zp_anomalous_atlas_30', 'zp_anomalous_atlas_40', 'zp_anomalous_atlas_50',
                             'zp_anomalous_atlas_60',
                             'zp_anomalous_atlas_75']  # anomalous xs

bkg_list: List[List[str]] = [['lllv_signal'],
                             ['tt_bkg_1', 'tt_bkg_2', 'tt_bkg_3', 'tt_bkg_4', 'tt_bkg_5', 'tt_bkg_6', 'tt_bkg_7',
                              'tt_bkg_8',
                              'tt_bkg_9', 'tt_bkg_10',
                              'tt_bkg_11', 'tt_bkg_12', 'tt_bkg_13', 'tt_bkg_14', 'tt_bkg_15', 'tt_bkg_16', 'tt_bkg_17',
                              'tt_bkg_18',
                              'tt_bkg_19', 'tt_bkg_20',
                              'tt_bkg_21', 'tt_bkg_22', 'tt_bkg_23', 'tt_bkg_24', 'tt_bkg_25', 'tt_bkg_26', 'tt_bkg_27',
                              'tt_bkg_28',
                              'tt_bkg_29', 'tt_bkg_30',
                              'tt_bkg_31', 'tt_bkg_32', 'tt_bkg_33', 'tt_bkg_34', 'tt_bkg_35', 'tt_bkg_36', 'tt_bkg_37',
                              'tt_bkg_38',
                              'tt_bkg_39', 'tt_bkg_40',
                              'tt_bkg_41', 'tt_bkg_42', 'tt_bkg_43', 'tt_bkg_44', 'tt_bkg_45', 'tt_bkg_46', 'tt_bkg_47',
                              'tt_bkg_48',
                              'tt_bkg_49', 'tt_bkg_50'],
                             ['llll_bkg'],
                             ['lllv_large_bkg'],
                             ['lllv_small_bkg']]
bkg_list_atlas: List[List[str]] = [['lllv_signal_atlas'],
                                   ['tt_bkg_atlas_1', 'tt_bkg_atlas_2', 'tt_bkg_atlas_3', 'tt_bkg_atlas_4',
                                    'tt_bkg_atlas_5',
                                    'tt_bkg_atlas_6', 'tt_bkg_atlas_7', 'tt_bkg_atlas_8', 'tt_bkg_atlas_9',
                                    'tt_bkg_atlas_10',
                                    'tt_bkg_atlas_11', 'tt_bkg_atlas_12', 'tt_bkg_atlas_13', 'tt_bkg_atlas_14',
                                    'tt_bkg_atlas_15',
                                    'tt_bkg_atlas_16', 'tt_bkg_atlas_17', 'tt_bkg_atlas_18', 'tt_bkg_atlas_19',
                                    'tt_bkg_atlas_20',
                                    'tt_bkg_atlas_21', 'tt_bkg_atlas_22', 'tt_bkg_atlas_23', 'tt_bkg_atlas_24',
                                    'tt_bkg_atlas_25',
                                    'tt_bkg_atlas_26', 'tt_bkg_atlas_27', 'tt_bkg_atlas_28', 'tt_bkg_atlas_29',
                                    'tt_bkg_atlas_30',
                                    'tt_bkg_atlas_31', 'tt_bkg_atlas_32', 'tt_bkg_atlas_33', 'tt_bkg_atlas_34',
                                    'tt_bkg_atlas_35',
                                    'tt_bkg_atlas_36', 'tt_bkg_atlas_37', 'tt_bkg_atlas_38', 'tt_bkg_atlas_39',
                                    'tt_bkg_atlas_40',
                                    'tt_bkg_atlas_41', 'tt_bkg_atlas_42', 'tt_bkg_atlas_43', 'tt_bkg_atlas_44',
                                    'tt_bkg_atlas_45',
                                    'tt_bkg_atlas_46', 'tt_bkg_atlas_47', 'tt_bkg_atlas_48', 'tt_bkg_atlas_49',
                                    'tt_bkg_atlas_50'],
                                   ['llll_bkg_atlas'],
                                   ['lllv_large_bkg_atlas'],
                                   ['lllv_small_bkg_atlas']]

# zp_mass_list = [5, 10, 20, 30, 40, 50, 60]
zp_mass_list: List[float] = [4, 5, 10, 20, 30, 40, 50, 60, 75]
zp_draw_list: List[bool] = [True, True, False, True, False, True, False, True, True]
zp_window_list: List[float] = [2, 2, 3.5, 4.9, 14.9, 24, 34, 49]
zp_window_list_atlas: List[float] = [2, 2, 3.5, 4.9, 14.9, 24, 34, 49]

# sgn_cross_section_list_original: List[float] = [0.05252, 0.04387, 0.0294, 0.01107, 0.003438, 0.0009372, 0.0001966, 0.00002434, 0.000000353]
# sgn_cross_section_list_original_atlas: List[float] = [0.02495, 0.02004, 0.01348, 0.004809, 0.001492, 0.0004124, 0.0000831, 0.00001094, 0.0000001591]

sgn_cross_section_list_original: List[float] = [0.2839, 0.163, 0.03877, 0.008192, 0.002173, 0.0005534, 0.0001125, 0.0000138, 0.000000198] # anomalous xs
sgn_cross_section_list_original_atlas: List[float] = [0.1366, 0.07723, 0.01798, 0.003573, 0.0009608, 0.0002342, 0.0000473,
                                                      0.000006072, 0.00000008885]  # anomalous xs

# sgn_efficiency_list: List[float] = [0.042, 0.089, 0.087, 0.13, 0.18, 0.2, 0.2, 0.17, 0.0078]
# sgn_efficiency_list_atlas: List[float] = [0.049, 0.11, 0.11, 0.17, 0.25, 0.33, 0.34, 0.29, 0.016]
sgn_efficiency_list: List[float] = [0.06, 0.13, 0.12, 0.14, 0.17, 0.19, 0.19, 0.16, 0.0073]  # anomalous xs
sgn_efficiency_list_atlas: List[float] = [0.073, 0.16, 0.16, 0.19, 0.24, 0.31, 0.33, 0.28, 0.016]  # anomalous xs

sgn_cross_section_list: List[float] = [i * j for i, j in zip(sgn_cross_section_list_original, sgn_efficiency_list)]
sgn_cross_section_list_atlas: List[float] = [i * j for i, j in
                                             zip(sgn_cross_section_list_original_atlas, sgn_efficiency_list_atlas)]

sm_cross_section_list: List[float] = [0.6142, 688.4, 0.3411, 0.9096, 0.04704]
sm_cross_section_list_atlas: List[float] = [0.3152, 584.1, 0.1408, 0.4263, 0.02335]

sm_mlll_efficiency_list: List[float] = [0.011, 0.0000057, 0.014, 0.0041, 0.0084]
sm_mlll_efficiency_list_atlas = [0.087, 0.0000054, 0.016, 0.0054, 0.0054]

sm_total_cross_section: float = np.sum(np.multiply(sm_cross_section_list, sm_mlll_efficiency_list))
sm_total_cross_section_atlas: float = np.sum(np.multiply(sm_cross_section_list_atlas, sm_mlll_efficiency_list_atlas))

sm_weight_list: List[float] = [
    (i * j / np.sum(np.multiply(sm_cross_section_list, sm_mlll_efficiency_list))) for i, j in
    zip(sm_cross_section_list, sm_mlll_efficiency_list)]
sm_weight_list_atlas: List[float] = [
    (i * j / np.sum(np.multiply(sm_cross_section_list_atlas, sm_mlll_efficiency_list_atlas))) for i, j in
    zip(sm_cross_section_list_atlas, sm_mlll_efficiency_list_atlas)]

luminosity: float = 3000000
luminosity_atlas: float = 150000
muon_mass: float = 0.1056583745

g_set = 0.01

histogram_title = 'All Hist'
histogram_title_atlas = 'All Hist Run2'
# histogram_full_path = './hist_cut/hist_all_hllhc.pdf'
# histogram_full_path_atlas = './hist_cut/hist_all_atlas.pdf'

# histogram_full_path = './hist_cut/hist_all_hllhc.png'
# histogram_full_path_atlas = './hist_cut/hist_all_atlas.png'
histogram_full_path = './hist_cut/hist_all_anomalous_hllhc.png' # anomalous xs
histogram_full_path_atlas = './hist_cut/hist_all_anomalous_atlas.png' # anomalous xs

# histogram_csv_full_path = './hist_cut/hist_all_hllhc_'
# histogram_csv_full_path_atlas = './hist_cut/hist_all_atlas_'
histogram_csv_full_path = './hist_cut/hist_all_anomalous_hllhc_' # anomalous xs
histogram_csv_full_path_atlas = './hist_cut/hist_all_anomalous_atlas_' # anomalous xs

# projected_sensitivity_plot_title = 'Projected Sensitivity HLLHC'
# projected_sensitivity_plot_title_atlas = 'Projected Sensitivity Run2'
projected_sensitivity_plot_title = 'Projected Sensitivity Anomalous HLLHC' # anomalous xs
projected_sensitivity_plot_title_atlas = 'Projected Sensitivity Anomalous Run2' # anomalous xs

# projected_sensitivity_plot_full_path = './hist_cut/projected_sensitivity_hllhc.pdf' 
# projected_sensitivity_plot_full_path_atlas = './hist_cut/projected_sensitivity_atlas.pdf' 
projected_sensitivity_plot_full_path = './hist_cut/projected_sensitivity_anomalous_hllhc.pdf' # anomalous xs
projected_sensitivity_plot_full_path_atlas = './hist_cut/projected_sensitivity_anomalous_atlas.pdf' # anomalous xs


cut_flow_table_title = 'Cut Flow Table HLLHC'
cut_flow_table_title_atlas = 'Cut Flow Table Run2'
cut_flow_table_full_path = './hist_cut/cut_flow_table_hllhc.pdf'
cut_flow_table_full_path_atlas = './hist_cut/cut_flow_table_atlas.pdf'

table_title = ['parton-lv preselection', 'Muon = 3 , Jet <= 2', 'PT > 5 GeV', '1.5 <  M(ll) < 2.8 GeV | M(ll) > 4 GeV',
               'M(ll) Cut']
table_width = 16
table_width_atlas = 18


def make_best_horizontal_cut(sgn_l_third_pt: np.ndarray,
                             sgn_original_number: int,
                             sgn_cross_section: float,
                             bkg_l_third_pt_list: List[np.ndarray],
                             bkg_original_number_list: List[int],
                             bkg_total_cross_section: float,
                             bkg_weight_list: List[float]) -> Tuple[float, float]:
    global luminosity
    horizontal_list = np.arange(5, 100, 0.1)
    sgn_upper_number_list: List[int] = []
    sgn_lower_number_list: List[int] = []
    bkg_upper_eff_list: List[int] = []
    bkg_lower_eff_list: List[int] = []
    for cut in horizontal_list:
        sgn_upper_number = sgn_l_third_pt[sgn_l_third_pt > cut]
        sgn_lower_number = sgn_l_third_pt[sgn_l_third_pt <= cut]
        sgn_upper_number_list.append(len(sgn_upper_number))
        sgn_lower_number_list.append(len(sgn_lower_number))

        bkg_upper_eff: float = 0
        bkg_lower_eff: float = 0
        for event_index, bkg_l_third_pt in enumerate(bkg_l_third_pt_list):
            bkg_upper_number = bkg_l_third_pt[bkg_l_third_pt > cut]
            bkg_lower_number = bkg_l_third_pt[bkg_l_third_pt <= cut]
            bkg_upper_eff += len(bkg_upper_number) * bkg_weight_list[event_index] / bkg_original_number_list[
                event_index]
            bkg_lower_eff += len(bkg_lower_number) * bkg_weight_list[event_index] / bkg_original_number_list[
                event_index]
        bkg_upper_eff_list.append(bkg_upper_eff)
        bkg_lower_eff_list.append(bkg_lower_eff)

    remove_cut_index: List[int] = []
    for i in range(len(horizontal_list)):
        if sgn_upper_number_list[i] * sgn_lower_number_list[i] * bkg_upper_eff_list[i] * bkg_lower_eff_list[
            i] == 0:
            if sgn_lower_number_list[i] == 0 and bkg_lower_eff_list[i] == 0 and sgn_upper_number_list[i] != 0 and \
                    bkg_upper_eff_list[i] != 0:
                continue
            else:
                remove_cut_index.append(i)
    horizontal_list = np.delete(horizontal_list, remove_cut_index)
    sgn_lower_number_list = np.delete(sgn_lower_number_list, remove_cut_index)
    sgn_upper_number_list = np.delete(sgn_upper_number_list, remove_cut_index)
    bkg_lower_eff_list = np.delete(bkg_lower_eff_list, remove_cut_index)
    bkg_upper_eff_list = np.delete(bkg_upper_eff_list, remove_cut_index)

    sgn_efficiency_upper = sgn_cross_section * luminosity * np.array(sgn_upper_number_list) / sgn_original_number
    sgn_efficiency_lower = sgn_cross_section * luminosity * np.array(sgn_lower_number_list) / sgn_original_number
    bkg_upper_efficiency = bkg_total_cross_section * luminosity * np.array(bkg_upper_eff_list)
    # bkg: total_xs * lumi * sum(weight[i] （fake之前的） * upper_number[i]) / number after mlll<80 （fake之后的）)
    bkg_lower_efficiency = bkg_total_cross_section * luminosity * np.array(bkg_lower_eff_list)

    efficiency_upper = sgn_efficiency_upper / np.sqrt(bkg_upper_efficiency)

    efficiency_lower: np.ndarray = np.zeros_like(efficiency_upper)
    for i in range(len(bkg_lower_efficiency)):
        if bkg_lower_efficiency[i] == 0:
            efficiency_lower[i] = 0
        else:
            efficiency_lower[i] = sgn_efficiency_lower[i] / np.sqrt(bkg_lower_efficiency[i])
    efficiency = np.sqrt(efficiency_upper ** 2 + efficiency_lower ** 2)
    max_efficiency: float = np.max(efficiency)
    max_efficiency_cut: float = horizontal_list[np.argmax(efficiency)].min()
    g_min_after_cut = g_set * np.sqrt(2 / max_efficiency)

    if len(efficiency) == 0:
        return None, None
    return max_efficiency_cut, g_min_after_cut


class TrileptonInvariantMass:
    def __init__(self,
                 event_name: str,
                 cross_section: float,
                 ll_invariant_mass: np.ndarray = np.array([]), l_third_pt: np.ndarray = np.array([]),
                 zp_mass: float = None,
                 is_bkg: bool = False):

        self.cross_section: float = cross_section
        self.is_bkg: bool = is_bkg
        self.event_name: str = event_name
        if not is_bkg:
            self.zp_mass: float = zp_mass

        self.ll_invariant_mass_history: List[np.ndarray] = []
        self.l_third_pt_history: List[np.ndarray] = []
        self.l_third_pt_history.append(l_third_pt)
        self.cut_history_number: np.ndarray = np.array([])
        if len(ll_invariant_mass) != 0:
            self.ll_invariant_mass_history.append(ll_invariant_mass)
            self.l_third_pt_history.append(l_third_pt)
            np.append(self.cut_history_number, ll_invariant_mass.shape[0])

    # def __check_if_validate(self) -> None:
    #     for i in range(len(self.ll_invariant_mass_history)):
    #         for j in range(len(self.ll_invariant_mass_history[i])):
    #             if len(self.ll_invariant_mass_history[i][j]) != len(self.l_third_pt_history[i][j]):
    #                 raise ValueError('The length of data is not the same.')

    def add_events(self, ll_invariant_mass: np.ndarray, l_third_pt: np.ndarray, is_bkg: False) -> None:
        if len(self.ll_invariant_mass_history) == 0:
            self.ll_invariant_mass_history.append(ll_invariant_mass)
            self.l_third_pt_history.append(l_third_pt)
            self.cut_history_number = np.array([ll_invariant_mass.shape[0]])
        else:
            np.append(self.ll_invariant_mass_history[0], ll_invariant_mass, axis=0)
            np.append(self.l_third_pt_history[0], l_third_pt, axis=0)
        self.is_bkg = is_bkg

    def __add_cut_history(self, cut_number: int) -> None:
        np.append(self.cut_history_number, cut_number)

    def make_cut(self,
                 ll_cut_upper: float = None,
                 ll_cut_lower: float = None,
                 l_cut_upper: float = None,
                 l_cut_lower: float = None) -> None:

        # copy and append the data
        ll_last = copy.deepcopy(self.ll_invariant_mass_history[-1])
        l_last = copy.deepcopy(self.l_third_pt_history[-1])
        if ll_cut_upper is not None:
            l_last = l_last[ll_last < ll_cut_upper]
            ll_last = ll_last[ll_last < ll_cut_upper]
        if ll_cut_lower is not None:
            l_last = l_last[ll_last > ll_cut_lower]
            ll_last = ll_last[ll_last > ll_cut_lower]
        if l_cut_upper is not None:
            ll_last = ll_last[l_last < l_cut_upper]
            l_last = l_last[l_last < l_cut_upper]
        if l_cut_lower is not None:
            ll_last = ll_last[l_last > l_cut_lower]
            l_last = l_last[l_last > l_cut_lower]

        self.ll_invariant_mass_history.append(ll_last)
        self.l_third_pt_history.append(l_last)
        # self.__check_if_validate()
        self.__add_cut_history(ll_last.shape[0])

        # TODO push to cut flow table


class ProjectedSensitivityPlot:
    def __init__(self, plot_num: int = 500) -> None:
        self.plot_number: int = plot_num
        self.g_min: List[float] = []
        self.g_min_combination: List[float] = []
        self.zp_mass_list: List[float] = []

    def __check_data_valid(self) -> None:
        if len(self.zp_mass_list) != len(self.g_min) or len(self.zp_mass_list) != len(self.g_min_combination):
            raise ValueError('The length of data is not the same.')

    def add_data(self, zp_mass: float, g_min: float, g_min_combination: float) -> None:
        self.zp_mass_list.append(zp_mass)
        self.g_min.append(g_min)
        if g_min_combination is not None:
            self.g_min_combination.append(g_min_combination)
        else:
            self.g_min_combination.append(-5)

    def draw_plot(self, output_pdf_full_path: str, plot_title: str) -> None:
        self.__check_data_valid()
        plt.figure(self.plot_number)
        plt.scatter(self.zp_mass_list, self.g_min, color='red', s=8, marker='x', label='$g\'_{min}$')
        zp_mass_list_filtered = [self.zp_mass_list[i] for i in range(len(self.zp_mass_list)) if
                                 self.g_min_combination[i] != -5]
        g_min_combination_filtered = [self.g_min_combination[i] for i in range(len(self.zp_mass_list)) if
                                      self.g_min_combination[i] != -5]
        print("gmin: " + str(self.g_min))
        print("gmin_after_horizontal_cut: " + str(g_min_combination_filtered))
        plt.scatter(zp_mass_list_filtered, g_min_combination_filtered, color='blue', s=8, marker='*',
                    label='$g\'$ after horizontal cut')
        plt.xlabel('Mass_zp')
        plt.ylabel('$g\'_{min}$')
        plt.legend()
        plt.xlim(0.01, 1000)
        plt.ylim(0.00001, 1)
        ticks: List[float] = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
        labels: List[str] = ['0.001', '0.01', '0.1', '1', '10', '100', '1000']
        plt.xticks(ticks, labels)
        plt.xscale('log')
        plt.yscale('log')
        plt.title(plot_title)
        plt.savefig(output_pdf_full_path, format="pdf")
        plt.close(self.plot_number)


def determine_best_cut_width(zp_mass: float,
                             sgn_event: TrileptonInvariantMass,
                             bkg_event_list: List[TrileptonInvariantMass]) -> float:
    window_list = np.arange(2, 55, 0.1)
    sgn_cut_efficiency: List[float] = []
    bkg_cut_efficiency: List[float] = []
    for width in window_list:
        sgn_ll_invariant_mass_close = sgn_event.ll_invariant_mass_history[-1]
        sgn_cut_efficiency_point = sgn_ll_invariant_mass_close[
            (sgn_ll_invariant_mass_close > (zp_mass - width)) & (sgn_ll_invariant_mass_close < (zp_mass + width))]
        sgn_cut_efficiency.append(len(sgn_cut_efficiency_point))

        bkg_sum_cut_efficiency: float = 0
        for bkg_index, bkg_event in enumerate(bkg_event_list):
            bkg_ll_invariant_mass_close = bkg_event.ll_invariant_mass_history[-1]
            bkg_cut_efficiency_point = bkg_ll_invariant_mass_close[
                (bkg_ll_invariant_mass_close > (zp_mass - width)) & (bkg_ll_invariant_mass_close < (zp_mass + width))]
            bkg_sum_cut_efficiency += len(bkg_cut_efficiency_point * sm_weight_list[bkg_index])
        # weight[i]= sigma[i] * eff[i] / sum(sigma[j] * eff[j]) (eff 是没有fake的情况 ttbar = 0.00054%)
        # bkg_eff = sum(weight[i] * bkg_cut_efficiency[i]), i = 0,1,2,3,4 (这里的eff是fake的)
        # if bkg_eff = 0 then

        if bkg_sum_cut_efficiency != 0:
            bkg_cut_efficiency.append(bkg_sum_cut_efficiency)
        else:
            bkg_cut_efficiency.append(1)

    bestCut = window_list[np.argmax(np.array(sgn_cut_efficiency) / np.sqrt(np.array(bkg_cut_efficiency)))]
    # make the cut
    sgn_event.make_cut(ll_cut_upper=zp_mass + bestCut, ll_cut_lower=zp_mass - bestCut)
    for bkg_event in bkg_event_list:
        bkg_event.make_cut(ll_cut_upper=zp_mass + bestCut, ll_cut_lower=zp_mass - bestCut)
    return window_list[np.argmax(np.array(sgn_cut_efficiency) / np.sqrt(np.array(bkg_cut_efficiency)))]


class Histogram:
    def __init__(self, histogram_num: int = 400):
        self.data_stack: List[TrileptonInvariantMass] = []
        self.histogram_num: int = histogram_num
        self.if_draw_list: List[bool] = []

    def add_data(self, data: TrileptonInvariantMass, if_draw_data: bool) -> None:
        data_copy = copy.deepcopy(data)
        self.data_stack.append(data_copy)
        self.if_draw_list.append(if_draw_data)
        del data_copy

    def draw_hist(self, output_pdf_full_path: str, bins: np.ndarray = np.arange(0, 80, 1)) -> None:
        plt.figure(self.histogram_num)
        for index, data in enumerate(self.data_stack):
            if self.if_draw_list[index]:
                if data.is_bkg:
                    if 'tt' in data.event_name:
                        data.ll_invariant_mass_history[-1]
                    plt.hist(data.ll_invariant_mass_history[-1],
                             bins=bins,
                             histtype='step',
                             density=True,
                             label=str(data.event_name))
                    print('{} hist done.'.format(data.event_name))
                else:
                    plt.hist(data.ll_invariant_mass_history[-1],
                             bins=bins,
                             histtype='step',
                             density=True,
                             label=r'$m_{{Z^{{\prime}}}}={}$ GeV'.format(data.zp_mass))
                    print(str(data.zp_mass) + ' hist done.')
            else:
                print(str(data.zp_mass) + ' not draw.')
        print('All hists done.')
        plt.legend()
        # plt.title('event')
        plt.yscale('log')
        plt.xlabel('$m_{min}(\mu\mu)$[GeV]')
        plt.ylabel('Probability Density [GeV$^{-1}$]')
        # plt.savefig(output_pdf_full_path, format="pdf")
        plt.savefig(output_pdf_full_path, format="png")

    def output_csv(self, output_csv_full_path: str) -> None:
        for data in self.data_stack:
            heights, _ = np.histogram(data.ll_invariant_mass_history[0], bins=40, range=(0, 80), density=True)
            np.savetxt(output_csv_full_path + data.event_name + '_mll.csv', heights, delimiter=',')


# class CutFlowTable:
#     bkg_data: List[List[int]]  # [[number(int) after cut1, ... , number(int) after final cut], ...]
#     bkg_cross_section: float
#     sgn_data: List[List[int]]  # [[number(int) after cut1, ... , number(int) after final cut], ...]
#     table_title: List[str]  # only contains cut titles
#     sgn_name: List[str]
#     sgn_cross_section: np.ndarray

#     def __init__(self,
#                  table_title: List[str],
#                  sgn_name: List[str],
#                  bkg_cross_section: float = None):
#         self.sgn_name = sgn_name
#         self.table_title = table_title
#         self.bkg_cross_section = bkg_cross_section
#         self.sgn_data = []
#         self.bkg_data = []

#         # initialize the data
#         for _ in range(len(sgn_name)):
#             self.sgn_data.append([])
#             self.bkg_data.append([])

#     def __check_data_valid(self) -> None:
#         if len(self.table_title) != len(self.bkg_data[0]) \
#                 or any(len(data) != len(self.table_title) for data in self.sgn_data):
#             raise ValueError('The length of data is not the same as the title.')

#     def set_bkg_cross_section(self, cross_section: float) -> None:
#         self.bkg_cross_section = cross_section

#     def set_sgn_cross_sections(self, sgn_cross_section: np.ndarray) -> None:
#         self.sgn_cross_section = sgn_cross_section

#     def push_cut(self, data: int,
#                  is_bkg: bool = False,
#                  data_name: str = None) -> None:
#         if data_name is not None:
#             if any(name == data_name for name in self.sgn_name):
#                 name_index = self.sgn_name.index(data_name)
#                 if is_bkg:
#                     self.bkg_data[name_index].append(data)
#                 else:
#                     self.sgn_data[name_index].append(data)
#             else:
#                 raise ValueError('This data is not bkg but the sgn name is not provided.')
#         elif is_bkg:
#             for i in range(len(self.bkg_data)):
#                 self.bkg_data[i].append(data)
#         else:
#             raise ValueError('Name is not provided.')

#     def draw_table(self, output_fig_full_path: str, table_caption: str, table_width: float) -> None:
#         # group bkg data according to the len(self.table_title) - 1
#         for i in range(len(self.sgn_data)):
#             group_size = len(self.table_title) - 1
#             remain = self.bkg_data[i][-1]
#             bkg_row_chopped = self.bkg_data[i][:-1]
#             bkg_row_reshape = np.array(bkg_row_chopped).reshape(-1, group_size)
#             summed_bkg_row = np.sum(bkg_row_reshape, axis=0)
#             self.bkg_data[i] = summed_bkg_row.tolist()
#             self.bkg_data[i].append(remain)

#         self.__check_data_valid()
#         data_table: List[List[str]] = []
#         title_row: List[str] = ['event', 'cross section'] + self.table_title
#         data_table.append(title_row)
#         del title_row
#         for index, sgn in enumerate(self.sgn_name):
#             row: List[str] = [f'{sgn}(SM)', f'{self.sgn_cross_section[index]:.3g}({self.bkg_cross_section:.3g})']
#             sgn_row = self.sgn_data[index]
#             # print("sgn row:" + str(sgn_row))
#             bkg_row = self.bkg_data[index]
#             # print("bkg row:" + str(self.bkg_data))
#             for i in range(len(sgn_row)):
#                 sgn_ratio = sgn_row[i] / sgn_row[0] * 100
#                 bkg_ratio = bkg_row[i] / bkg_row[0] * 100
#                 row.append(f'{sgn_row[i]}[{sgn_ratio:.3g}%]({bkg_row[i]}[{bkg_ratio:.3g}%])')
#             data_table.append(row)

#         plt.figure(figsize=(table_width, 4))
#         plt.title(table_caption)
#         plt.axis('off')
#         table = plt.table(cellText=data_table, loc='center', cellLoc='center', colLabels=None)
#         table.auto_set_font_size(False)
#         table.set_fontsize(10)
#         table.scale(1, 1.5)
#         table.auto_set_column_width([i for i in range(len(self.table_title) + 2)])
#         plt.savefig(output_fig_full_path)


def derive_data(event: str, data: TrileptonInvariantMass, is_bkg: bool) -> None:
    print('Extracting ' + event + '...')
    file_location = './hist_cut/ll_data/'

    ll_data = np.load(file_location + event + '_ll_invariant_mass_close.npy')
    print(ll_data)
    l_data = np.load(file_location + event + '_ll_pt_close_third.npy')

    data.add_events(ll_data, l_data, is_bkg)


def run_analysis(is_hllhc: bool = True) -> None:
    global sgn_list
    global sgn_list_atlas  # todo merge this in the future
    global bkg_list
    global bkg_list_atlas

    global zp_window_list
    global zp_window_list_atlas

    global sgn_cross_section_list
    global sgn_cross_section_list_atlas

    global luminosity
    global luminosity_atlas

    global histogram_title
    global histogram_title_atlas
    global histogram_full_path
    global histogram_full_path_atlas
    global histogram_csv_full_path
    global histogram_csv_full_path_atlas
    global projected_sensitivity_plot_title
    global projected_sensitivity_plot_title_atlas
    global projected_sensitivity_plot_full_path
    global projected_sensitivity_plot_full_path_atlas
    global cut_flow_table_title
    global cut_flow_table_title_atlas
    global cut_flow_table_full_path
    global cut_flow_table_full_path_atlas

    global table_width
    global table_width_atlas

    if not is_hllhc:
        sgn_list = sgn_list_atlas
        bkg_list = bkg_list_atlas
        zp_window_list = zp_window_list_atlas
        sgn_cross_section_list = sgn_cross_section_list_atlas
        luminosity = luminosity_atlas
        histogram_title = histogram_title_atlas
        histogram_full_path = histogram_full_path_atlas
        histogram_csv_full_path = histogram_csv_full_path_atlas
        projected_sensitivity_plot_title = projected_sensitivity_plot_title_atlas
        projected_sensitivity_plot_full_path = projected_sensitivity_plot_full_path_atlas
        cut_flow_table_title = cut_flow_table_title_atlas
        cut_flow_table_full_path = cut_flow_table_full_path_atlas
        table_width = table_width_atlas

    all_hist = Histogram()
    # cut_flow_table = CutFlowTable(table_title, sgn_name=sgn_list)
    # cut_flow_table.set_bkg_cross_section(sm_cross_section)
    # cut_flow_table.set_sgn_cross_sections(np.array(sgn_cross_section_list))

    projected_sensitivity_plot = ProjectedSensitivityPlot()

    # load all sm data
    bkg_data_list_copy: List[TrileptonInvariantMass] = []
    for event_index, event_list in enumerate(bkg_list):
        # remove the '_number' in the event name, only for bkg because sgn only has one event
        parts = event_list[0].split("_")  # 分割字符串
        if parts[-1].isdigit():  # 检查最后一部分是否是数字
            parts = parts[:-1]  # 如果是，移除它
        event_name = "_".join(parts)  # 重新连接字符串
        bkg_event_data: TrileptonInvariantMass = TrileptonInvariantMass(
            cross_section=sm_cross_section_list[event_index],
            event_name=event_name,
            is_bkg=True)
        for event in event_list:
            derive_data(event, bkg_event_data, is_bkg=True)
        bkg_data_list_copy.append(bkg_event_data)

    # add sm to histogram
    for bkg_data in bkg_data_list_copy:
        all_hist.add_data(bkg_data, True)

    for event_index, event in enumerate(sgn_list):
        zp_mass: float = zp_mass_list[event_index]
        bsm_data: TrileptonInvariantMass = TrileptonInvariantMass(
            event_name=event,
            cross_section=sgn_cross_section_list[event_index],
            zp_mass=zp_mass)
        derive_data(event, bsm_data, False)
        # copy sm data for date processing
        bkg_data_list: TrileptonInvariantMass = copy.deepcopy(bkg_data_list_copy)

        # record the original number of bsm and sm
        bsm_original_number: int = bsm_data.ll_invariant_mass_history[0].shape[0]
        bkg_original_number_list: List[int] = [bkg_data.ll_invariant_mass_history[0].shape[0] for bkg_data in
                                               bkg_data_list]
        print("bkg original number: " + str(bkg_original_number_list))

        # add to histogram
        all_hist.add_data(bsm_data, zp_draw_list[event_index])

        # make cuts
        # determine the best vertical cut width``
        cut_width: float = determine_best_cut_width(zp_mass, bsm_data,
                                                    bkg_data_list)
        print(f'{event}\'s best cut width: {cut_width: .1f}')
        # # add to cut flow table
        # cut_flow_table.push_cut(bsm_data.ll_invariant_mass_history.shape[0], False, event)
        # cut_flow_table.push_cut(sm_data.ll_invariant_mass_history.shape[0], True, event)
        # # delete all te
        print("BSM number: {}".format(bsm_data.ll_invariant_mass_history[-1].shape[0]))
        for bkg_data in bkg_data_list:
            print("{} number: {}".format((bkg_data.event_name), bkg_data.ll_invariant_mass_history[-1].shape[0]))

        # calculate g_min and g_min_after_horizontal_cut
        s = sgn_cross_section_list[event_index] * luminosity * bsm_data.ll_invariant_mass_history[-1].shape[
            0] / bsm_original_number
        # print(str(bsm_data.ll_invariant_mass.shape[0]))
        b: float = 0
        for bkg_index, bkg_event in enumerate(bkg_data_list):
            b += sm_total_cross_section * luminosity \
                 * sm_weight_list[bkg_index] \
                 * bkg_event.ll_invariant_mass_history[-1].shape[0] / bkg_original_number_list[bkg_index]
        # change sm_cross_section into sigma_total
        # sum(sm_data.ll_invariant_mass.shape[0] （fake之后）* weight（fake之前的） / number after mlll < 80 GeV（fake之后的）)

        if b == 0:
            g_min = g_set * np.sqrt(3 / s)
            g_min_after_horizontal_cut = None
        else:
            g_min = g_set * np.sqrt(2 / (s / np.sqrt(b)))

            # make horizontal cut
            bkg_l_third_pt_list: List[np.ndarray] = [bkg_event.l_third_pt_history[-1] for bkg_event in bkg_data_list]
            horizontal_cut, g_min_after_horizontal_cut = make_best_horizontal_cut(
                sgn_l_third_pt=bsm_data.l_third_pt_history[-1],
                sgn_original_number=bsm_original_number,
                sgn_cross_section=bsm_data.cross_section,
                bkg_l_third_pt_list=bkg_l_third_pt_list,
                bkg_original_number_list=bkg_original_number_list,
                bkg_total_cross_section=sm_total_cross_section,
                bkg_weight_list=sm_weight_list)
            if horizontal_cut is None:
                g_min_after_horizontal_cut = g_min
        # add to projected sensitivity plot
        projected_sensitivity_plot.add_data(zp_mass, g_min, g_min_after_horizontal_cut)

    # draw all histograms
    all_hist.draw_hist(histogram_full_path)
    all_hist.output_csv(histogram_csv_full_path)

    # draw cut flow table
    # cut_flow_table.draw_table(cut_flow_table_full_path, cut_flow_table_title, table_width=table_width)

    # draw projected sensitivity plot
    projected_sensitivity_plot.draw_plot(projected_sensitivity_plot_full_path, projected_sensitivity_plot_title)


if __name__ == '__main__':
    run_analysis()
    # run_analysis(is_hllhc=False)
