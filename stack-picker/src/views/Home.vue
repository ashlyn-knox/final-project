<template>
<div>
  <Hero />
  <article>
    <h2>Introduction to Project</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Leo integer malesuada nunc vel. Pellentesque adipiscing commodo elit at imperdiet. Vulputate dignissim suspendisse in est ante in nibh.</p>

    <!-- TODO load content dynamically with a loop -->
    <div class="logo-array">
      <img src="../assets/images/logos/vue.png" alt="vue logo">
      <img src="../assets/images/logos/python-logo.png" alt="vue logo">
      <img src="../assets/images/logos/ExpressJS-logo.png" alt="express logo">
      <img src="../assets/images/logos/flask-logo.jpg" alt="flask logo">
    </div>
  </article>
  <section>

  </section>
  <!-- So what statement -->
  <article>
    <h2>Why is this important?</h2>
    <p>Leo integer malesuada nunc vel. Pellentesque adipiscing commodo elit at imperdiet.</p>
    <section>
      <div>
        <h3>Python Server</h3>
        <p>Section requires editing. this should be a quick intro blurb</p>
        <ul>
          <li>Data Science</li>
          <li>AI and Machine Learning</li>
          <li>Synchronous</li>
          <li>Elegant Syntax</li>
        </ul>
      </div>
      <div>
        <h3>JavaScript Server</h3>
        <ul>
          <li>Asynchronous</li>
          <li>IOT</li>
          <li>Real Time Applications</li>
          <li>Scalable</li>
        </ul>
      </div>
      </section>
  </article>
  <section class="image-ribbon">

  </section>
  <article>
    <div>
      <img src="#" alt="">
      </div>
    <div>
    <h2>Another Options</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <button>Link to resources</button>
    </div>
  </article>
</div>
</template>

<script>
import Hero from '../components/Hero.vue'

export default {
  name: 'Home',
  components: {
    Hero
  }
}
</script>

<style scoped>

</style>
