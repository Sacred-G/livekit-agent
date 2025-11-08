'use client'

import { useState } from 'react'

interface WelcomeScreenProps {
  onJoinRoom: (url: string, token: string) => void
}

export function WelcomeScreen({ onJoinRoom }: WelcomeScreenProps) {
  const [participantName, setParticipantName] = useState('')
  const [isConnecting, setIsConnecting] = useState(false)

  const handleConnect = async () => {
    if (!participantName) {
      alert('Please enter your name')
      return
    }

    setIsConnecting(true)
    
    try {
      // Generate token by calling your Vercel API
      const response = await fetch('/api/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          roomName: 'security-plus-class',
          participantName,
        }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.error || 'Failed to generate token')
      }

      const { token, livekitUrl } = await response.json()
      onJoinRoom(livekitUrl, token)
    } catch (error) {
      console.error('Failed to connect:', error)
      alert(`Failed to connect: ${error.message}. Please try again.`)
    } finally {
      setIsConnecting(false)
    }
  }

  return (
    <div className="max-w-2xl mx-auto">
      <div className="security-card">
        <div className="text-center mb-6">
          <div className="w-20 h-20 bg-security-blue rounded-full mx-auto mb-4 flex items-center justify-center">
            <svg className="w-10 h-10 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h2 className="text-2xl font-bold text-security-dark mb-2">
            Join Security+ Class
          </h2>
          <p className="text-gray-600">
            Connect to your live Security+ exam preparation session
          </p>
        </div>
        
        <div className="space-y-4">
          <div>
            <label htmlFor="participant-name" className="block text-sm font-medium text-gray-700 mb-2">
              Your Name
            </label>
            <input
              id="participant-name"
              type="text"
              value={participantName}
              onChange={(e) => setParticipantName(e.target.value)}
              placeholder="Enter your full name"
              className="security-input w-full"
              onKeyPress={(e) => e.key === 'Enter' && handleConnect()}
            />
          </div>

          <button
            onClick={handleConnect}
            disabled={isConnecting || !participantName.trim()}
            className="security-button w-full disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isConnecting ? (
              <span className="flex items-center justify-center">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Connecting to LiveKit Cloud...
              </span>
            ) : (
              'Join Security+ Class'
            )}
          </button>
        </div>

        <div className="mt-6 p-4 bg-blue-50 rounded-lg">
          <h3 className="font-semibold text-blue-900 mb-2">🎓 What you'll experience:</h3>
          <ul className="text-sm text-blue-800 space-y-1">
            <li>• Live voice instruction from Security+ expert</li>
            <li>• Interactive Q&A sessions</li>
            <li>• Real-time exam practice questions</li>
            <li>• Personalized learning experience</li>
            <li>• Powered by LiveKit Cloud for crystal-clear audio</li>
          </ul>
        </div>

        <div className="mt-4 p-4 bg-green-50 rounded-lg">
          <h3 className="font-semibold text-green-900 mb-2">✅ Ready to start learning</h3>
          <p className="text-sm text-green-800">
            Just enter your name above and click "Join Security+ Class" to begin your session.
          </p>
        </div>
      </div>
    </div>
  )
}
