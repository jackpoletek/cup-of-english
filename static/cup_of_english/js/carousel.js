document.addEventListener("DOMContentLoaded", function () {
  const items = document.querySelectorAll(".carousel-item");
  let index = 0;

  function showNext() {
    items[index].classList.remove("active");
    index = (index + 1) % items.length;
    items[index].classList.add("active");
  }

  if (items.length > 0) {
    setInterval(showNext, 4000);
  }
});
