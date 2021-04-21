<template>
  <div>
    <Header
    pageTitle="Resources"
    message="Articles that were used to create the algorithm underlying this page."
    />
    <b-container>
      <b-table striped hover :items="sources">What</b-table>
    </b-container>
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
      sources: [
        {
          site: 'Back4App',
          topic: 'Backend frameworks',
          url: 'https://blog.back4app.com/backend-frameworks/'
        },
        {
          site: 'Uptech',
          topic: 'Web development stack choices',
          url: 'https://uptech.team/blog/web-development-stack'
        },
        {
          site: 'Yalantis',
          topic: 'Stack choice questions',
          url: 'https://yalantis.com/blog/tech-stack-for-web-app-development/'
        },
        {
          site: 'Modern Web',
          topic: 'Stack choice questions',
          url: 'https://modernweb.com/choosing-technology-stack/'
        },
        {
          site: 'Medium',
          topic: 'Python frameworks',
          url: 'https://medium.com/front-end-weekly/top-10-python-frameworks-in-2020-b0b6e61a592a'
        }
      ]
    }
  }
}
</script>
