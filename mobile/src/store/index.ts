import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { Agent, User, UserPreferences, Conversation } from '../types';

interface AppState {
  // User state
  user: User | null;
  isAuthenticated: boolean;
  
  // Agent state
  availableAgents: Agent[];
  selectedAgent: Agent | null;
  
  // Conversation state
  conversations: Conversation[];
  currentConversation: Conversation | null;
  
  // UI state
  isVoiceMode: boolean;
  isSettingsOpen: boolean;
  
  // Actions
  setUser: (user: User | null) => void;
  setAuthenticated: (authenticated: boolean) => void;
  setAvailableAgents: (agents: Agent[]) => void;
  setSelectedAgent: (agent: Agent | null) => void;
  addConversation: (conversation: Conversation) => void;
  updateConversation: (id: string, updates: Partial<Conversation>) => void;
  setCurrentConversation: (conversation: Conversation | null) => void;
  setVoiceMode: (enabled: boolean) => void;
  setSettingsOpen: (open: boolean) => void;
  updateUserPreferences: (preferences: Partial<UserPreferences>) => void;
}

export const useAppStore = create<AppState>()(
  persist(
    (set: any, get: any) => ({
      // Initial state
      user: null,
      isAuthenticated: false,
      availableAgents: [],
      selectedAgent: null,
      conversations: [],
      currentConversation: null,
      isVoiceMode: true,
      isSettingsOpen: false,

      // User actions
      setUser: (user: User | null) => set({ user }),
      setAuthenticated: (authenticated: boolean) => set({ isAuthenticated: authenticated }),
      
      // Agent actions
      setAvailableAgents: (agents: Agent[]) => set({ availableAgents: agents }),
      setSelectedAgent: (agent: Agent | null) => set({ selectedAgent: agent }),
      
      // Conversation actions
      addConversation: (conversation: Conversation) => 
        set((state: any) => ({ 
          conversations: [conversation, ...state.conversations] 
        })),
      
      updateConversation: (id: string, updates: Partial<Conversation>) =>
        set((state: any) => ({
          conversations: state.conversations.map((conv: any) =>
            conv.id === id ? { ...conv, ...updates } : conv
          ),
          currentConversation: 
            state.currentConversation?.id === id 
              ? { ...state.currentConversation, ...updates }
              : state.currentConversation
        })),
      
      setCurrentConversation: (conversation: Conversation | null) => set({ currentConversation: conversation }),
      
      // UI actions
      setVoiceMode: (enabled: boolean) => set({ isVoiceMode: enabled }),
      setSettingsOpen: (open: boolean) => set({ isSettingsOpen: open }),
      
      // User preferences
      updateUserPreferences: (preferences: Partial<UserPreferences>) =>
        set((state: any) => ({
          user: state.user 
            ? { 
                ...state.user, 
                preferences: { ...state.user.preferences, ...preferences } 
              }
            : null
        })),
    }),
    {
      name: 'livekit-agent-storage',
      partialize: (state: any) => ({
        user: state.user,
        selectedAgent: state.selectedAgent,
        conversations: state.conversations,
        isVoiceMode: state.isVoiceMode,
      }),
    }
  )
);

// Selectors for common state combinations
export const useAuth = () => {
  const { user, isAuthenticated, setUser, setAuthenticated } = useAppStore();
  return { user, isAuthenticated, setUser, setAuthenticated };
};

export const useAgents = () => {
  const { availableAgents, selectedAgent, setAvailableAgents, setSelectedAgent } = useAppStore();
  return { availableAgents, selectedAgent, setAvailableAgents, setSelectedAgent };
};

export const useConversations = () => {
  const { 
    conversations, 
    currentConversation, 
    addConversation, 
    updateConversation, 
    setCurrentConversation 
  } = useAppStore();
  return { 
    conversations, 
    currentConversation, 
    addConversation, 
    updateConversation, 
    setCurrentConversation 
  };
};

export const useUI = () => {
  const { isVoiceMode, isSettingsOpen, setVoiceMode, setSettingsOpen } = useAppStore();
  return { isVoiceMode, isSettingsOpen, setVoiceMode, setSettingsOpen };
};

export const useUserPreferences = () => {
  const { user, updateUserPreferences } = useAppStore();
  const preferences = user?.preferences;
  return { preferences, updateUserPreferences };
};
