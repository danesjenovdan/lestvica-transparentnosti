<template>
  <content-section variant="yellow">
    <div class="narrow center">
      <h2><em>Pet priporočil</em> za tvojo občino</h2>
      <p>
        Glede na rezultate, ki jih je v raziskavi dosegla tvoja občina, smo
        podali pet predlogov, ki jih lahko upošteva za bolj odprto in
        transparentno delovanje. Spodbujamo te, da jim posreduješ spodnje
        predpripravljeno elektronsko sporočilo in jih pozoveš, da priporočila
        tudi upoštevajo.
      </p>
      <p>
        Ker to niso edine spremembe, ki jih lahko izvede za izboljšanje števila
        točk, predlagamo, da občinski funkcionarji podrobno preučijo rezultate
        celotne analize ter sprejmejo odločitve, ki bodo koristile občankam in
        občanom.
      </p>
    </div>
    <div class="narrow">
      <div class="recommendations">
        <div
          v-for="(recommendation, i) in recommendations"
          :key="recommendation.title"
          class="recommendation cols"
        >
          <div class="col number-col">{{ i + 1 }}.</div>
          <div class="col text-col">
            <h3>
              {{ recommendation.title }}
            </h3>
            <p>{{ recommendation.text }}</p>
          </div>
        </div>
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
  computed: {
    ...mapState(['municipalityData']),
    recommendations() {
      return (this.municipalityData?.recommendations || [])
        .slice()
        .sort((a, b) => b.importance - a.importance)
        .slice(0, 5);
    },
  },
};
</script>

<style lang="scss" scoped>
.content-section {
  h2 {
    color: #173d58;
    margin-bottom: 0.5em;

    em {
      color: #5aa996;
      font-style: normal;
    }
  }

  p {
    font-size: 18px;
  }
}

.recommendations {
  margin-top: 6rem;

  .recommendation {
    margin-bottom: 5rem;

    .number-col {
      flex: 0 0 100px;
      font-size: 72px;
      font-weight: 700;
      color: #ff7a40;
      text-align: right;
      margin-right: 2rem;
    }

    .text-col {
      h3,
      p {
        font-size: 26px;
        line-height: 1.2;
      }

      h3 {
        font-weight: 500;
        margin-bottom: 1rem;
      }

      p {
        font-weight: 300;
      }
    }
  }
}
</style>
