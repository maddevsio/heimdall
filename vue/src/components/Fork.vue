<template>
  <div class="fork">
    <div class="fork__bridge">
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
      <div class="fork__line"></div>
    </div>
    <div class="fork__wrapper wrapper">
      <div class="fork__icon">
        <img src="@/assets/img/bridge.svg" alt="img">
      </div>
      <h2 class="fork__title">Free and reliable solution</h2>
      <p class="fork__text">Heimdall is the open source Security Monitoring tool for Ethereum Smart Contracts</p>
      <div class="fork__link">
        <a href="https://github.com/maddevsio/heimdall" class="button button_alt" target="_blank">
          <span class="button__icon">
            <img src="@/assets/img/git.svg" alt="img">
          </span>
          <span class="button__text">
            Fork me on Github
          </span>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'fork'
  }
</script>

<style lang="scss">
  .fork {
    position: relative;
    padding: 66px 0 60px;
    text-align: center;
    color: #fff;
    background-color: #6732ff;

    &__icon {
      margin-bottom: 28px;
    }

    &__title {
      margin: 0;
      font-weight: bold;
      font-size: 37px;
      margin-bottom: 10px;
    }

    &__text {
      margin: 0;
      font-size: 16px;
      margin-bottom: 28px;
      letter-spacing: 0.01em;
    }

    &__wrapper {
      position: relative;
      z-index: 8;
    }


    &__bridge {
      position: absolute;
      z-index: 1;
      top: 8px;
      left: 0;
      right: 0;
    }

    &__line {
      height: 8px;
      margin-bottom: 16px;

      &:nth-child(odd) {
        background: transparent url('../assets/img/lines/purpule-box/line-top.svg') 0 0 repeat-x;
        animation: bridgeLine1 30s linear 0s infinite;
      }

      &:nth-child(even) {
        background: transparent url('../assets/img/lines/purpule-box/line-bottom.svg') 0 0 repeat-x;
        animation: bridgeLine1 30s linear 0s infinite;
      }

      &:nth-child(1) {
        animation-delay: -1s;
      }

      &:nth-child(2) {
        animation-delay: -1s;
        animation-duration: 25s;
      }

      &:nth-child(3) {
        animation-delay: -1s;
        animation-duration: 18s;
      }

      &:nth-child(4) {
        animation-delay: -4s;
        animation-duration: 23s;
      }

      &:nth-child(5) {
        animation-delay: -2.5s;
        animation-duration: 17s;
      }

      &:nth-child(6) {
        animation-delay: -7s;
        animation-duration: 22s;
      }

      &:nth-child(7) {
        animation-delay: -5.6s;
        animation-duration: 27s;
      }

      &:nth-child(8) {
        animation-duration: 18s;
      }

      &:nth-child(9) {
        animation-delay: -12s;
        animation-duration: 19.5s;
      }

      &:nth-child(10) {
        animation-delay: -13s;
        animation-duration: 27s;
      }

      &:nth-child(11) {
        animation-delay: -9s;
        animation-duration: 27s;
      }

      &:nth-child(12) {
        animation-delay: -1s;
        animation-duration: 30s;
      }

      &:nth-child(13) {
        animation-delay: -16s;
        animation-duration: 27s;
      }

      &:nth-child(14) {
        animation-delay: -10s;
        animation-duration: 25s;
      }

      &:nth-child(15) {
        animation-delay: -12s;
        animation-duration: 22s;
      }

      &:nth-child(16) {
        animation-delay: -1.5s;
        animation-duration: 16s;
      }
    }
  }

  @media only screen and (max-width: 767px) {
    .fork {
      padding: 40px 0 49px;

      &__icon {
        margin-bottom: 32px;
      }

      &__title {
        font-size: 26px;
        margin-bottom: 16px;
        padding: 0 10px;
      }
    }
  }


  @keyframes forkLine1 {
    from {
      background-position: 0 0;
    }

    to {
      background-position: 1286px 0;
    }
  }
</style>
