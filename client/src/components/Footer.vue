<template>
<!-- Footer -->
<footer class="footer">
  <section class="footer-main">
    <!-- Extra Resources -->
    <div>
      <h3>Resources</h3>
      <ul>
        <li v-for="(resource, index) in resources" :key="index">
          <a :href="resource.url">{{ resource.name }}</a>
        </li>
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
      <img width="80px" :src="author.photo" :alt="author.name">
      <p>{{ author.name }}</p>
      <p>Junior Developer</p>
      <!--Social Media Icons -->
      <ul class="social-media">
        <!-- Github -->
        <li><a :href="author.github">Github</a></li>
        <!-- LinkedIn -->
        <li><a :href="author.linkedin"></a>LinkedIn</li>
        <!-- Fedora -->
        <li><a :href="author.pagure">Fedora Pagure</a></li>
      </ul>
    </div>
  </section>
  <section class="footer-copyright">
    <p>&#169; Copyright 2021 | {{ author.name }}</p>
  </section>
</footer>
</template>

<script>
export default {
  data () {
    return {
      author: {
        name: 'Ashlyn Knox',
        photo: require('../assets/images/ashlyn.jpg'),
        github: 'https://github.com/ashlyn-knox',
        linkedin: 'https://linkedin.com/in/ashlyn-knox13',
        pagure: 'https://pagure.io/user/lilyx'
      },
      resources: [
        {
          name: 'Flask',
          url: 'https://flask.palletsprojects.com/en/1.1.x/',
          logo: require('../assets/logos/flask-logo.jpg'),
          alt: 'Flask Logo'
        },
        {
          name: 'Vue',
          url: 'https://vuejs.org/',
          logo: require('../assets/logos/vue.png'),
          alt: 'Vue Logo'
        },
        {
          name: 'Express',
          url: 'https://expressjs.com/',
          logo: require('../assets/logos/ExpressJS-logo.png'),
          alt: 'Express Logo'
        },
        {
          name: 'Python',
          url: 'https://python.org/',
          logo: require('../assets/logos/python-logo.png'),
          alt: 'Python Logo'
        },
        {
          name: 'Node',
          url: 'https://nodejs.org/',
          logo: require('../assets/logos/node.png'),
          alt: 'Node Logo'
        }
      ]
    }
  }
}
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
