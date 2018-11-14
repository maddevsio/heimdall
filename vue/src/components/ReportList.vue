<template>
  <div class="report">
    <div class="report__wrapper wrapper">
      <div class="report__top">
        <h1 class="report__title">Heimdall Report</h1>
        <div class="report__path">
          <a href="#" target="_blank" class="report__link-git">username/reponame</a>
        </div>
      </div>
      <ul class="report__list">
        <li class="report__item">
          <div class="report-item">
            <h2 class="report-item__title">neureal_token_test.sol</h2>
            <div class="report-item__section">
              <div class="report-item__head">
                <div class="report-item__description">Contract TESTToken Issue: Exception state</div>
                <div class="report-item__badge report-item__badge_information">Informational</div>
              </div>
              <div class="report-item__content report-item__content_information">
                <div class="report-item__row">
                  <div class="report-item__label">Path</div>
                  <div class="report-item__value">neureal_token_test.sol:161</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Function</div>
                  <div class="report-item__value">fallback()</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Address</div>
                  <div class="report-item__value">439</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Debug</div>
                  <div class="report-item__value">The exception is triggered under the following conditions: storage_10: 0x8000 calldatasize_TESTToken: 0x3</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Description</div>
                  <div class="report-item__value">A reachable exception (opcode 0xfe) has been detected. This can be caused by type errors, division by zero, out-of-bounds array access, or assert violations. This is acceptable in most situations. Note however that `assert()` should only be used to check invariants. Use `require()` for regular input checking.</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Code</div>
                  <div class="report-item__value">phase_ == Phase.Sale</div>
                </div>
              </div>
            </div>
            <div class="report-item__section">
              <div class="report-item__head">
                <div class="report-item__description">Contract TESTToken Issue: Exception state</div>
                <div class="report-item__badge report-item__badge_warning">Warning</div>
              </div>
              <div class="report-item__content report-item__content_warning">
                <div class="report-item__row">
                  <div class="report-item__label">Path</div>
                  <div class="report-item__value">neureal_token_test.sol:161</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Function</div>
                  <div class="report-item__value">fallback()</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Address</div>
                  <div class="report-item__value">439</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Debug</div>
                  <div class="report-item__value">The exception is triggered under the following conditions: storage_10: 0x8000 calldatasize_TESTToken: 0x3</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Description</div>
                  <div class="report-item__value">A reachable exception (opcode 0xfe) has been detected. This can be caused by type errors, division by zero, out-of-bounds array access, or assert violations. This is acceptable in most situations. Note however that `assert()` should only be used to check invariants. Use `require()` for regular input checking.</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Code</div>
                  <div class="report-item__value">phase_ == Phase.Sale</div>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="report__item report__item_small">
          <div class="report-item">
            <h2 class="report-item__title">KOTH.sol <i class="icon-check"></i></h2>
          </div>
        </li>
        <li class="report__item">
          <div class="report-item">
            <h2 class="report-item__title">Lottery.sol</h2>
            <div class="report-item__section">
              <div class="report-item__head">
                <div class="report-item__description">Contract OpenAddressLottery Issue: Integer Underflow</div>
                <div class="report-item__badge report-item__badge_warning">Warning</div>
              </div>
              <div class="report-item__content report-item__content_warning">
                <div class="report-item__row">
                  <div class="report-item__label">Path</div>
                  <div class="report-item__value">Lottery.sol:85</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Function</div>
                  <div class="report-item__value">**ambiguous** f</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Address</div>
                  <div class="report-item__value">1204</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Debug</div>
                  <div class="report-item__value">block_number: 0x0 storage_0: 0x0 caller: 0x0 calldata_OpenAddressLottery[0]: 0x80ca7aec00000000000000000000000000000000000000000000000000000000 calldatasize_OpenAddressLottery: 0x4 callvalue: 0x0</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Description</div>
                  <div class="report-item__value">A possible integer underflow exists in the function `**ambiguous** f`. The subtraction may result in a value < 0.</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Code</div>
                  <div class="report-item__value">block.number - 1</div>
                </div>
              </div>
            </div>
            <div class="report-item__section">
              <div class="report-item__head">
                <div class="report-item__description">Contract OpenAddressLottery Issue: Integer Underflow</div>
                <div class="report-item__badge report-item__badge_warning">Warning</div>
              </div>
              <div class="report-item__content report-item__content_warning">
                <div class="report-item__row">
                  <div class="report-item__label">Path</div>
                  <div class="report-item__value">Lottery.sol:85</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Function</div>
                  <div class="report-item__value">**ambiguous** f</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Address</div>
                  <div class="report-item__value">1204</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Debug</div>
                  <div class="report-item__value">gasprice: 0xf9ca802a3e95281fffffff234472a69368a9231b0516b19314a288b91293dc0d storage_0: 0x0 caller: 0x0 calldata_OpenAddressLottery[0]: 0x80ca7aec00000000000000000000000000000000000000000000000000000000 calldatasize_OpenAddressLottery: 0x4 callvalue: 0x0</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Description</div>
                  <div class="report-item__value">A possible integer overflow exists in the function `**ambiguous** f`. The addition or multiplication may result in a value higher than the maximum representable integer.</div>
                </div>
                <div class="report-item__row">
                  <div class="report-item__label">Code</div>
                  <div class="report-item__value">tx.gasprice * 7</div>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'report-list'
  }
