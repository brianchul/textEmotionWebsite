<template>
  <div id="search" class="searchWrapper">
    <img src="../assets/logo.png" class="logo">
    <div class="slogan">URL在手，喜怒哀樂應有盡有</div>
    <div class="searchbar">   
      <input placeholder="請輸入ptt網址" size="100" v-model="url"/>
      <div class="send" @click="send">送出</div>
    </div>  
  </div>
</template>

<script>
export default {
  name: 'search',
  data: {
    url: '',
    contents: [],
  },
  methods: {
    send() {
      axios.post('',{
        content: this.url
      }).then((res) => {
        console.log(res)
      })
    }
  }
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
</style>
