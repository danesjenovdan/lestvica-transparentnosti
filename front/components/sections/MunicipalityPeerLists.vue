<template>
  <content-section variant="white">
    <div class="cols">
      <div class="col">
        <div class="peer-list">
          <div class="peer-list-header">
            <h3>PRIMERJAVA PO ŠTEVILU PREBIVALCEV</h3>
            <h4>Občine z TODO ali manj prebivalcev</h4>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
              ultrices gravida. Risus commodo viverra maecenas accumsan. lacus
              vel facilisis.
            </p>
          </div>
          <div class="peer-list-elements">
            <div
              v-for="peer in populationPeers"
              :key="peer.id"
              :class="[
                'peer-list-element',
                { active: municipalityData.id === peer.id },
              ]"
            >
              <div class="name">{{ peer.rank }}. {{ peer.name }}</div>
              <div class="score">{{ Math.round(peer.total_score) }} točk</div>
            </div>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="peer-list">
          <div class="peer-list-header">
            <h3>PRIMERJAVA PO VELIKOSTI PRORAČUNA</h3>
            <h4>Občine z TODO € ali manjšim proračunom</h4>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
              ultrices gravida. Risus commodo viverra maecenas accumsan. lacus
              vel facilisis.
            </p>
          </div>
          <div class="peer-list-elements">
            <div
              v-for="peer in budgetPeers"
              :key="peer.id"
              :class="[
                'peer-list-element',
                { active: municipalityData.id === peer.id },
              ]"
            >
              <div class="name">{{ peer.rank }}. {{ peer.name }}</div>
              <div class="score">{{ Math.round(peer.total_score) }} točk</div>
            </div>
          </div>
        </div>
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
    populationPeers() {
      return (this.municipalityData?.bucket_peers?.population || [])
        .slice()
        .sort((a, b) => b.total_score - a.total_score);
    },
    budgetPeers() {
      return (this.municipalityData?.bucket_peers?.budget || [])
        .slice()
        .sort((a, b) => b.total_score - a.total_score);
    },
  },
};
</script>

<style lang="scss" scoped>
.peer-list {
  margin: 0 auto;
  max-width: 480px;
  border: 1px solid #173d58;

  .peer-list-header {
    padding: 1.5rem 2rem;
    border-bottom: 1px solid #173d58;

    h3 {
      color: #173d58;
      font-size: 20px;
      font-weight: 700;
      font-style: italic;
      margin-bottom: 0.5rem;
    }

    h4 {
      color: #173d58;
      font-size: 16px;
      font-weight: 500;
      margin-bottom: 0.5rem;
    }

    p {
      font-size: 14px;
      font-weight: 300;
      line-height: 1.2;
      margin-bottom: 0;
    }
  }

  .peer-list-elements {
    padding: 0.75rem 1.25rem;
    max-height: 600px;
    overflow: hidden;
    overflow-y: scroll;

    .peer-list-element {
      padding: 1rem 0.75rem 0.75rem 0.75rem;
      font-size: 20px;
      display: flex;
      align-items: center;

      &:not(:last-child) {
        border-bottom: 1px solid #173d58;
      }

      &.active {
        background-color: #ffe4d8;
      }

      .name {
        flex: 1;
      }

      .score {
        flex: 0 0 auto;
        font-weight: 900;
      }
    }
  }
}
</style>
