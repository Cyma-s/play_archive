<template>
  <div class="div_out">
    <h1>{{ msg }}</h1>
      <p>video_title : {{video.video_title}}</p>
      <p>video_id : {{video.video_id}}</p>
      <a v-bind:href="video.video_url" target="_blank" rel="noopener">영상 링크</a>
      <p>isdeleted : {{video.is_deleted}}</p>
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
div {
  /* width : 1000px; */
  align-self: cn;
  background-color: #ebebeb;
  border: 1px solid rgb(27, 209, 11);
}
</style>
