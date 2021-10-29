<template>
  <div id="app">
    <input v-model="my_list_id_raw" placeholder="플레이리스트 아이디를 넣어주세요." />
    <p> 선택한 플레이리스트 : {{ my_list_id_raw }}</p>
    <p> 플레이리스트 id : {{ my_list_id }}</p>

    <button v-on:click="getPlaylist">get data</button>
    {{ my_list_info }}
    <pre text-align: left>{{JSON.stringify(my_list_info, null, 2)}}</pre>
    {{ my_list_local_info }}
    <button v-on:click="refreshPlayList">refresh Playlist</button>
    {{refresh_result}}
    <button v-on:click="backupPlaylist">backup Playlist</button>
    {{backup_result}}
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
      my_list_id_raw: "PLhRJBsMSloa3-6Lq_qGmJgQFvuLCxAGSB",
      my_list_info: "My list Information is here",
      my_list_local_info: "my_list_local_info",
      refresh_result: "refresh_result",
      backup_result: "backup_result"
    };
  },
  computed: {
    my_list_id: function () {
      var list = this.my_list_id_raw.split("=")
      if(list.length == 0){
        return ""
      }
      return list[list.length - 1]
    }
  },
  methods: {
    getPlaylist: function () {
      var vm = this;
      axios
        .get(host + "get_playlist" + "?id=" + vm.my_list_id)
        .then(function (response) {
          vm.my_list_info = JSON.parse(response.data.live);
          vm.my_list_local_info = "뭐" + response.data.local;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    refreshPlayList: function () {
      var vm = this;

      axios
        .get(host + "refresh_playlist" + "?id=" + vm.my_list_id)
        .then(function (response) {
          vm.backupPlaylist = response.data
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    backupPlaylist: function () {
      var vm = this;

      axios
        .get(host + "backup_playlist" + "?id=" + vm.my_list_id)
        .then(function (response) {
          vm.backup_result = response.data
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
