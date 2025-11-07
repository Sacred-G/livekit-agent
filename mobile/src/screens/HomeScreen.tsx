import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
  Alert,
} from 'react-native';
import { useAgents, useAuth } from '../store';
import { Agent } from '../types';
import { useLiveKit } from '../services/livekit';

interface Props {
  navigation: any;
}

const HomeScreen: React.FC<Props> = ({ navigation }) => {
  const { availableAgents, selectedAgent, setSelectedAgent } = useAgents();
  const { user } = useAuth();
  const { connectToAgent, connectionState } = useLiveKit();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadAgents();
  }, []);

  const loadAgents = async () => {
    try {
      // Mock agents - in real app, this would come from your backend
      const mockAgents: Agent[] = [
        {
          id: 'assistant',
          name: 'General Assistant',
          description: 'Helpful AI assistant for everyday tasks',
          capabilities: ['conversation', 'information', 'tasks'],
          status: 'online'
        },
        {
          id: 'security',
          name: 'Security Expert',
          description: 'Specialized in cybersecurity and best practices',
          capabilities: ['security', 'analysis', 'guidance'],
          status: 'online'
        },
        {
          id: 'tutor',
          name: 'Learning Tutor',
          description: 'Educational assistant for various subjects',
          capabilities: ['teaching', 'explanation', 'learning'],
          status: 'online'
        }
      ];

      // useAgents().setAvailableAgents(mockAgents);
      setLoading(false);
    } catch (error) {
      console.error('Failed to load agents:', error);
      setLoading(false);
      Alert.alert('Error', 'Failed to load available agents');
    }
  };

  const handleAgentSelect = async (agent: Agent) => {
    if (agent.status !== 'online') {
      Alert.alert('Agent Unavailable', 'This agent is currently offline');
      return;
    }

    setSelectedAgent(agent);
    
    try {
      // In a real implementation, you would generate a token from your backend
      const serverUrl = 'wss://your-livekit-server.com';
      const token = 'your-generated-token';
      
      await connectToAgent(agent, serverUrl, token);
      navigation.navigate('Call');
    } catch (error) {
      console.error('Failed to connect to agent:', error);
      Alert.alert('Connection Error', 'Failed to connect to the agent');
    }
  };

  const renderAgentItem = ({ item }: { item: Agent }) => (
    <TouchableOpacity
      style={[
        styles.agentCard,
        selectedAgent?.id === item.id && styles.selectedCard,
        item.status !== 'online' && styles.disabledCard
      ]}
      onPress={() => handleAgentSelect(item)}
      disabled={item.status !== 'online'}
    >
      <View style={styles.agentHeader}>
        <View style={styles.avatar}>
          <Text style={styles.avatarText}>
            {item.name.charAt(0).toUpperCase()}
          </Text>
        </View>
        <View style={styles.agentInfo}>
          <Text style={styles.agentName}>{item.name}</Text>
          <Text style={styles.agentDescription}>{item.description}</Text>
        </View>
        <View style={[
          styles.statusIndicator,
          { backgroundColor: item.status === 'online' ? '#4CAF50' : '#9E9E9E' }
        ]} />
      </View>
      
      <View style={styles.capabilities}>
        {item.capabilities.map((capability, index) => (
          <View key={index} style={styles.capabilityTag}>
            <Text style={styles.capabilityText}>{capability}</Text>
          </View>
        ))}
      </View>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#007AFF" />
        <Text style={styles.loadingText}>Loading agents...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.welcomeText}>
          Welcome back{user?.displayName ? `, ${user.displayName}` : ''}!
        </Text>
        <Text style={styles.subtitleText}>Choose an agent to start a conversation</Text>
      </View>

      <FlatList
        data={availableAgents}
        renderItem={renderAgentItem}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.listContainer}
        showsVerticalScrollIndicator={false}
      />

      <TouchableOpacity
        style={styles.historyButton}
        onPress={() => navigation.navigate('History')}
      >
        <Text style={styles.historyButtonText}>Conversation History</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F7',
  },
  header: {
    padding: 20,
    paddingBottom: 10,
  },
  welcomeText: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#1D1D1F',
    marginBottom: 5,
  },
  subtitleText: {
    fontSize: 16,
    color: '#86868B',
  },
  listContainer: {
    paddingHorizontal: 20,
  },
  agentCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  selectedCard: {
    borderWidth: 2,
    borderColor: '#007AFF',
  },
  disabledCard: {
    opacity: 0.6,
  },
  agentHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
  },
  avatar: {
    width: 50,
    height: 50,
    borderRadius: 25,
    backgroundColor: '#007AFF',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  avatarText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  agentInfo: {
    flex: 1,
  },
  agentName: {
    fontSize: 18,
    fontWeight: '600',
    color: '#1D1D1F',
    marginBottom: 2,
  },
  agentDescription: {
    fontSize: 14,
    color: '#86868B',
  },
  statusIndicator: {
    width: 12,
    height: 12,
    borderRadius: 6,
  },
  capabilities: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
  },
  capabilityTag: {
    backgroundColor: '#E3F2FD',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  capabilityText: {
    fontSize: 12,
    color: '#1976D2',
    fontWeight: '500',
  },
  historyButton: {
    backgroundColor: '#007AFF',
    margin: 20,
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
  },
  historyButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 10,
    fontSize: 16,
    color: '#86868B',
  },
});

export default HomeScreen;
