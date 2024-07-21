
def run_utilities(batch_size = 100, dim1 = 64, dim2 = 120, num_epoch = 100, is_atlas=False):
    pfn_result_folder = "./pfn_results/"
    utilities_result_folder = "./hllhc_results/"
    branch_ratio_title: str = "Signal Efficiency HLLHC"
    
    # standard numerical library imports
    import numpy as np
    from matplotlib import pyplot as plt

    # const
    luminosity = 3000000

    lllv_sgn_sigma_total = 0.6122  
    llll_bkg_sigma_total = 0.3421  
    tt_bkg_sigma_total = 689.6 
    lllv_bkg_sigma_total = 0.9132
    lllv_small_bkg_sigma_total = 0.04704
    pp_sgn_sigma_total = 158000
    

    lllv_sgn_sel_efficiency = 0.035  # from cut flow table
    llll_bkg_sel_efficiency = 0.05  # from cut flow table
    tt_bkg_sel_efficiency = 0.000033  # from cut flow table
    lllv_bkg_sel_efficiency = 0.013  # from cut flow table
    lllv_small_bkg_sel_efficiency = 0.028  # from cut flow table
    
    if is_atlas:
        batch_size = 100
        dim1 = 64
        dim2 = 128
        num_epoch = 100
        luminosity = 3000000 * 0.05
        lllv_sgn_sigma_total = 0.3152
        llll_bkg_sigma_total = 0.1408
        tt_bkg_sigma_total = 584.1
        lllv_bkg_sigma_total = 0.4263
        lllv_small_bkg_sigma_total = 0.02335
        
        lllv_sgn_sel_efficiency = 0.033
        llll_bkg_sel_efficiency = 0.064
        tt_bkg_sel_efficiency = 0.000056
        lllv_bkg_sel_efficiency = 0.02
        lllv_small_bkg_sel_efficiency = 0.021
        
        utilities_result_folder = "./atlas_results/"
        pfn_result_folder = "./pfn_run2_results/"
        branch_ratio_title: str = "Signal Efficiency RUN2"
        

    # load results
    llll_Y_test = np.load("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch)) + '-llll_Y_test.npy')
    llll_pfn_pred = np.load("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch)) + '-llll_preds.npy')
    llll_sgn_number = np.count_nonzero(llll_Y_test[:, 0] == 1)
    llll_bkg_number = np.count_nonzero(llll_Y_test[:, 1] == 1)
    print("shape is" + str(np.shape(llll_Y_test)))
    llll_sgn_efficiency = np.zeros(500)
    llll_bkg_efficiency = np.zeros(500)

    lllv_Y_test = np.load("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch)) + '-lllv_Y_test.npy')
    lllv_pfn_pred = np.load("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch)) + '-lllv_preds.npy')
    lllv_sgn_number = np.count_nonzero(lllv_Y_test[:, 0] == 1)
    lllv_bkg_number = np.count_nonzero(lllv_Y_test[:, 1] == 1)
    lllv_sgn_efficiency = np.zeros(500)
    lllv_bkg_efficiency = np.zeros(500)
    
    lllv_small_Y_test = np.load("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch)) + '-lllv_small_Y_test.npy')
    lllv_small_pfn_pred = np.load("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch)) + '-lllv_small_preds.npy')
    lllv_small_sgn_number = np.count_nonzero(lllv_small_Y_test[:, 0] == 1)
    lllv_small_bkg_number = np.count_nonzero(lllv_small_Y_test[:, 1] == 1)
    lllv_small_sgn_efficiency = np.zeros(500)
    lllv_small_bkg_efficiency = np.zeros(500)

    tt_Y_test = np.load("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch)) + '-tt_Y_test.npy')
    tt_pfn_pred = np.load("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch)) + '-tt_preds.npy')
    tt_sgn_number = np.count_nonzero(tt_Y_test[:, 0] == 1)
    tt_bkg_number = np.count_nonzero(tt_Y_test[:, 1] == 1)
    tt_bkg_efficiency = np.zeros(500)

    sgn_x = np.zeros(500)
    llll_sgn_x = np.zeros(500)
    lllv_sgn_x = np.zeros(500)
    tt_sgn_x = np.zeros(500)
    bkg_x = np.zeros(500)
    sgn_bkg_x = np.zeros(500)
    sgn_efficiency = np.zeros(500)
    tt_sgn_efficiency = np.zeros(500)
    llll_sgn_efficiency = np.zeros(500)
    lllv_sgn_efficiency = np.zeros(500)
    lllv_small_sgn_efficiency = np.zeros(500)
    
    j = 0
    for i in np.linspace(0, 100, 500):
        cut = 0.01 * i
        
        # llll bkg
        llll_sgn_condition = np.logical_and(llll_Y_test[:, 0] == 1, llll_pfn_pred[:, 1] <= cut)
        llll_bkg_condition = np.logical_and(llll_Y_test[:, 1] == 1, llll_pfn_pred[:, 1] <= cut)
        llll_sgn_cut = llll_pfn_pred[llll_sgn_condition, 0]
        llll_bkg_cut = llll_pfn_pred[llll_bkg_condition, 1]
        llll_sgn_cut_number = llll_sgn_cut.shape[0]
        llll_bkg_cut_number = llll_bkg_cut.shape[0]
        print('llll:', llll_sgn_cut_number, llll_bkg_cut_number)
        llll_sgn_eff = llll_sgn_cut_number / llll_sgn_number
        llll_sgn_efficiency[j] = llll_sgn_eff
        llll_bkg_eff = llll_bkg_cut_number / llll_bkg_number
        llll_bkg_efficiency[j] = llll_bkg_eff

        # lllv bkg
        lllv_sgn_condition = np.logical_and(lllv_Y_test[:, 0] == 1, lllv_pfn_pred[:, 1] <= cut)
        lllv_bkg_condition = np.logical_and(lllv_Y_test[:, 1] == 1, lllv_pfn_pred[:, 1] <= cut)
        lllv_sgn_cut = lllv_pfn_pred[lllv_sgn_condition, 0]
        lllv_bkg_cut = lllv_pfn_pred[lllv_bkg_condition, 1]
        lllv_sgn_cut_number = lllv_sgn_cut.shape[0]
        lllv_bkg_cut_number = lllv_bkg_cut.shape[0]
        print('lllv:', lllv_sgn_cut_number, lllv_bkg_cut_number)
        lllv_sgn_eff = lllv_sgn_cut_number / lllv_sgn_number
        lllv_sgn_efficiency[j] = lllv_sgn_eff
        lllv_bkg_eff = lllv_bkg_cut_number / lllv_bkg_number
        lllv_bkg_efficiency[j] = lllv_bkg_eff
        
        # lllv small bkg
        lllv_small_sgn_condition = np.logical_and(lllv_small_Y_test[:, 0] == 1, lllv_small_pfn_pred[:, 1] <= cut)
        lllv_small_bkg_condition = np.logical_and(lllv_small_Y_test[:, 1] == 1, lllv_small_pfn_pred[:, 1] <= cut)
        lllv_small_sgn_cut = lllv_small_pfn_pred[lllv_small_sgn_condition, 0]
        lllv_small_bkg_cut = lllv_small_pfn_pred[lllv_small_bkg_condition, 1]
        lllv_small_sgn_cut_number = lllv_small_sgn_cut.shape[0]
        lllv_small_bkg_cut_number = lllv_small_bkg_cut.shape[0]
        print('lllv small:', lllv_small_sgn_cut_number, lllv_small_bkg_cut_number)
        lllv_small_sgn_eff = lllv_small_sgn_cut_number / lllv_small_sgn_number
        lllv_small_sgn_efficiency[j] = lllv_small_sgn_eff
        lllv_small_bkg_eff = lllv_small_bkg_cut_number / lllv_small_bkg_number
        lllv_small_bkg_efficiency[j] = lllv_small_bkg_eff

        # tt
        tt_sgn_condition = np.logical_and(tt_Y_test[:, 0] == 1, tt_pfn_pred[:, 1] <= cut)
        tt_bkg_condition = np.logical_and(tt_Y_test[:, 1] == 1, tt_pfn_pred[:, 1] <= cut)
        tt_sgn_cut = tt_pfn_pred[tt_sgn_condition, 0]
        tt_bkg_cut = tt_pfn_pred[tt_bkg_condition, 1]
        tt_sgn_cut_number = tt_sgn_cut.shape[0]
        tt_bkg_cut_number = tt_bkg_cut.shape[0]
        print('tt:', tt_sgn_cut_number, tt_bkg_cut_number)
        tt_sgn_eff = tt_sgn_cut_number / tt_sgn_number
        tt_sgn_efficiency[j] = tt_sgn_cut_number / tt_sgn_number
        tt_bkg_eff = tt_bkg_cut_number / tt_bkg_number
        tt_bkg_efficiency[j] = tt_bkg_eff

        sgn_eff = np.average([lllv_sgn_eff, llll_sgn_eff, tt_sgn_eff])
        llll_sgn_x[j] = llll_sgn_eff
        lllv_sgn_x[j] = lllv_sgn_eff
        tt_sgn_x[j] = tt_sgn_eff
        sgn_x[j] = sgn_eff * lllv_sgn_sigma_total * lllv_sgn_sel_efficiency
        bkg_x[j] = llll_bkg_sigma_total * llll_bkg_sel_efficiency * llll_bkg_eff \
                   + tt_bkg_sigma_total * tt_bkg_sel_efficiency * tt_bkg_eff \
                   + lllv_bkg_sigma_total * lllv_bkg_sel_efficiency * lllv_bkg_eff \
                   + lllv_small_bkg_sigma_total * lllv_small_bkg_sel_efficiency * lllv_small_bkg_eff
        print(str(sgn_x[j]))
        print(str(llll_bkg_sigma_total * llll_bkg_sel_efficiency * llll_bkg_eff))
        print(str(tt_bkg_sigma_total * tt_bkg_sel_efficiency * tt_bkg_eff))
        print(str(lllv_bkg_sigma_total * lllv_bkg_sel_efficiency * lllv_bkg_eff))
        print(str(lllv_small_bkg_sigma_total * lllv_small_bkg_sel_efficiency * lllv_small_bkg_eff))
        sgn_bkg_x[j] = sgn_x[j] + bkg_x[j]
        sgn_efficiency[j] = sgn_eff

        j = j + 1

    sgn_bkg_delta = np.sqrt(sgn_bkg_x / luminosity) 
    bkg_delta = np.sqrt(bkg_x / luminosity)
    pp_delta = np.sqrt(pp_sgn_sigma_total / luminosity)

    sgn_x = np.where(sgn_x == 0, 1, sgn_x)
    delta_br1 = (sgn_bkg_delta ** 2 + bkg_delta ** 2 + (pp_delta ** 2) * (sgn_x ** 2) / (
                pp_sgn_sigma_total ** 2)) 
    delta_br2 = np.sqrt(delta_br1) / sgn_x
    delta_br = delta_br2[1:]

    plt.figure(figsize=(8, 6))
    min_delta_br = np.min(delta_br)
    min_delta_br_index = np.argmin(delta_br)
    plt.plot(sgn_efficiency[1:], delta_br)
    plt.text(sgn_efficiency[min_delta_br_index] - 0.2, min_delta_br - 0.002,
             'min = (' + '%.3g' % (sgn_efficiency[min_delta_br_index]) + ', ' + '%.3g' % (min_delta_br) + ')')
    plt.text(0.825, min_delta_br + 0.025, 'sgn_eff={:.2g}%'.format(sgn_efficiency[min_delta_br_index] * 100))
    plt.text(0.825, min_delta_br + 0.02, 'llll_bkg_eff={:.2g}%'.format(llll_bkg_efficiency[min_delta_br_index] * 100))
    plt.text(0.825, min_delta_br + 0.015, 'lllv_large_bkg_eff={:.2g}%'.format(lllv_bkg_efficiency[min_delta_br_index] * 100))
    plt.text(0.825, min_delta_br + 0.01, 'lllv_small_bkg_eff={:.2g}%'.format(lllv_small_bkg_efficiency[min_delta_br_index] * 100))
    plt.text(0.825, min_delta_br + 0.005, 'tt_bkg_eff={:.2g}%'.format(tt_bkg_efficiency[min_delta_br_index] * 100))

    plt.yscale('log')
    plt.ylabel('$\delta Br / Br$')
    plt.xlabel(branch_ratio_title)
    print(pfn_result_folder)
    plt.savefig("{}{}-{}-{}-{}_delta_br({:.3}).png".format(pfn_result_folder, str(batch_size), str(dim1), str(dim2), str(num_epoch), min_delta_br))
    # plt.subplots_adjust(left=0.8, right=0.9, bottom=0.1, top=0.9)
    # plt.show()

    # plt.figure(1)
    # plt.plot(np.linspace(0, 100, 500), wztt_sgn_efficiency)
    # plt.plot(np.linspace(0, 100, 500), h_sgn_efficiency)
    # plt.plot(np.linspace(0, 100, 500), zz_sgn_efficiency)
    # plt.xscale('log')
    # plt.legend(['wztt', 'h', 'zz'])
    # plt.ylabel('signal efficiency')
    # plt.xlabel('cut')
    # plt.show()

    # plt.figure(5)
    # h_sgn_condition = (h_Y_test[:, 0] == 1)
    # h_bkg_condition = (h_Y_test[:, 0] == 0)
    # plt.hist((1 - h_pfn_pred[h_sgn_condition, 0]), bins=50, density=True, histtype='step', label='signal', stacked=True)
    # plt.hist((h_pfn_pred[h_bkg_condition, 1]), bins=50, density=True, histtype='step', label='background', stacked=True)
    # plt.savefig('hist_h.png')
    # plt.show()

    # plt.figure(6)
    # zz_sgn_condition = (zz_Y_test[:, 0] == 1)
    # zz_bkg_condition = (zz_Y_test[:, 0] == 0)
    # plt.hist((1 - zz_pfn_pred[zz_sgn_condition, 0]), bins=50, density=True, histtype='step', label='signal', stacked=True)
    # plt.hist((zz_pfn_pred[zz_bkg_condition, 1]), bins=50, density=True, histtype='step', label='background', stacked=True)
    # plt.savefig('hist_zzr.png')
    # plt.show()
    #
    # plt.figure(7)
    # wztt_sgn_condition = (wztt_Y_test[:, 0] == 1)
    # wztt_bkg_condition = (wztt_Y_test[:, 0] == 0)
    # plt.hist((1 - wztt_pfn_pred[wztt_sgn_condition, 0]), bins=50, density=True, histtype='step', label='signal',
    #          stacked=True)
    # plt.hist((wztt_pfn_pred[wztt_bkg_condition, 1]), bins=50, density=True, histtype='step', label='background',
    #          stacked=True)
    # plt.savefig('hist_wztt.png')
    # plt.show()
    print('done')


if __name__ == '__main__':
    # run_utilities(is_atlas=False)
    run_utilities(is_atlas=True)