</script>

<style lang="scss">
  .report {

    &__top {
      margin-bottom: 56px;
    }

    &__title {
      margin-top: 5px;
      margin-bottom: 34px;
      font-size: 46px;
      text-align: center;
      letter-spacing: -0.012em;
    }

    &__path {
      text-align: center;
    }

    &__link-git {
      display: inline-block;
      text-decoration: inherit;
      font-weight: bold;
      font-size: 22px;
      color: #6732ff;

      &::before {
        content: '';
        display: inline-block;
        vertical-align: middle;
        margin-top: -5px;
        margin-right: 7px;
        width: 32px;
        height: 32px;
        background: transparent url('../assets/img/git-violet.svg') 0 0 no-repeat;
        background-size: 100% 100%;
      }
    }

    &__list {
      padding: 0;
      margin: 0;
      width: 100%;
      max-width: 1090px;
      margin: auto;
    }

    &__item {
      margin-bottom: 58px;
      list-style: none;
      &_small {
        margin-bottom: -10px;
      }
    }

  }

  .report__item:last-child {
    margin-bottom: 0;
  }

  .report__item:last-child .report-item__section:last-child {
    margin-bottom: 0;
  }

  .report-item {

    &__title {
      margin: 0;
      margin-bottom: 23px;
      font-size: 35px;
    }

    &__section {
      margin-bottom: 42px;
    }

    &__head {
      display: flex;
      justify-content: space-between;
      align-items: start;
      margin-bottom: 9px;
    }

    &__description {
      font-weight: bold;
      font-size: 22px;
    }

    &__badge {
      margin-top: 3px;
      display: inline-block;
      font-weight: bold;
      font-size: 11px;
      letter-spacing: 0.03em;
      padding: 3px 19px 2px;
      color: #fff;
      background-color: #292929;
      border-radius: 2px;

      &_information {
        background-color: #ff7500;
      }

      &_warning {
        background-color: #ff004a;
      }
    }

    &__content {
      background-color: #edf2f6;
      padding: 8px 22px 16px;
      border-radius: 2px;
      border-left: 4px solid #000;
      font-size: 16px;

      &_information {
        border-left-color: #ff7500;
      }

      &_warning {
        border-left-color: #ff004a;
      }
    }

    &__row {
      padding: 10px 0 9px;
      &::after {
        content: '';
        display: table;
        clear: both;
      }
    }

    &__label {
      float: left;
      width: 100px;
    }

    &__value {
      margin-left: 108px;
    }
  }

  .icon-check {
    display: inline-block;
    vertical-align: middle;
    width: 34px;
    height: 34px;
    background: transparent url('../assets/img/check-mark.png') 0 0 no-repeat;
    background-size: 100% 100%;
    margin-top: -10px;
  }

  @media only screen and (max-width: 1439px) {
    .report {
      padding: 0 50px;
    }
  }

  @media only screen and (max-width: 1023px) {
    .report {
      padding: 20px;
    }
  }

  @media only screen and (max-width: 767px) {
    .report {
      padding: 0 6px;

      &__top {
        margin-bottom: 42px;
      }

      &__title {
        font-size: 30px;
        margin-bottom: 30px;
      }

      &__link-git {
        font-size: 18px;
      }
    }

    .report-item {
      &__title {
        font-size: 24px;
        margin-bottom: 32px;
        letter-spacing: -0.017em;
      }

      &__head {
        flex-direction: column;
        margin-bottom: 20px;
      }

      &__description {
        font-size: 18px;
        margin-bottom: 17px;
      }

      &__badge {
        padding: 4px 18px 3px;
      }

      &__content {
        padding: 8px 8px 10px;
        font-size: 14px;
        line-height: 1.64;
        word-break: break-all;
      }

      &__label {
        width: 84px;
      }

      &__value {
        margin-left: 90px;
      }
    }
  }
</style>
