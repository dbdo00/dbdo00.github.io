let darkMode = localStorage.getItem('darkMode'); 
const darkModeToggle = document.querySelector("#dark-mode");
const enableDarkMode = () => {
  document.documentElement.dataset.darkMode =  'yes';
  localStorage.setItem('darkMode', 'enabled');
}
const disableDarkMode = () => {
  document.documentElement.dataset.darkMode =  'no'; 
  localStorage.setItem('darkMode', null);
}
if (darkMode === 'enabled') {
  enableDarkMode();
}
darkModeToggle.addEventListener('click', () => {
console.log("click");
  darkMode = localStorage.getItem('darkMode'); 
  if (darkMode !== 'enabled') {
    enableDarkMode();
  } else {  
    disableDarkMode(); 
  }
});