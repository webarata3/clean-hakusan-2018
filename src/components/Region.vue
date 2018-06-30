<template>
  <div class="region" v-cloak>
    <div class="select-region">
      <label for="region">地域</label>
      <select :value="regionNo" id="region" name="region" @change="changeRegion">
        <optgroup label="松任地域">
          <option value="01" selected>松任Ａ</option>
          <option value="02">松任Ｂ・旭</option>
          <option value="03">松任Ｃ</option>
          <option value="04">石川・柏野</option>
          <option value="05">笠間・宮保・加賀野</option>
          <option value="06">出城・御手洗</option>
          <option value="07">一木</option>
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
          <option value="20">吉野谷（中宮除く）</option>
          <option value="21">鳥越（仏師ヶ野除く）</option>
          <option value="22">中宮・仏師ヶ野・尾口（深瀬除く）</option>
          <option value="23">深瀬・白峰</option>
        </optgroup>
      </select>
    </div>
    <a href="http://www.city.hakusan.ishikawa.jp/shiminseikatsubu/kankyo/4r/gomi_chikunokensaku.html">地域が不明な方はこちらで確認してください</a>
  </div>
</template>

<script>
  export default {
    name: 'Region',
    props: [
      'regionNo'
    ],
    data: function () {
      return {
      };
    },
    methods: {
      changeRegion: function (evnet) {
        this.$emit('change-region', event.target.value);
      }
    }
  };
</script>

<style scoped>
  select {
    appearance: none;
    background: url(/static/image/arrow.png) 99% 50% no-repeat, linear-gradient(to bottom, #fff 0%, #efebe1 100%);
    background-size: 20px, 100%;
    border: 1px solid #999;
    flex: 1;
    padding: 10px;
    width: 100%;
  }

  .region {
    align-items: center;
    display: flex;
    flex-direction: column;
    font-size: 14pt;
    padding: 10px 20px;
  }

  .region a, .region a:hover, .region a:active, .region a:visited {
    color: #ff4040;
    font-size: 10pt;
    text-align: right;
    text-decoration: none;
    margin-top: 5px;
    width: 100%;
  }

  .select-region {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
  }

  label {
    font-size: 16px;
    margin-right: 8px;
    white-space: nowrap;
  }
</style>
