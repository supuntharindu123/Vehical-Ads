const slide = document.querySelectorAll(".slide");
const dot = document.querySelectorAll(".dot");
const current = 0;

slideanimation(current);

function slideanimation(n) {
  for (let i = 0; i < slide.length; i++) {
    slide[i].style.display = "none";
  }
  for (let i = 0; i < dot.length; i++) {
    dot[i].style.backgroundColor = "white";
  }

  if (n >= slide.length) {
    n = 0;
  }
  slide[n].style.display = "block";
  dot[n].style.backgroundColor = "black";
  n++;
  setTimeout(() => slideanimation(n), 10000);
}
