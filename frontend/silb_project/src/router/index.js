import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CadastroUsuario from '../modles/cadastro/CadastroUsuario.vue'
import Dashboard from "../modles/admin/Dashboard";
import Banco from "../views/Banco";
Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/cadastro',
    name: 'CadastroUsuario',
    component: CadastroUsuario
  },
  {
    path: '/banco',
    name: 'Banco',
    component: Banco
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
