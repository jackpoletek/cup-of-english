document.addEventListener("DOMContentLoaded", function () {
  const items = document.querySelectorAll(".carousel-item");
  let index = 0;

  function showNext() {
    items.forEach((item) => item.classList.remove("active"));
    index = (index + 1) % items.length;
    items[index].classList.add("active");
  }

  if (items.length > 0) {
    items[0].classList.add("active");
    setInterval(showNext, 5000);
  }
});
