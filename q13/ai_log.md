核心提示：空白姓名时 main 应以 SystemExit(2) 退出，且不得修改测试。
智能体改动：仅修改 src/greetlab/cli.py，使用 strip() 检查空白姓名。
测试验证：python -m pytest test_cli.py，修复后 1 passed。
人工检查：检查 diff，确认仅修改 cli.py；重新运行测试通过。

