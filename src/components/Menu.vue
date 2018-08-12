<template>
  <div class="menu">
    <button class="headerButton" @click="clickMenu"></button>
    <transition name="menu-background">
      <div class="modal" v-if="modal" @click="closeMenu"></div>
    </transition>
    <transition name="menu-main">
      <menu type="toolbar" v-if="modal" v-cloak>
        <ul>
          <li><a href="#">使い方（作成中）<span class="fa fa-external-link" aria-hidden="true"></span></a></li>
          <li><a href="#" @click.prevent="clickDisclaimerMenu">免責事項</a></li>
          <li><a href="#" @click.prevent="clickCreditMenu">クレジット</a></li>
        </ul>
      </menu>
    </transition>
    <div class="disclaimer" v-if="disclaimer" @click="clickDisclaimer">
      <div>
        <h1>免責事項</h1>
        <div class="text">
          当サイトの情報は、慎重に管理・作成しますが、すべての情報が正確・完全であることは保証しません。そのことをご承知の上、利用者の責任において情報を利用してください。当サイトを利用したことによるいかなる損失について、一切保証しません。<br>
          また、当サイトは石川県白山市役所が作成したものではありません。問い合わせ等を白山市にしないようにお願いします。問い合わせはTwitter（@webarata3）もしくは、webarata3 at gmail.comまでお願いします。
        </div>
      </div>
    </div>
    <div class="credit" v-if="credit" @click="clickCredit">
      <div>
        <h1>クレジット</h1>
        <div>
          <h2>Vue.js</h2>
          <div class="link">
            <a href="https://vuejs.org/">Vue.js</a>
          </div>
          <div class="license">
            <pre>The MIT License (MIT)

Copyright (c) 2013-present, Yuxi (Evan) You

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.</pre>
          </div>
        </div>
        <div>
          <h2>axios</h2>
          <div class="link">
            <a href="https://github.com/axios/axios">axios</a>
          </div>
          <div class="license">
            <pre>Copyright (c) 2014-present Matt Zabriskie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.</pre>
          </div>
        </div>
        <div>
          <h2>Moment.js</h2>
          <div class="link">
            <a href="https://momentjs.com/">Moment.js</a>
          </div>
          <div class="license">
            <pre>Copyright (c) JS Foundation and other contributors

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.</pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Menu',
    data: function () {
      return {
        modal: false,
        disclaimer: false,
        credit: false
      };
    },
    methods: {
      clickMenu: function (event) {
        this.modal = true;
      },
      closeMenu: function (event) {
        this.modal = false;
      },
      clickCreditMenu: function (event) {
        this.credit = true;
      },
      clickCredit: function (event) {
        this.credit = false;
      },
      clickDisclaimerMenu: function (event) {
        this.disclaimer = true;
      },
      clickDisclaimer: function (event) {
        this.disclaimer = false;
      }
    }
  };
</script>

<style scoped>
  button {
    background: url(/static/image/menu.svg) center center no-repeat;
  }

  .modal {
    background-color: rgba(0, 0, 0, 0.7);
    height: 100vh;
    left: 0;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
  }

  .menu {
    position: relative;
  }

  menu {
    background-color: #fff;
    border-left: 1px solid #000;
    height: 100vh;
    padding: 5px;
    position: fixed;
    right: 0;
    top: 0;
    width: 150px;
    z-index: 1500;
  }

  menu ul {
    display: flex;
    flex-direction: column;
    font-size: 18px;
    line-height: 1.5em;
    white-space: nowrap;
  }

  menu a, menu a:hover, menu a:active, menu a:visited {
    display: block;
    color: #000;
    text-decoration: none;
    padding: 5px;
  }

  .menu-background-enter-active, .menu-background-leave-active {
    transition: opacity 0.3s;
  }

  .menu-backgroud-enter, .menu-background-leave-to {
    opacity: 0;
  }

  .menu-main-enter-active, .menu-main-leave-active {
    transition: right 0.3s;
  }
  .menu-main-enter, .menu-main-leave-to {
    right: -150px;
  }

  .headerButton {
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

  .fa-external-link {
    margin-left: 5px;
  }

  .disclaimer, .credit {
    background-color: rgba(0, 0, 0, 0.7);
    height: 100vh;
    left: 0;
    overflow: scroll;
    padding: 20px;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 2000;
  }

  .disclaimer > div, .credit > div {
    background-color: #fff;
    color: #000;
    margin: 10px 0;
    padding: 5px;
  }

  .disclaimer > div > div, .credit > div > div {
    margin-bottom: 20px;
  }

  .disclaimer h1, .credit h1 {
    background-color: #888;
    color: #fff;
    margin-bottom: 5px;
    padding: 5px;
  }

  .disclaimer .text {
    font-size: 14pt;
    line-height: 1.4em;
  }

  .credit h2 {
    border-bottom: 1px solid #888;
    font-size: 16px;
    padding: 5px;
  }

  .link {
    margin-bottom: 10px;
  }

  .link a, .link a:hover, .link a:active, .link a:visited {
    color: #00f;
    font-size: 14px;
  }

  pre {
    font-size: 14px;
    white-space: pre-wrap;
  }
</style>
