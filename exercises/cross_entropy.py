import numpy as np
def cross_entropy_loss(y_pred, y_true):
    epsilon = 1e-12
    y_pred_clipped = np.clip(y_pred, epsilon, 1 - epsilon)
    correct_logprobs = -np.log(y_pred_clipped[range(len(y_true)), y_true])
    total_loss = np.sum(correct_logprobs)
    loss = total_loss / len(y_true)
    return loss
