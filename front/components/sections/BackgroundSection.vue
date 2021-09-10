<template>
  <div :class="['background-section', variant]">
    <slot />
  </div>
</template>

<script>
export default {
  props: {
    variant: {
      type: String,
      default: 'white',
    },
  },
};
</script>
