<template>
  <div v-bind:class="video_id">
    <h1>{{ msg }}</h1>
    <p>
      <div>video_title : {{video_title}}</div>
      <div>video_id : {{video_id}}</div>
      <a v-bind:href="video_url" target="_blank" rel="noopener">영상 링크</a>
      <div>isdeleted : {{is_deleted}}</div>
    <p>
  </div>
</template>

<script>
export default {
  name: 'video',
  props: {
    video: {
      is_deleted: false,
      video_id: "uUvthLpSHrQ",
      video_title: "twinkle night feat.somunia - nyankobrq & yaca",
      video_url: "https://www.youtube.com/watch?v=uUvthLpSHrQ"
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
