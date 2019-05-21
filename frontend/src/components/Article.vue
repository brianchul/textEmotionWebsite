<template>
  <div class="articleWrapper">
    <div class="title">文章</div>
    <div class="content" slot="content" v-html="content.Content">
      {{content.Content}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Article',
  props: {
    content: Object,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.articleWrapper {
  width: 50%;
}
.title {
  height: 45px;
  font-size: 32px;
}
.content {
  left: 30px;
  right: 30px;
  position: absolute;
  top: 70px;
  bottom: 0px;
  padding: 30px;
  text-align: left;
  overflow: scroll;
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
