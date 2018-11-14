<template>
  <div class="advantages">
    <div class="advantages__wrapper wrapper">
      <h2 class="advantages__title">Why do you need Heimdall?</h2>
      <ul class="advantages__list">
        <li class="advantages__item">
          <img src="@/assets/img/security.svg" alt="img" class="advantages__icon">
          <h3 class="advantages__caption">Security monitoring</h3>
          <p class="advantages__text">Keeps track of the <a href="https://mythril.ai/" class="advantages__link" target="_blank">Mythril</a> security reports and display their statuses as a badge in the repository. </p>
        </li>
        <li class="advantages__item">
          <img src="@/assets/img/code.svg" alt="img" class="advantages__icon">
          <h3 class="advantages__caption">Registry of the repositories</h3>
          <p class="advantages__text">Allows you to add the repository into the <a href="https://github.com/maddevsio/heimdall" class="advantages__link" target="_blank">Heimdall</a> registry that it is monitoring and reporting about</p>
        </li>
        <li class="advantages__item">
          <img src="@/assets/img/docs.svg" alt="img" class="advantages__icon">
          <h3 class="advantages__caption">Report display </h3>
          <p class="advantages__text">Heimdall does not generate reports but presents Mythril <a href="https://heimdall.maddevs.io/report/github/maddevsio/heimdall" class="advantages__link" target="_blank">report</a> in a nice and convenient way</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'advantages'
  }
</script>

<style lang="scss">
  .advantages {
    padding: 116px 0 60px;

    &__link {
      color: #6732ff;
      text-decoration: none;
      &:hover {
        text-decoration: underline;
      }
    }

    &__title {
      margin: 0;
      margin-bottom: 40px;
      font-size: 38px;
      line-height: 1.42;
      color: #292929;
      text-align: center;
      font-weight: bold;
    }

    &__list {
      padding: 0;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      width: 100%;
      max-width: 1100px;
    }

    &__item {
      list-style: none;
      padding: 0;
      margin: 0;
      width: 100%;
      max-width: 310px;
      text-align: center;
    }

    &__icon {
      margin-bottom: 34px;
    }

    &__caption {
      margin: 0;
      margin-bottom: 7px;
      font-size: 22px;
    }

    &__text {
      margin: 0;
      padding: 0 16px;
    }
  }

  @media only screen and (max-width: 1439px) {
    .advantages {
      &__list {
        max-width: 930px;
      }
    }
  }

  @media only screen and (max-width: 1023px) {
    .advantages {
      padding: 100px 0 70px;
      &__title {
        letter-spacing: -0.02em;
      }
      &__caption {
        line-height: 1.2;
      }
    }
  }

  @media only screen and (max-width: 767px) {
    .advantages {
      padding: 31px 10px;
      &__title {
        font-size: 26px;
      }
      &__list {
        max-width: 300px;
        flex-wrap: wrap;
      }
      &__item {
        margin-bottom: 49px;
      }
      &__icon {
        margin-bottom: 16px;
      }
      &__caption {
        font-size: 18px;
      }
      &__text {
        padding: 0;
      }
    }
  }
</style>
