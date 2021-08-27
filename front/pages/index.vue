<template>
  <div>
    <page-header />

    <landing-intro />

    <content-section variant="white">
      <div class="narrow">
        <p class="center">
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
          officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde
          omnis iste natus error sit voluptatem accusantium doloremque
          laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
          veritatis et quasi architecto beatae vitae dicta sunt explicabo.
        </p>
      </div>
    </content-section>

    <map-with-tabs />

    <content-section variant="blue">
      <div class="narrow">
        <h2>
          Ali občine sledijo standardom <em>odprtosti</em> in
          <em>transparentnosti</em> javne uprave?
        </h2>
        <p>
          <span class="large">
            Odprtost in transparentnost občinskih podatkov javnega značaja
            omogoča sodelovanje v procesih lokalne samouprave.
          </span>
          To lahko sega od preprostega spremljanja relevantnih tematik in
          izvajanja nadzora nad delovanjem lokalnih oblasti pa vse do neposredne
          udeležbe v nekaterih političnih postopkih. In ker delovanje občinskih
          svetov še kako vpliva na naša vsakdanja življenja, z analizo odprtosti
          in transparentnosti prikazovanja občinskih podatkov opozarjamo na
          prepogosto neustrezno ravnanje slovenskih občin na tem področju.
        </p>
        <p>
          Večina občin pri odpiranju svojega delovanja ni ne proaktivna ne
          inovativna, temveč zgolj slepo sledi zastarelim smernicam ter
          suhoparni in neambiciozni zakonski ureditvi, ki tako rekoč ne
          predvideva aktivne participacije prebivalcev. Še bolj osupljivo pa je,
          da
          <span class="highlighted">
            kar <span class="large">XY občin</span> na nekaterih področjih ne
            zadošča niti minimalnim zakonskim standardom in s tem krši
            zakonodajo.
          </span>
        </p>
      </div>

      <div class="boxes">
        <div class="box">
          <div class="box-text">
            <strong>
              <span class="large">77</span> občinskih svetov se je v letu 2020
              sestalo manj kot štirikrat, kot to sicer določa Zakon o lokalni
              samoupravi,
            </strong>
            kar pomeni, da svetniki v celotnem koledarskem letu svojim lokalnim
            skupnostim niso posvetili niti toliko časa, kot veleva zakonodaja.
          </div>
        </div>
        <div class="box">
          <div class="box-text">
            <strong>
              <span class="large">150</span> občinskih svetov proračuna za leto
              2020 ni sprejelo pred začetkom leta oziroma z največ trimesečnim
              zamikom, kot to določa Zakon o javnih financah,
            </strong>
            s čimer so občankam in občanom resno okrnili možnost za informiranje
            in vključenost v postopke odločanja o porabi občinskih sredstev.
          </div>
        </div>
        <div class="box">
          <div class="box-text">
            <strong>
              <span class="large">89</span> občin nima objavljene izjave o
              dostopnosti spletnega mesta, ki jo sicer zahteva Zakon o
              dostopnosti spletišč in mobilnih aplikacij,
            </strong>
            kar pomeni, da dostopnosti svojega spletnega mesta niso niti
            analizirali, kaj šele, da bi ga prilagodili osebam z oviranostmi.
          </div>
        </div>
      </div>

      <div class="narrow">
        <p>
          Pogosto je slabo stanje na področju odprtosti delovanja občin
          posledica ohlapne zakonodaje, ki praktično ne naslavlja vprašanj
          dostopnosti podatkov, tako da si lahko občinski sveti pravila v
          poslovnikih večinoma postavljajo kar sami. Tam opredelijo, kako in
          katere podatke, povezane s svojim delovanjem, bodo oziroma ne bodo
          prikazovali javnosti. Poslovniki sicer urejajo tudi širše delovanje
          občin in so ključen dokument, ki občankam in občanom omogoča
          razumevanje njihovih pravic.
        </p>
        <p>
          Za odprto delovanje občin namreč ni pomembno le, da so informacije
          objavljene, temveč tudi v kakšni obliki so objavljene oziroma
          predstavljene uporabnicam in uporabnikom spletnih mest. Brskanje po
          teh ne bi smela biti frustrirajoča izkušnja, ki zainteresiranim članom
          lokalnih skupnosti vzame več ur, ampak preprosta in intuitivna pot, ki
          sestoji iz največ nekaj klikov.
        </p>
        <p>
          In čeprav je to ključen del zadovoljive uporabniške izkušnje,
          slovenske občine številne pomembne podatke in datoteke prepogosto
          skrijejo v zapletene labirinte spletnih hiperpovezav, za njihovo
          odkrivanje pa sta potrebna najmanj magisterij iz računalništva in
          doktorat iz politologije.
        </p>
      </div>

      <div class="described-example">
        <div class="description-col">
          <div class="description">
            Nekatere občine vsa gradiva za sejo objavijo v eni sami datoteki
            PDF, po kateri se z bližnjico CTRL + F ne da iskati.
          </div>
        </div>
        <div class="example-col">
          <div class="example"></div>
          <div class="caption">Primer lorem ipsum dolor sit amet</div>
        </div>
      </div>
      <div class="described-example">
        <div class="example-col">
          <div class="example"></div>
          <div class="caption">Primer lorem ipsum dolor sit amet</div>
        </div>
        <div class="description-col">
          <div class="description">
            Nekatere občine vsa gradiva za sejo objavijo v eni sami datoteki
            PDF, po kateri se z bližnjico CTRL + F ne da iskati.
          </div>
        </div>
      </div>
    </content-section>

    <municipality-search />

    <page-footer />
  </div>
</template>

<script>
import PageHeader from '~/components/PageHeader.vue';
import LandingIntro from '~/components/sections/LandingIntro.vue';
import ContentSection from '~/components/sections/ContentSection.vue';
import MapWithTabs from '~/components/sections/MapWithTabs.vue';
import MunicipalitySearch from '~/components/sections/MunicipalitySearch.vue';
import PageFooter from '~/components/PageFooter.vue';

export default {
  components: {
    PageHeader,
    LandingIntro,
    ContentSection,
    MapWithTabs,
    MunicipalitySearch,
    PageFooter,
  },
  async asyncData({ store }) {
    await store.dispatch('ensureMunicipalitiesList');
  },
};
</script>
