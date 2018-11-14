<template>
  <div class="jumbo">
    <div class="jumbo__bridge">
      <div class="jumbo__line"></div>
      <div class="jumbo__line"></div>
      <div class="jumbo__line"></div>
      <div class="jumbo__line"></div>
      <div class="jumbo__line"></div>
    </div>
    <img class="jumbo__image" src="@/assets/img/browser@2x.png" alt="img">
  </div>
</template>

<script>
  export default {
    name: 'jumbo'
  }
</script>

<style lang="scss">
  .jumbo {
    position: relative;
    padding: 60px 0;
    text-align: center;

    &__bridge {
      position: absolute;
      z-index: 0;
      top: 39.3%;
      left: 0;
      right: 0;
    }

    &__line {
      height: 14px;
      margin-bottom: 18px;

      &:nth-child(1) {
        background: transparent url('../assets/img/lines/browser-bg/line1.svg') 0 0 repeat-x;
        animation: bridgeLine1 90s linear 0s infinite;
      }

      &:nth-child(2) {
        background: transparent url('../assets/img/lines/browser-bg/line2.svg') 0 0 repeat-x;
        animation: bridgeLine2 85s linear 0s infinite;
      }

      &:nth-child(3) {
        background: transparent url('../assets/img/lines/browser-bg/line3.svg') 0 0 repeat-x;
        animation: bridgeLine3 85s linear 0s infinite;
      }

      &:nth-child(4) {
        background: transparent url('../assets/img/lines/browser-bg/line4.svg') 0 0 repeat-x;
        animation: bridgeLine4 87s linear 0s infinite;
      }

      &:nth-child(5) {
        background: transparent url('../assets/img/lines/browser-bg/line5.svg') 0 0 repeat-x;
        animation: bridgeLine5 100s linear 0s infinite;
      }

      img {
        display: block;
      }
    }

    &__image {
      position: relative;
      z-index: 8;
      width: 900px;
      display: inline-block;
    }
  }

  @media only screen and (max-width: 1023px) {
    .jumbo {
      padding: 40px 15px;
    }
  }

  @media only screen and (max-width: 767px) {
    .jumbo {
      padding: 72px 10px 40px;

      &__bridge {
        top: 29.3%
      }

    }
  }

  @keyframes bridgeLine1 {
    from {
      background-position: 0 0;
    }

    to {
      background-position: 1286px 0;
    }
  }

  @keyframes bridgeLine2 {
    from {
      background-position: 0 0;
    }

    to {
      background-position: 1422px 0;
    }
  }

  @keyframes bridgeLine3 {
    from {
      background-position: -480px 0;
    }

    to {
      background-position: 960px 0;
    }
  }

  @keyframes bridgeLine4 {
    from {
      background-position: -100px 0;
    }

    to {
      background-position: 1282px 0;
    }
  }

  @keyframes bridgeLine5 {
    from {
      background-position: 0 0;
    }

    to {
      background-position: 1440px 0;
    }
  }
</style>
