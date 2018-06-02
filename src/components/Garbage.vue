<template>
  <main>
    <div id="loader" class="loader" v-cloak>
      <svg viewBox="0 0 32 32" width="32" height="32">
        <circle id="spinner" cx="16" cy="16" r="14" fill="none"></circle>
      </svg>
    </div>
    <div class="region" v-cloak>
      <div>一木地区</div>
      <div>
        <button class="change-region-button">地区を変える</button>
      </div>
    </div>
    <GarbageList :now-date="nowDate" :garbage-list="garbage.garbageList"></GarbageList>
  </main>
</template>

<script>
import common from './common'
import GarbageList from './GarbageList'

export default {
  name: 'Garbage',
  components: {
    GarbageList
  },
  data: function () {
    return {}
  },
  props: {
    nowDate: String,
    garbage: Object
  },
  computed: {
    viewDate: function () {
      return common.getViewDate(this.nowDate)
    }
  }
}
</script>

<style>
  main {
    display: flex;
    flex-direction: column;
    flex: 1;
  }

  .region {
    align-items: center;
    display: flex;
    flex-direction: row;
    font-size: 14pt;
    padding: 10px 5px 5px 20px;
  }

  .region > div:nth-child(1) {
    flex: 1;
  }

  .region > div:nth-child(2) {
    white-space: nowrap;
  }

  .change-region-button {
    background-color: #409eff;
    border: 1px solid #409eff;
    border-radius: 5px;
    color: #fff;
    font-size: 12pt;
    outline: none;
    padding: 3px;
  }

  .change-region-button:hover, .change-region-button:active {
    background-color: #3a8ee6;
    border: 1px solid #3a8ee6;
  }
</style>
