<template>
  <div class="code">
    <div class="code__wrapper wrapper">
      <div class="code__inner">
        <div class="code__head">
          <div class="code-tabs" :class="{'is-operations': operationsIsActive}">
            <div class="code-tabs__top">
              <div class="code-tabs__left" @click="operationsIsActive = true">Operations</div>
              <div class="code-tabs__right" @click="operationsIsActive = false">Delivery</div>
            </div>
          </div>
        </div>
        <div class="code__intro" v-show="operationsIsActive">
          Follow next steps for getting Heimdall badge:
        </div>
        <div class="code__main" v-if="operationsIsActive">
          <ol class="code__list">
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Badge URL</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    https://heimdall.maddevs.io/badge/github/{{ badgePath }}
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Report URL</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    https://heimdall.maddevs.io/report/github/{{ badgePath }}
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Markdown badge</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    [![Heimdall Scanner](https://heimdall.maddevs.io/badge/github/{{ badgePath }})](https://heimdall.maddevs.io/report/github/{{ badgePath }})
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">HTML badge</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    &lt;a href="https://heimdall.maddevs.io/report/github/{{ badgePath }}"&gt;
                    <br>
                      &nbsp;&nbsp;&nbsp;&nbsp;&lt;img src="https://heimdall.maddevs.io/badge/github/{{ badgePath }}"&gt;
                    <br>
                    &lt;/a&gt;
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
          </ol>
        </div>
        <div class="code__main" v-else>
          <ol class="code__list">
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Install mythril via pypi <span class="code-card__marked">Mythril</span> require additional setup doc from mythril source code:</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    Whenever you disassemble or analyze binary code, Mythril will try to
                    resolve function names using its local signature database. The database
                    must be provided at ``~/.mythril/signatures.json``. You can start out
                    with the `default file &lt;signatures.json&gt;`__ as follows:
                    <br>
                    ::
                    <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;$ cd ~/.mythril
                    <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;$ wget https://raw.githubusercontent.com/b-mueller/mythril/master/signatures.json
                    <br>
                    ::
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Install project dependencies:</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    $ pip install -r requirements.txt
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Go to project scanner dir</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    $ cd scanner
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Create github personal token:</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    <span class="code-card__marked">https://github.com/settings/tokens</span>
                  </code>
                  <div class="code-card__copy">copy link</div>
                </div>
              </div>
            </li>
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Setup firebase connection:</div>
                <div class="code-card__content" @click="copyCode">
                  <div class="code-card__label">FIREBASE_CERTIFICATE</div>
                  <code class="code-card__code">
                    Take certificate from Project Settings -> Service account -> Generate new private key
                    <br>
                    Place this certificate inside project root.
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
                <div class="code-card__label">FIREBASE_DATABASE</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    Take certificate from Project Settings -> Service account -> Generate new private key
                    <br>
                    Place this certificate inside project root.
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
            <li class="code__item">
              <div class="code-card">
                <div class="code-card__title">Run ginicorn:</div>
                <div class="code-card__content" @click="copyCode">
                  <code class="code-card__code">
                    $ gunicorn main:run --bind localhost:8000 --worker-class aiohttp.GunicornWebWorker -e GITHUB_TOKEN=&lt;token_here&gt; -e FIREBASE_CERTIFICATE=&lt;FIREBASE_CERTIFICATE_PATH&gt; -e FIREBASE_DATABASE=&lt;FIREBASE_DATABASE&gt; -t 200 --reload
                  </code>
                  <div class="code-card__copy">copy code</div>
                </div>
              </div>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'block-code',
    data: function () {
      return {
        operationsIsActive: true
      }
    },
    props: [
      'badgePath'
    ],
    methods: {
      copyCode (e) {
        var $codeElement = e.target.parentNode.querySelector('code')
        var $link = e.target.parentNode.querySelector('.code-card__copy')

        this.$copyText($codeElement.innerText.trim())
        $link.innerHTML = 'copied'
      }
    }
  }
</script>

<style lang="scss">
  .code {
    position: relative;

    &__inner {
      position: relative;
      z-index: 3;
    }

    &__wrapper {
      position: relative;
      overflow: hidden;
      padding: 64px 10px 40px;
      background-color: #f6f8fa;

      &::before,
      &::after {
        content: '';
        display: block;
        position: absolute;
        z-index: 1;
        width: 500px;
        height: 130px;
        background: transparent url('../assets/img/lines.svg') 0 0 no-repeat;
        opacity: 0.1;
      }

      &::before {
        top: 64px;
        right: -140px;
      }

      &::after {
        background-position: right top;
        bottom: 64px;
        left: -140px;
      }
    }

    &__head {
      text-align: center;
      margin-bottom: 10px;
    }

    &__intro {
      text-align: center;
      margin-bottom: 32px;
      font-size: 18px;
    }

    &__main {
      margin-bottom: 20px;
    }

    &__main {
      width: 100%;
      max-width: 480px;
      margin: auto;
    }

    &__item {
      list-style: none;
      padding: 0;
      margin: 0;
      margin-left: -40px;
      margin-bottom: 54px;
      position: relative;
      counter-increment: section;
      &::before {
        content: counters(section, '.', decimal-leading-zero) '.';
        position: absolute;
        top: -3px;
        left: -56px;
        z-index: 4;
        font-size: 22px;
        color: #6732ff;
        font-weight: bold;
      }
      &:last-child {
        margin-bottom: 0;
      }
    }
  }

  .code-tabs {
    display: inline-block;
    font-weight: bold;

    &__left {
      position: relative;
      display: inline-block;
      vertical-align: middle;
      padding-right: 80px;
      margin-right: 10px;
      font-size: 22px;
      color: #6732ff;
      cursor: pointer;
      &::after {
        content: '⟶';
        position: absolute;
        top: 0;
        bottom: 0;
        margin: auto;
        right: 10px;
        z-index: 3;
        color: #292929;
        font-size: 22px;
        height: 30px;
      }
    }

    &__right {
      display: inline-block;
      vertical-align: middle;
      font-size: 36px;
    }

    &.is-operations {
      .code-tabs__left {
        font-size: 36px;
        color: #292929;
        cursor: inherit;
        &::after {
          content: '⟵';
        }
      }

      .code-tabs__right {
        font-size: 22px;
        color: #6732ff;
        cursor: pointer;
      }
    }
  }

  @media only screen and (max-width: 1023px) {
    .code {
      &__wrapper {
        &::before,
        &::after {
          display: none;
        }
      }
    }
  }

  @media only screen and (max-width: 767px) {
    .code {
      &__intro {
        padding: 0 20px;
      }

      &__item {
        &::before {
          font-size: 18px;
          top: 0;
          left: 0;
          z-index: 4;
        }
      }

      &__bottom {
        font-size: 14px;
        padding: 18px;
      }

    }

    .code-tabs {
      &__left {
        font-size: 18px;
        padding-right: 50px;
        margin-right: 0;
      }

      &__right {
        font-size: 24px;
      }

      &.is-operations {
        .code-tabs__left {
          font-size: 24px;
          padding-right: 60px;
        }

        .code-tabs__right {
          font-size: 18px;
        }
      }
    }
  }
</style>
