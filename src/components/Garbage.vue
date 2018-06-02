<template>
  <main>
    <div id="loader" class="loader" v-cloak>
      <svg viewBox="0 0 32 32" width="32" height="32">
        <circle id="spinner" cx="16" cy="16" r="14" fill="none"></circle>
      </svg>
    </div>
    <div class="region" v-cloak>
      <select name="region">
        <optgroup label="松任地区">
          <option selected>一木地区</option>
          <option selected>一木地区</option>
          <option selected>一木地区</option>
          <option selected>一木地区</option>
        </optgroup>
      </select>
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
