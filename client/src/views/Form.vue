<template>
  <div>
    <Header
      pageTitle="Stack Picker Form"
      message="Fill out this form to get an app stack recommendation."
    />
    <!-- Form -->
    <b-container>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">

        <!-- Preferred programming languages -->
        <b-form-group
          label="What programming languages do you prefer?"
          v-slot="{ ariaDescribedby }"
        >
          <b-form-checkbox-group
            id="language-pref-checkboxes"
            v-model="form.languagesPreference"
            :aria-describedby="ariaDescribedby"
            :options="form.languages"
            name="langauge-preference"
          >
            <!-- Checkboxes -->
            <b-form-checkbox
            v-for="option in options"
            :key="option.index"
            value="option.language"
            :aria-describedby="ariaDescribedby"
            name="language-preference"
            >
            {{ option.language}}
            </b-form-checkbox>
              <b-form-checkbox value="test" v-model="form.langaugesPreference">Test</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <!-- Language output Debug test -->
        <span> Selected: {{ languagesPreference }}</span>

        <!-- Backend Framework -->
        <b-form-group
          label="What qualities in a backend framework do you value?"
          v-slot="{ ariaDescribedby }"
        >
          <b-form-checkbox-group
            id="checkbox-group-2"
            v-model="selected"
            :aria-describedby="ariaDescribedby"
            name="backend-qualities"
          >
            <b-form-checkbox
              v-for="(backendQuality, index) in backendQuality"
              :key="index"
              value="language"
              >{{ backendQuality.quality }}</b-form-checkbox
            >
          </b-form-checkbox-group>
        </b-form-group>

        <!-- Real time functionality -->
        <b-form-group
          label="Is real-time interaction important?"
          v-slot="{ ariaDescribedby }"
        >
          <b-form-radio
            v-model="selected"
            :aria-describedby="ariaDescribedby"
            name="some-radios"
            value="A"
            >Yes</b-form-radio
          >
          <b-form-radio
            v-model="selected"
            :aria-describedby="ariaDescribedby"
            name="some-radios"
            value="B"
            >No</b-form-radio
          >
        </b-form-group>

        <!-- Scalability -->
        <b-form-group
          id="input-group-3"
          label="How important is scalability important to your project?"
          label-for="input-3"
        >
          <b-form-select
            id="input-3"
            v-model="form.levels"
            :options="levels"
            required
          ></b-form-select>
        </b-form-group>

        <!-- Machine Learning -->
        <b-form-group
          label="Does your app use machine learning?"
          v-slot="{ ariaDescribedby }"
        >
          <b-form-radio
            v-model="selected"
            :aria-describedby="ariaDescribedby"
            name="some-radios"
            value="1"
            >Yes</b-form-radio
          >
          <b-form-radio
            v-model="selected"
            :aria-describedby="ariaDescribedby"
            name="some-radios"
            value="1"
            >No</b-form-radio
          >
        </b-form-group>

        <!-- Frontend Framework -->
        <b-form-group
          id="input-group-4"
          label="What are your frontend design preferences?"
          v-slot="{ ariaDescribedby }"
        >
          <b-form-checkbox-group
            v-model="form.checked"
            id="checkboxes-4"
            :aria-describedby="ariaDescribedby"
            name="frontend-frameworks"
          >
            <b-form-checkbox
              v-for="(framework, index) in frameworks"
              :key="index"
              value="framework"
              >{{ framework.name }}</b-form-checkbox
            >
          </b-form-checkbox-group>
        </b-form-group>

        <b-button type="reset" variant="danger">Reset</b-button>
        <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>
    </b-container>

    <!-- Use an if statement to only show this content after the form has been submitted -->
    <b-container>
      <h2>Form Data Results</h2>
      <p>Perhaps consider using {{ recommendedStack }} for your project!</p>
      <b-card>
        <img
          width="100px"
          v-for="(logo, index) in logos"
          :key="index"
          :src="logo.url"
          :alt="logo.alt"
        />
      </b-card>
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
      recommendedStack: '',
      form: {
        languagesPreference: [],
        languages: [
          {
            language: 'Javascript'
          },
          {
            language: 'Python'
          },
          {
            language: 'Ruby'
          },
          {
            language: 'PHP'
          }
        ]
      },
      levels: [
        { text: 'Select One', value: null },
        'Not Important',
        'Somewhat Important',
        'Important',
        'Very Important'
      ],
      show: true,

      frameworks: [
        {
          name: 'React'
        },
        {
          name: 'Vue'
        },
        {
          name: 'Angular'
        },
        {
          name: 'Jquery'
        }
      ],
      backendQuality: [
        {
          quality: 'extensible'
        },
        {
          quality: 'unopinionated'
        },
        {
          quality: 'open-source'
        },
        {
          quality: 'Modular'
        },
        {
          quality: 'MVC architecture'
        },
        {
          quality: 'Asynchronous'
        },
        {
          quality: 'Clear Error Reporting'
        }
      ]
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
      this.form.languagesPreference = []
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>
