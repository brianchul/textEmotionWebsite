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
  width: 70%;
}
.title {
  height: 45px;
  font-size: 32px;
}
.content {
  width: 70%;
  position: absolute;
  top: 45px;
  bottom: 0px;
  text-align: left;
  display: flex;
  justify-content: center;
  align-items: center;
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
