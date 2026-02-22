#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import datetime
import os

def number_game():
    """
    猜数字游戏
    """
    print("\n🎮 猜数字游戏")
    print("我随机生成了一个1-100之间的整数")
    
    target = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\n请输入你的猜测 (1-100): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("请输入1-100之间的数字！")
                continue
                
            if guess < target:
                print("太小了，再试试！")
            elif guess > target:
                print("太大了，再试试！")
            else:
                print(f"🎉 恭喜你！猜对了！")
                print(f"正确答案是: {target}")
                print(f"你用了 {attempts} 次猜中")
                break
                
        except ValueError:
            print("请输入有效的数字！")

def todo_manager():
    """
    简单的待办事项管理器
    """
    todo_list = []
    
    while True:
        print("\n📋 待办事项管理器")
        print("1. 查看待办事项")
        print("2. 添加待办事项")
        print("3. 删除待办事项")
        print("4. 返回主菜单")
        
        choice = input("\n请选择操作 (1-4): ")
        
        if choice == "1":
            if not todo_list:
                print("当前没有待办事项")
            else:
                print("\n你的待办事项:")
                for i, item in enumerate(todo_list, 1):
                    print(f"  {i}. {item}")
                    
        elif choice == "2":
            task = input("请输入待办事项: ")
            if task.strip():
                todo_list.append(task.strip())
                print(f"已添加: {task.strip()}")
            else:
                print("待办事项不能为空")
                
        elif choice == "3":
            if not todo_list:
                print("没有可删除的待办事项")
            else:
                print("\n当前待办事项:")
                for i, item in enumerate(todo_list, 1):
                    print(f"  {i}. {item}")
                try:
                    index = int(input("请输入要删除的序号: ")) - 1
                    if 0 <= index < len(todo_list):
                        removed = todo_list.pop(index)
                        print(f"已删除: {removed}")
                    else:
                        print("无效的序号")
                except ValueError:
                    print("请输入有效的数字")
                    
        elif choice == "4":
            break
        else:
            print("无效的选择，请重新输入")

def system_info():
    """
    显示系统信息
    """
    print("\n💻 系统信息")
    
    # 当前时间
    now = datetime.datetime.now()
    print(f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"当前年份: {now.year}")
    print(f"当前星期: 星期{now.weekday() + 1}")
    
    # 农历年份
    # 注意：2026年是农历丙午马年
    lunar_year = "丙午马年"
    print(f"农历年份: {lunar_year} (2026年2月17日进入)")
    
    # 工作目录
    print(f"当前工作目录: {os.getcwd()}")
    
    # Python版本
    import platform
    print(f"Python版本: {platform.python_version()}")
    
    # 操作系统信息
    print(f"操作系统: {platform.system()} {platform.release()}")

def main():
    """
    主函数
    """
    print("=" * 40)
    print("    多功能Python脚本演示")
    print("=" * 40)
    
    while True:
        print("\n📁 主菜单")
        print("1. 🎮 猜数字游戏")
        print("2. 📋 待办事项管理器")
        print("3. 💻 系统信息")
        print("4. 🚪 退出程序")
        
        choice = input("\n请选择功能 (1-4): ")
        
        if choice == "1":
            number_game()
        elif choice == "2":
            todo_manager()
        elif choice == "3":
            system_info()
        elif choice == "4":
            print("\n感谢使用，再见！👋")
            break
        else:
            print("无效的选择，请重新输入")

if __name__ == "__main__":
    main()
