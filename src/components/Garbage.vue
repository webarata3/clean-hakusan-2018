<template>
  <GarbageList :now-date="nowDate" :garbage-list="garbage.garbageList"></GarbageList>
</template>

<script>
  import common from './common';
  import GarbageList from './GarbageList';

  export default {
    name: 'Garbage',
    components: {
      GarbageList
    },
    data: function () {
      return {
        region: '07'
      };
    },
    props: {
      nowDate: String,
      garbage: Object
    },
    computed: {
      viewDate: function () {
        return common.getViewDate(this.nowDate);
      }
    }
  };
</script>

<style>
  main {
    display: flex;
    flex-direction: column;
    flex: 1;
  }

  .region {
    align-items: center;
    font-size: 14pt;
    padding: 10px 20px;
  }

  select {
    appearance: none;
    background: url(/static/image/arrow.png) 99% 50% no-repeat, linear-gradient(to bottom, #fff 0%, #efebe1 100%);
    background-size: 20px, 100%;
    border: 1px solid #999;
    padding: 10px;
    width: 100%;
  }
</style>
