/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        security: {
          blue: '#0066cc',
          dark: '#1a1a1a',
          light: '#f8f9fa',
        },
      },
    },
  },
  plugins: [],
}
