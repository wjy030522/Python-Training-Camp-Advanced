# Python训练营进阶部分

本项目包含一系列Python深度学习算法和计算机视觉实现的练习，涵盖了从基础算法到OpenCV图像处理的多个方面。学生需要补全缺失的代码，通过测试验证自己的实现是否正确。

## 练习内容

### 第1部分: 深度学习算法基础
1. **IoU_Calculation.ipynb**: 实现目标检测中的交并比(IoU)计算
2. **NMS_Implementation.ipynb**: 实现目标检测中的非极大值抑制(NMS)算法
3. **Convolution_Implementation.ipynb**: 手写实现2D卷积操作
4. **LeakyReLU_Activation.ipynb**: 实现LeakyReLU激活函数及其梯度
5. **MaxPool_Implementation.ipynb**: 实现最大池化操作
6. **CrossEntropy_Loss.ipynb**: 实现交叉熵损失函数
7. **SmoothL1_Loss.ipynb**: 实现SmoothL1损失函数

### 第2部分: 计算机视觉基础
8. **OpenCV_Edge_Detection.ipynb**: 使用OpenCV实现图像边缘检测
9. **OpenCV_Contour_Detection.ipynb**: 使用OpenCV实现图像轮廓检测

## 使用方法

1. 打开对应的练习文件（如`Exercises/01-IoU_Calculation.ipynb`）
2. 阅读文件顶部的说明，了解需要实现的功能
3. 在标记为`#####`的位置编写你的代码
4. 运行所有单元格，验证你的实现是否正确

## 建议学习顺序

建议按照上述编号顺序学习，从基础算法到图像处理应用：
1. 先掌握目标检测的基础算法（IoU计算、NMS）
2. 学习深度学习的核心组件实现（卷积、激活函数、池化、损失函数）
3. 最后学习OpenCV图像处理（边缘检测、轮廓检测）

## 环境要求
- Python 3.6+
- Jupyter Notebook
- 依赖库: NumPy, OpenCV, Matplotlib

## 目录结构

```
Python-Training-Camp-Advance/
├── Exercises/             # 练习题目录
│   ├── 01-IoU_Calculation.ipynb
│   ├── 02-NMS_Implementation.ipynb
│   ├── 03-Convolution_Implementation.ipynb
│   ├── 04-LeakyReLU_Activation.ipynb
│   ├── 05-MaxPool_Implementation.ipynb
│   ├── 06-CrossEntropy_Loss.ipynb
│   ├── 07-SmoothL1_Loss.ipynb
│   ├── 08-OpenCV_Edge_Detection.ipynb
│   └── 09-OpenCV_Contour_Detection.ipynb
└── requirements.txt      # 项目依赖
```

## 运行方法

```bash
# 安装依赖
pip install -r requirements.txt

# 启动Jupyter Notebook
jupyter notebook
```

## 注意事项
- 每个练习文件中都有详细的注释说明，请仔细阅读
- 需要填写的代码部分用`#####`标记
- 务必先独立思考和实现，再参考答案

## 评分标准

实现结果有通过和不通过两种状态：
- 通过：所有测试用例都符合预期
- 不通过：至少有一个测试用例失败 