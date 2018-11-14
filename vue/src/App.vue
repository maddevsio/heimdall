<template>
  <div class="page" id="app">
    <div class="page__header">
      <app-header></app-header>
    </div>
    <div class="page__main">
      <router-view></router-view>
    </div>
    <div class="page__footer">
      <app-footer></app-footer>
    </div>
  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import Footer from '@/components/Footer.vue'

  export default {
    name: 'app',
    components: {
      'app-header': Header,
      'app-footer': Footer
    }
  }
</script>

<style lang="scss">
    // Variables
    $large: 1440px;
    $desktop: 1024px;
    $tablet: 768px;
    $mobile: 320px;

    // Reset
    html,
    body {
      margin: 0;
      height: 100%;
    }

    *,
    *::before,
    *::after {
      box-sizing: border-box;
      outline: none;
    }

    img {
      -webkit-user-select: none;
      -moz-user-select: none;
      display: inline-block;
      vertical-align: top;
      border: none;
      max-width: 100%;
    }

    a {
      color: inherit;
      text-decoration: inherit;
    }

    // Fonts
    @font-face {
      font-family: 'sfui';
      src: url('/assets/fonts/sfui/SFUIDisplay-Regular.otf');
    }

    @font-face {
      font-family: 'sfui';
      src: url('/assets/fonts/sfui/SFUIDisplay-Medium.otf');
      font-weight: 500;
    }

    @font-face {
      font-family: 'sfui';
      src: url('/assets/fonts/sfui/SFUIDisplay-Bold.otf');
      font-weight: bold;
    }

    @import url('https://fonts.googleapis.com/css?family=Fira+Mono');

    // Main
    body {
      font-family: 'sfui', sans-serif;
      font-size: 16px;
      line-height: 1.4;
      color: #292929;
    }

    .page {
      height: 100%;
      display: flex;
      flex-direction: column;

      &__main {
        flex-grow: 1;
      }
    }

    .wrapper {
      width: 100%;
      padding: 0 10px;
      max-width: 1440px;
      margin: 0 auto;
    }

    // Button
    .button {
      padding: 0;
      margin: 0;
      display: inline-block;
      background: none;
      border: none;
      box-shadow: none;
      text-align: center;
      cursor: pointer;
      font-size: inherit;

      padding: 12px 20px;
      background-color: #000;
      color: #fff;

      &_block {
        display: block;
        width: 100%;
      }

      &_main {
        padding: 11px 21px;
        background-color: #6732ff;
        border-radius: 3px;
        font-weight: bold;
        font-size: 15px;
        letter-spacing: -0.01em;
        &:hover {
          background-color: #7E52FF;
        }
        &:active{
          background-color: #5228CC;
        }
      }

      &_alt {
        padding: 11px 21px;
        background-color: #fff;
        color: #292929;
        border-radius: 3px;
        font-weight: bold;
        font-size: 15px;
        letter-spacing: -0.01em;
        &:hover {
          background-color: #F6F8FA;
        }
        &:active {
          background-color: #F2EEFF;
        }
      }

      &__text,
      &__icon {
        display: inline-block;
        vertical-align: middle;
      }

      &__text + &__icon,
      &__icon + &__text {
        margin-left: 8px;
      }
    }

    // Field
    .field {
      padding: 11px 19px;
      margin: 0;
      display: block;
      width: 100%;
      background: none;
      background-color: #fff;
      border: 1px solid #000;
      box-shadow: none;
      color: #000;
      font-size: inherit;

      &::-webkit-input-placeholder {
        opacity: 1;
        color: inherit;
      }

      &::-moz-placeholder {
        opacity: 1;
        color: inherit;
      }

      &:-ms-input-placeholder {
        opacity: 1;
        color: inherit;
      }

      &_main {
        padding: 9px 9px 10px;
        color: #292929;
        border: 1px solid #ccc;
        border-radius: 3px;

        &::-webkit-input-placeholder {
          color: #ccc;
        }

        &::-moz-placeholder {
          color: #ccc;
        }

        &:-ms-input-placeholder {
          color: #ccc;
        }

        &:hover {
          border-color: #B398FF;
        }

        &:active {
          border-color: #BBBBBB;
        }
      }
    }

  .code-card {

    &_main {
      .code-card__title {
        font-size: 16px;
      }
    }

    &__title {
      font-weight: bold;
      font-size: 22px;
      margin-bottom: 10px;
    }

    &__code {
      border-radius: 3px;
      padding: 25px 17px;
      font-family: 'Fira Mono', sans-serif;
      font-weight: normal;
      display: block;
      background-color: #edf2f6;
      font-size: 16px;
      color: #2f1010;
      border-left: 4px solid rgba(0, 0, 0, 0.03);
      letter-spacing: 0.027em;
      line-height: 1.5;
      transition: border-color 200ms ease-in-out 0ms;
      word-break: break-all;
    }

    &__content {
      position: relative;
      cursor: pointer;
      &:hover {
        .code-card__copy {
          opacity: 1;
        }
        .code-card__code {
          border-left-color: #6732ff;
        }
      }
    }

    &__copy {
      margin-top: 10px;
      display: inline-block;
      color: #6732ff;
      font-size: 12px;
      cursor: pointer;
      transition: opacity 200ms ease-in-out 0ms;
      opacity: 0;
      -webkit-user-select: none;
      -moz-user-select: none;

      &::before {
        content: '';
        display: inline-block;
        vertical-align: middle;
        margin-top: -2px;
        margin-right: 8px;
        height: 14px;
        width: 14px;
        background: transparent url('./assets/img/copy-icon-purpule.svg') 0 0 no-repeat;
        background-size: 14px 14px;
      }
    }
    &__marked {
      color: #6732ff;
    }
    &__label {
      margin: 16px 0;
      font-weight: bold;
    }
  }

  @media only screen and (max-width: 767px) {
    .code-card {
      &__title {
        font-size: 18px;
        padding-left: 40px;
      }
    }
  }
</style>
