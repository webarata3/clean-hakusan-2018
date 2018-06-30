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
        region: ''
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
