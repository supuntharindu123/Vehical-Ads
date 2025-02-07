let profile = document.querySelector(".userprofile");
let profilenav = document.querySelector(".profilenav");
profile.addEventListener("click", function () {
  if (profilenav.classList.contains("profilelog")) {
    profilenav.classList.remove("profilelog");
  } else {
    profilenav.classList.add("profilelog");
    profile.classList.add("active");
  }
});

const nav = document.querySelectorAll(".nav-item");
Array.from(nav).forEach((nav) => {
  nav.addEventListener("click", () => {
    nav.classList.add("active1");
  });
});
