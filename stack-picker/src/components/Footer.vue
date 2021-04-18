<template>
<!-- Footer -->
<footer class="footer">
  <section class="footer-main">
    <!-- Extra Resources -->
    <div>
      <h3>Resources</h3>
      <ul>
        <li><a href="https://flask.palletsprojects.com/en/1.1.x/">Flask Docs</a></li>
        <li><a href="https://expressjs.com/">Express Docs</a></li>
        <li><a href="https://vuejs.org/">Vue Docs</a></li>
        <li><a href="https://python.org">Python Docs</a></li>
        <li><a href="https://nodejs.org/en/">NodeJs Docs</a></li>
      </ul>
    </div>
    <nav>
      <!-- Rename this title and page names -->
      <h3>Site Nav</h3>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/form">Form</a></li>
        <li><a href="/results">Results</a></li>
        <li><a href="/docs">Docs</a></li>
      </ul>
    </nav>
    <!-- My info -->
    <div>
      <img src="#" alt="Ashlyn Knox Headshot">
      <p>Ashlyn Knox</p>
      <p>Junior Developer</p>
      <!--Social Media Icons -->
      <ul class="social-media">
        <!-- Github -->
        <li><a href="#">Github</a></li>
        <!-- LinkedIn -->
        <li><a href="#">LinkedIn</a></li>
        <!-- Fedora -->
        <li><a href="#">Fedora</a></li>
      </ul>
    </div>
  </section>
  <section class="footer-copyright">
    <p>&#169; Copyright 2021 | Ashlyn Knox</p>
  </section>
</footer>
</template>

<script>
export default {}
</script>

<style scoped>
ul {
  list-style-type: none;
}

.footer {
  display: flex;
  flex-direction: column;
}
.footer-main {
  background-color: grey;
  color: ghostwhite;
  margin: 0 auto;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.social-media {
  display: flex;
}
.footer-copyright {
  width: 100%;
  background-color: black;
  color: grey;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items:center;
}
</style>
