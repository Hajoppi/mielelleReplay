/* ============
 * Routes File
 * ============
 *
 * The routes and redirects are defined in this file.
 */
import Graph from './pages/Graph/Index';
export default [
    // Home
    {
      path: '/',
      name: 'graph',
      component: Graph,
    },
    {
      path: '/*',
      redirect: '/',
    },
  ];
  