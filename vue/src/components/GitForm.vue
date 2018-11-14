<template>
  <div class="git-form">
    <div class="git-form__form" v-if="!formSended">
      <form action="#" method="POST" @submit.prevent="submitFormHandler">
        <label class="git-form__label">Github repository path (owner/repository)</label>
        <div class="git-form__main">
          <div class="git-form__input">
            <input
              type="text"
              name="git_path"
              class="field field_main"
              ref="git_path"
              placeholder="maddevsio/heimdall"
              autocomplete="off"
              required
              @input="checkOnInput"
              :class="{'has-error': hasError}"
            >
            <div class="git-form__message" v-show="hasError">Please enter the valid Git repository path</div>
          </div>
          <div class="git-form__button">
            <button type="submit" class="button button_main button_block">Get the badge</button>
          </div>
        </div>
      </form>
    </div>
    <div class="git-form__code" v-else>
      <div class="code-card code-card_main">
        <div class="code-card__title">Place this code to README.md</div>
        <div class="code-card__content" @click="copyPath">
          <code class="code-card__code">
            [![Heimdall Scanner](https://heimdall.maddevs.io/badge/github/{{ badgePath }})](https://heimdall.maddevs.io/report/github/{{ badgePath }})
          </code>
          <div class="code-card__copy">copy code</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'gitForm',
    data: function () {
      return {
        badgePath: '',
        formSended: false,
        isValid: false,
        validPattern: /^([0-9a-zA-Z._-]+)\/([0-9a-zA-Z._-]+)$/i,
        hasError: false,
        realTimeChecking: false
      }
    },
    methods: {
      submitFormHandler () {
        this.validate()

        if (this.isValid) {
          this.sendForm()
        } else {
          this.realTimeChecking = true
        }
      },
      validate () {
        var $input = this.$refs.git_path
        var str = $input.value
        var textIsValid = str.match(this.validPattern)

        this.hasError = false
        this.isValid = true

        if (str.length > 0) {
          if (!textIsValid) {
            this.hasError = true
            this.isValid = false
          }
        } else {
          this.hasError = true
          this.isValid = false
        }
      },
      sendForm () {
        this.badgePath = this.$refs.git_path.value
        this.formSended = true
        this.$emit('path-changed', this.badgePath)
      },
      copyPath (e) {
        var $codeElement = e.target.parentNode.querySelector('code')
        var $link = e.target.parentNode.querySelector('.code-card__copy')

        this.$copyText($codeElement.innerText.trim())
        $link.innerHTML = 'copied'
      },
      checkOnInput () {
        if (this.realTimeChecking) {
          this.validate()
        }
      }
    }
  }
</script>

<style lang="scss">
  .git-form {

    &__label {
      color: #292929;
      font-weight: normal;
      font-size: 16px;
      letter-spacing: 0.03em;
      display: block;
      margin-bottom: 8px;
    }

    &__main {
      display: flex;
      justify-content: space-between;
    }

    &__message {
      margin-top: 8px;
      font-size: 14px;
      color: #CA2228;
    }

    &__input {
      width: 100%;
      max-width: 324px;
      input {
        &.has-error {
          border-color: #CA2228;
        }
      }
    }
  }

  @media only screen and (max-width: 767px) {
    .git-form {
      padding: 0 6px;
      &__label {
        font-size: 13px;
        margin-bottom: 14px;
        letter-spacing: 0.01em;
        font-weight: bold;
      }

      &__main {
        flex-wrap: wrap;
      }

      &__input {
        margin-bottom: 28px;
        max-width: none;
      }

      &__button {
        width: 100%;
      }
    }
  }
</style>
