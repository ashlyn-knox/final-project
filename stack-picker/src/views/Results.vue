<template>
  <div>
    <Header
    pageTitle="Search Results"
    message="Check out these links for information on getting your stack up and running."
     />
    <!-- Table goes here -->
    <div>
      <b-table striped hover :items="items"></b-table>
    </div>
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
      pageInfo: {
        name: 'Results'
      },
      items: []
    }
  }
}
</script>
