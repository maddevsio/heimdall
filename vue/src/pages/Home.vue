<template>
  <div class="layout">
    <section class="layout__section">
      <intro @path-changed="changePath($event)"></intro>
    </section>

    <section class="layout__section">
      <jumbo></jumbo>
    </section>

    <section class="layout__section">
      <advantages></advantages>
    </section>

    <section class="layout__section">
      <block-code :badgePath="badgePath"></block-code>
    </section>

    <section class="layout__section">
      <monitor @path-changed="changePath($event)"></monitor>
    </section>

    <section class="layout__section">
      <fork></fork>
    </section>
  </div>
</template>

<script>
  import Intro from '@/components/Intro.vue'
  import Jumbo from '@/components/Jumbo.vue'
  import Advantages from '@/components/Advantages.vue'
  import Code from '@/components/Code.vue'
  import Monitor from '@/components/Monitor.vue'
  import Fork from '@/components/Fork.vue'
  import GitForm from '@/components/GitForm.vue'

  /* eslint-disable comma-dangle */
  export default {
    name: 'home',
    components: {
      'intro': Intro,
      'jumbo': Jumbo,
      'advantages': Advantages,
      'block-code': Code,
      'monitor': Monitor,
      'fork': Fork,
      'git-form': GitForm,
    },
    data: function () {
      return {
        badgePath: 'owner/repository'
      }
    },
    methods: {
      changePath: function (e) {
        this.badgePath = e
      }
    }
  }
</script>
