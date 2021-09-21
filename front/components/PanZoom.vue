<template>
  <div ref="container" class="pan-zoom-container">
    <div ref="content" class="pan-zoom-content">
      <slot />
    </div>
  </div>
</template>

<script>
import panZoom from '~/utils/pan-zoom';

export default {
  mounted() {
    panZoom({
      container: this.$refs.container,
      content: this.$refs.content,
      initialTransform: this.initialTransform,
      onReady: (panZoom) => {
        this.$emit('ready', panZoom);
      },
      onTransformChange: (point, scale) => {
        this.$emit('change', { point, scale });
      },
    });
  },
};
</script>

<style lang="scss" scoped>
.pan-zoom-container {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;

  .pan-zoom-content {
    width: 100%;
    height: 100%;
  }
}
</style>
