from exercises.smooth_l1 import smooth_l1_loss
import numpy as np

def test_smooth_l1():
    beta = 1.0
    # 测试样例1：误差较小
    y_pred1 = np.array([0.1, 1.2, -0.3])
    y_true1 = np.array([0.0, 1.0, 0.0])
    expected_losses1 = 0.5 * np.square(np.array([0.1, 0.2, -0.3])) / beta
    expected1 = np.mean(expected_losses1)
    result1 = smooth_l1_loss(y_pred1, y_true1, beta=beta)
    print(f"测试样例1 (小误差): Expected={expected1:.4f}, Got={result1:.4f} ->",
          "yes" if np.allclose(result1, expected1) else "no")

    # 测试样例2：误差较大
    y_pred2 = np.array([2.5, -1.8, 0.5])
    y_true2 = np.array([0.0, 0.0, 2.0])
    expected_losses2 = np.abs(np.array([2.5, -1.8, -1.5])) - 0.5 * beta
    expected2 = np.mean(expected_losses2)
    result2 = smooth_l1_loss(y_pred2, y_true2, beta=beta)
    print(f"测试样例2 (大误差): Expected={expected2:.4f}, Got={result2:.4f} ->",
          "yes" if np.allclose(result2, expected2) else "no")

    # 测试样例3：混合误差
    y_pred3 = np.array([0.2, 1.0, -2.0, 3.0])
    y_true3 = np.array([0.0, 0.5, 0.0, 1.5])
    expected_losses3 = np.array([0.5*0.2**2/beta, 0.5*0.5**2/beta, abs(-2.0)-0.5*beta, abs(1.5)-0.5*beta])
    expected3 = np.mean(expected_losses3)
    result3 = smooth_l1_loss(y_pred3, y_true3, beta=beta)
    print(f"测试样例3 (混合误差): Expected={expected3:.4f}, Got={result3:.4f} ->",
          "yes" if np.allclose(result3, expected3) else "no")

if __name__ == "__main__":
    test_smooth_l1()
