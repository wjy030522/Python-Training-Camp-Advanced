import re
import subprocess
from collections import defaultdict

def run_pytest_and_score():
    # 运行pytest并捕获输出
    result = subprocess.run(
        ['python3', '-m', 'pytest', 'tests/', '-v'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # 解析测试结果
    test_results = defaultdict(dict)
    current_file = None
    
    # 使用正则匹配测试结果行
    pattern = re.compile(
        r'tests/(test_\w+)\.py::([\w:]+) (\w+)'
    )
    
    for line in result.stdout.split('\n'):
        match = pattern.search(line)
        if match:
            file_name, test_name, status = match.groups()
            test_results[file_name][test_name] = status == 'PASSED'
    
    # 计算得分
    total_tests = sum(len(tests) for tests in test_results.values())
    passed_tests = sum(sum(1 for passed in tests.values() if passed) 
                      for tests in test_results.values())
    
    score = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    # 打印详细报告
    print("\n" + "="*50)
    print("测试结果详情:")
    for file_name, tests in test_results.items():
        print(f"\n{file_name}:")
        for test_name, passed in tests.items():
            status = "✓ PASSED" if passed else "✗ FAILED"
            print(f"  {test_name:50} {status}")
    
    print("\n" + "="*50)
    print(f"最终得分: {score:.1f}分 (通过 {passed_tests}/{total_tests} 个测试)")
    print("="*50 + "\n")
    
    # 保存结果到文件
    with open("test_score.txt", "w") as f:
        f.write(f"Passed: {passed_tests}/{total_tests}\n")
        f.write(f"Score: {score:.1f}\n")
    
    return score

if __name__ == "__main__":
    run_pytest_and_score()
