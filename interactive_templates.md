# 🎯 Interactive Security+ Exercise Templates

## 📐 Network Security Topology Template

```
                    🌐 Internet
                        │
                    🔥 Firewall
                        │
                    🏢 DMZ
               ┌─────────────────┐
               │  🌐 Web Server  │
               │  📧 Mail Server │
               └─────────────────┘
                        │
                    🔥 Firewall
                        │
                 🏢 Internal Network
    ┌─────────────────────────────────────────────────┐
    │  🗄️ Database    💻 Workstations    🏛️ DC      │
    │  Server         (Domain Users)    Controller    │
    │                                                 │
    │  🛡️ IDS/IPS     🖨️ Printers        📁 File     │
    │  Sensor         Network            Server      │
    └─────────────────────────────────────────────────┘
                        │
                    🔐 VPN Concentrator
                        │
                 👤 Remote Users
```

## 🔐 Cipher Challenge Template

### Caesar Cipher Example
```
Plaintext:  H E L L O W O R L D
Shift:      +3 +3 +3 +3 +3 +3 +3 +3 +3 +3
Ciphertext: K H O R Z Z R U G

To decrypt: Shift each letter back by 3
```

### Frequency Analysis Template
```
Letter Count Analysis:
A: ████████ 8
B: ██ 2  
C: █████ 5
D: ████████████ 12
E: ███████████████████ 18
...

Most common letters in English: E, T, A, O, I, N, S, H, R
```

## 🚨 Incident Response Flowchart Template

```
🚨 Detection
    │
    ├─ 📊 Monitor: SIEM, IDS/IPS, Logs
    ├─ 🔍 Identify: Type, Scope, Impact  
    └─ 📢 Alert: Response team, Management
    │
📊 Analysis
    │
    ├─ 🔬 Investigate: Root cause, affected systems
    ├─ 📏 Contain: Isolate, prevent spread
    └─ 📋 Document: Timeline, evidence
    │
🛡️ Containment
    │
    ├─ 🚪 Short-term: Isolate systems
    ├─ 🛡️ Long-term: Permanent fixes
    └─ 🔄 Backup: Critical data preservation
    │
🧹 Eradication
    │
    ├─ 🦠 Remove: Malware, backdoors
    ├─ 🔧 Patch: Vulnerabilities
    └─ 🔄 Rebuild: Compromised systems
    │
🔄 Recovery
    │
    ├─ ✅ Restore: From clean backups
    ├─ 🧪 Test: System functionality
    └─ 👁️ Monitor: For recurrence
    │
📚 Lessons Learned
    │
    ├─ 📝 Report: Incident details
    ├─ 🎯 Improve: Processes, tools
    └─ 🏋️ Train: Staff awareness
```

## 📊 Access Control Matrix Template

```
┌─────────────┬─────────┬─────────┬─────────┬─────────┐
│   Resource  │  Admin  │ Manager │  User   │  Guest  │
├─────────────┼─────────┼─────────┼─────────┼─────────┤
│ 📁 Files    │   RWE   │   RW    │    R    │         │
│ 🗄️ Database │   RWE   │   R     │         │         │
│ 🌐 Network  │   RWE   │   RW    │    R    │         │
│ ⚙️ Admin    │   RWE   │         │         │         │
│ 📊 Reports  │   RWE   │   RW    │    R    │         │
└─────────────┴─────────┴─────────┴─────────┴─────────┘

Legend: R=Read, W=Write, E=Execute
```

## 🤝 TCP Handshake Diagram Template

```
Client                    Server
  │                         │
  │    SYN (Seq=100)        │
  ├─────────────────────────►│
  │                         │
  │ SYN-ACK (Seq=300, Ack=101) │
  │◄─────────────────────────┤
  │                         │
  │    ACK (Seq=101, Ack=301)│
  ├─────────────────────────►│
  │                         │
  │   🎉 Connection Established!   │
```

## 🔍 Port Scan Analysis Template

```
Port Scan Results:
Target: 192.168.1.100

Open Ports Analysis:
┌─────────┬─────────────┬─────────────────┬─────────────┐
│ Port    │ Service     │ Risk Level      │ Recommendation │
├─────────┼─────────────┼─────────────────┼─────────────┤
│ 22      │ SSH         │ 🔴 Medium       │ Use key auth  │
│ 80      │ HTTP        │ 🔴 High         │ Redirect to HTTPS │
│ 443     │ HTTPS       │ 🟢 Low          │ Keep updated  │
│ 3389    │ RDP         │ 🔴 High         │ Restrict access │
│ 5900    │ VNC         │ 🔴 High         │ Disable or VPN │
└─────────┴─────────────┴─────────────────┴─────────────┘

Priority Actions:
1. 🚨 Disable VNC (port 5900) - use SSH instead
2. 🔒 Restrict RDP access - require VPN
3. 🌐 Force HTTPS redirect from HTTP
4. 🔐 Implement SSH key authentication
```

## 🎯 How to Use These Templates

1. **Choose an exercise** from the agent's menu
2. **Draw the template** on your screen using any tool:
   - Whiteboard app (Miro, Jamboard)
   - Drawing tool (Paint, Sketch)
   - Even paper and pencil!
3. **Share your screen** with the agent
4. **Get real-time feedback** and guidance

**Voice Commands to Start:**
- "Start network exercise"
- "Give me a cipher challenge"  
- "Let's do incident response"
- "Show me port scan analysis"
- "List all interactive exercises"

The agent will see your work and provide personalized feedback! 🚀
