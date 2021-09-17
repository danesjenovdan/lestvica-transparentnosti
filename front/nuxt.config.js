const BASE_PATH = '/les-trans-test/';
const FULL_PATH = `https://danesjenovdan.si${BASE_PATH}`;

const PAGE_TITLE = 'Lestvica transparentnosti';
const OG_TITLE = 'Lestvica odprtosti in transparentnosti slovenskih občin';
const OG_DESCRIPTION =
  'Preveri, ali tvoja občina omogoča informiranje o njenem delovanju in vplivanje na njene odločitve.';
const OG_IMAGE = `${FULL_PATH}OG-LESTVICA.png`;

export default {
  target: 'static',
  router: {
    base: BASE_PATH,
  },

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: PAGE_TITLE,
    htmlAttrs: {
      lang: 'sl',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'format-detection', content: 'telephone=no' },
      { property: 'og:site_name', content: PAGE_TITLE },
      { property: 'og:type', content: 'website' },
      { name: 'author', content: 'Danes je nov dan' },
      { name: 'twitter:creator', content: '@danesjenovdan' },
      { name: 'twitter:card', content: 'summary_large_image' },
      {
        hid: 'og-title',
        property: 'og:title',
        content: OG_TITLE,
      },
      {
        hid: 'twitter-title',
        name: 'twitter:title',
        content: OG_TITLE,
      },
      {
        hid: 'description',
        name: 'description',
        content: OG_DESCRIPTION,
      },
      {
        hid: 'og-description',
        property: 'og:description',
        content: OG_DESCRIPTION,
      },
      {
        hid: 'twitter-description',
        name: 'twitter:description',
        content: OG_DESCRIPTION,
      },
      {
        hid: 'og-image',
        property: 'og:image',
        content: OG_IMAGE,
      },
      {
        hid: 'twitter-image',
        name: 'twitter:image',
        content: OG_IMAGE,
      },
    ],
    link: [
      // favicons
      {
        rel: 'icon',
        type: 'image/x-icon',
        href: `${BASE_PATH}/favicon.ico`,
      },
      {
        rel: 'icon',
        type: 'image/png',
        sizes: '32x32',
        href: `${BASE_PATH}/favicon-32x32.png`,
      },
      {
        rel: 'shortcut icon',
        href: `${BASE_PATH}/favicon-32x32.png`,
      },
      {
        rel: 'apple-touch-icon',
        sizes: '512x512',
        href: `${BASE_PATH}/favicon-512x512.png`,
      },
      // fonts
      {
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com',
      },
      {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: true,
      },
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Lexend:wght@300;600&display=swap',
      },
      {
        rel: 'stylesheet',
        href: 'https://use.typekit.net/mdt7xgm.css',
      },
    ],
    script: [
      {
        src: 'https://plausible.lb.djnd.si/js/plausible.js',
        async: true,
        defer: true,
        'data-domain': 'danesjenovdan.si',
      },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~/assets/styles/index.scss'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},

  loading: {
    color: '#ff7a40',
  },
};
