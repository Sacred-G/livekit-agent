# LiveKit Cloud Setup Guide

## 🌟 Why LiveKit Cloud?

LiveKit Cloud is the **easiest way** to deploy your Security+ agent:

✅ **No server management** - Fully hosted service  
✅ **Global CDN** - Low latency worldwide  
✅ **Automatic scaling** - Handles any number of students  
✅ **Free tier** - 50,000 minutes/month free  
✅ **Enterprise security** - SSL, DDoS protection  
✅ **5-minute setup** - No configuration required  

## 🚀 Quick Setup (5 minutes)

### **Step 1: Create LiveKit Cloud Account**

1. Go to [cloud.livekit.io](https://cloud.livekit.io)
2. **Sign up** with GitHub, Google, or email
3. **Verify your email** (check inbox)
4. **Create your first project**:
   - Project name: `security-plus-agent`
   - Region: Choose nearest to your users

### **Step 2: Get Your Credentials**

After creating your project, you'll see your dashboard:

```
🔑 Project Credentials
┌─────────────────────────────────────┐
│ Host: wss://security-plus-1234.livekit.cloud │
│ API Key: DEVf1234567890abcdef         │
│ Secret: [Click to reveal]            │
└─────────────────────────────────────┘
```

**Copy these 3 values** - you'll need them for Vercel.

### **Step 3: Configure Vercel**

1. **Deploy to Vercel** (if not done yet):
   ```bash
   npm install
   vercel --prod
   ```

2. **Add Environment Variables** in Vercel Dashboard:
   - Go to your project → Settings → Environment Variables
   - Add these 3 variables:

   | Variable Name | Value from LiveKit Cloud |
   |---------------|--------------------------|
   | `LIVEKIT_HOST` | `wss://your-project-1234.livekit.cloud` |
   | `LIVEKIT_API_KEY` | `DEVf1234567890abcdef` |
   | `LIVEKIT_API_SECRET` | `[Your secret key]` |

3. **Redeploy** with new variables:
   ```bash
   vercel --prod
   ```

### **Step 4: Test Your Setup**

1. **Visit your Vercel app**: `https://your-app.vercel.app`
2. **Enter your name** and click "Join Security+ Class"
3. **Allow microphone access** when prompted
4. **You should connect** to LiveKit Cloud instantly!

## 🔧 Advanced Configuration

### **Custom Room Settings**

You can customize room behavior in your Vercel environment:

```env
# Optional: Room configuration
LIVEKIT_ROOM_NAME=security-plus-class
LIVEKIT_TOKEN_TTL=86400  # 24 hours in seconds
```

### **Security Best Practices**

1. **Restrict domains** in LiveKit Cloud dashboard:
   - Go to Project → Settings → Allowed Domains
   - Add your Vercel domain: `your-app.vercel.app`

2. **Enable recording** (optional):
   - Perfect for reviewing Security+ sessions
   - Go to Project → Settings → Recording

3. **Monitor usage**:
   - Dashboard shows real-time usage
   - Set alerts for usage limits

## 📊 LiveKit Cloud Free Tier

**Free forever:**
- ✅ 50,000 minutes/month
- ✅ 100 concurrent participants
- ✅ All features included
- ✅ No credit card required

**Paid plans** (when you scale):
- 🚀 $0.004/minute after free tier
- 🚀 Unlimited participants
- 🚀 Priority support
- 🚀 Custom branding

## 🔍 Troubleshooting

### **Common Issues**

**"Connection failed" error:**
- ✅ Check LIVEKIT_HOST in Vercel env vars
- ✅ Verify API key and secret are correct
- ✅ Ensure domain is allowed in LiveKit Cloud

**"Token generation failed":**
- ✅ Check Vercel function logs
- ✅ Verify all 3 env variables are set
- ✅ Try redeploying: `vercel --prod`

**No audio:**
- ✅ Allow microphone access in browser
- ✅ Check browser console for WebRTC errors
- ✅ Try different browser (Chrome recommended)

### **Debug Mode**

Enable debug logging in your browser console:
```javascript
// In browser console
localStorage.setItem('debug', 'livekit:*')
```

## 🎯 Next Steps

Once LiveKit Cloud is working:

1. **Deploy your Security+ Python agent** to a cloud service
2. **Connect the agent** to your LiveKit Cloud room
3. **Test the full experience** with real students
4. **Monitor usage** in LiveKit Cloud dashboard

## 📞 Support

- **LiveKit Cloud docs**: [docs.livekit.io](https://docs.livekit.io)
- **Vercel docs**: [vercel.com/docs](https://vercel.com/docs)
- **Discord community**: [discord.gg/livekit](https://discord.gg/livekit)

---

**🎉 You're now using LiveKit Cloud!** Your Security+ agent will have enterprise-grade reliability without any server management.
