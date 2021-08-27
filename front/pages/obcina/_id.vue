<template>
  <div>
    <page-header />

    <municipality-header />

    <content-section variant="white">
      <div class="narrow">
        <p class="center">
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
          officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde
          omnis iste natus error sit voluptatem accusantium doloremque
          laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
          veritatis et quasi architecto beatae vitae dicta sunt explicabo.
        </p>
      </div>
    </content-section>

    <municipality-peer-lists />

    <municipality-recommendations />

    <page-footer />
  </div>
</template>

<script>
import PageHeader from '~/components/PageHeader.vue';
import PageFooter from '~/components/PageFooter.vue';
import MunicipalityHeader from '~/components/sections/MunicipalityHeader.vue';
import ContentSection from '~/components/sections/ContentSection.vue';
import MunicipalityPeerLists from '~/components/sections/MunicipalityPeerLists.vue';
import MunicipalityRecommendations from '~/components/sections/MunicipalityRecommendations.vue';

export default {
  components: {
    PageHeader,
    PageFooter,
    MunicipalityHeader,
    ContentSection,
    MunicipalityPeerLists,
    MunicipalityRecommendations,
  },
  async asyncData({ params, store }) {
    await store.dispatch('ensureMunicipalitiesList');
    await store.dispatch('ensureMunicipalityData', { id: Number(params.id) });
  },
};
</script>
