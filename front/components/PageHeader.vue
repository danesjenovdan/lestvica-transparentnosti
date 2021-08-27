<template>
  <background-section variant="dark-blue">
    <header>
      <div class="container">
        <nav class="cols header">
          <div class="col main-col">
            <h1><nuxt-link to="/">Lestvica transparentnosti</nuxt-link></h1>
            <search-field />
          </div>
          <div class="col toc-col">
            <toc-button />
          </div>
        </nav>
      </div>
    </header>
  </background-section>
</template>

<script>
import BackgroundSection from '~/components/sections/BackgroundSection.vue';
import SearchField from '~/components/SearchField.vue';
import TocButton from '~/components/TocButton.vue';

export default {
  components: {
    BackgroundSection,
    SearchField,
    TocButton,
  },
};
</script>

<style lang="scss" scoped>
header {
  border-bottom: 1px solid rgba(#fff, 0.3);

  nav.header {
    padding: 1rem 0;

    .main-col {
      flex: 4;
      display: flex;
      justify-content: space-between;
      align-items: center;

      h1 {
        margin: 0;
        color: #fff;
        font-family: 'Lexend', sans-serif;
        font-size: 28px;
        font-weight: 600;

        a {
          text-decoration: none;

          &:hover,
          &:focus {
            $hover-bg-color: rgba(#fff, 0.15);

            outline: none;
            background-color: $hover-bg-color;
            box-shadow: -0.2em 0 0 $hover-bg-color, 0.2em 0 0 $hover-bg-color;
          }
        }
      }
    }

    .toc-col {
      flex: 3;
      display: flex;
      justify-content: flex-end;
      align-items: center;
    }
  }
}
</style>
