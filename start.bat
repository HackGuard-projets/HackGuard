@echo off

set /p answer=Do you want to continue (Y/N)? 

if /i "%answer%"=="Y" (
  python main.py
  if errorlevel 1 (
    py main.py
  )
)

timeout /t 5 /nobreak
