import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  Alert,
  Dimensions,
  Animated,
} from 'react-native';
import { useAgents } from '../store';
import { useLiveKit } from '../services/livekit';
import Icon from 'react-native-vector-icons/MaterialIcons';

interface Props {
  navigation: any;
}

const { width, height } = Dimensions.get('window');

const CallScreen: React.FC<Props> = ({ navigation }) => {
  const { selectedAgent } = useAgents();
  const { 
    disconnect, 
    mute, 
    isMuted, 
    volume, 
    setSpeakerVolume, 
    connectionState, 
    callState, 
    isConnected,
    isInCall 
  } = useLiveKit();
  
  const [callDuration, setCallDuration] = useState(0);
  const [pulseAnim] = useState(new Animated.Value(1));

  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (isInCall) {
      interval = setInterval(() => {
        setCallDuration(prev => prev + 1);
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isInCall]);

  useEffect(() => {
    // Pulse animation when speaking
    const pulseAnimation = Animated.loop(
      Animated.sequence([
        Animated.timing(pulseAnim, {
          toValue: 1.2,
          duration: 1000,
          useNativeDriver: true,
        }),
        Animated.timing(pulseAnim, {
          toValue: 1,
          duration: 1000,
          useNativeDriver: true,
        }),
      ])
    );
    
    if (isInCall) {
      pulseAnimation.start();
    }
    
    return () => pulseAnimation.stop();
  }, [isInCall, pulseAnim]);

  const handleEndCall = async () => {
    try {
      await disconnect();
      navigation.goBack();
    } catch (error) {
      console.error('Error ending call:', error);
      Alert.alert('Error', 'Failed to end the call');
    }
  };

  const handleMuteToggle = async () => {
    try {
      await mute(!isMuted);
    } catch (error) {
      console.error('Error toggling mute:', error);
    }
  };

  const handleVolumeChange = async (newVolume: number) => {
    try {
      await setSpeakerVolume(newVolume);
    } catch (error) {
      console.error('Error changing volume:', error);
    }
  };

  const formatDuration = (seconds: number): string => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const getConnectionStatusText = (): string => {
    switch (connectionState) {
      case 'connecting':
        return 'Connecting...';
      case 'connected':
        return callState === 'connected' ? 'Connected' : 'Waiting for agent...';
      case 'reconnecting':
        return 'Reconnecting...';
      case 'failed':
        return 'Connection Failed';
      default:
        return 'Disconnected';
    }
  };

  const getConnectionStatusColor = (): string => {
    switch (connectionState) {
      case 'connected':
        return '#4CAF50';
      case 'connecting':
      case 'reconnecting':
        return '#FF9800';
      case 'failed':
        return '#F44336';
      default:
        return '#9E9E9E';
    }
  };

  if (!selectedAgent) {
    return (
      <View style={styles.container}>
        <Text style={styles.errorText}>No agent selected</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity onPress={() => navigation.goBack()}>
          <Icon name="arrow-back" size={24} color="#FFFFFF" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Voice Call</Text>
        <View style={{ width: 24 }} />
      </View>

      {/* Agent Info */}
      <View style={styles.agentSection}>
        <Animated.View style={[styles.avatarContainer, { transform: [{ scale: pulseAnim }] }]}>
          <View style={styles.avatar}>
            <Text style={styles.avatarText}>
              {selectedAgent.name.charAt(0).toUpperCase()}
            </Text>
          </View>
          <View style={[styles.statusDot, { backgroundColor: getConnectionStatusColor() }]} />
        </Animated.View>
        
        <Text style={styles.agentName}>{selectedAgent.name}</Text>
        <Text style={styles.statusText}>{getConnectionStatusText()}</Text>
        
        {isInCall && (
          <Text style={styles.durationText}>{formatDuration(callDuration)}</Text>
        )}
      </View>

      {/* Audio Visualization Placeholder */}
      <View style={styles.visualizationContainer}>
        <View style={styles.visualizationBars}>
          {[1, 2, 3, 4, 5, 6, 7, 8].map((index) => (
            <View
              key={index}
              style={[
                styles.visualizationBar,
                { height: Math.random() * 60 + 20 }
              ]}
            />
          ))}
        </View>
      </View>

      {/* Controls */}
      <View style={styles.controlsContainer}>
        {/* Volume Control */}
        <View style={styles.volumeControl}>
          <Icon name="volume-down" size={24} color="#FFFFFF" />
          <TouchableOpacity
            style={styles.volumeSlider}
            onPress={() => handleVolumeChange(Math.max(0, volume - 0.1))}
          >
            <View style={[styles.volumeTrack, { width: `${volume * 100}%` }]} />
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.volumeSlider}
            onPress={() => handleVolumeChange(Math.min(1, volume + 0.1))}
          >
            <Icon name="volume-up" size={24} color="#FFFFFF" />
          </TouchableOpacity>
        </View>

        {/* Action Buttons */}
        <View style={styles.actionButtons}>
          <TouchableOpacity
            style={[styles.actionButton, styles.muteButton, isMuted && styles.mutedButton]}
            onPress={handleMuteToggle}
          >
            <Icon 
              name={isMuted ? "mic-off" : "mic"} 
              size={24} 
              color="#FFFFFF" 
            />
            <Text style={styles.actionButtonText}>
              {isMuted ? "Unmute" : "Mute"}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.actionButton, styles.speakerButton]}
            onPress={() => {}}
          >
            <Icon name="speaker" size={24} color="#FFFFFF" />
            <Text style={styles.actionButtonText}>Speaker</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.actionButton, styles.textButton]}
            onPress={() => {}}
          >
            <Icon name="chat" size={24} color="#FFFFFF" />
            <Text style={styles.actionButtonText}>Text</Text>
          </TouchableOpacity>
        </View>

        {/* End Call Button */}
        <TouchableOpacity
          style={styles.endCallButton}
          onPress={handleEndCall}
        >
          <Icon name="call-end" size={28} color="#FFFFFF" />
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1C1C1E',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingTop: 60,
    paddingHorizontal: 20,
    paddingBottom: 20,
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  agentSection: {
    alignItems: 'center',
    paddingTop: 40,
    paddingBottom: 60,
  },
  avatarContainer: {
    position: 'relative',
    marginBottom: 20,
  },
  avatar: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: '#007AFF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  avatarText: {
    fontSize: 48,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  statusDot: {
    position: 'absolute',
    bottom: 5,
    right: 5,
    width: 20,
    height: 20,
    borderRadius: 10,
    borderWidth: 3,
    borderColor: '#1C1C1E',
  },
  agentName: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 8,
  },
  statusText: {
    fontSize: 16,
    color: '#8E8E93',
    marginBottom: 8,
  },
  durationText: {
    fontSize: 18,
    color: '#007AFF',
    fontWeight: '500',
  },
  visualizationContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 40,
  },
  visualizationBars: {
    flexDirection: 'row',
    alignItems: 'center',
    height: 100,
    gap: 4,
  },
  visualizationBar: {
    flex: 1,
    backgroundColor: '#007AFF',
    borderRadius: 2,
    minHeight: 20,
  },
  controlsContainer: {
    paddingHorizontal: 20,
    paddingBottom: 40,
  },
  volumeControl: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 40,
  },
  volumeSlider: {
    flex: 1,
    height: 40,
    justifyContent: 'center',
    marginHorizontal: 15,
  },
  volumeTrack: {
    height: 4,
    backgroundColor: '#007AFF',
    borderRadius: 2,
  },
  actionButtons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 40,
  },
  actionButton: {
    alignItems: 'center',
    paddingVertical: 15,
    paddingHorizontal: 20,
    borderRadius: 25,
    backgroundColor: '#2C2C2E',
    minWidth: 80,
  },
  muteButton: {
    backgroundColor: '#2C2C2E',
  },
  mutedButton: {
    backgroundColor: '#D70015',
  },
  speakerButton: {
    backgroundColor: '#2C2C2E',
  },
  textButton: {
    backgroundColor: '#2C2C2E',
  },
  actionButtonText: {
    color: '#FFFFFF',
    fontSize: 12,
    marginTop: 5,
    fontWeight: '500',
  },
  endCallButton: {
    alignSelf: 'center',
    width: 64,
    height: 64,
    borderRadius: 32,
    backgroundColor: '#D70015',
    justifyContent: 'center',
    alignItems: 'center',
  },
  errorText: {
    fontSize: 18,
    color: '#FFFFFF',
    textAlign: 'center',
    marginTop: 100,
  },
});

export default CallScreen;
