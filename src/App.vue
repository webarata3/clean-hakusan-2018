<template>
  <div id="app">
    <header>
      <h1 class="header-title">白山市ごみ収集日程</h1>
      <button id="butAdd" class="headerButton"></button>
    </header>
    <Garbage :now-date="nowDate" :garbage="garbage"></Garbage>
    <Footer></Footer>
  </div>
</template>

<script>
import common from './components/common'
import axios from 'axios'
import Garbage from './components/Garbage'
import Footer from './components/Footer'

export default {
  name: 'App',
  components: {
    Garbage,
    Footer
  },
  mounted: function () {
    const self = this
    setInterval(() => {
      self.nowDate = common.getCurrentDate()
    }, 1000)
  },
  created: function () {
    axios.get('/static/api/ichiki')
      .then(response => {
        this.garbage = response.data
      })
  },
  data: function () {
    return {
      nowDate: '',
      garbage: {}
    }
  }
}
</script>

<style>
  #loader:not([v-cloak]) {
    display: none;
  }

  [v-cloak] {
    display: none;
  }

  html, body {
    height: 100%;
    width: 100%;
    font-family: 'Helvetica', 'Verdana', sans-serif;
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
    box-shadow: 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 2px 9px 1px rgba(0, 0, 0, 0.12), 0 4px 2px -2px rgba(0, 0, 0, 0.2);
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
    animation: line 1.6s cubic-bezier(0.4, 0, 0.2, 1) infinite, rotate 1.6s linear infinite;
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
