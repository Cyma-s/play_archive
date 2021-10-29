<template>
  <div v-bind:class="video_id">
    <h1>{{ msg }}</h1>
      <div>video_title : {{video.video_title}}</div>
      <div>video_id : {{video.video_id}}</div>
      <a v-bind:href="video.video_url" target="_blank" rel="noopener">영상 링크</a>
      <div>isdeleted : {{video.is_deleted}}</div>
  </div>
</template>

<script>
export default {
  name: 'videoElem',
  props: {
    video: Object
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
