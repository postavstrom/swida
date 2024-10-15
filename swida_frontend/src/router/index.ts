import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import OrderView from '../views/OrderView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/orders/create',
      name: 'order',
      component: OrderView
    },
    {
      path: '/orders',
      name: 'orders',
      component: () => import('../views/OrdersListView.vue')
    },
    {
      path: '/orders/:id/edit',
      name: 'order-edit',
      component: OrderView
    }
  ]
})

export default router
