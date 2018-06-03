import moment from 'moment';
moment.locale('ja');

const common = {
  BASIC_DATE_FORMAT: 'YYYYMMDD',
  VIEW_DATE_FORMAT: 'YYYY年M月D日',
  VIEW_GARBAGE_DATE_FORMAT: 'M月D日(ddd)',
  VIEW_UNTIL_DAY: ['今日', '明日', '明後日'],
  getCurrentDate: function () {
    return moment().format(this.BASIC_DATE_FORMAT);
  },
  getViewDate: function (date) {
    return moment(date, this.BASIC_DATE_FORMAT).format(this.VIEW_DATE_FORMAT);
  },

  getViewGarbageDate: function (date) {
    return moment(date, this.BASIC_DATE_FORMAT).format(this.VIEW_GARBAGE_DATE_FORMAT);
  }
};

export default common;
