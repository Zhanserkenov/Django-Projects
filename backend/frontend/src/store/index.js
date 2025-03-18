import { createStore } from 'vuex';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export default createStore({
  state: { token: localStorage.getItem('token') || '' },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
    },
    LOGOUT(state) {
      state.token = '';
      localStorage.removeItem('token');
    },
  },
  actions: {
    async login({ commit }, credentials) {
      const response = await axios.post(`${API_URL}login/`, credentials);
      commit('SET_TOKEN', response.data.access);
    },
    logout({ commit }) {
      commit('LOGOUT');
    },
  },
});
