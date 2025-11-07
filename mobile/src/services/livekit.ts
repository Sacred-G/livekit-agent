import { Room, Agent, ConnectionState, CallState } from '../types';
import { LiveKitRoom, AudioSession } from '@livekit/react-native';
import { Track } from 'livekit-client';

export class LiveKitService {
  private static instance: LiveKitService;
  private currentRoom: Room | null = null;
  private connectionState: ConnectionState = 'disconnected';
  private callState: CallState = 'idle';

  private constructor() {}

  static getInstance(): LiveKitService {
    if (!LiveKitService.instance) {
      LiveKitService.instance = new LiveKitService();
    }
    return LiveKitService.instance;
  }

  async connectToAgent(agent: Agent, serverUrl: string, token: string): Promise<Room> {
    try {
      this.connectionState = 'connecting';
      this.callState = 'calling';

      // Start audio session
      await AudioSession.startAudioSession();

      // Create room instance
      const room: Room = {
        id: `room_${Date.now()}`,
        name: `Conversation with ${agent.name}`,
        agentId: agent.id,
        participantId: `user_${Date.now()}`,
        token,
        serverUrl,
        createdAt: new Date(),
        isActive: true
      };

      this.currentRoom = room;
      this.connectionState = 'connected';
      this.callState = 'connected';

      return room;
    } catch (error) {
      this.connectionState = 'failed';
      this.callState = 'failed';
      throw error;
    }
  }

  async disconnect(): Promise<void> {
    try {
      if (this.currentRoom) {
        this.currentRoom.isActive = false;
        this.currentRoom = null;
      }
      
      await AudioSession.stopAudioSession();
      this.connectionState = 'disconnected';
      this.callState = 'ended';
    } catch (error) {
      console.error('Error disconnecting:', error);
      throw error;
    }
  }

  async muteMicrophone(isMuted: boolean): Promise<void> {
    // Implementation will depend on LiveKit room instance
    console.log(`Microphone ${isMuted ? 'muted' : 'unmuted'}`);
  }

  async setSpeakerVolume(volume: number): Promise<void> {
    // Volume range: 0.0 to 1.0
    console.log(`Speaker volume set to ${volume}`);
  }

  getConnectionState(): ConnectionState {
    return this.connectionState;
  }

  getCallState(): CallState {
    return this.callState;
  }

  getCurrentRoom(): Room | null {
    return this.currentRoom;
  }

  isConnected(): boolean {
    return this.connectionState === 'connected';
  }

  isInCall(): boolean {
    return this.callState === 'connected';
  }
}

// React Hook for LiveKit functionality
import { useState, useEffect, useCallback } from 'react';

export function useLiveKit() {
  const [connectionState, setConnectionState] = useState<ConnectionState>('disconnected');
  const [callState, setCallState] = useState<CallState>('idle');
  const [currentRoom, setCurrentRoom] = useState<Room | null>(null);
  const [isMuted, setIsMuted] = useState(false);
  const [volume, setVolume] = useState(0.8);

  const service = LiveKitService.getInstance();

  useEffect(() => {
    // Update state from service
    const interval = setInterval(() => {
      setConnectionState(service.getConnectionState());
      setCallState(service.getCallState());
      setCurrentRoom(service.getCurrentRoom());
    }, 100);

    return () => clearInterval(interval);
  }, [service]);

  const connectToAgent = useCallback(async (agent: Agent, serverUrl: string, token: string) => {
    try {
      const room = await service.connectToAgent(agent, serverUrl, token);
      return room;
    } catch (error) {
      console.error('Failed to connect to agent:', error);
      throw error;
    }
  }, [service]);

  const disconnect = useCallback(async () => {
    try {
      await service.disconnect();
    } catch (error) {
      console.error('Failed to disconnect:', error);
      throw error;
    }
  }, [service]);

  const mute = useCallback(async (muted: boolean) => {
    try {
      await service.muteMicrophone(muted);
      setIsMuted(muted);
    } catch (error) {
      console.error('Failed to toggle mute:', error);
      throw error;
    }
  }, [service]);

  const setSpeakerVolume = useCallback(async (newVolume: number) => {
    try {
      await service.setSpeakerVolume(newVolume);
      setVolume(newVolume);
    } catch (error) {
      console.error('Failed to set volume:', error);
      throw error;
    }
  }, [service]);

  return {
    connectionState,
    callState,
    currentRoom,
    isMuted,
    volume,
    connectToAgent,
    disconnect,
    mute,
    setSpeakerVolume,
    isConnected: connectionState === 'connected',
    isInCall: callState === 'connected'
  };
}
