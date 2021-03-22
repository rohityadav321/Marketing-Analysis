// $(window).load(function () {
//   // Animate loader off screen
//   $(".load").fadeOut("slow");
// });
document.onreadystatechange = function () {
  var state = document.readyState;
  if (state == "interactive") {
    document.querySelector(".screen").style.visibility = "hidden";
  } else if (state == "complete") {
    setTimeout(function () {
      document.getElementById("interactive");
      document.querySelector(".load").style.visibility = "hidden";
      document.querySelector(".screen").style.visibility = "visible";
    }, 500);
  }
};

function modeToggle() {
  var body = document.body;
  var button = document.getElementsByTagName("button");
  var navbar = document.getElementsByClassName("rcye");
  var active = document.querySelector(".active");
  var nav = document.getElementsByClassName("list");
  var foot = document.getElementsByClassName("footer");
  var icon = document.getElementsByClassName("icon");
  var val = document.getElementsByClassName("val");
  body.classList.toggle("darkmode");
  for (var i = 0; i < button.length; i++) {
    button[i].classList.toggle("darkbuttons");
  }
  val.classList.toggle("darkval");
  active.classList.toggle("darkactive");
  navbar.classList.toggle("darknavbar");
  foot.classList.toggle("darkfooter");
  nav.classList.toggle("darknavs");
  icon.classList.toggle("darkicon");
}
