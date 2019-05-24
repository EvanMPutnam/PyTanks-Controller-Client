rem Base path of your PyTank repositories
set game_base=C:\Users\Evan\Desktop\Code\Pytanks

rem Start the game server (Install from here https://github.com/JoelEager/pyTanks.Server)
start cmd.exe /c python %game_base%\pyTanks.Server\start.py
powershell -command "Start-Sleep -s 3"

rem Start the first AI (Install from here https://github.com/JoelEager/pyTanks.Player)
start cmd.exe /c python %game_base%\pyTanks.Player\start.py
powershell -command "Start-Sleep -s 1"

rem Start the second controller based charachter.
start cmd.exe /c python %game_base%\pyTanks.PlayerKeyboard\start.py
powershell -command "Start-Sleep -s 1"

rem Open the web page. (Install from here https://github.com/JoelEager/pyTanks.Viewer)
%game_base%\pyTanks.Viewer\index.html