<template>
  <background-section id="lestvica-odprtosti-in-transparentnosti">
    <div class="map-with-tabs">
      <div class="search-fields">
        <search-field dark :on-select="onSelectFirst" />
        <search-field
          dark
          placeholder="Vpiši občino za primerjavo"
          :on-select="onSelectSecond"
        />
      </div>
      <div class="cols">
        <div class="col tabs-col">
          <div class="tabs">
            <div
              :class="['tab', { active: selectedTab === 0 }]"
              @click="onTabClick(0)"
            >
              <h3>Odprtost in transparentnost slovenskih občin</h3>
              <p>Skupni rezultati analize odprtosti in transparentnosti.</p>
            </div>
            <div
              :class="['tab', { active: selectedTab === 1 }]"
              @click="onTabClick(1)"
            >
              <h3>Transparentnost delovanja občinskega sveta</h3>
              <p>
                Zagotavljanje pravočasnih in ustreznih informacij ter javne
                narave procesov odločanja.
              </p>
            </div>
            <div
              :class="['tab', { active: selectedTab === 2 }]"
              @click="onTabClick(2)"
            >
              <h3>Preglednost spletnega mesta in dostop do informacij</h3>
              <p>
                Enostavno in uporabniku prijazno prikazovanje javnih občinskih
                podatkov.
              </p>
            </div>
            <div
              :class="['tab', { active: selectedTab === 3 }]"
              @click="onTabClick(3)"
            >
              <h3>Transparentnost in vključenost v sprejemanje proračuna</h3>
              <p>
                Prizadevanja za vključevanje občank in občanov v postopek
                sprejemanja proračuna in njegovo poenostavitev.
              </p>
            </div>
            <div
              :class="['tab', { active: selectedTab === 4 }]"
              @click="onTabClick(4)"
            >
              <h3>Dostopnost spletnega mesta</h3>
              <p>
                Zagotavljanje enostavnega dostopa do informacij in funkcij
                spletnega mesta čim večjemu številu oseb.
              </p>
            </div>
            <div
              :class="['tab', { active: selectedTab === 5 }]"
              @click="onTabClick(5)"
            >
              <h3>Vključenost v delovanje občine in obveščanje</h3>
              <p>
                Obseg in načini obveščanja ter vključevanja javnosti v delovanje
                občine.
              </p>
            </div>
          </div>
        </div>
        <div class="col map-col">
          <div :class="['peer-list', { closed: !peerListOpen }]">
            <div ref="peerList" class="peer-list-elements">
              <div
                v-for="(peer, i) in peers"
                :key="peer.id"
                class="peer-list-element"
              >
                <!-- <div class="name">{{ peer.rank }}. {{ peer.name }}</div> -->
                <div class="name">{{ i + 1 }}. {{ peer.name }}</div>
                <div class="score">{{ Math.round(peer.score) }} točk</div>
              </div>
            </div>
            <div class="peer-list-toggle" @click="peerListOpen = !peerListOpen">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 18">
                <path
                  d="M.02 8.8l.05-.18c.07-.17.1-.2.22-.33l8-8c.1-.09.2-.17.33-.22.42-.18.96 0 1.2.37a1.02 1.02 0 010 1.11c-.02.06-.07.1-.11.15L2.4 9l7.3 7.3.12.15.1.17c.17.42.02.96-.37 1.22-.33.21-.8.21-1.11 0l-.16-.13-8-8c-.04-.05-.1-.1-.12-.16a1 1 0 01-.15-.36 1.02 1.02 0 010-.39z"
                />
              </svg>
            </div>
          </div>
          <client-only>
            <pan-zoom @ready="onPanZoomReady">
              <municipalities-map :pan-zoom="panZoom" :get-bucket="getBucket" />
            </pan-zoom>
          </client-only>
        </div>
      </div>
      <div>
        <div class="legend">Temnejša barva predstavlja več doseženih točk.</div>
      </div>
    </div>
  </background-section>
</template>

