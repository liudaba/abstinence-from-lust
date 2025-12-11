@echo off
chcp 65001 >nul
echo 正在启动戒色助手...
cd /d "G:\戒色"
python "戒色助手.py"
if errorlevel 1 (
    echo 程序运行出错!
    pause
)
echo 程序已启动
pause
