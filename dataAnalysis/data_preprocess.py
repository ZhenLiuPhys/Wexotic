# standard library imports
# from __future__ import absolute_import, division, print_function
import math
from typing import List

# standard numerical library imports
import numpy as np


# load_data
# def load_data(loaded_event_list=None, data_num=1000000) -> [np.ndarray, np.ndarray]:
def load_data(loaded_event_list=None, data_num=30000, no_z=False, is_atlas=False) -> [np.ndarray, np.ndarray]:
    loaded_event = {}
    if is_atlas:
        loaded_event['lllv_signal_data'] = np.load('./data/lllv_signal_atlas_data.npy')
        loaded_event['lllv_signal_label'] = np.load('./data/lllv_signal_atlas_label.npy')
        
        loaded_event['llll_bkg_data'] = np.load('./data/llll_bkg_atlas_data.npy')
        loaded_event['llll_bkg_label'] = np.load('./data/llll_bkg_atlas_label.npy')
        
        loaded_event['lllv_large_bkg_data'] = np.load('./data/lllv_large_bkg_atlas_data.npy')
        loaded_event['lllv_large_bkg_label'] = np.load('./data/lllv_large_bkg_atlas_label.npy')
        
        loaded_event['lllv_small_bkg_data'] = np.load('./data/lllv_small_bkg_atlas_data.npy')
        loaded_event['lllv_small_bkg_label'] = np.load('./data/lllv_small_bkg_atlas_label.npy')
        print("Processing atlas data...")
    else:
        loaded_event['lllv_signal_data'] = np.load('./data/lllv_signal_data.npy')
        loaded_event['lllv_signal_label'] = np.load('./data/lllv_signal_label.npy')
        
        loaded_event['llll_bkg_data'] = np.load('./data/llll_bkg_data.npy')
        loaded_event['llll_bkg_label'] = np.load('./data/llll_bkg_label.npy')
        
        loaded_event['lllv_large_bkg_data'] = np.load('./data/lllv_large_bkg_data.npy')
        loaded_event['lllv_large_bkg_label'] = np.load('./data/lllv_large_bkg_label.npy')
        
        loaded_event['lllv_small_bkg_data'] = np.load('./data/lllv_small_bkg_data.npy')
        loaded_event['lllv_small_bkg_label'] = np.load('./data/lllv_small_bkg_label.npy')
        print("Processing hllhc data...")
    
    tt_bkg_data = np.load('./data/tt_bkg_1_data.npy')
    tt_bkg_label = np.load('./data/tt_bkg_1_label.npy')
    for i in range(2, 50):
        tt_bkg_data = np.concatenate((tt_bkg_data, np.load('./data/tt_bkg_' + str(i) + '_data.npy')), axis=0)
        tt_bkg_label = np.concatenate((tt_bkg_label, np.load('./data/tt_bkg_' + str(i) + '_label.npy')), axis=0)
    loaded_event['tt_bkg_data'] = tt_bkg_data
    loaded_event['tt_bkg_label'] = tt_bkg_label
    del tt_bkg_data, tt_bkg_label
    

    print('lllv_signal_shape: ', loaded_event['lllv_signal_data'].shape, loaded_event['lllv_signal_label'].shape)
    print('llll_bkg_shape: ', loaded_event['llll_bkg_data'].shape, loaded_event['llll_bkg_label'].shape)
    print('lllv_large_bkg_shape: ', loaded_event['lllv_large_bkg_data'].shape, loaded_event['lllv_large_bkg_label'].shape)
    print('lllv_small_bkg_shape: ', loaded_event['lllv_small_bkg_data'].shape, loaded_event['lllv_small_bkg_label'].shape)
    print('tt_bkg_shape: ', loaded_event['tt_bkg' + '_data'].shape, loaded_event['tt_bkg' + '_label'].shape)
    
    # cut three bkg data and sgn data to 1:1:1:3 according to the smallest data size
    min_size = min((loaded_event['lllv_signal_data'].shape[0] / 3), loaded_event['llll_bkg_data'].shape[0], loaded_event['lllv_large_bkg_data'].shape[0], loaded_event['tt_bkg_data'].shape[0])
    loaded_event['lllv_signal_data'] = loaded_event['lllv_signal_data'][:int(min_size * 3), :, :]
    loaded_event['lllv_signal_label'] = loaded_event['lllv_signal_label'][:int(min_size * 3)]
    loaded_event['llll_bkg_data'] = loaded_event['llll_bkg_data'][:int(min_size), :, :]
    loaded_event['llll_bkg_label'] = loaded_event['llll_bkg_label'][:int(min_size)]
    loaded_event['lllv_large_bkg_data'] = loaded_event['lllv_large_bkg_data'][:int(min_size), :, :]
    loaded_event['lllv_large_bkg_label'] = loaded_event['lllv_large_bkg_label'][:int(min_size)]
    loaded_event['lllv_small_bkg_data'] = loaded_event['lllv_small_bkg_data'][:int(min_size), :, :]
    loaded_event['lllv_small_bkg_label'] = loaded_event['lllv_small_bkg_label'][:int(min_size)]
    loaded_event['tt_bkg_data'] = loaded_event['tt_bkg_data'][:int(min_size), :, :]
    loaded_event['tt_bkg_label'] = loaded_event['tt_bkg_label'][:int(min_size)]
    
    print("cut to min size: ", min_size)
    sgn_data = np.concatenate((loaded_event['lllv_signal_data'], loaded_event['llll_bkg_data'], loaded_event['lllv_large_bkg_data'], loaded_event['tt_bkg_data']), axis=0) 
    sgn_label = np.concatenate((loaded_event['lllv_signal_label'], loaded_event['llll_bkg_label'], loaded_event['lllv_large_bkg_label'], loaded_event['tt_bkg_label']), axis=0)
    print('shape: ', sgn_data.shape, sgn_label.shape)
    
    assert no_z == False, 'no_z is deprecated'
    # if no_z:
    #     sgn_label = np.concatenate(
    #         (loaded_event['w_sgn_label'], loaded_event['wz_bkg_label'], loaded_event['tt_bkg_label']), axis=0)
    #     sgn_data = np.concatenate(
    #         (loaded_event['w_sgn_data'], loaded_event['wz_bkg_data'], loaded_event['tt_bkg_data']),
    #         axis=0)
    # else:
    #     sgn_data = np.concatenate((loaded_event['w_sgn_data'], loaded_event['wz_bkg_data'], loaded_event['tt_bkg_data'], loaded_event['z_bkg_data']),
    #                               axis=0)
    #     sgn_label = np.concatenate((loaded_event['w_sgn_label'], loaded_event['wz_bkg_label'], loaded_event['tt_bkg_label'], loaded_event['z_bkg_label']), axis=0)
    # print('shape: ', sgn_data.shape, sgn_label.shape)
    # sgn_label = np.concatenate((w_sgn_label_cut, w_z_bkg_label_cut), axis=0)
    return sgn_data, sgn_label
    # for name in loaded_event_list:
    #     try:
    #         if 'w_sgn' in name:
    #             if '1' in name:
    #                 loaded_event['w_sgn_data'] = np.load('./data/' + name + '_data.npy')
    #                 print(loaded_event['w_sgn_data'].shape)
    #                 loaded_event['w_sgn_label'] = np.load('./data/' + name + '_label.npy')
    #             else:
    #                 tmp_data = np.load('./data/' + name + '_data.npy')
    #                 print(tmp_data.shape)
    #                 np.concatenate((loaded_event['w_sgn_data'], tmp_data), axis=0)
    #                 tmp_label = np.load('./data/' + name + '_label.npy')
    #                 np.concatenate((loaded_event['w_sgn_label'], tmp_label), axis=0)
    #         elif 'w_z_bkg' in name:
    #             if '1' in name:
    #                 loaded_event['w_z_bkg_data'] = np.load('./data/' + name + '_data.npy')
    #                 print(loaded_event['w_z_bkg_data'].shape)
    #                 loaded_event['w_z_bkg_label'] = np.load('./data/' + name + '_label.npy')
    #             else:
    #                 tmp_data = np.load('./data/' + name + '_data.npy')
    #                 np.concatenate((loaded_event['w_z_bkg_data'], tmp_data), axis=0)
    #                 tmp_label = np.load('./data/' + name + '_label.npy')
    #                 np.concatenate((loaded_event['w_z_bkg_label'], tmp_label), axis=0)
    #     except FileNotFoundError:
    #         from data_extraction import extract_data
    #         extract_data()
    #         loaded_event[name + '_data'] = np.load('./data/' + name + '_data.npy')
    #         loaded_event[name + '_data'] = np.load('./data/' + name + '_label.npy')
    #     print('shape: ', loaded_event['w_sgn' + '_data'].shape, loaded_event['w_sgn' + '_label'].shape)
    #     print('shape: ', loaded_event['w_z_bkg' + '_data'].shape, loaded_event['w_z_bkg' + '_label'].shape)
    #     print(name + ' data and label loaded')

    # # expand the data
    # # cut w_z_bkg data to the same size as w_sgn_data
    # scale = math.ceil((data_num / (loaded_event['w_z_bkg_data'].shape[0] * 2)))
    # scale_sgn = math.ceil((loaded_event['w_z_bkg_data'].shape[0] / loaded_event['w_sgn_data'].shape[0]))
    #
    # w_sgn_data_expanded = np.tile(loaded_event['w_sgn_data'], (scale_sgn * scale, 1, 1))
    # w_sgn_label_expanded = np.repeat(loaded_event['w_sgn_label'], (scale_sgn * scale))
    # w_z_bkg_data_expanded = np.tile(loaded_event['w_z_bkg_data'], (scale + 1, 1, 1))
    # w_z_bkg_label_expanded = np.repeat(loaded_event['w_z_bkg_label'], (scale + 1))
    #
    # w_sgn_data_expanded = w_sgn_data_expanded[:int(data_num / 2), :]
    # w_sgn_label_expanded = w_sgn_label_expanded[:int(data_num / 2)]
    # w_z_bkg_data_expanded = w_z_bkg_data_expanded[:int(data_num / 2), :]
    # w_z_bkg_label_expanded = w_z_bkg_label_expanded[:int(data_num / 2)]
    #
    # data_expanded = np.concatenate((w_sgn_data_expanded, w_z_bkg_data_expanded), axis=0)
    # label_expanded = np.concatenate([w_sgn_label_expanded, w_z_bkg_label_expanded], axis=0)
    #
    # for name in loaded_event_list:
    #     print(name + ' data shape: ' + str(loaded_event[name + '_data'].shape))
    #
    # print('w_sgn_data_expanded:', w_sgn_data_expanded.shape)
    # print('w_z_bkg_data_expanded:', w_z_bkg_data_expanded.shape)
    # print('data_expanded_shape:', data_expanded.shape)
    # print('label_expanded_shape:', label_expanded.shape)
    #
    # return data_expanded, label_expanded
if __name__ == '__main__':
    load_data()