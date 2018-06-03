<template>
  <div class="garbage-list">
    <GarbageItem :now-date="nowDate" :garbage="garbage" v-for="garbage in garbageList" :key="garbage.key"></GarbageItem>
  </div>
</template>

<script>
import GarbageItem from './GarbageItem';

export default {
  name: 'GarbageList',
  components: {
    GarbageItem
  },
  data: function () {
    return {
    };
  },
  props: {
    nowDate: String,
    garbageList: Array
  }
};
</script>

<style>
  .garbage-list {
    display: flex;
    flex: 1;
    flex-direction: column;
  }
</style>
