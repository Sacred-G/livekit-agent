// Global type declarations for dependencies that will be installed
// This file prevents TypeScript errors before npm install

declare module 'react' {
  export * from 'react';
}

declare module 'react-native' {
  export * from 'react-native';
}

declare module '@livekit/react-native' {
  export * from '@livekit/react-native';
}

declare module 'livekit-client' {
  export * from 'livekit-client';
}

declare module 'zustand' {
  export * from 'zustand';
}

declare module 'zustand/middleware' {
  export * from 'zustand/middleware';
}

declare module '@react-navigation/native' {
  export * from '@react-navigation/native';
}

declare module '@react-navigation/stack' {
  export * from '@react-navigation/stack';
}

declare module '@react-navigation/bottom-tabs' {
  export * from '@react-navigation/bottom-tabs';
}

declare module 'react-native-vector-icons/MaterialIcons' {
  export * from 'react-native-vector-icons/MaterialIcons';
}

// Global types
declare const console: {
  log: (...args: any[]) => void;
  warn: (...args: any[]) => void;
  error: (...args: any[]) => void;
};

declare function setInterval(callback: () => void, ms: number): NodeJS.Timeout;
declare function clearInterval(id: NodeJS.Timeout): void;
