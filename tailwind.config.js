/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./website/**/*.html",
    "./website/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
        raleway: ['Raleway', 'sans-serif'],
        'fragment-mono': ['Fragment Mono', 'monospace'],
        rancho: ['Rancho', 'cursive'],
      },
      colors: {
        'brand-blue': '#3a9afe',
        'brand-green': 'rgb(136, 187, 0)',
        'brand-orange': 'rgb(255, 187, 0)',
      }
    },
  },
  plugins: [],
}