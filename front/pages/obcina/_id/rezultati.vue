<template>
  <content-section>
    <div class="narrow">
      <h2>{{ municipalityData.name }}</h2>

      <div
        v-for="(question, i) in municipalityData.questions"
        :key="i"
        class="qa"
      >
        <div class="q-score">
          <p class="q">
            {{ question.question__text }}
          </p>
          <p class="score">{{ question.score }} / {{ question.max_score }}</p>
        </div>
        <p class="a">
          {{ question.text }}
        </p>
      </div>
    </div>
  </content-section>
</template>

<script>
import { mapState } from 'vuex';
import ContentSection from '~/components/sections/ContentSection.vue';

export default {
  components: {
    ContentSection,
  },
  async asyncData({ params, store }) {
    await store.dispatch('ensureMunicipalitiesList');
    await store.dispatch('ensureMunicipalityData', { id: Number(params.id) });
  },
  computed: {
    ...mapState(['municipalitiesList', 'municipalityData']),
  },
};
</script>

<style lang="scss" scoped>
.qa {
  margin-bottom: 3em;

  .q-score {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 1px solid #000;

    .q,
    .score {
      margin-bottom: 0;
    }

    .score {
      flex: 0 0 auto;
      font-weight: 900;
      margin-left: 1em;
    }
  }

  .a {
    margin-top: 0.5em;
    font-size: 16px;
    font-style: italic;
    font-weight: 300;
  }
}
</style>
