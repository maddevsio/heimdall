<template>
  <div class="monitor">
    <div class="monitor__wrapper wrapper">
      <div class="monitor__icon">
        <img src="@/assets/img/heimdallicon.svg" alt="HEIMDALL">
      </div>
      <h2 class="monitor__text">
        Monitor the code status
      </h2>
      <div class="monitor__form">
        <git-form @path-changed="changePath($event)"></git-form>
      </div>
    </div>
  </div>
</template>

<script>
  import GitForm from '@/components/GitForm.vue'

  export default {
    name: 'monitor',
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
  .monitor {
    padding: 117px 0 121px;

    &__icon {
      margin-bottom: 24px;
      text-align: center;
    }

    &__text {
      margin: 0 auto 24px;
      text-align: center;
      font-size: 38px;
      max-width: 700px;
    }

    &__form {
      margin: auto;
      max-width: 480px;
    }
  }

  @media only screen and (max-width: 1023px) {
    .monitor {
      padding: 78px 0 84px;
    }
  }

  @media only screen and (max-width: 767px) {
    .monitor {
      padding: 62px 0 89px;
      &__text {
        margin-bottom: 17px;
        padding: 0 8px;
        font-size: 26px;
        line-height: 1.4;
      }
    }
  }

</style>
