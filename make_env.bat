@echo off
:: Create a new conda environment
echo Creating a new Conda environment: djenv
call conda create -n djenv python=3.10 pip -y

:: Activate the new environment
echo Activating the djenv environment
call conda activate djenv

:: Install the requirements using pip (assumes requirements.txt exists in the same directory)
echo Installing requirements via pip
call pip install -r requirements.txt

:: Notify completion
echo Environment setup complete!
call pause