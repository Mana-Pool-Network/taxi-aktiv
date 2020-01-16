<template>
  <div class="main shuttle">
    <div class="content ">
      <div class="container">
        <div class="shuttle-block limousine-whyus__block text-center py-3 my-4">
          <div class="shuttle-block__title">
            Шаттл-сервис
          </div>
        </div>
      </div>
      <div class="shuttle-bg p-4">
        <div class="container">
          <b-row>
            <b-col
              xl="6"
              lg="6"
              md="12"
              sm="12"
            >
              <p class="shuttle-text">
                Если вы хотите поехать в аэропорт или назначить выставочную дату, мы
                доставим вас спокойно и надежно к вашему терминалу.
              </p>
              <p class="shuttle-text">
                Мы встретим вас у входной двери и доставим в аэропорт вовремя.
              </p>
              <p class="shuttle-text">
                В зависимости от количества людей и чемоданов, у нас есть подходящая машина.
              </p>
              <p class="shuttle-text">
                В случае неожиданного изменения даты отъезда вы можете легко
                перебронировать номер, и это будет стоить вам всего лишь быстрого звонка. 
                В другое время или в другой день.
              </p>
            </b-col>
            <b-col
              xl="6"
              lg="6"
              md="12"
              sm="12"
            >
              <p class="shuttle-text">
                Мы также поможем вам с планированием времени и дадим рекомендации,
                когда вы должны прибыть в аэропорт, чтобы не пропустить время для
                пунктуальной регистрации.
              </p>
              <p class="shuttle-text">
                Мы включаем задержки в воздушное движение,
                проблемные дорожные ситуации и погодные факторы в ожидаемое время в
                пути.
              </p>
              <p class="shuttle-text">
                С обратным трансфером мы являемся удобной и быстрой альтернативой
                общественному транспорту. Мы вовремя в оговоренное время с табличкой с
                фамилией в месте встречи или на выходе, чтобы доставить вас к нашему
                автомобилю с вашим багажом.
              </p>
            </b-col>
          </b-row>
        </div>
      </div>
      <div class="shuttle-bg mt-5">
        <div class="container">
          <b-row>
            <b-col xl="12">
              <div class="shuttle-guarantor text-center pt-3 mb-4">
                Мы гарантируем вам спокойную и непринужденную поездку!
              </div>
            </b-col>
            <b-col
              align-self="center"
              xl="6"
              lg="6"
              md="5"
              class="mx-5 mb-4 "
            >
              <div class="shuttle-guarantor__text p-lg-5 p-md-1">
                Вы получите всю информацию о нашей службе трансфера, когда сделаете
                запрос или сделаете заказ.
              </div>
            </b-col>
            <b-col
              align-self="center"
              xl="4"
              lg="4"
              md="5"
              class="text-center mb-4"
            >
              <button
                type="button"
                class="shuttle-guarantor__btn"
              >
                Сделать заказ >
              </button>
            </b-col>
          </b-row>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
export default {
    name: "ShuttleService",
    components: {
        Footer
    }
};
</script>

<style >
/* .main {
   min-height: 100vh;
   display: flex;
   flex-direction: column;
   justify-content: space-between;
} */
.shuttle {
   background: linear-gradient( rgba(255, 255, 255, 0.7)), url("../../img/services/shuttle/bg-shuttle.jpg") no-repeat center center fixed !important;
   background-color: white !important;
   background-size: cover;
}
</style>