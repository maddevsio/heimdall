<template>
  <div class="layout">
    <section class="layout__section">
      <report-list></report-list>
    </section>
  </div>
</template>

<script>
  import ReportList from '@/components/ReportList.vue'

  /* eslint-disable comma-dangle */
  export default {
    name: 'report',
    components: {
      'report-list': ReportList,
    }
  }
</script>
