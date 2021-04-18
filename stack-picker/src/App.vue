<template>
  <div id="app">
    <Nav />
    <b-container>
    <router-view />
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Footer from './components/Footer.vue'
import Nav from './components/Nav.vue'

export default {
  components: {
    Footer,
    Nav
  }
}
</script>

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
