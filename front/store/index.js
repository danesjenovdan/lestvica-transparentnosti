export const state = () => ({
  municipalitiesList: null,
  municipalitiesData: new Map(),
  municipalityData: null,
});

export const mutations = {
  setMunicipalitiesList(state, { data }) {
    state.municipalitiesList = data;
  },
  setMunicipalityData(state, { id, data }) {
    state.municipalitiesData.set(id, data);
    state.municipalityData = data;
  },
};

export const actions = {
  async ensureMunicipalitiesList({ state, commit }) {
    let data = state.municipalitiesList;
    if (!data) {
      data = await this.$axios.$get('/obcine-mini/');
      commit('setMunicipalitiesList', {
        data,
      });
    }
    return data;
  },
  async ensureMunicipalityData({ state, commit }, { id }) {
    let data = state.municipalitiesData.get(id);
    if (!data) {
      data = await this.$axios.$get(`/obcine/${id}/`);
    }
    commit('setMunicipalityData', { id, data });
    return data;
  },
};
