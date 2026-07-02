document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const input = document.querySelector("input[type='text']");
    const button = document.querySelector("button");

    // Form validation
    form.addEventListener("submit", function(event) {
        if (input.value.trim() === "") {
            alert("Please enter a valid GitHub username!");
            event.preventDefault(); // Stop form submission
        }
    });

    // Button hover zoom effect
    button.addEventListener("mouseover", () => {
        button.style.transform = "scale(1.05)";
        button.style.transition = "transform 0.2s ease"; // smooth animation
    });

    button.addEventListener("mouseout", () => {
        button.style.transform = "scale(1)";
    });
});