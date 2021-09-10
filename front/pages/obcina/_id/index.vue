<template>
  <div>
    <page-header />

    <municipality-header />

    <municipality-peer-lists />

    <municipality-recommendations />

    <municipality-email />

    <page-footer />
  </div>
</template>

<script>
import PageHeader from '~/components/PageHeader.vue';
import PageFooter from '~/components/PageFooter.vue';
import MunicipalityHeader from '~/components/sections/MunicipalityHeader.vue';
import MunicipalityPeerLists from '~/components/sections/MunicipalityPeerLists.vue';
import MunicipalityRecommendations from '~/components/sections/MunicipalityRecommendations.vue';
import MunicipalityEmail from '~/components/sections/MunicipalityEmail.vue';

export default {
  components: {
    PageHeader,
    PageFooter,
    MunicipalityHeader,
    MunicipalityPeerLists,
    MunicipalityRecommendations,
    MunicipalityEmail,
  },
  async asyncData({ params, store }) {
    await store.dispatch('ensureMunicipalitiesList');
    await store.dispatch('ensureMunicipalityData', { id: Number(params.id) });
  },
};
</script>
