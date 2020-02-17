<template>
  <div class="small">
    <line-chart style="height: 100%" :chart-data="datacollection" :options="chartOptions"></line-chart>
  </div>
</template>

<script>
import LineChart from './LineChart'
import donationsJson from '../../../donations.json'
import moment from 'moment';

export default {
  name: 'graph-index',
  components: {
    LineChart
  },
  data () {
    return {
      datacollection: null,
      donations: [],
      labels: [],
      dates: [],
      chartData: [],
      backgroundColors: [],
      interval: 0,
      index: 0,
    }
  },
  mounted () {
    const donations = donationsJson;
    this.donations = donations.map( d => {
      const date = moment(d.TransactionDate, "DD.MM.YYYY").format("DD.MM");
      d.TransactionDate = date;
      return d;
    });
    this.dates = donations
      .map(d => d.TransactionDate)
      .filter((date,index,self) => {
        return self.indexOf(date) === index;
      });
    this.dates = this.dates.sort((a,b) => {
      return moment(a, "DD.MM.YYYY")._d - moment(b,"DD.MM.YYYY")._d
    });
    this.dates = this.dates.map(d => moment(d,"DD.MM.YYYY").format("DD.MM"));
    this.interval = setInterval(this.addDate, 1000);
    this.addDate();
    this.fillData();
  },
  methods: {
    fillData () {
      this.datacollection = {
        labels: this.dates,
        datasets: [
          {
            backgroundColor: this.backgroundColors,
            data: this.chartData,
            fill: false,
          },
        ]
      }
    },
    addDate() {
      const index = this.index;
      if (index >= this.dates.length) {
        clearInterval(this.interval);
        setTimeout(() => this.$emit('reload'), 5000);
        return
      }
      const last = this.chartData[index-1] || 0
      const date = this.dates[index];
      const donationsOfTheDay = this.donations.filter(d => d.TransactionDate === date);
      const amount = donationsOfTheDay.length;
      const totalByDay = donationsOfTheDay.reduce((total, value) => total + value.Amount,0);
      this.chartData.push(last + totalByDay);
      this.backgroundColors.push(`rgba(50, 170, 50, ${0.4 + amount/100})`)
      this.fillData();
      this.index += 1;
    }
  },
  computed: {
    chartOptions() {
      return {
        fill: false,
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          duration: 2000
        },
        scales: {
          yAxes: [{
            display: true,
            ticks: {
              fontSize: 20,
              beginAtZero: true,
              min: 0,
              max: 22450,
            }
          }],
          xAxes: [{
            ticks: {
              fontSize: 20,
            },
            display: true,
            showLabel: true,
          }],
        },
        legend: {
          display: false,
        }
      };
    },
  }
}
</script>

<style>
  .small {
    max-width: 100%;
    height: 98vh;
  }
</style>