<template>
  <formComponent/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import formComponent from '@/components/formComponent.vue'

export default defineComponent({
  name: 'App',
  components: {
    formComponent
  }
})
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: whitesmoke;
  margin-top: 60px;
}
body{
  background-color: #252525;
}
</style>
