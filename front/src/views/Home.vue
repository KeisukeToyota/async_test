<template>
  <div class="home">
    <NumberInput></NumberInput>
    <Button></Button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import Button from '@/components/Button.vue'
import NumberInput from '@/components/NumberInput.vue'

@Component({
  components: {
    Button,
    NumberInput
  }
})
export default class Home extends Vue {}
</script>
