<template>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand to="/">Stack App</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-navbar-nav>
          <b-nav-item to="/form">Form</b-nav-item>
          <b-nav-item to="/results">Results</b-nav-item>
          <b-nav-item to="/resources">Resources</b-nav-item>
        </b-navbar-nav>

        <b-nav-item-dropdown right>

          <template #button-content>
            Download
          </template>
          <b-dropdown-item href="#">Download</b-dropdown-item>
          <b-dropdown-item href="#">Clear Search</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
