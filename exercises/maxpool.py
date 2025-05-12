# exercises/maxpool.py
"""
练习：最大池化 (Max Pooling)

描述：
实现一个简单的二维最大池化操作。

请补全下面的函数 `maxpool`。
"""
import numpy as np

def maxpool(x, kernel_size, stride):
    """
    执行二维最大池化操作。

    Args:
        x (np.array): 输入二维数组，形状 (H, W)。
        kernel_size (int): 池化窗口的大小 (假设为正方形 k x k)。
        stride (int): 池化窗口移动的步幅。

    Return:
        np.array: 最大池化结果，形状 (out_H, out_W)。
                  out_H = (H - kernel_size) // stride + 1
                  out_W = (W - kernel_size) // stride + 1
    """
    H,W=x.shape
    out_H=(H-kernel_size)//stride+1
    out_W=(W-kernel_size)//stride+1
    out=np.zeros((out_H,out_W))
    for i in range(out_H):
        for j in range(out_W):
            h_start=i*stride
            w_start=j*stride
            window=x[h_start:h_start+kernel_size,w_start:w_start+kernel_size]
            out[i,j]=np.max(window)
    return out
    # 请在此处编写代码
    # 提示：
    # 1. 计算输出的高度和宽度。
    # 2. 初始化输出数组。
    # 3. 使用嵌套循环遍历输出数组的每个位置 (i, j)。
    # 4. 计算当前池化窗口在输入数组 x 中的起始位置 (h_start, w_start)。
    # 5. 提取当前池化窗口 window = x[h_start:h_start+kernel_size, w_start:w_start+kernel_size]。
    # 6. 找到窗口中的最大值 np.max(window)。
    # 7. 将最大值存入输出数组 out[i, j]。
    pass 