from __future__ import absolute_import, division, print_function


def run_pfn(batch_size=100, dim1=64, dim2=128, num_epoch=100, is_atlas=False):
    pfn_result_folder = "./pfn_results/"
    utilities_result_folder = "./hllhc_results/"
    if is_atlas:
        batch_size = 100
        dim1 = 64
        dim2 = 128
        num_epoch = 100
        pfn_result_folder = "./pfn_run2_results/"
        utilities_result_folder = "./atlas_results/"

    # standard library imports
    import numpy as np
    from typing import List
    import os
    from energyflow.archs import PFN
    from energyflow.utils import data_split

    import matplotlib.pyplot as plt
    from data_preprocess import load_data
    from tau_test_data_preprocess import load_wz_data, load_h_data, load_tt_data, load_lllv_small_data

    os.environ['--xla_gpu_cuda_data_dir'] = '/usr/lib/cuda'

    # print(os.environ)
    # define parameters
    # data_size = 1000000
    # train, val, test = 75000, 10000, 15000
    val = 0.1
    test = 0.2
    Phi_sizes, F_sizes = (dim1, dim1, dim1), (dim2, dim2, dim2)

    # load data
    [X, y] = load_data(is_atlas=is_atlas)
    min_size = X.shape[0]
    [X_lllv_test, y_lllv_test] = load_wz_data(min_size, is_atlas=is_atlas)
    [X_lllv_small_test, y_lllv_small_test] = load_lllv_small_data(min_size, is_atlas=is_atlas)
    [X_llll_test, y_llll_test] = load_h_data(min_size, is_atlas=is_atlas)
    [X_tt_test, y_tt_test] = load_tt_data(min_size, is_atlas=is_atlas)

    # remap
    # X = remap_pids(X, pid_i=3, error_on_unknown=False)
    # particle_id_list = np.unique(X[:, :, 3])
    X[:, :, 3] = np.where(X[:, :, 3] == 11, 1.0, X[:, :, 3])
    X[:, :, 3] = np.where(X[:, :, 3] == -11, 1.1, X[:, :, 3])
    X[:, :, 3] = np.where(X[:, :, 3] == 13, 1.2, X[:, :, 3])
    X[:, :, 3] = np.where(X[:, :, 3] == -13, 1.3, X[:, :, 3])
    X_lllv_test[:, :, 3] = np.where(X_lllv_test[:, :, 3] == 11, 1.0, X_lllv_test[:, :, 3])
    X_lllv_test[:, :, 3] = np.where(X_lllv_test[:, :, 3] == -11, 1.1, X_lllv_test[:, :, 3])
    X_lllv_test[:, :, 3] = np.where(X_lllv_test[:, :, 3] == 13, 1.2, X_lllv_test[:, :, 3])
    X_lllv_test[:, :, 3] = np.where(X_lllv_test[:, :, 3] == -13, 1.3, X_lllv_test[:, :, 3])
    X_lllv_small_test[:, :, 3] = np.where(X_lllv_small_test[:, :, 3] == 11, 1.0, X_lllv_small_test[:, :, 3])
    X_lllv_small_test[:, :, 3] = np.where(X_lllv_small_test[:, :, 3] == -11, 1.1, X_lllv_small_test[:, :, 3])
    X_lllv_small_test[:, :, 3] = np.where(X_lllv_small_test[:, :, 3] == 13, 1.2, X_lllv_small_test[:, :, 3])
    X_lllv_small_test[:, :, 3] = np.where(X_lllv_small_test[:, :, 3] == -13, 1.3, X_lllv_small_test[:, :, 3])
    X_tt_test[:, :, 3] = np.where(X_tt_test[:, :, 3] == 11, 1.0, X_tt_test[:, :, 3])
    X_tt_test[:, :, 3] = np.where(X_tt_test[:, :, 3] == -11, 1.1, X_tt_test[:, :, 3])
    X_tt_test[:, :, 3] = np.where(X_tt_test[:, :, 3] == 13, 1.2, X_tt_test[:, :, 3])
    X_tt_test[:, :, 3] = np.where(X_tt_test[:, :, 3] == -13, 1.3, X_tt_test[:, :, 3])
    X_llll_test[:, :, 3] = np.where(X_llll_test[:, :, 3] == 11, 1.0, X_llll_test[:, :, 3])
    X_llll_test[:, :, 3] = np.where(X_llll_test[:, :, 3] == -11, 1.1, X_llll_test[:, :, 3])
    X_llll_test[:, :, 3] = np.where(X_llll_test[:, :, 3] == 13, 1.2, X_llll_test[:, :, 3])
    X_llll_test[:, :, 3] = np.where(X_llll_test[:, :, 3] == -13, 1.3, X_llll_test[:, :, 3])

    # # normalize
    # event_mask_train = []
    # event_mask_wz = []
    # event_mask_tt = []
    # event_mask_zz = []
    # event_mask_h = []
    # event_mask_z = []
    # for event_list in [X, X_lllv_test, X_h_test, X_z_test, X_tt_test, X_zz_test]:
    #     # for x in event_list:
    #     #     mask = x[:, 0] > 0
    #     #     # event_mask_train.append((np.count_nonzero(mask) > 1))
    #     #     yphi_avg = np.average(x[mask, 1:3], weights=x[mask, 0], axis=0)
    #     #     x[mask, 1:3] -= yphi_avg
    #     #     x[mask, 0] /= x[:, 0].sum()
    #     event_list[:, :, 3] = np.where(event_list[:, :, 3] == 11, 1.0, event_list[:, :, 3])
    #     event_list[:, :, 3] = np.where(event_list[:, :, 3] == -11, 1.1, event_list[:, :, 3])
    #     event_list[:, :, 3] = np.where(event_list[:, :, 3] == 13, 1.2, event_list[:, :, 3])
    #     event_list[:, :, 3] = np.where(event_list[:, :, 3] == -13, 1.3, event_list[:, :, 3])

    # construct labels
    Y = np.zeros((len(y), 2))
    Y[y == 1, 0] = 1
    Y[y == 2, 1] = 1

    # construct test labels
    Y_lllv_test = np.zeros((len(y_lllv_test), 2))
    Y_lllv_test[y_lllv_test == 1, 0] = 1
    Y_lllv_test[y_lllv_test == 2, 1] = 1

    Y_lllv_small_test = np.zeros((len(y_lllv_small_test), 2))
    Y_lllv_small_test[y_lllv_small_test == 1, 0] = 1
    Y_lllv_small_test[y_lllv_small_test == 2, 0] = 1

    Y_tt_test = np.zeros((len(y_tt_test), 2))
    Y_tt_test[y_tt_test == 1, 0] = 1
    Y_tt_test[y_tt_test == 2, 1] = 1

    Y_llll_test = np.zeros((len(y_llll_test), 2))
    Y_llll_test[y_llll_test == 1, 0] = 1
    Y_llll_test[y_llll_test == 2, 1] = 1

    print(np.shape(X))
    random_index = np.random.permutation(X.shape[0])
    X = X[random_index]
    Y = Y[random_index]

    # for x in X:
    #     mask = x[:, 0] > 0
    #     yphi_avg = np.average(x[mask, 1:3], weights=x[mask, 0], axis=0)
    #     x[mask, 1:3] -= yphi_avg
    #     x[mask, 0] /= x[:, 0].sum()

    print('Finished preprocessing')
    # time = time.strftime("%m-%d-%H-%M", time.localtime())

    # (p_train, p_val, p_test,
    #  phi_train, phi_val, phi_test,
    #  charge_train, charge_val, charge_test,
    #  mass_train, mass_val, mass_test,
    #  Y_train, Y_val, Y_test) = data_split(X[:, :, 0], X[:, :, 1:2], X[:, :, 3], X[:, :, 4], Y, val=val, test=test)
    # (X_train, X_val, X_test,
    #  Y_train, Y_val, Y_test) = data_split(X, Y, val=val, test=test)
    (X_train, X_val, X_test,
     Y_train, Y_val, Y_test) = data_split(X, Y, val=val, test=test)

    X_lllv_test = X_lllv_test[:X_test.shape[0], :, :]
    Y_lllv_test = Y_lllv_test[:Y_test.shape[0], :]
    X_lllv_small_test = X_lllv_small_test[:X_test.shape[0], :, :]
    Y_lllv_small_test = Y_lllv_small_test[:Y_test.shape[0], :]
    X_tt_test = X_tt_test[:X_test.shape[0], :, :]
    Y_tt_test = Y_tt_test[:Y_test.shape[0], :]
    X_llll_test = X_llll_test[:X_test.shape[0], :, :]
    Y_llll_test = Y_llll_test[:Y_test.shape[0], :]

    X_lllv_test = np.concatenate((X_test, X_lllv_test), axis=0)
    Y_lllv_test = np.concatenate((Y_test, Y_lllv_test), axis=0)
    X_lllv_small_test = np.concatenate((X_test, X_lllv_small_test), axis=0)
    Y_lllv_small_test = np.concatenate((Y_test, Y_lllv_small_test), axis=0)
    X_tt_test = np.concatenate((X_test, X_tt_test), axis=0)
    Y_tt_test = np.concatenate((Y_test, Y_tt_test), axis=0)
    X_llll_test = np.concatenate((X_test, X_llll_test), axis=0)
    Y_llll_test = np.concatenate((Y_test, Y_llll_test), axis=0)
    print("Train size: ", X_train.shape[0])
    print("Val size: ", X_val.shape[0])
    print("Test size: ", X_test.shape[0])
    print('Done train/val/test split')

    my_pfn = PFN(input_dim=X.shape[-1], Phi_sizes=Phi_sizes, F_sizes=F_sizes)

    # train model
    history = my_pfn.fit(X_train, Y_train,
                         epochs=num_epoch,
                         batch_size=batch_size,
                         validation_data=(X_val, Y_val),
                         verbose=1)
    plt1, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10))
    ax1.plot(history.history['acc'])
    ax1.plot(history.history['val_acc'])
    ax1.set_title('PFN accuracy')
    ax1.set_ylabel('loss')
    ax1.set_yscale('log')
    ax1.set_xlabel('epoch')
    ax1.legend(['train', 'val'], loc='upper left')
    # plt.savefig('PFN accuracy.png')
    # plt.show()

    # plt.figure()
    ax2.plot(history.history['loss'])
    ax2.plot(history.history['val_loss'])
    ax2.set_title('PFN loss')
    ax2.set_ylabel('Loss')
    ax2.set_yscale('log')
    ax2.set_xlabel('Epoch')
    ax2.legend(['Train', 'Test'], loc='upper left')
    plt1.savefig("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                        str(num_epoch)) + '-PFN results.png')
    # plt.show()

    # get predictions on test data
    lllv_preds = my_pfn.predict(X_lllv_test, batch_size=batch_size)
    lllv_small_preds = my_pfn.predict(X_lllv_small_test, batch_size=batch_size)
    tt_preds = my_pfn.predict(X_tt_test, batch_size=batch_size)
    llll_preds = my_pfn.predict(X_llll_test, batch_size=batch_size)
    # pfn_test_preds = my_pfn.predict(X_test, Y_test, batch_size=1000)
    # np.save('lllv_preds.npy', lllv_preds)

    # save result to file
    np.save("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                   str(num_epoch)) + '-lllv_Y_test.npy', Y_lllv_test)
    np.save("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                   str(num_epoch)) + '-lllv_small_Y_test.npy', Y_lllv_small_test)
    np.save("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                   str(num_epoch)) + '-tt_Y_test.npy', Y_tt_test)
    np.save("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                   str(num_epoch)) + '-llll_Y_test.npy', Y_llll_test)
    np.save("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                   str(num_epoch)) + '-llll_preds.npy', llll_preds)
    np.save("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                   str(num_epoch)) + '-lllv_preds.npy', lllv_preds)
    np.save("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                   str(num_epoch)) + '-lllv_small_preds.npy', lllv_small_preds)
    np.save("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                   str(num_epoch)) + '-tt_preds.npy', tt_preds)

    plt.figure()
    lllv_sgn_condition = (Y_lllv_test[:, 0] == 1)
    lllv_bkg_condition = (Y_lllv_test[:, 0] == 0)
    lllv_small_sgn_condition = (Y_lllv_small_test[:, 0] == 1)
    lllv_small_bkg_condition = (Y_lllv_small_test[:, 0] == 0)
    tt_sgn_condition = (Y_tt_test[:, 0] == 1)
    tt_bkg_condition = (Y_tt_test[:, 0] == 0)
    llll_sgn_condition = (Y_llll_test[:, 0] == 1)
    llll_bkg_condition = (Y_llll_test[:, 0] == 0)

    # lllv plot distribution
    sgn_hist_all = np.concatenate((1 - lllv_preds[lllv_sgn_condition, 0], 1 - tt_preds[tt_sgn_condition, 0],
                                   1 - llll_preds[llll_sgn_condition, 0]), axis=0)
    plt.hist(sgn_hist_all, bins=50, density=True, histtype='step', label='signal', stacked=True, log=True)
    plt.hist((lllv_preds[lllv_bkg_condition, 1]), bins=50, density=True, histtype='step', label='lllv background',
             stacked=True, log=True)

    # llll plot distribution
    plt.hist((llll_preds[llll_bkg_condition, 1]), bins=50, density=True, histtype='step', label='llll background',
             stacked=True, log=True)

    # lllv small plot distribution
    plt.hist((lllv_small_preds[lllv_small_bkg_condition, 1]), bins=50, density=True, histtype='step',
             label='lllv small background', stacked=True, log=True)

    # tt plot distribution
    plt.hist((tt_preds[tt_bkg_condition, 1]), bins=50, density=True, histtype='step', label='tt background',
             stacked=True, log=True)

    plt.legend()
    plt.title('PFN output')
    plt.savefig("{}{}-{}-{}-{}".format(utilities_result_folder, str(batch_size), str(dim1), str(dim2),
                                       str(num_epoch)) + '-hists.png')
    plt.close()


if __name__ == "__main__":
    run_pfn(is_atlas=False)
    run_pfn(is_atlas=True)
