<template>
  <div id="app">
    <router-view :key="componentKey" v-on:reload="reload"></router-view>
  </div>
</template>
<script>
/* ============
* Entry Point
* ============
*
* The entry point of the application
*/

export default {
/**
 * The name of the application.
 */
name: 'main-index',
data(){
  return {
    componentKey: 0,
  };
},
methods: {
  reload() {
    this.componentKey += 1;
  }
}
};
</script>
