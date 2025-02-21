function showEventDetails(eventName) {
  alert(`You clicked on ${eventName}.`);
  // Redirect to a specific event description page (you can expand this later)
}
// Sign-Up Form Validation
document.getElementById("signupForm")?.addEventListener("submit", function (e) {
  e.preventDefault();

  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  if (password !== confirmPassword) {
      alert("Passwords do not match. Please try again.");
      return;
  }

  alert("Sign-Up Successful!");
  window.location.href = "login.html"; // Redirect to Log In page after successful sign-up
});

// Log-In Form Validation
document.getElementById("loginForm")?.addEventListener("submit", function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!email || !password) {
      alert("Please fill in all fields.");
      return;
  }

  window.location.href = "index.html"; // Redirect to Home page after successful log-in
});
