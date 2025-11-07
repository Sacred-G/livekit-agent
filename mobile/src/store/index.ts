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
    (set, get) => ({
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
      setUser: (user) => set({ user }),
      setAuthenticated: (authenticated) => set({ isAuthenticated: authenticated }),
      
      // Agent actions
      setAvailableAgents: (agents) => set({ availableAgents: agents }),
      setSelectedAgent: (agent) => set({ selectedAgent: agent }),
      
      // Conversation actions
      addConversation: (conversation) => 
        set((state) => ({ 
          conversations: [conversation, ...state.conversations] 
        })),
      
      updateConversation: (id, updates) =>
        set((state) => ({
          conversations: state.conversations.map(conv =>
            conv.id === id ? { ...conv, ...updates } : conv
          ),
          currentConversation: 
            state.currentConversation?.id === id 
              ? { ...state.currentConversation, ...updates }
              : state.currentConversation
        })),
      
      setCurrentConversation: (conversation) => set({ currentConversation: conversation }),
      
      // UI actions
      setVoiceMode: (enabled) => set({ isVoiceMode: enabled }),
      setSettingsOpen: (open) => set({ isSettingsOpen: open }),
      
      // User preferences
      updateUserPreferences: (preferences) =>
        set((state) => ({
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
      partialize: (state) => ({
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
