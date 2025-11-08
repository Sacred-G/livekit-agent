import { NextRequest, NextResponse } from 'next/server'
import { AccessToken } from 'livekit-server-sdk'

export async function POST(request: NextRequest) {
  try {
    const { roomName, participantName } = await request.json()

    if (!roomName || !participantName) {
      return NextResponse.json(
        { error: 'Room name and participant name are required' },
        { status: 400 }
      )
    }

    // Get LiveKit Cloud configuration from environment
    const livekitHost = process.env.LIVEKIT_HOST || 'wss://your-project-1234.livekit.cloud'
    const apiKey = process.env.LIVEKIT_API_KEY
    const apiSecret = process.env.LIVEKIT_API_SECRET

    if (!apiKey || !apiSecret) {
      return NextResponse.json(
        { error: 'LiveKit Cloud configuration missing. Please set LIVEKIT_HOST, LIVEKIT_API_KEY, and LIVEKIT_API_SECRET in your environment variables.' },
        { status: 500 }
      )
    }

    // Create access token for LiveKit Cloud
    const at = new AccessToken(apiKey, apiSecret, {
      identity: participantName,
      name: participantName,
      metadata: JSON.stringify({
        role: 'student',
        subject: 'security-plus',
        joinedAt: new Date().toISOString()
      })
    })

    // Add grants for the participant
    at.addGrant({
      room: roomName,
      roomJoin: true,
      canPublish: true,
      canSubscribe: true,
      canPublishData: true,
      // Additional permissions for Security+ features
      canUpdateOwnMetadata: true,
      hidden: false
    })

    // Set token to expire in 24 hours
    at.ttl = 24 * 60 * 60 // 24 hours in seconds

    // Generate JWT token for LiveKit Cloud
    const token = await at.toJwt()

    return NextResponse.json({ 
      token,
      livekitUrl: livekitHost,
      expiresIn: 24 * 60 * 60 // 24 hours
    })
  } catch (error) {
    console.error('Token generation error:', error)
    return NextResponse.json(
      { error: 'Failed to generate token. Please check your LiveKit Cloud configuration.' },
      { status: 500 }
    )
  }
}
