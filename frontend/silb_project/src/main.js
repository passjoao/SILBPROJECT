import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import './assets/css/tailwind.css'
import axios from 'axios'
import vueaxios from 'vue-axios'
import moment from 'moment'
import firebase from "firebase";
  
Vue.config.productionTip = false

Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('DD/MM/YYYY')
  }
});


// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false


const urlBase = 'http://localhost:8000/api/v1/'
export default urlBase
Vue.use(axios, vueaxios)

var firebaseConfig = {
    apiKey: "AIzaSyC8d7qyPFi_2otiTaZTEAyjv08qJpUJDxw",
    authDomain: "silbproject.firebaseapp.com",
    databaseURL: "https://silbproject.firebaseio.com",
    projectId: "silbproject",
    storageBucket: "silbproject.appspot.com",
    messagingSenderId: "557455423181",
    appId: "1:557455423181:web:d4ad037b45d096693c5b84",
    measurementId: "G-Y6TSCYPSJN"
  };
firebase.initializeApp(firebaseConfig);
firebase.analytics();

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')



