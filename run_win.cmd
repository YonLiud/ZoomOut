echo off
cls
echo [101;93m ZoomOut [0m
echo [101;93m By YonLiud ^& JustPelmen [0m
echo.
where py >nul 2>&1 && goto boot || goto exit

:exit
    echo [91mPython Is Not Installed[0m
    pause
    Exit /B 5
:boot
    echo [102;90mPython is Installed![0m
    echo [93mInstalling Lib...[0m
    pip3 install win10toast
    pip3 install flask
    echo [92mDone![0m
    echo [93mStarting Browser...[0m
    start http://localhost:5000
    echo [104;97mStarting ZoomOut![0m
    py app.py
    echo [104;97mApp has been closed[0m