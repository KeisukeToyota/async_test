<template>
  <button @click="changeText">{{ text }}</button>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:5042'

@Component
export default class Button extends Vue {
  public text: string = 'Button'

  public changeText () {
    axios.post(BASE_URL + '/hello', {
      'n': this.$store.state.n
    }).then((res) => {
      this.$store.state.n = res.data['n']
    })
  }
}
</script>
