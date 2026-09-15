const glow = document.querySelector(".cursor-glow");

window.addEventListener("pointermove", (e) => {
  if (!glow) return;
  glow.animate(
    { left: `${e.clientX}px`, top: `${e.clientY}px` },
    { duration: 500, fill: "forwards" }
  );
});

const cards = document.querySelectorAll(".date-card");
cards.forEach((card, index) => {
  card.style.opacity = "0";
  card.style.transform = "translateY(40px)";
  card.animate(
    [
      { opacity: 0, transform: "translateY(40px)" },
      { opacity: 1, transform: "translateY(0)" }
    ],
    { duration: 800, delay: 150 + index * 120, fill: "forwards", easing: "cubic-bezier(.2,.8,.2,1)" }
  );
});

const form = document.getElementById("dateForm");
if (form) {
  form.addEventListener("submit", () => {
    document.body.style.transition = "opacity .45s";
    document.body.style.opacity = ".35";
  });
}
