<template>
  <content-section variant="dark-blue">
    <div class="narrow center">
      <h2>TE ZANIMA, KAKO SE JE ODREZALA <em>TVOJA OBČINA</em>?</h2>
      <div>
        <p>
          V iskalnik vpiši ime svoje občine in preveri, na katerem mestu
          lestvice odprtosti in transparentnosti se je znašla. Ugotoviš lahko,
          kako skrbi za prikazovanje javnih podatkov, do kakšne mere ti omogoča
          sodelovanje v postopkih odločanja in kaj smo ji priporočili, da stanje
          izboljša, ali pa jo primerjaš s podobnimi slovenskimi občinami.
        </p>
        <div class="search-wrapper">
          <search-field size="large" show-button />
        </div>
      </div>
    </div>
  </content-section>
</template>

<script>
import ContentSection from '~/components/sections/ContentSection.vue';
import SearchField from '~/components/SearchField.vue';

export default {
  components: {
    ContentSection,
    SearchField,
  },
};
</script>

<style lang="scss" scoped>
@import '~/assets/styles/breakpoints';

h2 {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.search-wrapper {
  margin-top: 4rem;

  @include media-breakpoint-down(md) {
    margin-top: 2rem;
  }

  .search-field {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
