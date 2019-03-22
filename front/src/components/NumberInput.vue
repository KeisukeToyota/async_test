<template>
  <input v-model="num" placeholder="input number...">
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class NumberInput extends Vue {
  _num: number = this.$store.state.n

  updateNumber (n: number) {
    this.$store.commit('updateNumber', n)
  }

  get num (): number {
    return this.$store.state.n
  }

  set num (n: number) {
    this.$store.commit('updateNumber', n)
  }
}
</script>
