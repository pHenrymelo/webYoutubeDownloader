<template>
    <div>
        <h1 class="title">Video Downloader</h1>

        <div>
            <form class="formDownload" @submit.prevent="donwloadVid">
                <input
                    id = "link"
                    v-model="formData.link"
                    class="input"
                    type="text">
                <button type="submit" class="btn-submit">Baixar</button>
            </form>
        </div>

    </div>
</template>
<script lang="ts">
import api from '@/services/api.ts'
import { defineComponent, reactive } from 'vue'
export default defineComponent({
  name: 'formComponent',
  setup () {
    const formData = reactive({
      link: ''
    })

    const donwloadVid = async () => {
      console.log(formData.link)

      api.post('/download', formData.link)
    }
    return {
      formData,
      donwloadVid
    }
  }

})

</script>

<style>

.formDownload {
    box-sizing: border-box;
    background-color: #505050;
    border: darkred 2px solid;
    border-radius: 5px;
    padding: 20px;
    width: 450px;
    height: 200px;
    margin-inline: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;

}

.input {
    width: 400px;
    height: 30px;
    font-weight: bold;
    background-color: darkred;
    border: #252525 solid 2px;
    border-radius: 5px;
    padding: 5px;
    color: aliceblue;
}

.btn-submit {
    width: 200px;
    height: 35px;
    border-radius: 5px;
    background-color: aliceblue;
    color: #252525;
    font-weight: bold;
    border: #252525 solid 2px;
    cursor: pointer;
}
</style>