<script>
import { mapState } from 'vuex';
import { GROUP_NAMES } from '~/utils/constants';
import BackgroundSection from '~/components/sections/BackgroundSection.vue';
import SearchField from '~/components/SearchField.vue';
import PanZoom from '~/components/PanZoom.vue';
import MunicipalitiesMap from '~/components/MunicipalitiesMap.vue';

export default {
  components: {
    BackgroundSection,
    SearchField,
    PanZoom,
    MunicipalitiesMap,
  },
  data() {
    return {
      panZoom: null,
      selectedTab: 0,
      peerListOpen: true,
    };
  },
  computed: {
    ...mapState(['municipalitiesList']),
    getScore() {
      if (this.selectedTab === 0) {
        return (m) => m.total_score;
      }
      const i = this.selectedTab - 1;
      const key = Object.keys(GROUP_NAMES)[i];
      return (m) => m.groups[key].score;
    },
    getBucket() {
      if (this.selectedTab === 0) {
        return (m) => m.total_bucket;
      }
      const i = this.selectedTab - 1;
      const key = Object.keys(GROUP_NAMES)[i];
      return (m) => m.groups[key].bucket;
    },
    peers() {
      return (this.municipalitiesList || [])
        .map((m) => ({
          name: m.name,
          rank: m.rank,
          score: this.getScore(m),
        }))
        .sort((a, b) => b.score - a.score);
    },
  },
  methods: {
    onPanZoomReady(panZoom) {
      this.panZoom = panZoom;
    },
    onSelectFirst(municipality) {},
    onSelectSecond(municipality) {},
    onTabClick(tabIndex) {
      this.selectedTab = tabIndex;
      this.$refs.peerList.scrollTop = 0;
    },
  },
};
</script>

<style lang="scss" scoped>
@import '~/assets/styles/breakpoints';

.map-with-tabs {
  .search-fields {
    display: flex;
    gap: 4rem;
    justify-content: center;
    margin-bottom: 3rem;
  }

  .cols {
    --cols-gap: 0;
    border-top: 1px solid #173d58;
    border-bottom: 1px solid #173d58;
    max-height: 700px;
  }

  .tabs-col {
    flex: 0 0 auto;

    .tabs {
      display: flex;
      flex-direction: column;
      width: 400px;
      height: 100%;

      .tab {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 1rem 2rem;
        background-color: #ffe4d8;
        border-right: 1px solid #173d58;
        cursor: pointer;

        &:not(:last-child) {
          border-bottom: 1px solid #173d58;
        }

        &.active {
          background-color: #fff;
          border-right: 0;
          cursor: default;

          h3 {
            color: #173d58;
          }

          p {
            color: #000;
          }
        }

        h3 {
          color: #4b4b4b;
          font-size: 20px;
          font-weight: 700;
          font-style: italic;
          text-transform: uppercase;
        }

        p {
          color: #4b4b4b;
          font-size: 14px;
          font-weight: 300;
          line-height: 1.2;
          margin-bottom: 0;
        }
      }
    }
  }

  .peer-list {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 1;
    margin: 0;
    max-width: 480px;
    border-right: 1px solid #173d58;

    &.closed {
      margin-left: -1px;

      .peer-list-elements {
        display: none;
      }

      .peer-list-toggle {
        svg {
          transform: scaleX(-1);
        }
      }
    }

    .peer-list-elements {
      background: #fff;
      padding: 0.75rem 1.25rem;
      height: 100%;
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

    .peer-list-toggle {
      position: absolute;
      top: 50%;
      left: 100%;
      transform: translateY(-50%);
      background-color: #fff;
      border: 1px solid #173d58;
      border-left: 0;
      display: flex;
      padding: 0.5rem;
      border-radius: 0 5px 5px 0;
      cursor: pointer;

      svg {
        width: 12px;
        height: 20px;
      }
    }
  }

  .map-col {
    background-color: #f1f1f1;
    position: relative;
  }

  .legend {
    text-align: right;
    font-size: 12px;
    font-weight: 500;
    padding: 1rem;
  }
}
</style>
