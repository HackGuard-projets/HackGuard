@echo off

pip install -r requirements.txt > nul 2>&1

set /p answer=Do you want to continue (Y/N)? 

if /i "%answer%"=="Y" (
  python main.py
  if errorlevel 1 (
    py main.py
  )
)

timeout /t 5 /nobreak
