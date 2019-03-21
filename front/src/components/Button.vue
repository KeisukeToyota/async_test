<template>
  <button @click="changeText">{{ text }}</button>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:5042/'

@Component
export default class Button extends Vue {
  public text: string = 'Button'

  public changeText () {
    axios.get(BASE_URL).then((res) => {
      this.text = res.data['text']
    })
  }
}
</script>
