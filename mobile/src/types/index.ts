export interface Agent {
  id: string;
  name: string;
  description: string;
  voice?: string;
  avatar?: string;
  capabilities: string[];
  status: 'online' | 'offline' | 'busy';
}

export interface Room {
  id: string;
  name: string;
  agentId: string;
  participantId: string;
  token: string;
  serverUrl: string;
  createdAt: Date;
  isActive: boolean;
}

export interface Message {
  id: string;
  roomId: string;
  content: string;
  type: 'text' | 'audio';
  sender: 'user' | 'agent';
  timestamp: Date;
  metadata?: Record<string, any>;
}

export interface Conversation {
  id: string;
  agentId: string;
  agentName: string;
  messages: Message[];
  startTime: Date;
  endTime?: Date;
  duration?: number;
  status: 'active' | 'completed' | 'failed';
}

export interface AudioSession {
  isConnected: boolean;
  isMuted: boolean;
  isSpeaking: boolean;
  volume: number;
}

export interface User {
  id: string;
  email: string;
  displayName: string;
  avatar?: string;
  preferences: UserPreferences;
}

export interface UserPreferences {
  preferredAgent?: string;
  voiceEnabled: boolean;
  textModeEnabled: boolean;
  notificationsEnabled: boolean;
  audioQuality: 'low' | 'medium' | 'high';
  language: string;
}

export interface LiveKitConfig {
  serverUrl: string;
  apiKey: string;
  apiSecret: string;
}

export interface AuthConfig {
  provider: 'firebase' | 'supabase' | 'custom';
  config: Record<string, any>;
}

export type ConnectionState = 
  | 'disconnected'
  | 'connecting'
  | 'connected'
  | 'reconnecting'
  | 'failed';

export type CallState = 
  | 'idle'
  | 'calling'
  | 'connected'
  | 'ended'
  | 'failed';

export interface AppError {
  code: string;
  message: string;
  details?: any;
}
