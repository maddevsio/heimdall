'use strict';

document.addEventListener('DOMContentLoaded', function() {

  // Badge path injection
  var GitForm = function($base, options) {
      var $input;
      var $errorMsg;
      var $form;

      var validPattern = /^([0-9a-zA-Z._-]+)\/([0-9a-zA-Z._-]+)$/gi;

      var isValid = false;
      var hasError = false;

      var badgePath = '';

      var realTimeChecking = false;

      if ($base) {
        init();
      }

      function init() {
        setElements();
        setEvents();
      }

      function setElements() {
        $input = $base.querySelector('.js-git-input');
        $form = $base.querySelector('form');
        $errorMsg = $base.querySelector('.js-git-form-msg');
      }

      function setEvents() {
        $input.addEventListener('input', inputHandler);
        $form.addEventListener('submit', submitHandler);
      }

      function submitHandler(e) {
        e.preventDefault();

        validate();

        if (isValid) {
          sendForm();
        } else {
          realTimeChecking = true;
        }
      }

      function inputHandler() {
        if (realTimeChecking) {
          validate();
        }
      }

      function validate() {
        var str = $input.value;
        var textIsValid = str.match(validPattern);

        hasError = false;
        isValid = true;

        if (str.length > 0) {
          if (!textIsValid) {
            hasError = true;
            isValid = false;
          }
        } else {
          hasError = true;
          isValid = false;
        }

        showErrors();
      }

      function showErrors() {
        if (hasError) {
          $input.classList.add('has-error');
          $errorMsg.classList.add('is-visible');
        } else {
          $input.classList.remove('has-error');
          $errorMsg.classList.remove('is-visible');
        }
      }

      function sendForm() {
        var badgePath = $input.value;

        showCode();

        CodeBadge.update(badgePath);
      }

      function showCode() {
        $base.querySelector('.js-git-form-bottom').classList.add('is-visible');
        $base.querySelector('.js-git-form-top').classList.remove('is-visible');
      }
  };

  GitForm(document.querySelector('.js-git-form-1'));
  GitForm(document.querySelector('.js-git-form-2'));

  // Change the code badge
  var CodeBadge = function() {
    var $base = document.querySelectorAll('.js-badge');

    function update(newText) {
      if ($base) {
        for (var i = 0; i < $base.length; i++) {
          $base[i].innerHTML = newText;
        }
      }
    }

    return {
      update: update
    }
  }();

  // Operations -> Delivery tabs
  (function() {
    var $tabOperations = document.querySelector('.js-tab-operation');
    var $tabDelivery = document.querySelector('.js-tab-delivery');

    var $codeBase = document.querySelector('.js-code-tabs');

    if ($tabOperations && $tabDelivery) {
      init();
    }

    function init() {
      setEvents();
    }

    function setEvents() {
      $tabOperations.addEventListener('click', operationsClick);
      $tabDelivery.addEventListener('click', deliveryClick);
    }

    function operationsClick(e) {
      $codeBase.classList.add('is-operations');
      openContent(this.getAttribute('data-tab'));
      closeContent('delivery');
    }

    function deliveryClick(e) {
      $codeBase.classList.remove('is-operations');
      openContent(this.getAttribute('data-tab'));
      closeContent('operations');
    }

    function openContent(target) {
      var $el = document.querySelectorAll('[data-block="' + target + '"]');
      for (var i = 0; i < $el.length; i++) {
        $el[i].classList.add('is-visible');
      }
    }

    function closeContent(target) {
      var $el = document.querySelectorAll('[data-block="' + target + '"]');
      for (var i = 0; i < $el.length; i++) {
        $el[i].classList.remove('is-visible');
      }
    }
  })();

  // Code copying
  (function() {
      var $trigger = document.querySelectorAll('.js-copy-code');
      var $anotherLinks = document.querySelectorAll('.code-card__copy');

      if ($trigger) {
        setEvents();
      }

      function setEvents() {
        for (var i = 0; i < $trigger.length; i++) {
          setCopying($trigger[i]);
        }
      }

      function setCopying($el) {
        var $codeElement = $el.querySelector('code');
        var $link = $el.querySelector('.code-card__copy');

        var clipboard = new ClipboardJS($el, {
          text: function() {
            return $codeElement.innerText;
          }
        });

        clipboard.on('success', function(e) {
          for (var i = 0; i < $anotherLinks.length; i++) {
            $anotherLinks[i].innerHTML = 'copy code';
          }

          $link.innerHTML = 'copied';
        });
      }
  })();
});
