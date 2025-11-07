# 🚀 LiveKit Security+ Agent - One-Click Startup

## Quick Start Scripts

### 📱 **For Mac Users**
```bash
./start-mac.command
```
Double-click the file or run in terminal

### 🪟 **For Windows Users**  
```cmd
start-windows.bat
```
Double-click the `.bat` file

### 🐧 **For Linux Users**
```bash
./start-linux.sh
```

---

## 🎯 What These Scripts Do

**Automatically starts:**
1. 🔧 **LiveKit Server** - Local WebRTC server
2. 🤖 **Security+ Vision Agent** - AI instructor with screen sharing
3. 🌐 **React Frontend** - Web interface at `http://localhost:3000`

**Features Enabled:**
- ✅ **Voice Conversation** - Speak naturally with the AI instructor
- ✅ **Screen Sharing** - Agent can see and analyze your screen
- ✅ **Security+ Content** - Full exam preparation curriculum
- ✅ **Session Persistence** - Remembers your progress

---

## 📋 Available Voice Commands

### 🎓 **Learning Commands**
- `"Teach me about malware"` - Start a lesson on any topic
- `"Quiz me"` - Practice questions (default 1, say `"Quiz me 3"` for 3 questions)
- `"Explain cryptography"` - Get detailed explanations
- `"What topics in domain 1?"` - See available topics

### 👁️ **Vision Commands** (when screen is shared)
- `"Can you see my screen?"` - Test vision capability
- `"Analyze my screen"` - Get description of what you're sharing
- `"What do you see?"` - Ask the agent to describe visual content

### 📊 **Progress Commands**
- `"Check my progress"` - See your learning statistics
- `"Session history"` - View previous sessions
- `"Get study tips"` - Security+ exam preparation tips

---

## 🔧 **Requirements**

**Before running, make sure you have:**

1. **UV Package Manager**
   ```bash
   # Mac/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Node.js** (version 18+)
   - Download from [nodejs.org](https://nodejs.org)

3. **API Keys** (already configured in `.env.local`)
   - OpenAI API key
   - Deepgram API key
   - LiveKit credentials

---

## 🌐 **Access Points**

**Once started, you can access:**

- **Frontend**: http://localhost:3000
- **LiveKit Server**: ws://localhost:7880
- **Agent Room**: `security-plus-room`

---

## 📝 **Log Files**

**If something goes wrong, check these logs:**

### **Mac/Linux:**
- Server: `/tmp/livekit-server.log`
- Agent: `/tmp/agent.log`  
- Frontend: `/tmp/frontend.log`

### **Windows:**
- Server: `livekit-server.log`
- Agent: `agent.log`
- Frontend: `frontend.log`

---

## 🛑 **Stopping Services**

**All scripts include automatic cleanup:**

- **Mac/Linux**: Press `Ctrl+C`
- **Windows**: Press any key when prompted

**Manual stop (if needed):**
```bash
# Stop all services
pkill -f "livekit-server"
pkill -f "vision_agent.py"  
pkill -f "npm run dev"
```

---

## 🎯 **Sample Usage Session**

1. **Start**: Double-click `start-mac.command` (or your platform's script)
2. **Open Browser**: Go to http://localhost:3000
3. **Begin Session**: Click "Start Security+ Session"
4. **Test Audio**: Say "Hello" - you should hear the instructor respond
5. **Test Vision**: Share screen and say "Can you see my screen?"
6. **Start Learning**: Say "Teach me about network security"

---

## 🔧 **Troubleshooting**

### **Port Already in Use**
```bash
# Check what's using ports 7880 and 3000
lsof -i :7880
lsof -i :3000

# Kill processes if needed
sudo lsof -ti:7880 | xargs kill
sudo lsof -ti:3000 | xargs kill
```

### **Agent Not Responding**
- Check logs in `/tmp/` (Mac/Linux) or current directory (Windows)
- Make sure API keys are valid in `.env.local`
- Restart the script

### **Can't Hear Audio**
- Check browser volume settings
- Ensure microphone permissions are granted
- Try refreshing the browser page

### **Screen Sharing Not Working**
- Make sure you clicked the screen share button in the browser
- Say "Can you see my screen?" to test
- Check that the vision agent is running (not the simple agent)

---

## 🎉 **Success!**

You now have a fully functional AI Security+ instructor that can:
- 🎤 **Talk with you** about cybersecurity topics
- 👁️ **See your screen** to analyze diagrams and configurations
- 📚 **Teach** all CompTIA Security+ domains
- 📝 **Track progress** across sessions
- 🎯 **Provide practice questions** with explanations

**Happy learning! 🚀**
