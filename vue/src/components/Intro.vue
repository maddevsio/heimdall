<template>
  <div class="intro">
    <div class="intro__wrapper wrapper">
      <h1 class="intro__text">
        Ethereum Smart Contracts Security Monitoring
      </h1>
      <div class="intro__form">
        <git-form @path-changed="changePath($event)"></git-form>
      </div>
    </div>
  </div>
</template>

<script>
  import GitForm from '@/components/GitForm.vue'

  export default {
    name: 'intro',
    components: {
      'git-form': GitForm
    },
    methods: {
      changePath: function (e) {
        this.$emit('path-changed', e)
      }
    }
  }
</script>

<style lang="scss">
  .intro {
    padding: 52px 0;

    &__text {
      margin: 0 auto 40px;
      text-align: center;
      font-size: 46px;
      max-width: 700px;
    }

    &__form {
      margin: auto;
      max-width: 480px;
    }
  }

  @media only screen and (max-width: 1023px) {
    .intro {
      &__text {
        margin-bottom: 48px;
        line-height: 1.3;
      }
    }
  }

  @media only screen and (max-width: 767px) {
    .intro {
      padding: 6px 0;
      &__text {
        margin-bottom: 36px;
        font-size: 29px;
        line-height: 1.45;
      }
    }
  }

</style>
