<template>
  <div class="commentWrapper">
    <div class="board">留言板</div>
    <div class="commentGroup">
      <div class="comment" v-for="item in content" :key="item.id">
        <div :class="handleColor(item.emotionScore)">{{Math.round(item.emotionScore * 100) / 100}}</div>
        <div class="push">{{item.CommentPush}}</div>
        <div class="author">{{item.Author}}</div>
        <div class="string">{{item.CommentString}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Comment',
  props: {
    content: Array,
  },
  methods: {
    handleColor: function(float) {
      if (float >= 0.8) {
        return 'score great';
      } else if (float < 0.8 && float >= 0.5) {
        return 'score mid';
      } else {
        return 'score bad';
      }
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.commentWrapper {
  position: relative;
  width: 50%;
}
.board {
  height: 45px;
  font-size: 32px;
}
.commentGroup {
  position: absolute;
  top: 70px;
  bottom: 0px;
  left: 30px;
  right: 30px;
  text-align: left;
  overflow: scroll;
}
.comment {
  display: flex;
  align-items: stretch; 
}
.score {
  width: 30px;
  flex: 0 0 30px;
}
.great {
  color: green;
}
.mid {
  color: yellow; 
}
.bad {
  color: red;
}
.push {
  flex: 0 0 30px;
}
.author {
  color: #ff6;
  margin-right: 10px;
}
.author::after {
  content: ":";
}
</style>
