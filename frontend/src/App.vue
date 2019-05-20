<template>
  <div class="main">
    <Search/>
  </div>
</template>

<script>
import Search from './components/Search.vue'

export default {
  name: 'app',
  components: {
    Search
  }
}
</script>

<style>
body {
 margin: 0; 
}
.main{
  height: 100vh;
  width: 100vw;
  margin: 0;
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  text-align: center;
  color:#fff;
  background-image: url("./assets/background.png");
  background-size: 100% 100%;
}
</style>
