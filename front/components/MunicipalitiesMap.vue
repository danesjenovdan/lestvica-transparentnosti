<template>
  <div class="municipalities-map">
    <municipalities-svg ref="svg" :class="{ hidden: !initialized }" />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import { BUCKET_COLORS } from '~/utils/constants';
import MunicipalitiesSvg from '~/components/MunicipalitiesSvg.vue';

export default {
  components: {
    MunicipalitiesSvg,
  },
  props: {
    panZoom: {
      type: Object,
      default: null,
    },
    highlightMunicipality: {
      type: Boolean,
      default: false,
    },
    getBucket: {
      type: Function,
      default: null,
    },
  },
  data() {
    return {
      initialPoint: { x: 0, y: 0 },
      initialScale: 0.9,
      initialized: false,
    };
  },
  computed: {
    ...mapState(['municipalitiesList', 'municipalityData']),
  },
  watch: {
    panZoom() {
      this.setInitialTransform();
    },
    getBucket() {
      this.colorizeMunicipalities();
    },
  },
  mounted() {
    this.colorizeMunicipalities();
  },
  methods: {
    setInitialTransform() {
      if (this.initialized && this.panZoom) {
        this.panZoom.setTransform(this.initialPoint, this.initialScale);
      }
    },
    colorizeMunicipalities() {
      let currentEl = null;
      const svgEl = this.$refs.svg.$el;
      this.municipalitiesList.forEach((o) => {
        const name = o.name.replace(' - ', '-');
        const el = svgEl.querySelector(`[data-name="${name}"]`);
        if (!el) {
          // eslint-disable-next-line no-console
          console.error('Missing SVG map element:', o.name);
        } else {
          const getBucket = this.getBucket || ((o) => o.total_bucket);
          console.log(getBucket(o));
          el.style.fill = BUCKET_COLORS[getBucket(o)] || 'red';
          if (
            this.highlightMunicipality &&
            this.municipalityData.name === name
          ) {
            el.style.stroke = '#ff7a40';
            currentEl = el;
          }
        }
      });
      if (!this.highlightMunicipality) {
        this.initialized = true;
        this.setInitialTransform();
      } else if (currentEl) {
        // move to front, by inserting it as a last child in the parent
        currentEl.parentElement.appendChild(currentEl);

        // center and scale
        const elRect = currentEl.getBoundingClientRect();
        const container = svgEl.parentElement.parentElement;
        const contRect = container.getBoundingClientRect();
        const scale = Math.min(5, 1 / ((elRect.width * 1.5) / contRect.width));
        const centX = contRect.x + contRect.width / 2;
        const centY = contRect.y + contRect.height / 2;
        const offX = (centX - elRect.x - elRect.width / 2) * scale;
        const offY = (centY - elRect.y - elRect.height / 2) * scale;
        this.initialPoint = { x: offX, y: offY };
        this.initialScale = scale;
        this.initialized = true;
        this.setInitialTransform();
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.municipalities-map {
  width: 100%;
  height: 100%;
  background-color: #f1f1f1;

  .hidden {
    visibility: hidden;
  }
}
</style>
