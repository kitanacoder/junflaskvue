import Vue from 'vue';
import VueRouter from 'vue-router';
import Ping from '../components/Ping.vue';
import Сars from '../components/Cars.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Cars',
    component: Cars,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
