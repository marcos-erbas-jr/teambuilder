var menuButton = document.getElementById("menu-button");
var menu = document.getElementById("conteudoNavbarSuportado");

menuButton.addEventListener("click", function() {
  if (menu.style.display === "block") {
    menu.style.display = "none";
  } else {
    menu.style.display = "block";
  }
});