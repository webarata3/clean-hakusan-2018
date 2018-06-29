<template>
  <div class="garbage-item"
       :class="{ today: isToday, tomorrow: isTomorrow, 'day-after-tomorrow': isDayAfterTomorrow }">
    <div class="garbage-title">
      <div v-for="(garbageTitle, garbageKey) in garbage.garbageTitleList" :key="garbageKey">{{ garbageTitle }}</div>
    </div>
    <div class="garbage-schedule">
      <div class="garbage-until-day"><span>{{ viewUntilDay }}</span></div>
      <div class="garbage-next-date">{{ viewNextDate }}</div>
    </div>
  </div>
</template>

<script>
import moment from 'moment';
import common from './common';

export default {
  name: 'GarbageItem',
  props: {
    nowDate: String,
    garbage: Object
  },
  computed: {
    nextDate: function () {
      return this.getImmediateDate(this.garbage.garbageDateList);
    },
    viewNextDate: function () {
      return common.getViewGarbageDate(this.nextDate);
    },
    untilDay: function () {
      return this.getUntilDay(this.nextDate, this.nowDate);
    },
    viewUntilDay: function () {
      return this.getViewUntilDay(this.untilDay);
    },
    isToday: function () {
      return this.untilDay === 0;
    },
    isTomorrow: function () {
      return this.untilDay === 1;
    },
    isDayAfterTomorrow: function () {
      return this.untilDay === 2;
    }
  },
  methods: {
    getImmediateDate: function (dateList) {
      for (let date of dateList) {
        if (date >= this.nowDate) return date;
      }
      return null;
    },
    getUntilDay: function (nextDate, nowDate) {
      return moment(nextDate, common.BASIC_DATE_FORMAT).diff(moment(nowDate, common.BASIC_DATE_FORMAT), 'days');
    },
    getViewUntilDay: function (untilDay) {
      return untilDay > 2 ? untilDay + '日後' : common.VIEW_UNTIL_DAY[untilDay];
    }
  }
};
</script>

<style scoped>
  .garbage-item {
    border: 1px solid #444;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.4);
    display: flex;
    flex: 1;
    flex-direction: row;
    margin: 5px;
    z-index: -1;
  }

  .garbage-title {
    background-color: #1698cc;
    color: #fff;
    flex: 1;
    font-size: 14px;
    line-height: 1.2em;
    padding: 5px;
    position: relative;
  }

  .garbage-title:before{
    content: "";
    position: absolute;
    top: 50%;
    right: -24px;
    margin-top: -12px;
    border: 12px solid transparent;
    border-left: 12px solid #1698cc;
    z-index: 2;
  }

  .garbage-title:after{
    content: "";
    position: absolute;
    top: 50%;
    right: -30px;
    margin-top: -16px;
    border: 16px solid transparent;
    border-left: 16px solid #1698cc;
    z-index: 1;
  }

  .garbage-title > div {
    margin-bottom: 8px;
  }

  .garbage-schedule {
    display: flex;
    flex: 1;
    flex-direction: column;
    padding: 5px;
    position: relative;
  }

  .garbage-until-day {
    flex: 1;
    font-size: 40px;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .garbage-next-date {
    bottom: 5px;
    color: #888;
    font-size: 16px;
    text-align: right;
    position: absolute;
    right: 5px;
  }

  .today {
    background-color: #ffff90;
  }

  .today .garbage-until-day {
    color: #f00;
  }

  .tomorrow .garbage-until-day {
    color: #f00;
  }

  .day-after-tomorrow .garbage-until-day {
    color: #00f;
  }
</style>
