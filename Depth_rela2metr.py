import numpy as np
def rela2metr(metr_depth_batch, rela_depth_batch,masks=None):
    ret = []
    for i in range(metr_depth_batch.shape[0]):
        metr_depth_array = metr_depth_batch[i]
        rela_depth_array = rela_depth_batch[i]
        metr_depth_array_invert = 1 / metr_depth_array # invert absolute depth with meters
        x = rela_depth_array.copy() #rela Depth
        y = metr_depth_array_invert.copy()  # metr invert Depth
        if masks is not None:
            x = x[masks[i]]
            y = y[masks[i]]
        x = x.flatten()
        y = y.flatten()
        A = np.vstack([x, np.ones(len(x))]).T
        s, t = np.linalg.lstsq(A, y, rcond=None)[0]
        rela_depth_aligned_invert = rela_depth_array * s + t
        rela_depth_aligned = 1 / rela_depth_aligned_invert
        ret.append(rela_depth_aligned)
    return np.array(ret)