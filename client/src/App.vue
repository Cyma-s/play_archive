<template>
  <div id="app">
    <div id="title">
      PLAY <br />
      ARCHIVE
    </div>

    <br /><br />
    <div id="desc">플레이리스트 아이디를 입력해주세요.</div>
    <br /><br /><br /><br />
    <input
      v-model="my_list_id_raw"
      placeholder="플레이리스트 아이디를 넣어주세요."
    />
    <!-- <p>선택한 플레이리스트 : {{ my_list_id_raw }}</p> -->
    <div>플레이리스트 id : {{ my_list_id }}</div>
    <br /><br /><br />
    <button v-on:click="getPlaylist">get data</button><br /><br />
    <!-- {{ my_list_info }} -->
    <!-- <pre text-align: left>{{JSON.stringify(my_list_info, null, 2)}}</pre> -->
    <!-- {{ my_list_local_info }} -->
    <button v-on:click="refreshPlayList">refresh Playlist</button><br /><br />
    <div text-align: left>
      <pre text-align: left>{{ JSON.stringify(refresh_result, null, 2) }}</pre>
    </div>
    <button v-on:click="backupPlaylist">backup Playlist</button><br /><br />
    <!-- {{backup_result}} -->

    <template v-for="(video, index) in my_video_list" v-bind:key="index">
      <VideoElem v-bind:video="video" />
    </template>
  </div>
</template>

<script>
import axios from "axios";
import VideoElem from "./components/VideoElem";

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
      backup_result: "backup_result",
      video_list: null,
    };
  },
  components: {
    VideoElem,
  },
  computed: {
    my_list_id: function () {
      var list = this.my_list_id_raw.split("=");
      if (list.length == 0) {
        return "";
      }
      return list[list.length - 1];
    },
    my_video_list: function () {
      if (this.video_list == null) {
        return [];
      }

      return this.video_list;
    },
  },
  methods: {
    getPlaylist: function () {
      var vm = this;
      axios
        .get(host + "get_playlist" + "?id=" + vm.my_list_id)
        .then(function (response) {
          console.log(response.data.live);
          vm.my_list_info = JSON.parse(response.data.live);
          vm.video_list = vm.my_list_info.videos;
          vm.my_list_local_info = "뭐" + JSON.parse(response.data.local);
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
          vm.refresh_result = response.data;
          vm.video_list = response.data.videos;
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
          vm.backup_result = response.data;
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
  text-align: center;
}
#desc {
  font-size: 35px;
}
#title {
  font-size: 100px;
  text-align: center;
  width: 100%;
  display: inline-block;
  position: relative;
}
input {
  width: 70%;
  border: 2px solid #aaa;
  border-radius: 4px;
  margin: 8px 0;
  outline: none;
  padding: 8px;
  box-sizing: border-box;
  transition: 0.3s;
}

input:focus {
  border-color: dodgerBlue;
  box-shadow: 0 0 8px 0 dodgerBlue;
}
button {
  background: #0069eb;
  color: #fff;
  border-radius: 6px;
  border: none;
  font-size: 16px;
  padding: 15px 30px;
  text-decoration: none;
}
</style>
