import subprocess
subprocess.run(["powershell", "-Command", "iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex"], )
subprocess.run(["powershell", "iwr -useb https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.ps1 | iex"], )
