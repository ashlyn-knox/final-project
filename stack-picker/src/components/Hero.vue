<template>
  <header id="hero">
    <div class=hero-content>
    <h1>Today I want to talk about</h1>
    <h1>{{ pageTitle }}</h1>
    <p>{{ message }}</p>
    <button>Click Here</button>
    </div>
    </header>
</template>

<script>
export default {
  props: [
    'pageTitle',
    'message'
  ]
}
</script>

<style scoped>
#hero {
  background-image: url('../assets/images/pexels-luizclas.jpg');
  background-position: center;
  background-size: cover;

  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;

  min-height: 80vh;
}

.hero-content {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
</style>
