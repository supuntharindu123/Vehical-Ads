const view = document.querySelectorAll(".view");
const gal = document.querySelectorAll(".gal");

function showgallery(n) {
  for (let i = 0; i < view.length; i++) {
    view[i].style.display = "None";
  }

  for (let i = 0; i < gal.length; i++) {
    gal[i].classList.remove("active");
  }
  gal[n].classList.add("active");

  view[n].style.display = "flex";
}
showgallery(0);
