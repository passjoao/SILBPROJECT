import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CadastroUsuario from '../modles/cadastro/CadastroUsuario.vue'
import Dashboard from "../modles/admin/Dashboard";
import Banco from "../views/Banco";
import Login from '../views/Login';
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
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/banco',
    name: 'Banco',
    component: Banco
  },
  {
    path: '/sesmarias',
    name: 'Sesmarias',
    component: () => import(/* webpackChunkName: "about" */ '../views/Sesmarias.vue')
  },
    {
    path: '/contact',
    name: 'Contact',
    component: () => import(/* webpackChunkName: "about" */ '../views/contact.vue')
  },
  {
    path: '/equipe',
    name: 'Equipe',
    component: () => import(/* webpackChunkName: "about" */ '../views/equipe.vue')
  },
  {
    path: '/legislacao',
    name: 'Legislação',
    component: () => import(/* webpackChunkName: "about" */ '../views/legislacao.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
