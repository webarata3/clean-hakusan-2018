<template>
  <footer>
    <div class="copyright">©2018 Shinichi ARATA（webarata3）</div>
    <div class="sns">
      <ul>
        <li><a href="https://twitter.com/webarata3"><span class="fa fa-twitter"></span></a></li>
        <li><a href="https://facebook.com/arata.shinichi"><span class="fa fa-facebook"></span></a></li>
        <li><a href="https://github.com/webarata3"><span class="fa fa-github"></span></a></li>
        <li><a href="https://ja.stackoverflow.com/users/2214/webarata3?tab=profile"><span
          class="fa fa-stack-overflow"></span></a></li>
      </ul>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  data: function () {
    return {};
  }
};
</script>

<style scoped>
  footer {
    display: flex;
    flex-direction: row;
    font-size: 14px;
    padding: 5px;
  }

  .copyright {
    flex: 1;
  }

  ul {
    display: flex;
    flex-direction: row;
  }

  li {
    margin-right: 5px;
  }

  a, a:hover, a:active, a:visited {
    color: black;
  }
</style>
