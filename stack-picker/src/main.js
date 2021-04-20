import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
//import axios from 'axios'
// router imports
import App from './App.vue'
import router from './router'
import store from './store'

// bootstrap imports
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Bootstrap setup
Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
