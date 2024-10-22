import unittest
import io

def run_tests():
    # 设置测试发现的起始目录和测试文件的匹配模式
    start_dir = 'tests'
    pattern = "test*.py"
    
    # 创建测试加载器
    test_loader = unittest.TestLoader()
    test_loader.testMethodPrefix = "test"
    
    # 发现测试用例
    test_suite = test_loader.discover(start_dir, pattern=pattern)
    
    # 将测试结果写入到一个 StringIO 对象中，而不是直接写入文件
    buffer = io.StringIO()
    
    # 创建测试运行器，指定输出流为我们刚刚创建的 StringIO 对象
    test_runner = unittest.TextTestRunner(stream=buffer)
    
    # 运行测试用例
    test_runner.run(test_suite)
    
    # 获取测试结果
    test_results = buffer.getvalue()
    
    # 将测试结果写入文件
    with open('test_results.txt', 'w') as result_file:
        result_file.write(test_results)

if __name__ == "__main__":
    run_tests()