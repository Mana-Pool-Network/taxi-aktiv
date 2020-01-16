<template>
  <div class="main female">
    <div class="content ">
      <div class="container">
        <div class="shuttle-block limousine-whyus__block text-center py-3 my-4">
          <div class="shuttle-block__title">
            Женское такси
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
                У нас вы можете заказать «женское такси» в любое время - так, чтобы
                каждая женщина могла быть забрана водителем по запросу.
              </p>
              <p class="shuttle-text">
                Женщина везёт женщину — эта опция ценится многими пассажирами-
                женщинами. 
                Чувствуете ли вы себя безопаснее с женщиной за рулем, можете
                поговорить с ней лучше или нет ночью, чтобы мужчина в машине захотел
                подняться — причины остаются за покупателями.
              </p>
              <p class="shuttle-text">
                Чувствуете ли вы себя безопаснее с женщиной за рулем, можете
                поговорить с ней лучше или нет ночью, чтобы мужчина в машине захотел
                подняться — причины остаются за покупателями.
              </p>
              <p class="shuttle-text">
                Сервис «женщина водит женщину» полностью интегрирован в другие
                сервисы.
              </p>
              <p class="shuttle-text">
                Местные поездки, трансферы из аэропорта, транспортировка
                пациентов на кассе - клиент королева!
              </p>
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
    name: "FemaleService",
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
.female {
  background: linear-gradient( rgba(255, 255, 255, 0.7)), url("../../img/services/female_taxi.jpg") no-repeat center center fixed !important;
  background-color: white !important;
  width: 100%;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>