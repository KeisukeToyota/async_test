<template>
  <input v-model="n" placeholder="input number...">
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class NumberInput extends Vue {
  public n: number = 0
}
</script>
