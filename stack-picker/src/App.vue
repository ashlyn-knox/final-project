<template>
  <div id="app">
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand to="/">Stack Picker</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <!-- Right aligned nav items -->
      <!-- TODO come up with a better page naming system -->
      <b-navbar-nav class="ml-auto">
           <b-navbar-nav>
        <b-nav-item to="/form">Form</b-nav-item>
        <b-nav-item to="/results">Results</b-nav-item>
        <b-nav-item to="/documentation">Docs</b-nav-item>
      </b-navbar-nav>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <!-- TODO make this dropdown a button that shows up after the form is submitted -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Download</b-dropdown-item>
          <b-dropdown-item href="#">Clear Search</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <b-container>
    <router-view/>
    </b-container>
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
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Source Sans Pro', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
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
