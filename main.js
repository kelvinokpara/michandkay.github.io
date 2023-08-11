// hamburger menu functionality

const hamButton = document.getElementById("hammenu");
const mobileNav = document.getElementById("mobilenav");

const webBody = document.getElementsByTagName("body");

console.log(hamButton, mobileNav);

hamButton.addEventListener("click", function () {
  console.log("done");
  mobileNav.classList.toggle("open");
});
