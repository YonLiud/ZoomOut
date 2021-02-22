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

:startup
    pip3 install win10toast >nul 2>&1
    pip3 install flask >nul 2>&1
    echo [92mDone![0m
    echo [93mStarting Browser...[0m
    start http://localhost:5000
    echo [104;97mStarting ZoomOut![0m
    py app.py
    echo [93mRemoving venv[0m
    del venv/
    Rmdir /S /Q venv
    echo [104;97mApp has been closed[0m
    exit

:boot
    echo [102;90mPython is Installed![0m
    echo [93mInstalling Lib...[0m
    pip3 install virtualenv >nul 2>&1
    if exist venv/ (
        echo [92mvenv already exists[0m
    ) else (
        echo [93mCreating virtual enviroment[0m
        python -m virtualenv venv
    )
    echo [104;97mStarting venv[0m [93mPlease Wait...[0m
    CALL venv\Scripts\activate.bat
    goto startup