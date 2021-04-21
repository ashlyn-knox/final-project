<template>
 <b-jumbotron>
    <template #header>{{ pageTitle }}</template>

    <template #lead>
      <p>{{ message }}</p>
    </template>

    </b-jumbotron>
</template>

<script>
export default {
  props: [
    'pageTitle',
    'message'
  ]
}
</script>
