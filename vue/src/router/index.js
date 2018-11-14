import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/Home'
import Report from '@/pages/Report'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/report',
      name: 'Report',
      component: Report
    }
  ]
})
