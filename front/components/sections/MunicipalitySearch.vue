<template>
  <content-section variant="dark-blue">
    <div class="narrow center">
      <h2>TE ZANIMA, KAKO SE JE ODREZALA <em>TVOJA OBČINA</em>?</h2>
      <div>
        <p>
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
          officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde
          omnis iste natus error sit voluptatem accusantium doloremque
          laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
          veritatis et quasi architecto beatae vitae dicta sunt explicabo.
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
h2 {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.search-wrapper {
  margin-top: 4rem;

  .search-field {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
