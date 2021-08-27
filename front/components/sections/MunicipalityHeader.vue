<template>
  <background-section variant="dark-blue">
    <div class="container">
      <div class="cols">
        <div class="col info-col">
          <div class="info-wrapper">
            <div class="cols">
              <div class="col title-col">
                <h1>{{ municipalityData.name }}</h1>
                <div class="rank">{{ municipalityData.rank }}. mesto</div>
              </div>
              <div class="col icon-col">
                <div class="gauge-wrapper">
                  <div class="gauge-icon">
                    <gauge :value="municipalityData.total_bucket" />
                  </div>
                  <div class="gauge-label">
                    <div>Najslabša ocena</div>
                    <div>Najboljša ocena</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="scores">
              <div
                v-for="(group, key) in municipalityData.groups"
                :key="key"
                class="score-row"
              >
                <div class="score-label">
                  {{ key }}
                </div>
                <div class="score-value">{{ group.score }} / 20</div>
              </div>
            </div>
            <div class="scores-caption">
              Za podrobne rezultate klikni
              <nuxt-link :to="`/obcina/${municipalityData.id}/rezultati`"
                >tukaj</nuxt-link
              >.
            </div>
          </div>
        </div>
        <div class="col map-col">
          <client-only>
            <pan-zoom @ready="onPanZoomReady">
              <municipalities-map :pan-zoom="panZoom" highlight-municipality />
            </pan-zoom>
          </client-only>
        </div>
      </div>
    </div>
  </background-section>
</template>

<script>
import { mapState } from 'vuex';
import BackgroundSection from '~/components/sections/BackgroundSection.vue';
import PanZoom from '~/components/PanZoom.vue';
import Gauge from '~/components/Gauge.vue';
import MunicipalitiesMap from '~/components/MunicipalitiesMap.vue';

export default {
  components: {
    BackgroundSection,
    PanZoom,
    MunicipalitiesMap,
    Gauge,
  },
  data() {
    return {
      panZoom: null,
    };
  },
  computed: {
    ...mapState(['municipalityData']),
  },
  methods: {
    onPanZoomReady(panZoom) {
      this.panZoom = panZoom;
    },
  },
};
</script>

<style lang="scss" scoped>
.info-col {
  padding: 5rem;
  color: #fff;

  .info-wrapper {
    padding-right: 6rem;

    .title-col {
      flex: 1.5;

      h1 {
        font-size: 48px;
        font-weight: 500;
      }

      .rank {
        font-size: 48px;
        font-weight: 700;
        font-style: italic;
        margin-top: 1.5rem;
      }
    }

    .icon-col {
      .gauge-wrapper {
        float: right;
        width: 150px;

        .gauge-icon {
          .gauge {
            display: block;
          }
        }

        .gauge-label {
          display: flex;
          justify-content: space-between;
          text-align: center;
          font-size: 11px;
          font-weight: 300;
          margin-top: 0.75rem;

          div {
            flex: 0;
            width: min-content;
          }
        }
      }
    }

    .scores {
      margin-top: 3rem;

      .score-row {
        display: flex;
        justify-content: space-between;
        border-top: 1px solid rgba(#fff, 0.5);
        padding: 1rem 0.75rem 0.75rem;
        font-size: 22px;
        line-height: 1;

        &:last-of-type {
          border-bottom: 1px solid rgba(#fff, 0.5);
        }

        .score-label {
          font-weight: 300;
        }

        .score-value {
          font-weight: 900;
          flex-shrink: 0;
        }
      }
    }

    .scores-caption {
      font-size: 16px;
      font-weight: 300;
      font-style: italic;
      text-align: right;
      margin-top: 1rem;
      margin-right: 0.75rem;
    }
  }
}

.map-col {
  .pan-zoom-container {
    background-color: #f1f1f1;
  }
}
</style>
