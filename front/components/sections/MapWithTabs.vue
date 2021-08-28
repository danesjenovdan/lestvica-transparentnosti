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
              <h3>Odprtost in transparentnost slovenskih občin</h3>
              <p>Skupni rezultati analize odprtosti in transparentnosti.</p>
            </div>
            <div class="tab">
              <h3>Transparentnost delovanja občinskega sveta</h3>
              <p>
                Zagotavljanje pravočasnih in ustreznih informacij ter javne
                narave procesov odločanja.
              </p>
            </div>
            <div class="tab">
              <h3>Preglednost spletnega mesta in dostop do informacij</h3>
              <p>
                Enostavno in uporabniku prijazno prikazovanje javnih občinskih
                podatkov.
              </p>
            </div>
            <div class="tab">
              <h3>Transparentnost in vključenost v sprejemanje proračuna</h3>
              <p>
                Prizadevanja za vključevanje občank in občanov v postopek
                sprejemanja proračuna in njegovo poenostavitev.
              </p>
            </div>
            <div class="tab">
              <h3>Dostopnost spletnega mesta</h3>
              <p>
                Zagotavljanje enostavnega dostopa do informacij in funkcij
                spletnega mesta čim večjemu številu oseb.
              </p>
            </div>
            <div class="tab">
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
              <municipalities-map :pan-zoom="panZoom" />
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

  .map-col {
    background-color: #f1f1f1;
  }

  .legend {
    text-align: right;
    font-size: 12px;
    font-weight: 500;
    padding: 1rem;
  }
}
</style>
