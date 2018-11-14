<template>
  <header class="header">
    <div class="header__wrapper wrapper">
      <div class="header__logo">
        <logo></logo>
      </div>
    </div>
  </header>
</template>

<script>
  import Logo from '@/components/Logo.vue'

  export default {
    name: 'app-header',
    components: {
      'logo': Logo
    }
  }
</script>

<style lang="scss">
  .header {
    padding: 40px 0;

    &__logo {
      text-align: center;
    }
  }

  @media only screen and (max-width: 1023px) {
    .header {
      padding: 30px 30px 30px;
    }
  }

  @media only screen and (max-width: 767px) {
    .header {
      padding: 40px;
    }
  }
</style>
