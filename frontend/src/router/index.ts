import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/impulse-newsletter',
      name: 'home',
      component: HomeView
    },
    {
      path: '/impulse-newsletter/unsubscribe',
      name: 'unsubscribe',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/UnsubscribeView.vue')
    },
    {
      path: '/impulse-newsletter/:pathMatch(.*)*',
      name: 'notfound',
      component: () => import('../views/NotFoundView.vue')
    }
  ]
})

export default router
