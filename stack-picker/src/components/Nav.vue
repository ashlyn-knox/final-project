<template>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand to="/">Stack Picker</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <!-- Right aligned nav items -->
      <!-- TODO come up with a better page naming system -->
      <b-navbar-nav class="ml-auto">
        <b-navbar-nav>
          <b-nav-item to="/form">Form</b-nav-item>
          <b-nav-item to="/results">Results</b-nav-item>
          <b-nav-item to="/documentation">Docs</b-nav-item>
        </b-navbar-nav>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <!-- TODO make this dropdown a button that shows up after the form is submitted -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Download</b-dropdown-item>
          <b-dropdown-item href="#">Clear Search</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
