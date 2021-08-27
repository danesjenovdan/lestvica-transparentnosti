<template>
  <div v-click-outside="() => (open = false)">
    <button class="toc-button" type="button" @click.prevent="open = !open">
      <div class="text">KAZALO</div>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="5.7 2.5 88.6 95">
        <path
          d="M5273.1 2400.1v-2c0-2.8-5-4-9.7-4s-9.7 1.3-9.7 4v2c0 1.8.7 3.6 2 4.9l5 4.9c.3.3.4.6.4 1v6.4c0 .4.2.7.6.8l2.9.9c.5.1 1-.2 1-.8v-7.2c0-.4.2-.7.4-1l5.1-5c1.3-1.3 2-3.1 2-4.9zm-9.7-.1c-4.8 0-7.4-1.3-7.5-1.8.1-.5 2.7-1.8 7.5-1.8s7.3 1.3 7.5 1.8c-.2.5-2.7 1.8-7.5 1.8z"
        />
        <path
          d="M5268.4 2410.3c-.6 0-1 .4-1 1s.4 1 1 1h4.3c.6 0 1-.4 1-1s-.4-1-1-1h-4.3zm4.3 3.4h-4.3c-.6 0-1 .4-1 1s.4 1 1 1h4.3c.6 0 1-.4 1-1s-.4-1-1-1zm0 3.3h-4.3c-.6 0-1 .4-1 1s.4 1 1 1h4.3c.6 0 1-.4 1-1 0-.5-.4-1-1-1zM89.8 2.5H10.2c-2.5 0-4.5 2-4.5 4.5v86c0 2.5 2 4.5 4.5 4.5h66.6c2.5 0 4.5-2 4.5-4.5V76.2h8.5c2.5 0 4.5-2 4.5-4.5V7c.1-2.5-2-4.5-4.5-4.5zM63.1 81.6H23.8a2.9 2.9 0 010-5.8H63c1.6 0 2.9 1.3 2.9 2.9.1 1.6-1.2 2.9-2.8 2.9zm0-19.1H23.8a2.9 2.9 0 010-5.8H63c1.6 0 2.9 1.3 2.9 2.9.1 1.6-1.2 2.9-2.8 2.9zm0-19.2H23.8a2.9 2.9 0 010-5.8H63c1.6 0 2.9 1.3 2.9 2.9s-1.2 2.9-2.8 2.9zm0-19.1H23.8a2.9 2.9 0 010-5.8H63c1.6 0 2.9 1.3 2.9 2.9.1 1.6-1.2 2.9-2.8 2.9zm25.5 46.2h-7.3V59.2h7.3v11.2zm0-16.9h-7.3V42.2h7.3v11.3zm0-17h-7.3V25.3h7.3v11.2zm-7.3-17V8.3h7.3v11.2h-7.3z"
        />
      </svg>
    </button>
    <div class="toc-wrapper">
      <nav v-if="open" class="toc">
        <ul>
          <li>
            <a href="#">
              <em>UVOD</em>
              Ali je delovanje slovenskih občin na spletu predstavljeno
              transparentno in dostopno?
            </a>
          </li>
          <li>
            <a href="#">
              <em>LESTVICA TRANSPARENTNOSTI IN DOSTOPNOSTI</em>
              Preveri ocene vseh občin
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
import ClickOutside from 'vue-click-outside';

export default {
  directives: {
    ClickOutside,
  },
  data() {
    return {
      open: false,
    };
  },
};
</script>

<style lang="scss" scoped>
button.toc-button {
  display: flex;
  align-items: center;
  border: none;
  background: #64bca7;
  padding: 0.5rem 1rem;
  font-size: 16px;
  font-weight: 500;
  color: #173d58;

  &:hover,
  &:focus {
    background-color: #a9d8ce;
  }

  .text {
    margin-top: 0.2em;
    color: #000;
  }

  svg {
    width: 24px;
    height: 24px;
    margin-left: 1rem;
  }
}

.toc-wrapper {
  position: relative;

  nav.toc {
    position: absolute;
    top: 0;
    right: 0;
    z-index: 1000;
    background-color: #a9d8ce;
    padding: 2rem 3rem;
    width: 450px;

    ul {
      &,
      li {
        list-style: none;
        margin: 0;
        padding: 0;
      }

      li {
        &:not(:last-child) {
          margin-bottom: 1rem;
          padding-bottom: 1rem;
          border-bottom: 1px solid #000;
        }

        a {
          display: block;
          color: #000;
          font-size: 16px;
          font-weight: 500;
          line-height: 1.4;
          text-decoration: none;

          em {
            display: block;
            font-size: 20px;
            font-weight: 900;
            font-style: italic;
            line-height: 1.2;
          }
        }
      }
    }
  }
}
</style>
