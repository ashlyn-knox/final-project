<template>
  <header id="hero">
    <div class=hero-content>
    <h1>Today I want to talk about Foundations</h1>
    <button>Click Here</button>
    </div>
    </header>
</template>

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
