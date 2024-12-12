@echo off

echo "@echo Off

echo "Welcome Discord Hacker! Anything you do with this tool will be done of your own free will. We are not responsible for what happens to you.  This tool is in full development."



set /p answer="Do you want to continue (Y/N)? "

if /i "%answer%"=="Y" (
  echo "You chose to continue."
) else if /i "%answer%"=="N" (
  echo "You chose to cancel."
) else (
  echo "Invalid input."
)

timeout /t 5 /nobreak

python main.py
