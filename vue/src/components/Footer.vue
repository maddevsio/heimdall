<template>
  <footer class="footer">
    <div class="footer__wrapper wrapper">
      <div class="footer__top">
        <div class="footer__card">
          <div class="dev-card">
            <div class="dev-card__title">GitHub and Mythril are <br> connected by Mad Devs</div>
            <div class="dev-card__icon">
              <img src="@/assets/img/m-dlogo.svg" alt="Mad Mevs">
            </div>
            <div class="dev-card__link">
              <a href="https://maddevs.io/" target="_blank">https://maddevs.io/</a>
            </div>
          </div>
        </div>
        <div class="footer__card">
          <div class="dev-card">
            <div class="dev-card__title">All the magic happened <br> thanks to Mythril</div>
            <div class="dev-card__icon">
              <img src="@/assets/img/mythril-logo.svg" alt="Mythril">
            </div>
            <div class="dev-card__link">
              <a href="https://mythril.ai/" target="_blank">https://mythril.ai/</a>
            </div>
          </div>
        </div>
      </div>
      <div class="footer__bottom">
        <div class="footer__text">To express gratitude or to get consultation or assistance in the system implementation write to <a href="mailto:rock@maddevs.io">rock@maddevs.io</a></div>
        <div class="footer__social">
          <ul class="social-main">
            <li class="social-main__item">
              <a href="https://github.com/maddevsio" target="_blank">
                <img src="@/assets/img/git.svg" alt="GitHub">
              </a>
            </li>
            <li class="social-main__item">
              <a href="https://www.instagram.com/maddevsio/" target="_blank">
                <img src="@/assets/img/insta.svg" alt="Instagram">
              </a>
            </li>
            <li class="social-main__item">
              <a href="https://twitter.com/MadDevsIO" target="_blank">
                <img src="@/assets/img/tw.svg" alt="Twitter">
              </a>
            </li>
            <li class="social-main__item">
              <a href="https://blog.maddevs.io/" target="_blank">
                <img src="@/assets/img/medium.svg" alt="Medium">
              </a>
            </li>
            <li class="social-main__item">
              <a href="https://t.me/maddevsio" target="_blank">
                <img src="@/assets/img/telek.svg" alt="Telegram">
              </a>
            </li>
            <li class="social-main__item">
              <a href="https://www.slideshare.net/maddevs/presentations" target="_blank">
                <img src="@/assets/img/pres.svg" alt="Pres">
              </a>
            </li>
            <li class="social-main__item">
              <a href="https://www.youtube.com/playlist?list=PLsmdb5W8ytypyXt1ut3lfBOnOZnDNqYIN" target="_blank">
                <img src="@/assets/img/you.svg" alt="YouTube">
              </a>
            </li>
            <li class="social-main__item">
              <a href="https://www.facebook.com/maddevsio" target="_blank">
                <img src="@/assets/img/fb.svg" alt="Facebook">
              </a>
            </li>
          </ul>
        </div>
        <div class="footer__copyright">© Mad Devs <i class="icon-rock"></i>, 2018</div>
      </div>
    </div>
  </footer>
</template>

<script>
  export default {
    name: 'app-footer'
  }
</script>

<style lang="scss">
  .footer {
    padding: 120px 0 17px;
    text-align: center;

    &__top {
      margin: auto;
      width: 100%;
      max-width: 1048px;
      padding-left: 80px;
      display: flex;
      justify-content: space-between;
      margin-bottom: 90px;
    }

    &__card {

    }

    &__bottom {

    }

    &__text {
      margin: auto;
      margin-bottom: 43px;
      width: 100%;
      max-width: 440px;
      letter-spacing: -0.01em;

      a {
        color: #6732ff;
        &:hover {
          text-decoration: underline;
        }
      }
    }

    &__social {
      margin-bottom: 79px;
    }

    &__copyright {

    }
  }

  .dev-card {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;

    &__title {
      font-size: 22px;
      margin-bottom: 46px;
      font-weight: bold;
    }

    &__icon {
      margin-bottom: 48px;
    }

    &__link {
      font-size: 14px;
      text-decoration: none;
      color: #6732ff;
      &:hover {
        text-decoration: underline;
      }
      a {
        &::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          z-index: 6;
          width: 100%;
          height: 100%;
        }
      }
    }
  }

  .social-main {
    padding-right: 36px;

    &__item {
      display: inline-block;
      margin: 0 18px;
      &:hover {
        opacity: 0.75;
      }
      img {
        width: 28px;
      }
    }
  }

  .icon-rock {
    display: inline-block;
    vertical-align: middle;
    margin-top: -4px;
    width: 24px;
    height: 24px;
    background: transparent url('../assets/img/gvnr-sign.png') 0 0 no-repeat;
    background-size: 100% 100%;
  }

  @media only screen and (max-width: 1439px) {
    .footer {
      &__top {
        max-width: 828px;
        padding-left: 38px;
      }
    }
  }

  @media only screen and (max-width: 1023px) {
    .footer {
      padding: 83px 0 17px;
      &__top {
        max-width: 708px;
        padding-left: 26px;
      }
    }

    .dev-card {
      &__icon {
        max-width: 340px;
      }
    }
  }

  @media only screen and (max-width: 767px) {
    .footer {
      padding: 60px 0 17px;
      &__top {
        flex-direction: column;
        padding-left: 0;
        margin-bottom: 20px;
      }
      &__card {
        margin-bottom: 56px;
      }
      &__text {
        padding: 0 10px;
      }

      &__social {
        margin: auto;
        margin-bottom: 35px;
        max-width: 300px;
      }

      &__copyright {
        font-size: 14px;
      }
    }

    .dev-card {
      &__title {
        margin-bottom: 30px;
      }
      &__icon {
        max-width: 240px;
        margin: auto;
        margin-bottom: 42px;
      }
    }

    .social-main {
      margin: 0;
      padding: 0;
      padding-right: 0;
      display: flex;
      justify-content: space-between;

      &__item {
        margin: initial;
      }
    }

  }
</style>
