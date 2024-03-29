<template>
  <background-section id="uvod" variant="dark-blue">
    <div class="container">
      <div class="cols">
        <div class="col text-col">
          <h1>
            Ali je delovanje slovenskih občin na spletu <em>odprto</em> in
            <em>transparentno</em>?
          </h1>
          <p>
            Čeprav se morda zdi, da igrajo v državi pomembno vlogo le odločitve
            vlade, tudi lokalna samouprava bistveno vpliva na naša vsakdanja
            življenja. Ker mora biti zato njihovo delovanje odprto in
            vključujoče, smo na inštitutu
            <a href="https://danesjenovdan.si" target="_blank"
              >Danes je nov dan</a
            >
            v sodelovanju z
            <a href="http://dopd.si" target="_blank"
              >Organizacijo za participatorno družbo</a
            >
            ter
            <a href="https://pic.si" target="_blank"
              >PIC – Pravni center za varstvo človekovih pravic in okolja</a
            >
            pripravili
            <strong
              >raziskavo transparentnosti in odprtosti slovenskih občin.</strong
            >
            V njej smo
            <strong>z 80 kazalniki ocenili vseh 212 slovenskih občin</strong>,
            pri čemer smo pregledovali vsebine in podatke za leto 2020.
          </p>
          <h2>Kaj smo ugotovili v raziskavi?</h2>
          <p>
            Zaključki kažejo zaskrbljujočo sliko. Večina občin pri odpiranju
            svojega delovanja ni proaktivna, temveč zgolj sledi zastarelim
            praksam in nizkim zakonskim standardom. Tudi kadar so podatki na
            spletnih mestih objavljeni, so pogosto skriti v zapletene labirinte
            hiperpovezav ali pa na voljo le v več sto strani dolgih in
            zapletenih dokumentih.
            <strong>
              Kar 95&nbsp;% občin pri pregledu vsebin ni doseglo niti polovice
              od 100 možnih točk</strong
            >, tudi najvišje ocenjena občina pa je dosegla le 67,2 točke. Občine
            tako v veliki meri ne omogočajo ustrezne participacije ali
            informiranja občank in občanov.
          </p>
          <p>
            V nadaljevanju so predstavljeni rezultati analize, kjer je mogoče
            najti podatke za posamezno občino, hkrati pa te primerjati tudi z
            vsemi občinami ali pa tistimi, ki imajo podobno število prebivalcev
            oziroma višino proračuna. Poleg tega pa smo pripravili tudi pogled
            na širšo sliko stanja odprtosti in transparentnosti na področju
            lokalne samouprave v Sloveniji.
            <strong>
              Za vsako občino smo podali nekaj priporočil, s pomočjo katerih bo
              lahko v prihodnje delovala bolj odprto, tebe pa spodbujamo, da jim
              pošlješ predpripravljeno elektronsko sporočilo in jih pozoveš, da
              jih upoštevajo.
            </strong>
          </p>
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
@import '~/assets/styles/breakpoints';

.text-col {
  flex: 4;
  padding: 7rem 0;
  color: #fff;

  @include media-breakpoint-down(md) {
    padding: 2rem 0;
  }

  h1,
  h2 {
    font-size: 54px;
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
      color: #ffc569;
    }
  }

  h2 {
    font-size: 30px;
    font-weight: 700;

    @include media-breakpoint-down(md) {
      font-size: 20px;
    }
  }

  p {
    font-size: 22px;
    font-weight: 300;
    line-height: 1.4;
    margin-bottom: 1.5em;

    @include media-breakpoint-down(md) {
      font-size: 16px;
      font-weight: 300;
    }
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
