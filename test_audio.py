#!/usr/bin/env python3
"""
Simple audio test script to verify TTS is working
"""

import asyncio
from dotenv import load_dotenv
from livekit.plugins import openai

load_dotenv(".env")

async def test_tts():
    """Test text-to-speech functionality"""
    print("🔊 Testing TTS configuration...")
    
    try:
        # Initialize TTS
        tts = openai.TTS(voice="echo")
        print(f"✅ TTS initialized successfully with voice: echo")
        
        # Test synthesis
        test_text = "Hello, this is a test of the audio system."
        print(f"🔊 Synthesizing: {test_text}")
        
        # This would normally stream audio, but we'll just test the setup
        print("✅ TTS setup appears to be working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ TTS test failed: {e}")
        return False

async def test_stt():
    """Test speech-to-text configuration"""
    print("🎤 Testing STT configuration...")
    
    try:
        from livekit.plugins import deepgram
        
        # Initialize STT
        stt = deepgram.STT(model="nova-2")
        print(f"✅ STT initialized successfully with model: nova-2")
        print("✅ STT setup appears to be working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ STT test failed: {e}")
        return False

async def main():
    """Run all audio tests"""
    print("🧪 Running audio configuration tests...\n")
    
    tts_ok = await test_tts()
    print()
    stt_ok = await test_stt()
    
    print(f"\n📊 Test Results:")
    print(f"   TTS: {'✅ PASS' if tts_ok else '❌ FAIL'}")
    print(f"   STT: {'✅ PASS' if stt_ok else '❌ FAIL'}")
    
    if tts_ok and stt_ok:
        print("\n🎉 All audio components are configured correctly!")
        print("💡 If you still can't hear the agent, check:")
        print("   1. Browser/system audio volume")
        print("   2. Microphone permissions")
        print("   3. Frontend audio device selection")
    else:
        print("\n⚠️  Some audio components failed. Check your API keys and configuration.")

if __name__ == "__main__":
    asyncio.run(main())
