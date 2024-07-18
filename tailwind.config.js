/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        ibm: ['IBM Plex Sans'],
        inter: ['Inter'],
      },
      colors: {
        'backg': '#ECFDF5',
        'primary': '#65A30D',
        'secondary': '#064E3B',
        'third': '#059669',
        'angka': '#F472B6',
        'hover': '#578D0B',
      },
    },
  },
  plugins: [],
}

