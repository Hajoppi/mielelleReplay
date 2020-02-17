/* ============
 * Main File
 * ============
 *
 * Will initialize the application.
 */

import Vue from 'vue';
import VueRouter from 'vue-router';
import routes from '/routes';

Vue.use(VueRouter);
const router = new VueRouter({
    routes,
});
Vue.router = router;

//Import styles
import './assets/main.scss';

/* ============
 * Main App
 * ============
 *
 * Last but not least, we import the main application.
 */

import App from './App';

/* eslint-disable no-new */
new Vue({
  /**
   * Bind the Vue instance to the HTML.
   */
  el: '#app',
  /**
   * The router.
   */
  router,
  /**
   * Will render the application.
   *
   * @param {Function} h Will create an element.
   */
  render: h => h(App),
});
