@echo off

set /p answer=Do you want to continue (Y/N)? 

if /i "%answer%"=="Y" (
  python main.py
  if errorlevel 1 (
    echo "python a échoué, tentative avec py..."
    py main.py
  )
)

timeout /t 5 /nobreak
