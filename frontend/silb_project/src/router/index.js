import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CadastroUsuario from '../modules/cadastro/CadastroUsuario.vue'
import AtualizarUsuario from '../modules/cadastro/AtualizarCadastro.vue'
import Dashboard from "../modules/admin/Dashboard/Dashboard";
import Banco from "../views/Banco";
import Login from '../views/Login';
import AddSesmaria from '@/modules/admin/FormSesmarias.vue'
import AddSesmeiro from '@/modules/admin/FormSesmeiro.vue'
import AddConfirmacao from '@/modules/admin/FormConfirmation.vue'
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
    path: '*',
    redirect: '/'
  },
  {
    path: '/addsesmaria',
    name: 'AddSesmaria',
    component: AddSesmaria
  },
  {
    path: '/addsesmeiro',
    name: 'AddSesmeiro',
    component: AddSesmeiro
  },
  {
    path: '/addconfirmacao',
    name: 'AddConfirmacao',
    component: AddConfirmacao
  },
  {
    path: '/cadastro',
    name: 'CadastroUsuario',
    component: CadastroUsuario
  },
  {
    path: '/AtualizarUsuario',
    name: 'AtualizarUsuario',
    component: AtualizarUsuario
  },
  {
    path: '/admin',
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
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
