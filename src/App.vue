<template>
  <div id="app">
    <header>
      <h1 class="header-title">白山市ごみ収集日程</h1>
      <Menu></Menu>
    </header>
    <main>
      <div class="alert">※ 白山市公式のアプリではありません。</div>
      <Region @change-region="changeRegion" :regionNo="regionNo"></Region>
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
  import Menu from './components/Menu';
  import Region from './components/Region';

  export default {
    name: 'App',
    components: {
      Garbage,
      Footer,
      Menu,
      Region
    },
    mounted: function () {
      const self = this;
      self.nowDate = common.getCurrentDate();
      setInterval(() => {
        self.nowDate = common.getCurrentDate();
      }, 1000);
    },
    created: function () {
      this.readVersion();
    },
    data: function () {
      return {
        version: '',
        regionNo: '',
        nowDate: '',
        garbage: {}
      };
    },
    methods: {
      readVersion: async function () {
        this.version = localStorage['version'] ? localStorage['version'] : '';

        let readVersion = '';
        await axios.get('/static/api/version.json').then(response => {
          readVersion = response.data['version'];
          localStorage['version'] = readVersion;
        }).catch(() => {
        });

        this.regionNo = localStorage['regionNo'] ? localStorage['regionNo'] : '01';
        if (readVersion === '') {
          if (this.version === '') {
            // サーバからversionNoが読み込めず、さらにすでに読み込まれているものがない（どうしようもない）とき
            alert('なにか問題がおきています。\n時間をおいて試してください');
          } else {
            // サーバからversionNoが読み込めなかった場合には、すでに読み込まれているものを使う
            this.initRegion();
          }
        } else {
          if (this.version === readVersion) {
            // サーバのversionNoから変わっていない場合には再度取得はせず、すでに読み込まれているものを使う
            this.initRegion();
          } else {
            // サーバからversionNoが読み込めて、読み込まれているものと違う場合（更新があった場合）
            this.regionNo = localStorage['regionNo'] ? localStorage['regionNo'] : '01';
            this.selectedRegionNo = this.regionNo;
            this.changeRegionDate();
          }
        }
      },
      changeRegion: function (value) {
        this.regionNo = value;
        localStorage['regionNo'] = value;
        localStorage['version'] = '';
        this.readVersion();
      },
      changeRegionDate: function () {
        axios.get('/static/api/' + this.regionNo + '.json').then(response => {
          this.garbage = response.data;
          localStorage['regionNo'] = this.regionNo;
          localStorage['garbage'] = JSON.stringify(this.garbage);
        });
      },
      initRegion: function () {
        this.selectedRegionNo = this.regionNo;
        this.garbage = JSON.parse(localStorage['garbage']);
      }
    }
  };
</script>

<style scoped>
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

  .header-title {
    align-items: center;
    display: flex;
    font-weight: 400;
    font-size: 20px;
    flex: 1;
  }

  main {
    display: flex;
    flex-direction: column;
    flex: 1;
  }

  .alert {
    margin: 10px 5px 0 5px;
    color: #f00;
    font-size: 14px;
  }
</style>
