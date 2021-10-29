<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Welcome to Your Vue.js App" />
  <div id="app">
    <button v-on:click="fetchData">get data</button>
    {{ test_msg }}
  </div>
</template>

<script>

import HelloWorld from "./components/HelloWorld.vue"
import axios from "axios"

export default {
  el: '#app',
  name: "App",
  data () {
    return {
      test_msg: "CLICK BUTTON!" 
    }
  },
  components: {
    HelloWorld,
  },
  methods: {
    fetchData: function() {
      var vm = this
      axios.get('http://localhost:5000/melody')
        .then(function(response) {
          console.log(response);
          console.log(vm.test_msg)
          vm.test_msg = response.data
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
