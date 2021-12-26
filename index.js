function scrollToTop() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
};
function visibleInvisible() {
  let photos = document.getElementById("photos");
  if (photos.classList.contains("invisible")) {
    photos.classList.remove("invisible");
  } else {
    photos.classList.add("invisible");
  };
  let videos = document.getElementById("videos");
  if (videos.classList.contains("invisible")) {
    videos.classList.remove("invisible");
  } else {
    videos.classList.add("invisible");
  };
  scrollToTop();
};
