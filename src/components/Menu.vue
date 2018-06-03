<template>
  <div class="menu">
    <button class="headerButton" @click="clickMenu"></button>
    <div class="modal" v-if="modal" @click="closeMenu">
      <menu type="toolbar" v-cloak>
        <ul>
          <li><a href="#">設定</a></li>
          <li><a href="#">使い方</a></li>
          <li><a href="#">免責事項</a></li>
          <li><a href="#" @click.prevent="clickCreditMenu">クレジット</a></li>
        </ul>
      </menu>
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
            <a href="https://github.com/axios/axios">Vue.js</a>
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
            <a href="https://momentjs.com/">Vue.js</a>
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
      }
    }
  };
</script>

<style>
  .menu {
    position: relative;
  }

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

  menu {
    background-color: #fff;
    border: 1px solid #444;
    border-radius: 5px;
    padding: 5px;
    position: absolute;
    right: 5px;
    top: 5px;
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
    text-decoration: none;
    padding: 5px;
  }

  .credit {
    background-color: rgba(0, 0, 0, 0.7);
    height: 100vh;
    left: 0;
    overflow: scroll;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
  }

  .credit > div {
    background-color: #fff;
    color: #000;
    margin: 20px;
    padding: 5px;
  }

  .credit > div > div {
    margin-bottom: 20px;
  }

  .credit h1 {
    background-color: #888;
    color: #fff;
    margin-bottom: 5px;
    padding: 5px;
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
