#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    """
    一个简单的Python脚本示例
    """
    # 打印欢迎信息
    print("欢迎使用简单的Python脚本示例！")
    
    # 获取用户输入
    name = input("请输入你的名字: ")
    
    # 处理并输出结果
    if name.strip():  # 检查输入是否非空
        print(f"你好，{name}！")
        print(f"你的名字有 {len(name)} 个字符")
    else:
        print("你没有输入名字")
    
    # 简单的计算示例
    print("\n--- 简单计算示例 ---")
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"数字列表: {numbers}")
    print(f"总和: {total}")
    print(f"平均值: {average:.2f}")  # 保留两位小数
    
    # 文件操作示例
    print("\n--- 文件操作示例 ---")
    try:
        with open("example.txt", "w", encoding="utf-8") as f:
            f.write(f"这是由 {name or '匿名用户'} 创建的示例文件\n")
            f.write(f"创建时间: 2026年\n")
        print("已创建文件: example.txt")
    except Exception as e:
        print(f"文件创建失败: {e}")

if __name__ == "__main__":
    main()
