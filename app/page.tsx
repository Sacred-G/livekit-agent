'use client'

import { useState, useEffect } from 'react'
import { SecurityPlusRoom } from '@/components/SecurityPlusRoom'
import { WelcomeScreen } from '@/components/WelcomeScreen'

export default function Home() {
  const [isJoined, setIsJoined] = useState(false)
  const [livekitUrl, setLivekitUrl] = useState('')
  const [token, setToken] = useState('')

  const handleJoinRoom = (url: string, roomToken: string) => {
    setLivekitUrl(url)
    setToken(roomToken)
    setIsJoined(true)
  }

  const handleLeaveRoom = () => {
    setIsJoined(false)
    setLivekitUrl('')
    setToken('')
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-security-light to-white">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold text-security-dark mb-4">
            Security+ Exam Teaching Assistant
          </h1>
          <p className="text-xl text-gray-600">
            Interactive voice-based CompTIA Security+ exam preparation
          </p>
        </header>

        {!isJoined ? (
          <WelcomeScreen onJoinRoom={handleJoinRoom} />
        ) : (
          <SecurityPlusRoom
            livekitUrl={livekitUrl}
            token={token}
            onLeaveRoom={handleLeaveRoom}
          />
        )}
      </div>
    </main>
  )
}
