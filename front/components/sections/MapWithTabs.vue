<template>
  <background-section id="lestvica-odprtosti-in-transparentnosti">
    <div class="map-with-tabs">
      <div class="search-fields">
        <search-field
          dark
          :on-select="onSelectFirst"
          :on-clear="onClearFirst"
        />
        <search-field
          dark
          placeholder="Vpiši občino za primerjavo"
          :on-select="onSelectSecond"
          :on-clear="onClearSecond"
        />
      </div>
      <div class="cols tab-map-cols">
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
          <client-only>
            <pan-zoom @ready="onPanZoomReady">
              <municipalities-map
                :pan-zoom="panZoom"
                :get-bucket="getBucket"
                :highlight-municipalities="selectedMunicipalities"
              />
            </pan-zoom>
          </client-only>
          <div :class="['peer-list', { closed: !peerListOpen }]">
            <div ref="peerList" class="peer-list-elements">
              <div
                v-for="peer in peers"
                :key="peer.id"
                class="peer-list-element"
              >
                <div class="name">{{ peer.rank }}. {{ peer.name }}</div>
                <div class="score">{{ peer.formattedScore }} točk</div>
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
          <div class="overlay">
            <div v-if="selectedMunicipality1" class="selected-info-overlay">
              <div class="info-wrapper">
                <div class="cols">
                  <div class="col title-col">
                    <h1>{{ selectedMunicipality1.name }}</h1>
                    <div class="rank">
                      {{ selectedMunicipality1.rank }}. mesto
                    </div>
                  </div>
                  <div class="col icon-col">
                    <div class="gauge-wrapper">
                      <div class="gauge-icon">
                        <gauge :value="selectedMunicipality1.total_bucket" />
                      </div>
                      <div class="gauge-label">
                        <div>Najslabša ocena</div>
                        <div>Najboljša ocena</div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="more-button">
                  <nuxt-link :to="`/obcina/${selectedMunicipality1.id}/`">
                    Poglej podrobno analizo
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 65 48">
                      <path
                        fill="#ff7a40"
                        d="M60 24L40 41.58V32a2 2 0 00-2-2H10a6 6 0 010-12h28a2 2 0 002-2V6.42z"
                      />
                      <path
                        d="M39.32 47.5A2 2 0 0136 46V34H10a10 10 0 010-20h26V2A2 2 0 0139.32.5l25 22a2 2 0 010 3zm.68-5.92L60 24 40 6.42V16a2 2 0 01-2 2H10a6 6 0 000 12h28a2 2 0 012 2z"
                      />
                    </svg>
                  </nuxt-link>
                </div>
                <div class="scores">
                  <div
                    v-for="(group, key) in selectedMunicipality1.groups"
                    :key="key"
                    class="score-row"
                  >
                    <div class="score-label">
                      {{ groupName(key) }}
                    </div>
                    <div class="score-value">{{ group.score }} / 20</div>
                  </div>
                </div>
              </div>
            </div>
            <div v-if="selectedMunicipality2" class="selected-info-overlay">
              <div class="info-wrapper">
                <div class="cols">
                  <div class="col title-col">
                    <h1>{{ selectedMunicipality2.name }}</h1>
                    <div class="rank">
                      {{ selectedMunicipality2.rank }}. mesto
                    </div>
                  </div>
                  <div class="col icon-col">
                    <div class="gauge-wrapper">
                      <div class="gauge-icon">
                        <gauge :value="selectedMunicipality2.total_bucket" />
                      </div>
                      <div class="gauge-label">
                        <div>Najslabša ocena</div>
                        <div>Najboljša ocena</div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="more-button">
                  <nuxt-link :to="`/obcina/${selectedMunicipality2.id}/`">
                    Poglej podrobno analizo
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 65 48">
                      <path
                        fill="#ff7a40"
                        d="M60 24L40 41.58V32a2 2 0 00-2-2H10a6 6 0 010-12h28a2 2 0 002-2V6.42z"
                      />
                      <path
                        d="M39.32 47.5A2 2 0 0136 46V34H10a10 10 0 010-20h26V2A2 2 0 0139.32.5l25 22a2 2 0 010 3zm.68-5.92L60 24 40 6.42V16a2 2 0 01-2 2H10a6 6 0 000 12h28a2 2 0 012 2z"
                      />
                    </svg>
                  </nuxt-link>
                </div>
                <div class="scores">
                  <div
                    v-for="(group, key) in selectedMunicipality2.groups"
                    :key="key"
                    class="score-row"
                  >
                    <div class="score-label">
                      {{ groupName(key) }}
                    </div>
                    <div class="score-value">{{ group.score }} / 20</div>
                  </div>
                </div>
                <!-- <div class="scores-caption">
                  Za podrobne rezultate klikni
                  <nuxt-link
                    :to="`/obcina/${selectedMunicipality2.id}/rezultati`"
                    >tukaj</nuxt-link
                  >.
                </div> -->
              </div>
            </div>
          </div>
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
import { formatScore } from '~/utils/format';
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
      selectedMunicipality1: null,
      selectedMunicipality2: null,
    };
  },
  computed: {
    ...mapState(['municipalitiesList']),
    selectedMunicipalities() {
      const array = [];
      if (this.selectedMunicipality1) {
        array.push(this.selectedMunicipality1);
      }
      if (this.selectedMunicipality2) {
        array.push(this.selectedMunicipality2);
      }
      return array;
    },
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
      let lastFormattedScore;
      let lastRank;
      return (this.municipalitiesList || [])
        .map((m) => {
          const score = this.getScore(m);
          const formattedScore = formatScore(score);
          return {
            name: m.name,
            score,
            formattedScore,
          };
        })
        .sort((a, b) => b.score - a.score)
        .map((m, i) => {
          let rank = i + 1;
          if (m.formattedScore === lastFormattedScore) {
            rank = lastRank;
          } else {
            lastFormattedScore = m.formattedScore;
            lastRank = rank;
          }
          return {
            ...m,
            rank,
          };
        });
    },
  },
  methods: {
    onPanZoomReady(panZoom) {
      this.panZoom = panZoom;
    },
    groupName(key) {
      return GROUP_NAMES[key]?.name || key;
    },
    onSelectFirst(municipality) {
      this.selectedMunicipality1 = municipality;
    },
    onSelectSecond(municipality) {
      this.selectedMunicipality2 = municipality;
    },
    onClearFirst() {
      this.selectedMunicipality1 = null;
    },
    onClearSecond() {
      this.selectedMunicipality2 = null;
    },
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

    .search-field:not(:first-child) {
      @include media-breakpoint-down(md) {
        display: none;
      }
    }
  }

  .cols.tab-map-cols {
    --cols-gap: 0;
    border-top: 1px solid #173d58;
    border-bottom: 1px solid #173d58;
    max-height: 700px;
  }

  .tabs-col {
    flex: 0 0 auto;

    @include media-breakpoint-down(md) {
      display: none;
    }

    .tabs {
      display: flex;
      flex-direction: column;
      width: 400px;
      height: 100%;
      overflow: hidden;
      overflow-y: auto;

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

    @include media-breakpoint-down(md) {
      position: static;
      height: 150px;
      border-right: 0;
      border-top: 1px solid #173d58;
    }

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
        padding: 0.5rem 1rem;
      }

      .peer-list-element {
        padding: 1rem 0.75rem 0.75rem 0.75rem;
        font-size: 20px;
        display: flex;
        align-items: center;

        @include media-breakpoint-down(md) {
          font-size: 16px;
          padding: 0.5rem 0 0.25rem;
        }

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

      @include media-breakpoint-down(md) {
        display: none;
      }

      svg {
        width: 12px;
        height: 20px;
      }
    }
  }

  .map-col {
    background-color: #f1f1f1;
    position: relative;

    .pan-zoom-container {
      @include media-breakpoint-down(md) {
        height: 250px;
      }
    }

    .overlay {
      position: absolute;
      top: 0;
      right: 0;
      padding: 1rem;

      @include media-breakpoint-down(md) {
        top: auto;
        bottom: 0;
        left: 0;
        padding: 0;
      }

      .selected-info-overlay {
        width: 350px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        background-color: rgba(#173d58, 0.95);

        @include media-breakpoint-down(md) {
          width: auto;
          margin-bottom: 0;
        }

        .info-wrapper {
          color: #fff;

          .cols {
            @include media-breakpoint-down(md) {
              flex-direction: row;
            }
          }

          .title-col {
            flex: 0 0 65%;

            h1 {
              font-size: 24px;
              font-weight: 500;
            }

            .rank {
              font-size: 24px;
              font-weight: 700;
              font-style: italic;
              margin-top: 0.5em;
            }
          }

          .icon-col {
            flex: 0 0 35%;

            .gauge-wrapper {
              float: right;
              width: 100%;

              .gauge-icon {
                .gauge {
                  display: block;
                }
              }

              .gauge-label {
                display: flex;
                justify-content: space-between;
                text-align: center;
                font-size: 9px;
                font-weight: 300;
                margin-top: 0.75rem;

                div {
                  flex: 0;
                  width: min-content;
                }
              }
            }
          }

          .more-button {
            a {
              display: inline-flex;
              background-color: #ffefe8;
              color: #000;
              font-size: 12px;
              font-weight: 500;
              text-decoration: none;
              padding: 0.45rem 0.5rem 0.25rem;
              margin-top: 1rem;

              svg {
                width: 1.25em;
                height: 1em;
                margin-top: -0.1em;
                margin-left: 0.5rem;
              }
            }
          }

          .scores {
            margin-top: 1rem;

            .score-row {
              display: flex;
              justify-content: space-between;
              border-top: 1px solid rgba(#fff, 0.5);
              padding: 0.5rem 0 0.25rem;
              font-size: 14px;
              line-height: 1;

              &:last-of-type {
                border-bottom: 1px solid rgba(#fff, 0.5);
              }

              .score-label {
                font-weight: 300;
              }

              .score-value {
                display: flex;
                align-items: center;
                font-weight: 900;
                flex-shrink: 0;
                padding-left: 1em;
              }
            }
          }
        }
      }
    }
  }

  .legend {
    text-align: right;
    font-size: 12px;
    font-weight: 500;
    padding: 1rem;
  }
}
</style>
