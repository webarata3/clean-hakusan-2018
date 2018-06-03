<template>
  <div id="app">
    <header>
      <h1 class="header-title">白山市ごみ収集日程</h1>
      <button id="butAdd" class="headerButton"></button>
    </header>
    <main>
      <div id="loader" class="loader" v-cloak>
        <svg viewBox="0 0 32 32" width="32" height="32">
          <circle id="spinner" cx="16" cy="16" r="14" fill="none"></circle>
        </svg>
      </div>
      <div class="region" v-cloak>
        <select v-model="selectedRegion" name="region" @change="changeRegion">
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
            <option value="20">吉野谷（中宮除く）</option>
            <option value="21">鳥越（仏師ヶ野除く）</option>
            <option value="22">中宮・仏師ヶ野・尾口（深瀬除く）</option>
            <option value="23">深瀬・白峰</option>
          </optgroup>
        </select>
      </div>
      <Garbage :now-date="nowDate" :garbage="garbage"></Garbage>
    </main>
    <Footer></Footer>
  </div>
</template>

<script>
import common from './components/common';
import axios from 'axios';
import Garbage from './components/Garbage';
import Footer from './components/Footer';

export default {
  name: 'App',
  components: {
    Garbage,
    Footer
  },
  mounted: function () {
    const self = this;
    setInterval(() => {
      self.nowDate = common.getCurrentDate();
    }, 1000);
  },
  created: function () {
    this.regionNo = localStorage['regionNo'] ? localStorage['regionNo'] : '01';
    this.selectedRegion = this.regionNo;
    this.changeRegionDate();
  },
  data: function () {
    return {
      regionNo: '',
      nowDate: '',
      selectedRegion: '',
      garbage: {}
    };
  },
  methods: {
    changeRegion: function (event) {
      this.regionNo = event.target.value;
      this.changeRegionDate();
    },
    changeRegionDate: function () {
      axios.get('/static/api/' + this.regionNo + '.json').then(response => {
        this.garbage = response.data;
        localStorage['regionNo'] = this.regionNo;
      });
    }
  }
};
</script>

<style>
#loader:not([v-cloak]) {
  display: none;
}

[v-cloak] {
  display: none;
}

html,
body {
  height: 100%;
  width: 100%;
  font-family: "Helvetica", "Verdana", sans-serif;
  color: #444;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html {
  overflow: hidden;
}

body {
  background: #fff;
  box-sizing: border-box;
  font-size: 20px;
  display: flex;
  flex-direction: column;
}

#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
}

header {
  color: #fff;
  background-color: #1e88e5;
  font-size: 24px;
  display: flex;
  padding: 16px;
  flex-direction: row;
  flex-wrap: nowrap;
  will-change: transform;
  justify-content: flex-start;
  align-items: stretch;
  align-content: center;
  box-shadow: 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 2px 9px 1px rgba(0, 0, 0, 0.12),
    0 4px 2px -2px rgba(0, 0, 0, 0.2);
  transition: transform 0.233s cubic-bezier(0, 0, 0.21, 1) 0.1s;
}

header .headerButton {
  width: 24px;
  height: 24px;
  margin-right: 16px;
  text-indent: -30000px;
  overflow: hidden;
  opacity: 0.54;
  transition: opacity 0.333s cubic-bezier(0, 0, 0.21, 1);
  border: none;
  outline: none;
  cursor: pointer;
}

header #butAdd {
  background: url(/static/image/menu.svg) center center no-repeat;
}

.header-title {
  align-items: center;
  display: flex;
  font-weight: 400;
  font-size: 20px;
  flex: 1;
}

/*
   アニメーション
   https://developers.google.com/web/fundamentals/codelabs/your-first-pwapp/?hl=ja
  */
.loader {
  left: 50%;
  top: 50%;
  position: fixed;
  transform: translate(-50%, -50%);
}

.loader #spinner {
  box-sizing: border-box;
  stroke: #417ab7;
  stroke-width: 3px;
  transform-origin: 50%;
  animation: line 1.6s cubic-bezier(0.4, 0, 0.2, 1) infinite,
    rotate 1.6s linear infinite;
}

@-webkit-keyframes rotate {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(450deg);
  }
}

@keyframes rotate {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(450deg);
  }
}

@-webkit-keyframes line {
  0% {
    stroke-dasharray: 2, 85.964;
    transform: rotate(0);
  }
  50% {
    stroke-dasharray: 65.973, 21.9911;
    stroke-dashoffset: 0;
  }
  100% {
    stroke-dasharray: 2, 85.964;
    stroke-dashoffset: -65.973;
    transform: rotate(90deg);
  }
}

@keyframes line {
  0% {
    stroke-dasharray: 2, 85.964;
    transform: rotate(0);
  }
  50% {
    stroke-dasharray: 65.973, 21.9911;
    stroke-dashoffset: 0;
  }
  100% {
    stroke-dasharray: 2, 85.964;
    stroke-dashoffset: -65.973;
    transform: rotate(90deg);
  }
}
</style>
