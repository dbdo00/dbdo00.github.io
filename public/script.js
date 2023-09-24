let darkMode = localStorage.getItem('darkMode'); 
const darkModeToggle = document.querySelector("#dark-mode");
const enableDarkMode = () => {
  document.body.classList.add('darkmode');
  localStorage.setItem('darkMode', 'enabled');
} 
if (darkMode === 'enabled') {
    enableDarkMode();
  }
const enableBrightMode = () => {
    document.body.classList.add('brightmode');

} 


const disableDarkMode = () => {
  document.body.classList.remove('darkmode');
  localStorage.setItem('darkMode', null);
//   enable bright mode
}

darkModeToggle.addEventListener('click', () => {
console.log("click");
console.log(darkMode);
darkMode = localStorage.getItem('darkMode'); 

  if (darkMode !== 'enabled') {
    document.body.classList.remove('brightmode')
    enableDarkMode();
  } else {  
    console.log("dark mode disabled");
    enableBrightMode();
    disableDarkMode();  }
});