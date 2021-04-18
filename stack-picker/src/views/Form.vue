<template>

  <b-jumbotron>
    <template #header>Stack Analysis Form</template>
    <template #lead>
      This is a simple hero unit, a simple jumbotron-style component for calling extra attention to
      featured content or information.
    </template>

    <hr class="my-4">

    <p>
      It uses utility classes for typography and spacing to space content out within the larger
      container.
    </p>

    <b-button variant="primary" href="#">Do Something</b-button>
    <b-button variant="success" href="#">Do Something Else</b-button>
  </b-jumbotron>
    <div>
      <!--the .prevent will stop it from trying to submit to server-->
    <b-form @submit.prevent="handleSubmit" v-if="showPetForm">
      <!--Note how the formData is used in these forms and declared in the data object-->
      <b-form-group id="input-group-2" label="Pet's Name:" label-for="input-2">
          <b-form-input
              id="input-2"
              v-model="formData.name"
              placeholder="Enter name"
              required
              ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="Species:" label-for="input-3">
          <b-form-select
              id="input-3"
              v-model="formData.species"
              :options="['cats', 'dogs']"
              required
              ></b-form-select>
        </b-form-group>

      <b-form-group id="input-group-2" label="Pet's Age:" label-for="input-2">
          <b-form-input
              id="input-2"
              type="number"
              v-model="formData.age"
              placeholder="Enter Age"
              required
              ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    </div>
  </template>

<script>
export default {}
</script>
