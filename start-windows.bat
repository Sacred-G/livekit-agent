@echo off
REM LiveKit Security+ Agent - One Click Start (Windows)
REM ================================================

title LiveKit Security+ Agent

echo 🚀 Starting LiveKit Security+ Agent...

REM Get script directory
cd /d "%~dp0"

REM Check if UV is installed
where uv >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ UV not found. Please install UV first:
    echo    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    pause
    exit /b 1
)

REM Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Node.js not found. Please install Node.js first.
    pause
    exit /b 1
)

REM Create keys file if not exists
if not exist "keys.txt" (
    echo APIJzcLNvtmYEiU: 7MfPzoCaV7LeSt05ZpYf6XD7G5TUfqb1WSFZxMpKGAKD > keys.txt
)

REM Start local LiveKit server
echo 🔧 Starting LiveKit server...
start /B "LiveKit Server" livekit-server --dev --key-file keys.txt > livekit-server.log 2>&1
timeout /t 3 /nobreak >nul

REM Start vision agent
echo 🤖 Starting Security+ Vision Agent...
start /B "Security+ Agent" uv run python vision_agent.py connect --room security-plus-room --url ws://localhost:7880 --api-key APIJzcLNvtmYEiU --api-secret "7MfPzoCaV7LeSt05ZpYf6XD7G5TUfqb1WSFZxMpKGAKD" > agent.log 2>&1
timeout /t 3 /nobreak >nul

REM Start frontend
echo 🌐 Starting Frontend...
cd frontend
start /B "Frontend" npm run dev > ../frontend.log 2>&1
cd ..
timeout /t 2 /nobreak >nul

REM Success message
echo.
echo ✅ All services started successfully!
echo ==================================
echo 🌐 Frontend: http://localhost:3000
echo 🎓 Agent: Security+ Vision Teacher
echo 👁️ Vision: ENABLED ^(can see your screen^)
echo 🔊 Audio: ENABLED
echo.
echo 📋 Available commands:
echo    • 'Quiz me' - Practice questions
echo    • 'Teach me about [topic]' - Start lesson
echo    • 'Can you see my screen?' - Test vision
echo    • 'Analyze my screen' - Screen analysis
echo.
echo 📝 Logs:
echo    • Server: livekit-server.log
echo    • Agent: agent.log
echo    • Frontend: frontend.log
echo.
echo Press any key to stop all services...
pause >nul

REM Cleanup
echo.
echo 🛑 Stopping services...
taskkill /f /im livekit-server.exe >nul 2>&1
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im node.exe >nul 2>&1
echo ✅ All services stopped
timeout /t 2 /nobreak >nul
