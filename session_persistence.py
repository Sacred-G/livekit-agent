"""
Session persistence utilities for LiveKit agents
"""
import json
import os
from datetime import datetime
from typing import Dict, Any, Optional

class SessionPersistence:
    """Handle session persistence across agent restarts."""
    
    def __init__(self, storage_dir: str = "sessions"):
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
    
    def save_session(self, session_id: str, data: Dict[str, Any]) -> None:
        """Save session data to file."""
        session_file = os.path.join(self.storage_dir, f"{session_id}.json")
        session_data = {
            "session_id": session_id,
            "last_updated": datetime.now().isoformat(),
            "data": data
        }
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2, default=str)
    
    def load_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Load session data from file."""
        session_file = os.path.join(self.storage_dir, f"{session_id}.json")
        
        if not os.path.exists(session_file):
            return None
        
        try:
            with open(session_file, 'r') as f:
                session_data = json.load(f)
                return session_data.get("data", {})
        except (json.JSONDecodeError, KeyError):
            return None
    
    def list_sessions(self) -> list:
        """List all available session files."""
        if not os.path.exists(self.storage_dir):
            return []
        
        sessions = []
        for filename in os.listdir(self.storage_dir):
            if filename.endswith('.json'):
                session_id = filename[:-5]  # Remove .json extension
                session_file = os.path.join(self.storage_dir, filename)
                
                try:
                    with open(session_file, 'r') as f:
                        session_data = json.load(f)
                        sessions.append({
                            "session_id": session_id,
                            "last_updated": session_data.get("last_updated"),
                            "file_size": os.path.getsize(session_file)
                        })
                except (json.JSONDecodeError, KeyError):
                    continue
        
        return sorted(sessions, key=lambda x: x.get("last_updated", ""), reverse=True)
    
    def delete_session(self, session_id: str) -> bool:
        """Delete a session file."""
        session_file = os.path.join(self.storage_dir, f"{session_id}.json")
        
        if os.path.exists(session_file):
            os.remove(session_file)
            return True
        return False
