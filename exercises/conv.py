import numpy as np
def conv2d_3x3(input_img, kernel):
    h, w = input_img.shape
    output = np.zeros((h - 2, w - 2))
    for i in range(h - 2):
        for j in range(w - 2):
            window = input_img[i:i+3, j:j+3]
            output[i, j] = np.sum(window * kernel)
    return output
