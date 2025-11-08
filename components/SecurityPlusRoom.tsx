'use client'

import { useState, useEffect } from 'react'
import {
  LiveKitRoom,
  AudioConference,
  ParticipantTile,
  RoomAudioRenderer,
  ControlBar,
  useLocalParticipant,
  useConnectionState,
} from '@livekit/components-react'
import { ConnectionState } from 'livekit-client'

interface SecurityPlusRoomProps {
  livekitUrl: string
  token: string
  onLeaveRoom: () => void
}

export function SecurityPlusRoom({ livekitUrl, token, onLeaveRoom }: SecurityPlusRoomProps) {
  const [isMuted, setIsMuted] = useState(false)
  const connectionState = useConnectionState()
  const { localParticipant } = useLocalParticipant()

  useEffect(() => {
    // Auto-unmute when joining
    if (connectionState === ConnectionState.Connected && localParticipant) {
      localParticipant.setMicrophoneEnabled(true)
    }
  }, [connectionState, localParticipant])

  const handleDisconnect = () => {
    onLeaveRoom()
  }

  if (connectionState === ConnectionState.Disconnected) {
    return (
      <div className="max-w-2xl mx-auto">
        <div className="security-card text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-security-blue mx-auto mb-4"></div>
          <p className="text-lg text-gray-600">Connecting to Security+ class...</p>
        </div>
      </div>
    )
  }

  if (connectionState === ConnectionState.Reconnecting) {
    return (
      <div className="max-w-2xl mx-auto">
        <div className="security-card text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-security-blue mx-auto mb-4"></div>
          <p className="text-lg text-gray-600">Reconnecting to class...</p>
        </div>
      </div>
    )
  }

  return (
    <LiveKitRoom
      serverUrl={livekitUrl}
      token={token}
      connect={true}
      audio={true}
      video={false}
      onDisconnected={handleDisconnect}
    >
      <div className="max-w-4xl mx-auto">
        <div className="security-card mb-6">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-2xl font-bold text-security-dark">
              Security+ Class Session
            </h2>
            <button
              onClick={handleDisconnect}
              className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg transition-colors"
            >
              Leave Class
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Instructor/Agent View */}
            <div>
              <h3 className="text-lg font-semibold text-gray-700 mb-3">Instructor</h3>
              <div className="bg-gray-100 rounded-lg p-4 h-48 flex items-center justify-center">
                <div className="text-center">
                  <div className="w-16 h-16 bg-security-blue rounded-full mx-auto mb-2 flex items-center justify-center">
                    <svg className="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <p className="text-sm text-gray-600">Security+ Instructor</p>
                  <p className="text-xs text-gray-500">Ready to teach</p>
                </div>
              </div>
            </div>

            {/* Your View */}
            <div>
              <h3 className="text-lg font-semibold text-gray-700 mb-3">You</h3>
              <ParticipantTile />
            </div>
          </div>

          {/* Audio Controls */}
          <div className="mt-6">
            <AudioConference />
            <RoomAudioRenderer />
          </div>

          {/* Control Bar */}
          <div className="mt-4 flex justify-center">
            <ControlBar
              variation="minimal"
              controls={{ microphone: true, leave: true }}
            />
          </div>

          {/* Session Info */}
          <div className="mt-6 p-4 bg-green-50 rounded-lg">
            <h3 className="font-semibold text-green-900 mb-2">Session Active</h3>
            <p className="text-sm text-green-800">
              You&apos;re connected to the Security+ exam preparation session. 
              Your instructor will guide you through the material and answer your questions.
            </p>
          </div>
        </div>
      </div>
    </LiveKitRoom>
  )
}
