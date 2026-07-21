print("Virtual Environment details :")
# Virtual Environment Guide

# To work with Python projects in isolation, you can use a virtual environment.  
# The process is straightforward: first create the environment, then activate it, install the packages you need, and finally deactivate it when done.

# The command to create a virtual environment is:
# python -m venv env

# Once created, you activate it depending on your operating system.  
# On Windows (Command Prompt): env\Scripts\activate  
# On Windows (PowerShell): .\env\Scripts\Activate.ps1  
# On Linux or macOS: source env/bin/activate  

# When the environment is active, your terminal prompt will show (env).  
# At this point, you can install packages inside the environment using pip, for example:
# pip install requests

# All packages installed will stay isolated inside the virtual environment folder.  
# When you are finished working, you can exit the environment with:
# deactivate

# This sequence—create, activate, install, deactivate—covers the complete workflow for using Python virtual environments.