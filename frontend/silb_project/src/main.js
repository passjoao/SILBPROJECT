import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './assets/css/tailwind.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import axios from 'axios'
import moment from 'moment'
  
Vue.config.productionTip = false

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('DD/MM/YYYY')
  }
});


Vue.config.productionTip = false


const urlBase = 'http://localhost:8000/api/v1/'
export default urlBase
Vue.use(axios)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')



