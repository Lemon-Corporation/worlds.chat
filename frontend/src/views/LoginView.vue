<template>
  <div class="login-page">
    <div class="cyber-lines"></div>
    <main class="login-container">
      <div class="login-header">
        <h1>WORLDS</h1>
        <p>Enter the Grid</p>
      </div>
      <form class="login-form" @submit.prevent="handleSubmit">
        <div class="input-group">
          <input
            type="text"
            id="username"
            v-model="username"
            required
            placeholder=" "
          />
          <label for="username">Username</label>
        </div>
        <div class="input-group">
          <input
            type="password"
            id="password"
            v-model="password"
            required
            placeholder=" "
          />
          <label for="password">Password</label>
        </div>
        <button type="submit" class="login-btn">Login</button>
      </form>
      <div class="links">
        <a href="#">Forgot Password?</a>
        <a href="#">Create Account</a>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    handleSubmit() {
      // Handle login logic here
      console.log("Login attempted with:", this.username, this.password);
      // You would typically make an API call here
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap");

:root {
  --bg-main: #1e1e2e;
  --bg-card: #2f2f3f;
  --text-primary: #ffffff;
  --text-secondary: #a0a0b0;
  --accent-purple: #6c5ce7;
  --accent-hover: #5a4bd1;
  --accent-cyan: #00fff9;
  --transition: all 0.3s ease;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.login-page {
  font-family: "Orbitron", sans-serif;
  background-color: var(--bg-main);
  color: var(--text-primary);
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  overflow: hidden;
  position: relative;
}

.login-container {
  background-color: var(--bg-card);
  border-radius: 10px;
  padding: 2rem;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 0 20px rgba(108, 92, 231, 0.3);
  position: relative;
  z-index: 1;
}

.login-header {
  text-align: center;
  margin-bottom: 2rem;
}

.login-header h1 {
  font-size: 3rem;
  color: var(--accent-purple);
  margin-bottom: 0.5rem;
  text-shadow: 0 0 10px rgba(108, 92, 231, 0.5);
  animation: glitch 5s infinite alternate;
}

.login-header p {
  color: var(--text-secondary);
  font-size: 1rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.input-group {
  position: relative;
}

.input-group label {
  position: absolute;
  left: 1rem;
  top: 0.8rem;
  color: var(--text-secondary);
  transition: var(--transition);
  pointer-events: none;
}

.input-group input {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  background-color: rgba(42, 42, 58, 0.8);
  border: 1px solid var(--accent-purple);
  border-radius: 5px;
  color: var(--text-primary);
  transition: var(--transition);
}

.input-group input:focus,
.input-group input:not(:placeholder-shown) {
  outline: none;
  border-color: var(--accent-cyan);
  box-shadow: 0 0 0 2px rgba(0, 255, 249, 0.2);
}

.input-group input:focus + label,
.input-group input:not(:placeholder-shown) + label {
  transform: translateY(-1.5rem) scale(0.8);
  color: var(--accent-cyan);
}

.login-btn {
  background-color: var(--accent-purple);
  color: var(--text-primary);
  border: none;
  padding: 0.75rem;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: var(--transition);
  position: relative;
  overflow: hidden;
  font-family: "Orbitron", sans-serif;
}

.login-btn:hover {
  background-color: var(--accent-hover);
}

.login-btn::before {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    to bottom right,
    rgba(255, 255, 255, 0.3) 0%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: rotate(45deg);
  transition: var(--transition);
}

.login-btn:hover::before {
  left: 100%;
}

.links {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.links a {
  color: var(--accent-purple);
  text-decoration: none;
  font-size: 0.9rem;
  transition: var(--transition);
}

.links a:hover {
  color: var(--accent-cyan);
  text-shadow: 0 0 5px rgba(0, 255, 249, 0.5);
}

.cyber-lines {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
  z-index: 0;
}

.cyber-lines::before,
.cyber-lines::after {
  content: "";
  position: absolute;
  width: 200vw;
  height: 200vh;
  top: -50%;
  left: -50%;
  background-image: linear-gradient(
      0deg,
      transparent 24%,
      rgba(108, 92, 231, 0.05) 25%,
      rgba(108, 92, 231, 0.05) 26%,
      transparent 27%,
      transparent 74%,
      rgba(108, 92, 231, 0.05) 75%,
      rgba(108, 92, 231, 0.05) 76%,
      transparent 77%,
      transparent
    ),
    linear-gradient(
      90deg,
      transparent 24%,
      rgba(108, 92, 231, 0.05) 25%,
      rgba(108, 92, 231, 0.05) 26%,
      transparent 27%,
      transparent 74%,
      rgba(108, 92, 231, 0.05) 75%,
      rgba(108, 92, 231, 0.05) 76%,
      transparent 77%,
      transparent
    );
  background-size: 50px 50px;
}

.cyber-lines::after {
  background-position: 25px 25px;
}

@keyframes glitch {
  0% {
    text-shadow: 0.05em 0 0 var(--accent-cyan),
      -0.05em -0.025em 0 var(--accent-purple);
  }
  14% {
    text-shadow: 0.05em 0 0 var(--accent-cyan),
      -0.05em -0.025em 0 var(--accent-purple);
  }
  15% {
    text-shadow: -0.05em -0.025em 0 var(--accent-cyan),
      0.025em 0.025em 0 var(--accent-purple);
  }
  49% {
    text-shadow: -0.05em -0.025em 0 var(--accent-cyan),
      0.025em 0.025em 0 var(--accent-purple);
  }
  50% {
    text-shadow: 0.025em 0.05em 0 var(--accent-cyan),
      0.05em 0 0 var(--accent-purple);
  }
  99% {
    text-shadow: 0.025em 0.05em 0 var(--accent-cyan),
      0.05em 0 0 var(--accent-purple);
  }
  100% {
    text-shadow: -0.025em 0 0 var(--accent-cyan),
      -0.025em -0.025em 0 var(--accent-purple);
  }
}

@media (max-width: 768px) {
  .login-container {
    padding: 1.5rem;
  }
  .login-header h1 {
    font-size: 2.5rem;
  }
}
</style>
