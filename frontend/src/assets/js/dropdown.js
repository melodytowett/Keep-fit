const dropdown = function () {
  const authDropdowns = document.querySelectorAll(".auth-dropdown");

  authDropdowns.forEach((dropdown) => {
    dropdown.addEventListener("click", (e) => {
      // Remove the active class from all dropdowns
      document
        .querySelectorAll(".auth-dropdown__container")
        .forEach((container) => {
          container.classList.remove("hidden");
        });

      e.preventDefault();
      const postUpdate = e.target.parentElement;
      const postUpdateContainer = postUpdate.querySelector(
        ".auth-dropdown__container"
      );
      postUpdateContainer.classList.add("hidden");
    });
  });

  document.querySelectorAll(".auth-dropdown__item").forEach((item) => {
    item.addEventListener("click", (e) => {
      e.preventDefault();
      document
        .querySelectorAll(".auth-dropdown__container")
        .forEach((container) => {
          container.classList.remove("hidden");
        });
    });
  });
};
