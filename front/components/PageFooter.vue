<template>
  <div>
    <background-section variant="medium-green">
      <div class="container">
        <div class="donation-bar">
          <div>Podpri naše delovanje!</div>
          <div>
            <a
              class="donate-button"
              href="https://danesjenovdan.si/doniraj"
              target="_blank"
            >
              <div class="text">DONIRAJ</div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="16.44 26 64.56 48"
              >
                <path
                  d="M53.18 73.82a1.99 1.99 0 002.14-.32l25-22a2 2 0 000-3l-25-22A2 2 0 0052 28v12H26a10.01 10.01 0 000 20h26v12a2 2 0 001.18 1.82zM26 56a6 6 0 010-12h28a2 2 0 002-2v-9.58L75.97 50 56 67.58V58a2 2 0 00-2-2H26z"
                />
              </svg>
            </a>
          </div>
        </div>
      </div>
    </background-section>
    <background-section variant="dark-green">
      <footer>
        <div class="container">
          <nav class="footer">
            <div class="cols">
              <div class="col nav-col">
                <div class="nav-link-wrapper">
                  <a href="#">Celotna zbirka podatkov</a>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="16.44 26 64.56 48"
                  >
                    <path
                      d="M53.18 73.82a1.99 1.99 0 002.14-.32l25-22a2 2 0 000-3l-25-22A2 2 0 0052 28v12H26a10.01 10.01 0 000 20h26v12a2 2 0 001.18 1.82zM26 56a6 6 0 010-12h28a2 2 0 002-2v-9.58L75.97 50 56 67.58V58a2 2 0 00-2-2H26z"
                    />
                  </svg>
                </div>
                <div class="nav-link-wrapper">
                  <a
                    href="https://drive.google.com/file/d/16q3N0QTiDRWioPXr4UNTk-ITMj3PJ12s/view?usp=sharing"
                    target="_blank"
                    >Metodologija</a
                  >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="16.44 26 64.56 48"
                  >
                    <path
                      d="M53.18 73.82a1.99 1.99 0 002.14-.32l25-22a2 2 0 000-3l-25-22A2 2 0 0052 28v12H26a10.01 10.01 0 000 20h26v12a2 2 0 001.18 1.82zM26 56a6 6 0 010-12h28a2 2 0 002-2v-9.58L75.97 50 56 67.58V58a2 2 0 00-2-2H26z"
                    />
                  </svg>
                </div>
              </div>
              <div class="col logo-col">
                <img
                  src="~/assets/images/acf.svg"
                  alt="Active citizens fund"
                  class="logo"
                />
              </div>
              <div class="col credits-col">
                <div>
                  Analizo so s finančno podporo
                  <a href="#" target="_blank">Active citizens fund Slovenija</a>
                  pripravili
                  <a
                    href="https://danesjenovdan.si"
                    target="_blank"
                    class="heavy-link"
                    >Danes je nov dan</a
                  >,
                  <a href="http://dopd.si" target="_blank" class="heavy-link"
                    >Organizacija za participatorno družbo</a
                  >
                  in
                  <a href="https://pic.si/" target="_blank" class="heavy-link"
                    >PIC - Pravni center za varstvo človekovih pravic in
                    okolja</a
                  >.
                </div>
              </div>
            </div>
          </nav>
        </div>
      </footer>
    </background-section>
  </div>
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
@import '~/assets/styles/breakpoints';

.donation-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  padding: 4rem 0;
  font-size: 22px;
  text-align: center;

  @include media-breakpoint-down(md) {
    flex-direction: column;
    padding: 2rem 0;
    gap: 1rem;
    font-size: 16px;
  }

  .donate-button {
    display: flex;
    align-items: center;
    border: 2px solid #000;
    padding: 0.5em 1em;
    font-size: 32px;
    font-weight: 900;
    line-height: 1;
    text-decoration: none;

    @include media-breakpoint-down(md) {
      font-size: 22px;
    }

    &:hover {
      background-color: rgba(#fff, 0.15);
    }

    .text {
      margin-top: 0.17em;
    }

    svg {
      width: auto;
      height: 0.75em;
      margin-left: 1rem;
    }
  }
}

footer {
  nav.footer {
    padding: 4rem 0;

    @include media-breakpoint-down(md) {
      padding: 2rem 0;
      text-align: center;
    }

    .nav-col {
      display: flex;
      flex-direction: column;
      justify-content: center;

      @include media-breakpoint-down(md) {
        align-items: center;
      }

      .nav-link-wrapper {
        display: flex;
        align-items: center;
        font-size: 20px;

        @include media-breakpoint-down(md) {
          font-size: 16px;
          margin-bottom: 1em;
        }

        &:not(:last-child) {
          margin-bottom: 1em;
        }

        a:hover {
          color: #173d58;
        }

        svg {
          width: auto;
          height: 0.75em;
          margin-left: 1rem;
        }
      }
    }

    .logo-col {
      flex: 0 0 auto;

      .logo {
        display: block;
        width: auto;
        height: 80px;

        @include media-breakpoint-down(md) {
          margin: 1.5rem auto;
        }
      }
    }

    .credits-col {
      flex: 1.5;
      font-size: 20px;
      line-height: 1.4;

      @include media-breakpoint-down(md) {
        font-size: 16px;
      }

      .heavy-link {
        font-weight: 900;
      }

      a:hover {
        color: #173d58;
      }
    }
  }
}
</style>
