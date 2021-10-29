<template>
  <div id="app">
    <input v-model="my_list_id" placeholder="여기를 수정해보세요" />
    <p>메시지: {{ my_list_id }}</p>
    <button v-on:click="getPlaylist">get data</button>
    {{ my_list_info }}
    <pre text-align: left>{{JSON.stringify(my_list_info, null, 2)}}</pre>
    {{ my_list_local_info }}
    <button v-on:click="backupPlaylist">backup Playlist</button>
  </div>
</template>

<script>
import axios from "axios";

const host = "http://localhost:5000/";

export default {
  el: "#app",
  name: "App",
  data() {
    return {
      my_list_id: "PLhRJBsMSloa3-6Lq_qGmJgQFvuLCxAGSB",
      my_list_info: "My list Information is here",
      my_list_local_info: "my_list_local_info",
    };
  },
  methods: {
    fetchData: function () {
      var vm = this;
      axios
        .get(host + "melody")
        .then(function (response) {
          console.log(response);
          console.log(vm.test_msg);
          vm.test_msg = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getPlaylist: function () {
      var vm = this;
      axios
        .get(host + "get_playlist" + "?id=" + vm.my_list_id)
        .then(function (response) {
          console.log(response);
          console.log(vm.test_msg);
          vm.my_list_info = JSON.parse(response.data.live);
          vm.my_list_local_info = "뭐" + response.data.local;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
