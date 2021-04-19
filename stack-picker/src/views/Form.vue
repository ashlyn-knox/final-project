<template>
  <div>
    <Header />
      <div>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <!-- Ai and machine learning TODO: Change values -->
          <b-form-group label="Does your app use machine learning?" v-slot="{ ariaDescribedby }">
            <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="A">Yes</b-form-radio>
            <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="B">No</b-form-radio>
          </b-form-group>
          <!-- TODO Change the name from flavour here and on data -->
    <b-form-group label=" What programming languages do you prefer?" v-slot="{ ariaDescribedby }">
      <b-form-checkbox-group
        id="checkbox-group-2"
        v-model="selected"
        :aria-describedby="ariaDescribedby"
        name="flavour-2"
      >
        <b-form-checkbox v-for="(language, index) in languages" :key="index" value="language">{{ language }}</b-form-checkbox>
      </b-form-checkbox-group>

    </b-form-group>

          <!-- Real time functionality TODO: Change values -->
          <b-form-group label="Is real time interaction important?" v-slot="{ ariaDescribedby }">
            <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="A">Yes</b-form-radio>
            <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="B">No</b-form-radio>
          </b-form-group>

            <b-form-group id="input-group-3" label="How important is scalability important to your project?" label-for="input-3">
              <b-form-select
                  id="input-3"
                  v-model="form.levels"
                  :options="levels"
                  required
                  ></b-form-select>
            </b-form-group>

            <b-form-group id="input-group-4" label="What are your frontend design preferences?"  v-slot="{ ariaDescribedby }">
              <b-form-checkbox-group
                  v-model="form.checked"
                  id="checkboxes-4"
                  :aria-describedby="ariaDescribedby"
                  >
                  <b-form-checkbox value=""></b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>

            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
        <!--TODO refer to this to design my componennts-->
        <!-- <b-card class="mt-3" header="Form Data Result"> -->
         <!-- <pre class="m-0">{{ form }}</pre> -->
        <!-- </b-card> -->
      </div>
      <section>
        <h2>Quick Overview</h2>
        <p>We recommend that you use INSERTNAME for you stack</p>
        <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <!-- Image goes here -->
        <div>
          </div>
          <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
        <b-button>click Here</b-button>
      </section>
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
      form: {
        email: '',
        name: '',
        food: null,
        checked: []
      },
      levels: [{ text: 'Select One', value: null }, 'Not Important', 'Somewhat Important', 'Important', 'Very Important'],
      show: true,
      languages: ['Javascript', 'Python', 'PHP', 'JSX'],
      frameworks: ['React', 'Vue', 'Angular', 'Jquery']
    }
  },
  methods: {
    onSubmit (event) {
      event.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset (event) {
      event.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.name = ''
      this.form.food = null
      this.form.checked = []
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>
