<template>
  <div v-if="contents.length === 0" class="searchWrapper">
    <img src="../assets/logo.png" class="logo" />
    <div class="slogan">URL在手，喜怒哀樂應有盡有</div>
    <div class="searchbar">
      <input placeholder="請輸入ptt網址" size="100" v-model="url"/>
      <div class="send" @click="send">送出</div>
    </div>
  </div>
  <div v-else class="contentWrapper">
    <div class="title">
      <div class="titleRow">
        <div class="titleTag">作者</div>
        <div class="titleItem">{{contents.article.ArticleAuthor}}</div>
      </div>
      <div class="titleRow">
        <div class="titleTag">標題</div>
        <div class="titleItem">{{contents.article.ArticleTitle}}</div>
      </div>
      <div class="titleRow">
        <div class="titleTag">來源</div>
        <div class="titleItem">{{contents.article.ArticleUrl}}</div>
      </div>
      <div class="titleRow">
        <div class="titleTag">時間</div>
        <div class="titleItem">{{contents.article.updated_time}}</div>
      </div>
      <div class="close" @click="contents = []">關閉</div>
    </div>
    <div class="contentGroup">
      <Article :content="contents.article" />
      <Comment :content="contents.comment" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Article from './Article.vue';
import Comment from './Comment.vue';

export default {
  name: 'search',
  data() {
    return {
      url: '',
      contents: []
    };
  },
  components: {
    Article,
    Comment,
  },
  methods: {
    send() {
      axios.post('https://emoptt.ddns.net:5000/api/article/query',{
        article_url: this.url
      }).then((res) => {
        this.contents = res.data.data;
        console.log(this.contents)
      })
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input {
  margin-left: 60px;
  padding-left: 10px;
}
.searchWrapper {
  background-color: black;
}
.logo {
  height: 150px;
  width: 600px;
  border-style: dotted;
  border-color: white; 
  margin-top: 20px;
  margin-bottom: 20px
}
.slogan {
  font-size: 20px;
  margin-bottom: 20px;
}
.searchbar {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin-bottom: 20px;
}
.send {
  width: 50px;
  height: 25px;
  margin-left: 10px;
  border-radius: 5px;
  box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.17);
  background-color: #007FAD;
}

.contentWrapper {
  width: 100vw;
  height: 100vh;
  background-color: black;
  display: flex;
  align-items: stretch;
}
.title {
  position: absolute;
  top: 0;
  width: 100vw;
  border-top: 1px solid #999;
  border-bottom: 1px solid #999;
  z-index: 10;
}
.titleRow {
  display: flex;
  height: 30px;
  line-height: 30px;
}
.titleTag {
  padding: 0 10px;
  background-color: #999;
  color: #000;
  text-align: center;
}
.titleItem {
  flex: 1 1 auto;
  padding-left: 20px;
  background-color: #000;
  color: #fff;
  text-align: left;
}
.contentGroup {
  position: absolute;
  width: calc(100% - 20px);
  top: 120px;
  bottom: 0;
  display: flex;
  background-color: #000;
  padding: 10px;
}
.close {
  position: absolute;
  top: 15px;
  right: 15px;
}
</style>
