<template>
  <content-section variant="yellow">
    <div class="narrow center">
      <h2><em>Pet priporočil</em> za tvojo občino</h2>
      <p>
        Glede na rezultate, ki jih je v raziskavi dosegla tvoja občina, smo
        podali pet predlogov, ki jih lahko upošteva za bolj odprto in
        transparentno delovanje. Spodbujamo te, da občinskim funkcionarjem
        posreduješ spodnje predpripravljeno elektronsko sporočilo in jih
        pozoveš, da priporočila tudi upoštevajo.
      </p>
      <p>
        Ker to niso edine spremembe, ki jih lahko tvoja občina sprejme za
        izboljšanje števila točk, predlagamo, da občinski funkcionarji podrobno
        preučijo rezultate celotne analize ter izvedejo ukrepe, ki bodo
        koristili občankam in občanom.
      </p>
    </div>
    <div class="side-image-wrapper">
      <img src="~/assets/images/ilustracija-obcina.svg" alt="" />
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
@import '~/assets/styles/breakpoints';

.content-section {
  h2 {
    color: #173d58;

    em {
      color: #5aa996;
      font-style: normal;
    }
  }

  p {
    font-size: 18px;

    @include media-breakpoint-down(md) {
      font-size: 16px;
    }
  }
}

.recommendations {
  margin-top: 6rem;

  @include media-breakpoint-down(md) {
    margin-top: 3rem;
  }

  .recommendation {
    margin-bottom: 5rem;
    flex-direction: row;

    @include media-breakpoint-down(md) {
      margin-bottom: 2rem;

      &:last-child {
        margin-bottom: 0;
      }
    }

    .number-col {
      flex: 0 0 100px;
      font-size: 72px;
      font-weight: 700;
      color: #ff7a40;
      text-align: right;
      margin-right: 2rem;

      @include media-breakpoint-down(md) {
        margin-right: 0;
        flex-basis: 50px;
        font-size: 38px;
      }
    }

    .text-col {
      h3,
      p {
        font-size: 26px;
        line-height: 1.2;

        @include media-breakpoint-down(md) {
          font-size: 16px;
        }
      }

      h3 {
        font-weight: 500;
        margin-top: 0;
        margin-bottom: 0.5em;
      }

      p {
        font-weight: 300;
      }
    }
  }
}

.side-image-wrapper.side-image-wrapper {
  img {
    transform: translate(50%, -35%);
  }
}
</style>
