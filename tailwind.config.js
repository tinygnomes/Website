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
        'brand-blue': '#00AEEF',
        'brand-yellow': '#FDB913',
        'brand-green': '#8DC63F',
        'brand-pink': '#F06EAA',
        'brand-orange': '#F58220',
      }
    },
  },
  plugins: [],
}