<template>
  <background-section>
    <div class="map-with-tabs">
      <div class="search-fields">
        <search-field dark />
        <search-field dark />
      </div>
      <div class="cols">
        <div class="col tabs-col">
          <div class="tabs">
            <div class="tab active">
              <h3>LESTVICA TRANSPARENTNOSTI IN DOSTOPNOSTI</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse. ultrices gravida. Risus commodo viverra
                maecenas accumsan lacus vel facilisis.
              </p>
            </div>
            <div class="tab">
              <h3>LESTVICA TRANSPARENTNOSTI IN DOSTOPNOSTI</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse. ultrices gravida. Risus commodo viverra
                maecenas accumsan lacus vel facilisis.
              </p>
            </div>
            <div class="tab">
              <h3>LESTVICA TRANSPARENTNOSTI IN DOSTOPNOSTI</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse. ultrices gravida. Risus commodo viverra
                maecenas accumsan lacus vel facilisis.
              </p>
            </div>
            <div class="tab">
              <h3>LESTVICA TRANSPARENTNOSTI IN DOSTOPNOSTI</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse. ultrices gravida. Risus commodo viverra
                maecenas accumsan lacus vel facilisis.
              </p>
            </div>
            <div class="tab">
              <h3>LESTVICA TRANSPARENTNOSTI IN DOSTOPNOSTI</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse. ultrices gravida. Risus commodo viverra
                maecenas accumsan lacus vel facilisis.
              </p>
            </div>
            <div class="tab">
              <h3>LESTVICA TRANSPARENTNOSTI IN DOSTOPNOSTI</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse. ultrices gravida. Risus commodo viverra
                maecenas accumsan lacus vel facilisis.
              </p>
            </div>
          </div>
        </div>
        <div class="col map-col">
          <client-only>
            <pan-zoom @ready="onPanZoomReady">
              <municipalities-map :pan-zoom="panZoom" />
            </pan-zoom>
          </client-only>
        </div>
      </div>
    </div>
  </background-section>
</template>

<script>
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
    };
  },
  methods: {
    onPanZoomReady(panZoom) {
      this.panZoom = panZoom;
    },
  },
};
</script>

<style lang="scss" scoped>
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
  }

  .tabs-col {
    flex: 0 0 auto;

    .tabs {
      width: 400px;

      .tab {
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

  .map-col {
    background-color: #f1f1f1;
  }
}
</style>
