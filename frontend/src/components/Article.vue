<template>
  <div class="articleWrapper">
    {{content}}
    <div class="content" slot="content" v-html="content.Content">
      {{content.Content.replace(/(\\r)*\\n/g, '<br />');}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Article',
  props: {
    content: Object,
  },
  created() {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.articleWrapper {
  width: 30vw;
}
.content {
  display: flex;
  flex-direction: column; 
}
.articleWrapper>>>.hl.f3 {
    color: #ff6;
}
.articleWrapper>>>.hl {
    color: #fff;
}
.articleWrapper>>>.f3 {
    color: #990;
}
</style>
