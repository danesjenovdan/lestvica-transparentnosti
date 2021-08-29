<template>
  <div>
    <page-header />

    <landing-intro />

    <content-section variant="white">
      <div class="narrow">
        <p class="center">
          Preveri, kako se je na lestvici odprtosti in transparentnosti odrezala
          posamezna občina, in jo primerjaj z ostalimi slovenskimi občinami.
          Ogledaš si lahko skupne rezultate ali pa brskaš po posameznih
          vsebinskih sklopih.
        </p>
      </div>
    </content-section>

    <map-with-tabs />

    <landing-0 />

    <landing-1 />

    <landing-2 />

    <landing-3 />

    <landing-4 />

    <landing-5 />

    <landing-6 />

    <municipality-search />

    <page-footer />
  </div>
</template>

<script>
import PageHeader from '~/components/PageHeader.vue';
import LandingIntro from '~/components/sections/LandingIntro.vue';
import ContentSection from '~/components/sections/ContentSection.vue';
import MapWithTabs from '~/components/sections/MapWithTabs.vue';
import Landing0 from '~/components/sections/Landing0.vue';
import Landing1 from '~/components/sections/Landing1.vue';
import Landing2 from '~/components/sections/Landing2.vue';
import Landing3 from '~/components/sections/Landing3.vue';
import Landing4 from '~/components/sections/Landing4.vue';
import Landing5 from '~/components/sections/Landing5.vue';
import Landing6 from '~/components/sections/Landing6.vue';
import MunicipalitySearch from '~/components/sections/MunicipalitySearch.vue';
import PageFooter from '~/components/PageFooter.vue';

export default {
  components: {
    PageHeader,
    LandingIntro,
    ContentSection,
    MapWithTabs,
    Landing0,
    Landing1,
    Landing2,
    Landing3,
    Landing4,
    Landing5,
    Landing6,
    MunicipalitySearch,
    PageFooter,
  },
  async asyncData({ store }) {
    await store.dispatch('ensureMunicipalitiesList');
  },
};
</script>
