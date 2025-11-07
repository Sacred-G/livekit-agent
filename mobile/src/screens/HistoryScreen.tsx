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
import { useConversations } from '../store';
import { Conversation } from '../types';
import Icon from 'react-native-vector-icons/MaterialIcons';

interface Props {
  navigation: any;
}

const HistoryScreen: React.FC<Props> = ({ navigation }: Props) => {
  const { conversations } = useConversations();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadConversations();
  }, []);

  const loadConversations = async () => {
    try {
      // Mock conversations - in real app, this would come from your backend
      const mockConversations: Conversation[] = [
        {
          id: 'conv_1',
          agentId: 'assistant',
          agentName: 'General Assistant',
          messages: [],
          startTime: new Date(Date.now() - 3600000), // 1 hour ago
          endTime: new Date(Date.now() - 3000000),  // 50 minutes ago
          duration: 600, // 10 minutes
          status: 'completed'
        },
        {
          id: 'conv_2',
          agentId: 'security',
          agentName: 'Security Expert',
          messages: [],
          startTime: new Date(Date.now() - 86400000), // 1 day ago
          endTime: new Date(Date.now() - 86000000),  // 23.5 hours ago
          duration: 240, // 4 minutes
          status: 'completed'
        }
      ];

      // useConversations() would be updated here
      setLoading(false);
    } catch (error) {
      console.error('Failed to load conversations:', error);
      setLoading(false);
      Alert.alert('Error', 'Failed to load conversation history');
    }
  };

  const formatDuration = (seconds: number): string => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}m ${secs}s`;
  };

  const formatRelativeTime = (date: Date): string => {
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMins / 60);
    const diffDays = Math.floor(diffHours / 24);

    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    if (diffDays < 7) return `${diffDays}d ago`;
    return date.toLocaleDateString();
  };

  const renderConversationItem = ({ item }: { item: Conversation }) => (
    <TouchableOpacity
      style={styles.conversationCard}
      onPress={() => {
        // Navigate to conversation details
        console.log('View conversation:', item.id);
      }}
    >
      <View style={styles.conversationHeader}>
        <View style={styles.agentInfo}>
          <View style={styles.avatar}>
            <Text style={styles.avatarText}>
              {item.agentName.charAt(0).toUpperCase()}
            </Text>
          </View>
          <View style={styles.conversationDetails}>
            <Text style={styles.agentName}>{item.agentName}</Text>
            <Text style={styles.conversationTime}>
              {formatRelativeTime(item.startTime)}
            </Text>
          </View>
        </View>
        
        <View style={styles.conversationMeta}>
          <View style={[
            styles.statusBadge,
            { backgroundColor: item.status === 'completed' ? '#4CAF50' : '#FF9800' }
          ]}>
            <Text style={styles.statusText}>{item.status}</Text>
          </View>
          <Text style={styles.durationText}>
            {item.duration ? formatDuration(item.duration) : 'N/A'}
          </Text>
        </View>
      </View>

      <View style={styles.conversationFooter}>
        <Text style={styles.messageCount}>
          {item.messages.length} messages
        </Text>
        <Icon name="chevron-right" size={20} color="#8E8E93" />
      </View>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#007AFF" />
        <Text style={styles.loadingText}>Loading conversation history...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Conversation History</Text>
        <Text style={styles.headerSubtitle}>
          {conversations.length} conversation{conversations.length !== 1 ? 's' : ''}
        </Text>
      </View>

      {conversations.length === 0 ? (
        <View style={styles.emptyState}>
          <Icon name="chat-bubble-outline" size={64} color="#C6C6C8" />
          <Text style={styles.emptyTitle}>No conversations yet</Text>
          <Text style={styles.emptySubtitle}>
            Start your first conversation to see it here
          </Text>
          <TouchableOpacity
            style={styles.startButton}
            onPress={() => navigation.navigate('Home')}
          >
            <Text style={styles.startButtonText}>Start Conversation</Text>
          </TouchableOpacity>
        </View>
      ) : (
        <FlatList
          data={conversations}
          renderItem={renderConversationItem}
          keyExtractor={(item) => item.id}
          contentContainerStyle={styles.listContainer}
          showsVerticalScrollIndicator={false}
        />
      )}
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
  headerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#1D1D1F',
    marginBottom: 5,
  },
  headerSubtitle: {
    fontSize: 16,
    color: '#86868B',
  },
  listContainer: {
    paddingHorizontal: 20,
  },
  conversationCard: {
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
  conversationHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  agentInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  avatar: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#007AFF',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  avatarText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  conversationDetails: {
    flex: 1,
  },
  agentName: {
    fontSize: 16,
    fontWeight: '600',
    color: '#1D1D1F',
    marginBottom: 2,
  },
  conversationTime: {
    fontSize: 14,
    color: '#86868B',
  },
  conversationMeta: {
    alignItems: 'flex-end',
  },
  statusBadge: {
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
    marginBottom: 4,
  },
  statusText: {
    fontSize: 12,
    color: '#FFFFFF',
    fontWeight: '500',
    textTransform: 'capitalize',
  },
  durationText: {
    fontSize: 12,
    color: '#86868B',
  },
  conversationFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingTop: 12,
    borderTopWidth: 1,
    borderTopColor: '#F2F2F7',
  },
  messageCount: {
    fontSize: 14,
    color: '#86868B',
  },
  emptyState: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 40,
  },
  emptyTitle: {
    fontSize: 20,
    fontWeight: '600',
    color: '#1D1D1F',
    marginTop: 16,
    marginBottom: 8,
  },
  emptySubtitle: {
    fontSize: 16,
    color: '#86868B',
    textAlign: 'center',
    marginBottom: 24,
  },
  startButton: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 24,
    paddingVertical: 12,
    borderRadius: 8,
  },
  startButtonText: {
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

export default HistoryScreen;
