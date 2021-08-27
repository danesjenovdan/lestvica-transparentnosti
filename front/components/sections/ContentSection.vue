<template>
  <background-section :variant="variant">
    <div class="container">
      <div class="content-section">
        <slot />
      </div>
    </div>
  </background-section>
</template>

<script>
import BackgroundSection from '~/components/sections/BackgroundSection.vue';

export default {
  components: {
    BackgroundSection,
  },
  props: {
    variant: {
      type: String,
      default: 'white',
    },
  },
};
</script>

<style lang="scss" scoped>
.content-section {
  padding: 7rem 0;
}

.content-section ::v-deep {
  .narrow {
    max-width: 900px;
    margin: 0 auto;
  }

  .center {
    text-align: center;
  }

  h2 {
    font-size: 48px;
    font-weight: 900;
    line-height: 1.2;
    text-transform: uppercase;
    color: var(--heading-color);
    margin-bottom: 1.2em;

    em {
      font-style: italic;
      color: var(--heading-em-color);
    }
  }

  p {
    font-size: 22px;
    font-weight: 500;
    line-height: 1.6;
    margin-bottom: 1.5em;

    .large {
      font-size: 32px;
      line-height: 1.4;
    }

    .highlighted {
      background-color: var(--highlight-color);
      padding-top: 0.45em;
      padding-bottom: 0.02em;
      font-weight: 700;
      box-shadow: -0.2em 0 0 var(--highlight-color),
        0.2em 0 0 var(--highlight-color);

      .large {
        line-height: 0;
      }
    }
  }

  .boxes {
    display: flex;
    gap: 2rem;
    justify-content: center;
    margin-top: 6rem;
    margin-bottom: 6rem;

    .box {
      width: 400px;
      background-color: var(--highlight-color);
      padding: 2.5rem 2rem 2rem;

      .box-text {
        font-size: 22px;
        line-height: 1.4;

        .large {
          font-size: 50px;
        }

        strong {
          display: inline-block;
          font-size: 28px;

          .large {
            line-height: 0;
          }
        }
      }
    }
  }

  .described-example {
    display: flex;
    justify-content: center;
    margin-top: 6rem;
    margin-bottom: 6rem;

    .description-col {
      display: flex;
      align-items: center;

      .description {
        background-color: var(--highlight-color);
        width: 400px;
        font-size: 28px;
        font-weight: 700;
        line-height: 1.4;
        padding: 2rem;
        position: relative;
        top: -1.5rem;
        z-index: 1;
      }
    }

    .example-col {
      .example {
        width: 740px;
        height: 400px;
        border: 12px solid var(--accent-color);
      }

      .caption {
        font-size: 18px;
        font-style: italic;
        font-weight: 500;
        margin-top: 1rem;
      }
    }

    .description-col + .example-col,
    .example-col + .description-col {
      margin-left: -3rem;
    }
  }
}
</style>
