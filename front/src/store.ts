import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    n: 0
  },
  mutations: {
    updateNumber (state, n) {
      state.n = n
    }
  },
  actions: {

  }
})
