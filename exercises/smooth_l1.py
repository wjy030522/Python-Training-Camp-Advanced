import numpy as np
def smooth_l1_loss(y_pred, y_true, beta=1.0):
    if beta <= 0:
        raise ValueError("beta must be positive")

    diff = y_pred - y_true
    abs_diff = np.abs(diff)
    condition = abs_diff < beta

    l2_loss = 0.5 * np.square(diff) / beta
    l1_loss = abs_diff - 0.5 * beta

    elementwise_loss = np.where(condition, l2_loss, l1_loss)
    loss = np.mean(elementwise_loss)

    return loss
