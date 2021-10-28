<template>
  <content-section variant="white">
    <div class="narrow">
      <p class="center">
        Ker smo ugotovili, da so občine z večjim številom prebivalcev in višjim
        proračunom bolj odprte in transparentne, direktne primerjave med
        posameznimi občinami niso vedno najprimernejše. Zato si poglej
        primerjavo izbrane občine s tistimi, ki imajo podobno število
        prebivalcev in količino sredstev v proračunu.
      </p>
    </div>
    <div class="cols">
      <div class="col peer-list-col">
        <div class="peer-list">
          <div class="peer-list-header">
            <h3>PRIMERJAVA PO ŠTEVILU PREBIVALCEV</h3>
            <!-- <h4>Občine z TODO ali manj prebivalcev</h4> -->
            <p>
              Primerjaj število točk, ki jih je na lestvici odprtosti in
              transparentnosti dosegla izbrana občina, z doseženimi točkami
              slovenskih občin, ki imajo podobno število prebivalcev.
            </p>
          </div>
          <div class="peer-list-elements">
            <nuxt-link
              v-for="peer in populationPeers"
              :key="peer.id"
              :class="[
                'peer-list-element',
                { active: municipalityData.id === peer.id },
              ]"
              :to="`/obcina/${peer.id}/`"
            >
              <div class="name">{{ peer.rank }}. {{ peer.name }}</div>
              <div class="score">{{ formatScore(peer.total_score) }} točk</div>
            </nuxt-link>
          </div>
        </div>
      </div>
      <div class="col peer-list-col">
        <div class="peer-list">
          <div class="peer-list-header">
            <h3>PRIMERJAVA PO VIŠINI PRORAČUNA</h3>
            <!-- <h4>Občine z TODO € ali manjšim proračunom</h4> -->
            <p>
              Primerjaj število točk, ki jih je na lestvici odprtosti in
              transparentnosti dosegla izbrana občina, z doseženimi točkami
              slovenskih občin, ki imajo podoben proračun.
            </p>
          </div>
          <div class="peer-list-elements">
            <nuxt-link
              v-for="peer in budgetPeers"
              :key="peer.id"
              :class="[
                'peer-list-element',
                { active: municipalityData.id === peer.id },
              ]"
              :to="`/obcina/${peer.id}/`"
            >
              <div class="name">{{ peer.rank }}. {{ peer.name }}</div>
              <div class="score">{{ formatScore(peer.total_score) }} točk</div>
            </nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </content-section>
</template>

<script>
import { mapState } from 'vuex';
import { formatScore } from '~/utils/format';
import ContentSection from '~/components/sections/ContentSection.vue';

export default {
  components: {
    ContentSection,
  },
  computed: {
    ...mapState(['municipalityData']),
    populationPeers() {
      return (this.municipalityData?.bucket_peers?.population || [])
        .slice()
        .sort((a, b) => b.total_score - a.total_score);
    },
    budgetPeers() {
      return (this.municipalityData?.bucket_peers?.budget || [])
        .slice()
        .sort((a, b) => b.total_score - a.total_score);
    },
  },
  methods: {
    formatScore,
  },
};
</script>

<style lang="scss" scoped>
@import '~/assets/styles/breakpoints';

.cols {
  margin-top: 7rem;

  @include media-breakpoint-down(md) {
    margin-top: 3rem;
  }
}

.peer-list-col {
  &:not(:last-child) {
    @include media-breakpoint-down(md) {
      margin-bottom: 2rem;
    }
  }
}

.peer-list {
  margin: 0 auto;
  max-width: 480px;
  border: 1px solid #173d58;

  .peer-list-header {
    padding: 1.5rem 2rem;
    border-bottom: 1px solid #173d58;

    @include media-breakpoint-down(md) {
      padding: 1rem;
    }

    h3 {
      color: #173d58;
      font-size: 20px;
      font-weight: 700;
      font-style: italic;
      margin-top: 0;
      margin-bottom: 0.5rem;
    }

    h4 {
      color: #173d58;
      font-size: 16px;
      font-weight: 500;
      margin-bottom: 0.5rem;
    }

    p {
      font-size: 14px;
      font-weight: 300;
      line-height: 1.2;
      margin-bottom: 0;
    }
  }

  .peer-list-elements {
    padding: 0.75rem 1.25rem;
    max-height: 600px;
    overflow: hidden;
    overflow-y: scroll;

    @include media-breakpoint-down(md) {
      padding: 1rem;
    }

    .peer-list-element {
      padding: 1rem 0.75rem 0.75rem 0.75rem;
      font-size: 20px;
      display: flex;
      align-items: center;
      text-decoration: none;

      &:not(:last-child) {
        border-bottom: 1px solid #173d58;
      }

      &.active {
        background-color: #ffe4d8;
      }

      .name {
        flex: 1;
      }

      .score {
        flex: 0 0 auto;
        font-weight: 900;
      }
    }
  }
}
</style>
