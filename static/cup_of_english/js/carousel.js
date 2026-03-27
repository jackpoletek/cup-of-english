document.addEventListener("DOMContentLoaded", function () {
  const carouselElement = document.querySelector("#header-carousel");

  // Exit safely if the carousel element is not found
  if (!carouselElement) return;

  // Get Bootstrap carousel instance or create a new one if it doesn't exist
  let carousel = bootstrap.Carousel.getInstance(carouselElement);

  if (!carousel) {
    carousel = new bootstrap.Carousel(carouselElement, {
      interval: 4000,
      ride: "carousel",
      pause: false,
      wrap: true,
    });
  }

  // Pause on hover and resume on mouse leave
  carouselElement.addEventListener("mouseenter", function () {
    carousel.pause();
  });

  carouselElement.addEventListener("mouseleave", function () {
    carousel.cycle();
  });

  // Caption animation on slide change
  carouselElement.addEventListener("slide.bs.carousel", function (event) {
    const nextItem = event.relatedTarget;
    const caption = nextItem.querySelector(".carousel-caption");

    if (caption) {
      caption.classList.remove("animate-caption");

      // Force reflow to restart the animation
      void caption.offsetWidth;

      caption.classList.add("animate-caption");
    }
  });
});
