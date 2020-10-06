import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './assets/css/tailwind.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import moment from 'moment'
import firebase from "firebase";

Vue.config.productionTip = false

const firebaseConfig = {
  apiKey: "AIzaSyC8d7qyPFi_2otiTaZTEAyjv08qJpUJDxw",
  authDomain: "silbproject.firebaseapp.com",
  databaseURL: "https://silbproject.firebaseio.com",
  projectId: "silbproject",
  storageBucket: "silbproject.appspot.com",
  messagingSenderId: "557455423181",
  appId: "1:557455423181:web:6616f5a47e1c3d2c3c5b84",
  measurementId: "G-TNTPH8ZS26"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

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
Vue.use(VueAxios, axios)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')



