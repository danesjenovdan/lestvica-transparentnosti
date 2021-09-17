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
@import '~/assets/styles/breakpoints';

.content-section {
  padding: 7rem 0;

  @include media-breakpoint-down(md) {
    padding: 3rem 0;
  }
}

.content-section ::v-deep {
  .narrow {
    max-width: 900px;
    margin: 0 auto;
  }

  .center {
    text-align: center;
  }

  h2,
  h3 {
    font-size: 48px;
    font-weight: 900;
    line-height: 1.2;
    text-transform: uppercase;
    color: var(--heading-color);
    margin-bottom: 1.2em;

    @include media-breakpoint-down(md) {
      font-size: 24px;
    }

    em {
      font-style: italic;
      color: var(--heading-em-color);
    }
  }

  h3 {
    margin-top: 2em;
    font-size: 32px;

    @include media-breakpoint-down(md) {
      font-size: 20px;
    }
  }

  p,
  ul,
  ul li,
  table {
    font-size: 22px;
    font-weight: 300;
    line-height: 1.6;
    margin-bottom: 1.5em;

    &:last-child {
      margin-bottom: 0;
    }

    @include media-breakpoint-down(md) {
      font-size: 16px;
      font-weight: 300;
    }

    .large {
      font-size: 32px;
      line-height: 1.4;

      @include media-breakpoint-down(md) {
        font-size: 22px;
      }
    }

    .highlighted {
      background-color: var(--highlight-color);
      padding-top: 0.45em;
      padding-bottom: 0.02em;
      font-weight: 700;
      box-shadow: -0.2em 0 0 var(--highlight-color),
        0.2em 0 0 var(--highlight-color);
      box-decoration-break: clone;

      .large {
        line-height: 0;
      }
    }
  }

  hr {
    margin: 4rem 0;
    height: 0;
    border: none;
    border-top: 1px solid var(--heading-color);

    @include media-breakpoint-down(md) {
      margin: 2rem 0;
    }
  }

  table {
    width: 100%;
    table-layout: fixed;
    border: 0;
    border-collapse: collapse;

    tr {
      border-bottom: 1px solid var(--heading-color);

      th,
      td {
        padding: 1rem 0.5rem;
      }

      th {
        font-weight: 900;
        text-align: left;
      }
    }
  }

  .boxes {
    display: flex;
    gap: 2rem;
    justify-content: center;
    margin: 6rem calc(-2 * var(--page-gutter));
    flex-wrap: wrap;
    max-width: 100vw;

    &:last-child {
      margin-bottom: 0;
    }

    &.boxes-2col {
      margin: 6rem auto;
      flex-wrap: wrap;
      max-width: 850px;
    }

    @include media-breakpoint-down(md) {
      flex-direction: column;
      margin: 2.5rem 0;
    }

    .box {
      width: 380px;
      background-color: var(--highlight-color);
      padding: 2.5rem 2rem 2rem;

      @include media-breakpoint-down(md) {
        width: 100%;
        flex-basis: 100%;
        padding: 1.25rem 1rem 1rem;
      }

      .box-text {
        font-size: 22px;
        line-height: 1.4;

        @include media-breakpoint-down(md) {
          font-size: 16px;
        }

        .large {
          font-size: 50px;

          @include media-breakpoint-down(md) {
            font-size: 28px;
          }
        }

        strong {
          display: inline-block;
          font-size: 28px;

          @include media-breakpoint-down(md) {
            font-size: 20px;
          }

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
    margin: 6rem calc(-1 * var(--page-gutter));

    @include media-breakpoint-down(md) {
      flex-direction: column;
      margin: 2.5rem 0;
    }

    &.described-example--reverse {
      flex-direction: row-reverse;

      @include media-breakpoint-down(md) {
        flex-direction: column;
      }

      .description-col + .example-col {
        margin-left: 0;
        margin-right: -3rem;

        @include media-breakpoint-down(md) {
          margin-right: 0;
          margin-top: -1.5rem;
        }
      }
    }

    &.described-example--wide {
      .example-col {
        .example {
          width: 900px;
        }
      }
    }

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

        @include media-breakpoint-down(md) {
          width: 100%;
          flex-basis: 100%;
          padding: 1rem;
          font-size: 20px;
          top: 0;
        }

        .large {
          font-size: 50px;
          line-height: 0;

          @include media-breakpoint-down(md) {
            font-size: 28px;
          }
        }
      }
    }

    .example-col {
      .example {
        width: 740px;
        border: 12px solid var(--accent-color);

        @include media-breakpoint-down(md) {
          width: auto !important;
          border-width: 6px;
          margin: 0 calc(-1 * var(--page-gutter));
        }

        img {
          display: block;
          width: 100%;
          height: auto;
        }
      }

      .caption {
        width: 740px;
        font-size: 18px;
        font-style: italic;
        font-weight: 500;
        margin-top: 1em;

        @include media-breakpoint-down(md) {
          width: 100%;
          font-size: 14px;
        }
      }
    }

    .description-col + .example-col {
      margin-left: -3rem;

      @include media-breakpoint-down(md) {
        margin-left: 0;
        margin-top: -1.5rem;
      }
    }
  }

  .side-image-wrapper {
    height: 0;
    position: relative;

    img {
      position: absolute;
      top: 0;
      right: -2rem;
      display: block;

      transform: translate(65%, -100%);
      width: 350px;
      height: 350px;

      // @include media-breakpoint-down(xxl) {
      //   transform: translate(65%, -110%);
      //   width: 300px;
      // }

      @include media-breakpoint-down(xl) {
        display: none;
      }
    }
  }
}
</style>
