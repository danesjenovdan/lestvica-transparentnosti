<template>
  <div
    :class="[
      'search-field',
      `search-field--${size}`,
      { 'search-field--dark': dark },
    ]"
  >
    <autocomplete
      ref="autocomplete"
      :search="search"
      :get-result-value="getResultValue"
      :default-value="''"
      :placeholder="placeholder != null ? placeholder : 'Poišči občino'"
      @submit="onSubmit"
    />
    <button v-if="showButton" type="button" @click="onSubmit">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="1.99 2 27.69 27.67">
        <path
          d="M29.13 25.28L24 20.18a2 2 0 00-2.58-.18l-1.68-1.68A10 10 0 1012 22a9.89 9.89 0 006.33-2.26L20 21.42a2 2 0 00.18 2.58l5.1 5.09a2 2 0 002.82 0l1-1a2 2 0 000-2.82zM6.34 17.66A8 8 0 1112 20a8 8 0 01-5.66-2.34zm20.35 10.06l-5.1-5.1 1-1 5.1 5.1z"
        />
      </svg>
    </button>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Autocomplete from '@trevoreyre/autocomplete-vue';

export default {
  components: {
    Autocomplete,
  },
  props: {
    size: {
      type: String,
      default: 'regular',
    },
    showButton: {
      type: Boolean,
      default: false,
    },
    dark: {
      type: Boolean,
      default: false,
    },
    placeholder: {
      type: String,
      default: null,
    },
    onClear: {
      type: Function,
      default: null,
    },
    onSelect: {
      type: Function,
      default: null,
    },
  },
  data() {
    return {
      lastInput: '',
    };
  },
  computed: {
    ...mapState(['municipalitiesList', 'municipalityData']),
    municipalities() {
      return (this.municipalitiesList || [])
        .slice()
        .sort((a, b) => a.name.toLowerCase().localeCompare(b.name, 'sl'));
    },
  },
  methods: {
    search(input) {
      this.lastInput = input;
      if (!input?.length && this.onClear) {
        this.onClear();
      }
      if (input.length < 2) {
        return [];
      }
      return this.municipalities.filter((m) =>
        m.name.toLowerCase().includes(input.toLowerCase())
      );
    },
    getResultValue(value) {
      return value.name;
    },
    onSubmit(value) {
      if (!value && this.lastInput?.length) {
        const input = this.lastInput.toLowerCase().trim();
        value = this.municipalities.find(
          (m) => m.name.toLowerCase().trim() === input
        );
      }
      if (!value) {
        return;
      }
      if (this.onSelect) {
        this.onSelect(value);
        return;
      }
      this.$router.push(`/obcina/${value.id}/`);
    },
  },
};
</script>

<style lang="scss" scoped>
@import '~/assets/styles/breakpoints';

.search-field {
  width: 250px;
  position: relative;
  text-align: left;
  z-index: 10;

  &.search-field--large {
    width: 450px;

    @include media-breakpoint-down(md) {
      width: auto;
    }
  }

  &.search-field--dark {
    button {
      color: #173d58;
    }
  }

  button {
    background: none;
    border: none;
    width: 40px;
    height: 40px;
    position: absolute;
    top: 2px;
    right: 0;
    color: #fff;
  }
}

.search-field ::v-deep {
  .autocomplete-input {
    width: 100%;
    border: none;
    background: transparent;
    color: #fff;
    font-size: 16px;
    font-weight: 300;
    line-height: 2;
    border-bottom: 1px solid #fff;
    padding: 0.125em 0.5em 0;

    &::placeholder {
      color: #fff;
    }

    &:focus {
      outline: none;
      background-color: rgba(#fff, 0.15);

      &::placeholder {
        opacity: 0.5;
      }
    }
  }

  .autocomplete-result-list {
    list-style: none;
    margin: -1px 0 0 0;
    padding: 0;
    max-height: 300px;
    overflow-y: auto;
    background-color: #fff;
    border: 1px solid #fff;

    .autocomplete-result {
      cursor: default;
      margin: 0;
      padding: 0.7em 0.5em 0.5em 0.5em;
      font-weight: 300;

      &:not(:last-child) {
        border-bottom: 1px solid #173d58;
      }

      &:hover,
      &[aria-selected='true'] {
        background-color: #ffe4d8;
      }
    }
  }
}

.search-field.search-field--large ::v-deep {
  .autocomplete-input {
    font-size: 20px;
    font-style: italic;
    border-bottom: 2px solid #fff;
  }
}

.search-field.search-field--dark ::v-deep {
  .autocomplete-input {
    color: #000;
    border-bottom-color: #173d58;

    &::placeholder {
      color: #000;
    }
  }

  .autocomplete-result-list {
    border-color: #173d58;
  }
}
</style>
