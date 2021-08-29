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
    highlightMunicipalities: {
      type: Array,
      default: null,
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
    highlightMunicipalities() {
      this.resetTransform();
      this.$nextTick(() => {
        this.colorizeMunicipalities();
      });
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
    resetTransform() {
      this.initialPoint = { x: 0, y: 0 };
      this.initialScale = 1;
      this.setInitialTransform();
    },
    colorizeMunicipalities() {
      const svgElement = this.$refs.svg.$el;
      const names = (
        this.highlightMunicipalities != null
          ? this.highlightMunicipalities
          : this.municipalityData
          ? [this.municipalityData]
          : []
      ).map((o) => o.name.replace(' - ', '-'));
      const elements = [];

      this.municipalitiesList.forEach((o) => {
        const name = o.name.replace(' - ', '-');
        const element = svgElement.querySelector(`[data-name="${name}"]`);
        if (element) {
          const getBucket = this.getBucket || ((o) => o.total_bucket);
          element.style.fill = BUCKET_COLORS[getBucket(o)] || 'red';
          if (names.includes(name)) {
            element.style.stroke = '#ff7a40';
            elements.push(element);
          } else {
            element.style.stroke = '';
          }
        }
      });

      if (elements.length) {
        let xMin = Infinity;
        let yMin = Infinity;
        let xMax = -Infinity;
        let yMax = -Infinity;

        elements.forEach((element) => {
          // move to front, by inserting it as a last child in the parent
          element.parentElement.appendChild(element);

          // center and scale
          const elementRect = element.getBoundingClientRect();
          xMin = Math.min(xMin, elementRect.x);
          yMin = Math.min(yMin, elementRect.y);
          xMax = Math.max(xMax, elementRect.x + elementRect.width);
          yMax = Math.max(yMax, elementRect.y + elementRect.height);
        });

        const container = svgElement.parentElement.parentElement;
        const containerRect = container.getBoundingClientRect();

        const width = xMax - xMin;
        const height = yMax - yMin;
        const size = Math.max(
          width / containerRect.width,
          height / containerRect.height
        );
        const scale = 1 / (size * 1.25);

        const centX = containerRect.x + containerRect.width / 2;
        const centY = containerRect.y + containerRect.height / 2;
        const offX = (centX - xMin - width / 2) * scale;
        const offY = (centY - yMin - height / 2) * scale;
        this.initialPoint = { x: offX, y: offY };
        this.initialScale = scale;
      }

      this.initialized = true;
      this.setInitialTransform();
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
