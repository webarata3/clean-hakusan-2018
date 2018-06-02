<template>
  <main>
    <div id="loader" class="loader" v-cloak>
      <svg viewBox="0 0 32 32" width="32" height="32">
        <circle id="spinner" cx="16" cy="16" r="14" fill="none"></circle>
      </svg>
    </div>
    <div class="region" v-cloak>
      <select name="region" @change="changeRegion">
        <optgroup label="松任地域">
          <option value="01">松任Ａ</option>
          <option value="02">松任Ｂ・旭</option>
          <option value="03">松任Ｃ</option>
          <option value="04">石川・柏野</option>
          <option value="05">笠間・宮保・加賀野</option>
          <option value="06">出城・御手洗</option>
          <option value="07" selected>一木</option>
          <option value="08">中奥・郷</option>
          <option value="09">千代野</option>
          <option value="10">林中・山島</option>
        </optgroup>
        <optgroup label="美川地域">
          <option value="11">美川</option>
          <option value="12">蝶屋</option>
          <option value="13">湊</option>
        </optgroup>
        <optgroup label="鶴来地区">
          <option value="14">一ノ宮</option>
          <option value="15">鶴来</option>
          <option value="16">舘畑</option>
          <option value="17">蔵山</option>
          <option value="18">林</option>
        </optgroup>
        <optgroup label="白山ろく地域">
          <option value="19">河内</option>
          <option value="20">吉野谷</option>
          <option value="21">鳥越</option>
          <option value="22">中宮・仏師ヶ野・尾口</option>
          <option value="23">深瀬・白峰</option>
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
      return {
        region: '07'
      }
    },
    props: {
      nowDate: String,
      garbage: Object
    },
    computed: {
      viewDate: function () {
        return common.getViewDate(this.nowDate)
      }
    },
    methods: {
      changeRegion: function (event) {
        this.region = event.target.value
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
