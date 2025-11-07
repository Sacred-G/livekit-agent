import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  Switch,
  Alert,
  ScrollView,
} from 'react-native';
import { useAuth, useUserPreferences } from '../store';
import Icon from 'react-native-vector-icons/MaterialIcons';

interface Props {
  navigation: any;
}

const SettingsScreen: React.FC<Props> = ({ navigation }) => {
  const { user, setAuthenticated } = useAuth();
  const { preferences, updateUserPreferences } = useUserPreferences();
  const [serverUrl, setServerUrl] = useState('wss://your-livekit-server.com');

  const handleSignOut = () => {
    Alert.alert(
      'Sign Out',
      'Are you sure you want to sign out?',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Sign Out',
          style: 'destructive',
          onPress: () => {
            setAuthenticated(false);
            // Navigate to login screen if you have one
          },
        },
      ]
    );
  };

  const handleToggleVoiceMode = (value: boolean) => {
    updateUserPreferences({ voiceEnabled: value });
  };

  const handleToggleTextMode = (value: boolean) => {
    updateUserPreferences({ textModeEnabled: value });
  };

  const handleToggleNotifications = (value: boolean) => {
    updateUserPreferences({ notificationsEnabled: value });
  };

  const handleAudioQualityChange = (quality: 'low' | 'medium' | 'high') => {
    updateUserPreferences({ audioQuality: quality });
  };

  const handleLanguageChange = (language: string) => {
    updateUserPreferences({ language });
  };

  const renderSettingItem = (
    title: string,
    subtitle?: string,
    rightComponent?: React.ReactNode,
    onPress?: () => void,
    icon?: string
  ) => (
    <TouchableOpacity style={styles.settingItem} onPress={onPress}>
      <View style={styles.settingLeft}>
        {icon && (
          <Icon name={icon} size={24} color="#007AFF" style={styles.settingIcon} />
        )}
        <View>
          <Text style={styles.settingTitle}>{title}</Text>
          {subtitle && <Text style={styles.settingSubtitle}>{subtitle}</Text>}
        </View>
      </View>
      {rightComponent}
    </TouchableOpacity>
  );

  const renderSection = (title: string, children: React.ReactNode) => (
    <View style={styles.section}>
      <Text style={styles.sectionTitle}>{title}</Text>
      <View style={styles.sectionContent}>{children}</View>
    </View>
  );

  return (
    <View style={styles.container}>
      <ScrollView showsVerticalScrollIndicator={false}>
        {/* User Profile Section */}
        {renderSection(
          'Profile',
          renderSettingItem(
            user?.displayName || 'Guest User',
            user?.email || 'Not signed in',
            <Icon name="chevron-right" size={20} color="#8E8E93" />,
            () => console.log('Navigate to profile'),
            'person'
          )
        )}

        {/* Audio Settings Section */}
        {renderSection(
          'Audio Settings',
          <>
            {renderSettingItem(
              'Voice Mode',
              'Enable voice conversations',
              <Switch
                value={preferences?.voiceEnabled ?? true}
                onValueChange={handleToggleVoiceMode}
                trackColor={{ false: '#E5E5EA', true: '#007AFF' }}
              />
            )}
            {renderSettingItem(
              'Text Mode',
              'Enable text-based chat',
              <Switch
                value={preferences?.textModeEnabled ?? true}
                onValueChange={handleToggleTextMode}
                trackColor={{ false: '#E5E5EA', true: '#007AFF' }}
              />
            )}
            {renderSettingItem(
              'Audio Quality',
              `Current: ${preferences?.audioQuality || 'medium'}`,
              <View style={styles.qualityButtons}>
                {(['low', 'medium', 'high'] as const).map((quality) => (
                  <TouchableOpacity
                    key={quality}
                    style={[
                      styles.qualityButton,
                      preferences?.audioQuality === quality && styles.qualityButtonActive,
                    ]}
                    onPress={() => handleAudioQualityChange(quality)}
                  >
                    <Text
                      style={[
                        styles.qualityButtonText,
                        preferences?.audioQuality === quality && styles.qualityButtonTextActive,
                      ]}
                    >
                      {quality.charAt(0).toUpperCase() + quality.slice(1)}
                    </Text>
                  </TouchableOpacity>
                ))}
              </View>
            )}
          </>
        )}

        {/* Notification Settings */}
        {renderSection(
          'Notifications',
          renderSettingItem(
            'Push Notifications',
            'Receive notifications for new messages',
            <Switch
              value={preferences?.notificationsEnabled ?? true}
              onValueChange={handleToggleNotifications}
              trackColor={{ false: '#E5E5EA', true: '#007AFF' }}
            />,
            undefined,
            'notifications'
          )
        )}

        {/* Server Settings */}
        {renderSection(
          'Server Settings',
          renderSettingItem(
            'LiveKit Server',
            serverUrl,
            <Icon name="edit" size={20} color="#8E8E93" />,
            () => console.log('Edit server URL'),
            'settings-ethernet'
          )
        )}

        {/* Language Settings */}
        {renderSection(
          'Language',
          renderSettingItem(
            'App Language',
            preferences?.language || 'English',
            <Icon name="chevron-right" size={20} color="#8E8E93" />,
            () => console.log('Select language'),
            'language'
          )
        )}

        {/* About Section */}
        {renderSection(
          'About',
          <>
            {renderSettingItem(
              'Version',
              '1.0.0',
              null,
              undefined,
              'info'
            )}
            {renderSettingItem(
              'Help & Support',
              'Get help with the app',
              <Icon name="chevron-right" size={20} color="#8E8E93" />,
              () => console.log('Navigate to help'),
              'help'
            )}
            {renderSettingItem(
              'Privacy Policy',
              'View our privacy policy',
              <Icon name="chevron-right" size={20} color="#8E8E93" />,
              () => console.log('View privacy policy'),
              'privacy-tip'
            )}
          </>
        )}

        {/* Sign Out Button */}
        <View style={styles.section}>
          <TouchableOpacity style={styles.signOutButton} onPress={handleSignOut}>
            <Icon name="logout" size={24} color="#D70015" />
            <Text style={styles.signOutText}>Sign Out</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.footer}>
          <Text style={styles.footerText}>LiveKit Voice Agent Mobile</Text>
          <Text style={styles.footerSubtext}>© 2024 All rights reserved</Text>
        </View>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F7',
  },
  section: {
    marginTop: 20,
    backgroundColor: '#FFFFFF',
    paddingVertical: 8,
  },
  sectionTitle: {
    fontSize: 13,
    fontWeight: '600',
    color: '#8E8E93',
    paddingHorizontal: 20,
    paddingBottom: 8,
    textTransform: 'uppercase',
  },
  sectionContent: {
    backgroundColor: '#FFFFFF',
  },
  settingItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#F2F2F7',
  },
  settingLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  settingIcon: {
    marginRight: 12,
  },
  settingTitle: {
    fontSize: 16,
    fontWeight: '500',
    color: '#1D1D1F',
  },
  settingSubtitle: {
    fontSize: 14,
    color: '#8E8E93',
    marginTop: 2,
  },
  qualityButtons: {
    flexDirection: 'row',
    gap: 8,
  },
  qualityButton: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 6,
    backgroundColor: '#F2F2F7',
    borderWidth: 1,
    borderColor: '#E5E5EA',
  },
  qualityButtonActive: {
    backgroundColor: '#007AFF',
    borderColor: '#007AFF',
  },
  qualityButtonText: {
    fontSize: 12,
    fontWeight: '500',
    color: '#8E8E93',
  },
  qualityButtonTextActive: {
    color: '#FFFFFF',
  },
  signOutButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 16,
    marginHorizontal: 20,
    marginVertical: 12,
    borderRadius: 8,
    backgroundColor: '#FFF5F5',
    borderWidth: 1,
    borderColor: '#FFE5E5',
  },
  signOutText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#D70015',
    marginLeft: 8,
  },
  footer: {
    alignItems: 'center',
    paddingVertical: 40,
  },
  footerText: {
    fontSize: 14,
    color: '#8E8E93',
    fontWeight: '500',
  },
  footerSubtext: {
    fontSize: 12,
    color: '#C6C6C8',
    marginTop: 4,
  },
});

export default SettingsScreen;
