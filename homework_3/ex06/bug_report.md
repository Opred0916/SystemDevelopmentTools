# Bug Report

## Issue

环境：Windows，Python 3.13

复现步骤：
1. 运行 `python welcome.py`
2. 输入用户名 `Alice`

期望结果：
程序输出 `Welcome, Alice!`

实际结果：
程序输出 `Welcome, !`

## Commit Message

修复用户名显示错误

用户名读取后没有正确传递给输出函数，导致欢迎信息中缺少用户名。

## Review

**Blocking**：当前程序无法正确显示用户输入的姓名，属于功能缺陷。建议检查用户名读取和传递逻辑，并补充测试。