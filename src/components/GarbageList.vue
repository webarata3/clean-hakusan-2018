<template>
  <div class="garbage-list">
    <GarbageItem :now-date="nowDate" :garbage="garbage" v-for="garbage in garbageList" :key="garbage.key"></GarbageItem>
  </div>
</template>

<script>
import GarbageItem from './GarbageItem'

export default {
  name: 'GarbageList',
  components: {
    GarbageItem
  },
  data: function () {
    return {
    }
  },
  props: {
    nowDate: String,
    garbageList: Array
  }
}
</script>

<style>
  .garbage-list {
    display: flex;
    flex: 1;
    flex-direction: column;
  }

  .garbage-list > div {
    border: 1px solid #444;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.4);
    flex: 1;
    margin: 5px;
  }
</style>
