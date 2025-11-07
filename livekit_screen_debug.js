// LiveKit Screen Sharing Debug Script
// Run this in browser console when the app is running

async function debugLiveKitScreenShare() {
    console.log('🔍 LiveKit Screen Share Debug');
    console.log('================================');
    
    // Check if we have a LiveKit room
    const room = window.__lk_room;
    if (!room) {
        console.error('❌ No LiveKit room found. Make sure you\'re connected to a session.');
        return;
    }
    
    console.log('✅ LiveKit room found:', room);
    console.log('Room state:', room.state);
    console.log('Local participant:', room.localParticipant);
    
    // Check participant permissions
    const participant = room.localParticipant;
    console.log('Participant permissions:', {
        canPublish: participant.permissions?.canPublish,
        canSubscribe: participant.permissions?.canSubscribe,
        canPublishData: participant.permissions?.canPublishData
    });
    
    try {
        console.log('🔄 Attempting to enable screen sharing...');
        
        // Try to enable screen share through LiveKit
        await participant.setScreenShareEnabled(true);
        console.log('✅ Screen sharing enabled successfully!');
        
        // Check if screen share track is published
        const screenTracks = participant.getTracks(Track.Source.ScreenShare);
        console.log('Screen share tracks:', screenTracks);
        
        if (screenTracks.length > 0) {
            console.log('✅ Screen share track is published:', screenTracks[0]);
        } else {
            console.warn('⚠️ No screen share tracks found after enabling');
        }
        
    } catch (error) {
        console.error('❌ Screen sharing failed:', error);
        console.error('Error name:', error.name);
        console.error('Error message:', error.message);
        
        // Provide specific solutions
        if (error.name === 'NotAllowedError') {
            console.log('💡 Solution: Grant screen sharing permission in browser');
        } else if (error.name === 'NotReadableError') {
            console.log('💡 Solution: Close other apps using screen sharing');
        } else if (error.message.includes('permission')) {
            console.log('💡 Solution: Check participant has canPublish permission');
        }
    }
}

// Auto-run the debug
debugLiveKitScreenShare();

console.log('🎯 Debug complete! Check the output above for issues.');
console.log('📝 You can also run debugLiveKitScreenShare() manually anytime.');
