<template>
  <div>
    <Header />
    <!-- Table goes here -->
    <div>
      <b-table striped hover :items="items"></b-table>
    </div>
    <!-- Remove or change this -->
    <p>Thank you</p>
  </div>
</template>

<script>

import Header from '../components/Header.vue'

export default {
  components: {
    Header
  },
  data () {
    return {
      items: []
    }
  }
}
</script>
