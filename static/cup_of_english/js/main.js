document.addEventListener("DOMContentLoaded", function () {
  console.log("Main JS loaded");

  const forms = document.querySelectorAll("form");

  forms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      const required = form.querySelectorAll("[required]");
      let valid = true;

      required.forEach((field) => {
        if (!field.value.trim()) {
          valid = false;
          field.classList.add("is-invalid");
        } else {
          field.classList.remove("is-invalid");
        }
      });

      if (!valid) {
        e.preventDefault();
        alert("Please fill all required fields.");
      }
    });
  });
});
