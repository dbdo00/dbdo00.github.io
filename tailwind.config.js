/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/post/*.html" ],
  theme: {
    extend: {},
  },
  plugins: [
	  require('@tailwindcss/typography'),
  ],
}

