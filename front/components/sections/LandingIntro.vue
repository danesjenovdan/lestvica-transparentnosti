<template>
  <background-section variant="dark-blue">
    <div class="container">
      <div class="cols">
        <div class="col text-col">
          <h1>
            Ali je delovanje slovenskih občin na spletu predstavljeno
            <em>TRANSPARENTNO</em> in <em>DOSTOPNO</em>?
          </h1>
          <div>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
              ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas
              accumsan lacus vel facilisis.
            </p>
            <p>
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
              officia deserunt mollit anim id est laborum. Sed ut perspiciatis
              unde omnis iste natus error sit voluptatem accusantium doloremque
              laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
              veritatis et quasi architecto beatae vitae dicta sunt explicabo.
            </p>
            <p>
              Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit
              aut fugit, sed quia consequuntur magni dolores eos qui ratione
              voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem
              ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
              non numquam eius modi tempora incidunt ut labore et dolore magnam
              aliquam quaerat voluptatem.
            </p>
          </div>
        </div>
        <div class="col image-col">
          <div class="image-wrapper">
            <img src="~/assets/images/ilustracija-landing.svg" alt="" />
          </div>
          <div class="arrow-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="191 54 465 739">
              <path
                d="M296 61h-97c22 279 256 255 257 494h-73l127 223 133-224h-88c-8-259-232-265-259-493zm7-7c26 236 249 233 259 493h94L510 793 370 547h78c-4-231-236-196-257-493h112z"
              />
            </svg>
          </div>
        </div>
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
};
</script>

<style lang="scss" scoped>
.text-col {
  flex: 4;
  padding: 7rem 0;
  color: #fff;

  h1 {
    font-size: 48px;
    font-weight: 900;
    line-height: 1.2;
    text-transform: uppercase;
    color: var(--heading-color);
    margin-bottom: 1.2em;

    em {
      font-style: italic;
      color: #ffc569;
    }
  }

  p {
    font-size: 22px;
    font-weight: 500;
    line-height: 1.4;
    margin-bottom: 1.5em;
  }
}

.image-col {
  flex: 3;
  position: relative;

  .image-wrapper {
    margin-left: 8rem;
    display: flex;
    height: 100%;
    align-items: center;

    img {
      display: block;
      width: 100%;
    }
  }

  .arrow-wrapper {
    position: absolute;
    left: 5rem;
    bottom: 2rem;
    width: 15%;

    svg {
      fill: #ff996c;
    }
  }
}
</style>
