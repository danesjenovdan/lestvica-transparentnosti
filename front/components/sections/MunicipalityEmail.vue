<template>
  <content-section variant="white">
    <div class="cols">
      <div class="col title-col">
        <div class="mail-title">
          <h3>POŠLJI SPOROČILO SVOJI OBČINI IN ZAHTEVAJ SPREMEMBE!</h3>
          <h4>
            Kopiraj sporočilo in ga pošlji na:
            <strong class="email">{{ municipalityData.email }}</strong>
          </h4>
        </div>
      </div>
      <div class="col mail-col">
        <textarea
          v-model="emailText"
          readonly
          onclick="this.select()"
        ></textarea>
      </div>
    </div>
  </content-section>
</template>

<script>
import { mapState } from 'vuex';
import ContentSection from '~/components/sections/ContentSection.vue';

export default {
  components: {
    ContentSection,
  },
  computed: {
    ...mapState(['municipalityData']),
    recommendations() {
      return (this.municipalityData?.recommendations || [])
        .slice()
        .sort((a, b) => b.importance - a.importance)
        .slice(0, 5);
    },
    emailText() {
      const pre = `
Spoštovani,

iz rezultatov nedavne raziskave odprtosti in transparentnosti slovenskih občin je mogoče razbrati, da ${this.municipalityData.name} ne izpolnjuje vseh pogojev za omogočanje informiranja in sodelovanja v procesih delovanja občine. Zato vam spodaj pošiljam pet predlogov sprememb, s katerimi lahko to stanje izboljšate.
      `.trim();

      const post = `
Odprtost in transparentnost vašega delovanja lahko namreč pomembno prispeva k dvigu participacije občank in občanov. Ta lahko sega od preprostega spremljanja relevantnih tematik in izvajanja nadzora nad delom lokalnih oblasti pa vse do neposredne udeležbe v nekaterih političnih postopkih.

Ker lahko poleg zgornjih petih predlogov rezultat občine izboljšate tudi na druge načine, vam predlagam, da si pogledate celotno analizo, ki jo najdete na: X.

V upanju, da boste upoštevali predloge in izboljšali pogoje za participacijo ter informiranje občank in občanov, vas lepo pozdravljam.
      `.trim();

      const recs = this.recommendations
        .map((r, i) => `${i + 1}. ${r.title}\n${r.text}`)
        .join('\n\n');

      return `${pre}\n\n${recs}\n\n${post}`;
    },
  },
};
</script>

<style lang="scss" scoped>
@import '~/assets/styles/breakpoints';

.title-col {
  flex: 1;

  @include media-breakpoint-down(md) {
    margin-bottom: 1rem;
  }

  .mail-title {
    background-color: #21435c;
    padding: 3rem;

    @include media-breakpoint-down(md) {
      padding: 1.25rem 1rem;
    }

    h3 {
      color: #fff;
      font-size: 48px;
      font-weight: 900;
      line-height: 1.2;
      margin-top: 0;
      margin-bottom: 1em;

      @include media-breakpoint-down(md) {
        font-size: 24px;
      }
    }

    h4 {
      color: #fff;
      font-size: 28px;
      font-weight: 300;
      line-height: 1.2;
      margin-bottom: 1em;

      @include media-breakpoint-down(md) {
        font-size: 18px;
        margin-bottom: 0;
      }

      strong.email {
        font-weight: 500;
        white-space: nowrap;
      }
    }
  }
}

.mail-col {
  flex: 2;

  textarea {
    display: block;
    width: 100%;
    height: 820px;
    border: 2px solid #21435c;
    padding: 2rem;
    resize: none;
    font-size: 18px;
    font-weight: 300;

    @include media-breakpoint-down(md) {
      padding: 1rem;
      font-size: 16px;
      height: 300px;
    }

    &:focus {
      outline: none;
    }
  }
}
</style>
