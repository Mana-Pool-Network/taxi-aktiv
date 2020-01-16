<template>
  <div class="transportation">
    <div class="content mb-5">
      <header class="transportation-bg">
        <div class="container">
          <div class="transportation-block text-center">
            <div class="transportation-block__title">
              Услуги перевозок на первоклассных
              машинах с опытными водителями
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
                <p class="transportation-text">
                  Taxi Aktiv Koeln предоставляет услуги транспортных перевозок, в Кёльне и
                  окрестностях. Мы хотим, чтобы после каждой поездки к нам возвращались снова
                  и снова.
                </p>
                <p class="transportation-text">
                  Комфортные, предсказуемые поездки в любую точку Кёльна, в уютных
                  салонах наших автомобилей — это цель, над которой мы работаем каждый день,
                  вот уже более 25-ти лет.
                </p>
                <p class="transportation-text">
                  Независимо от того где вы, или в какую точку направляетесь — Taxi Aktiv
                  сможет быть вашим надёжным партнёром.
                </p>
                <p class="transportation-text">
                  Наличие водителей, с лицензией
                  медицинских поездок позволит Вам оказать заботу о родных и близких и при
                  необходимости отвезти их в лечебное учреждение.
                </p>
              </b-col>
              <b-col
                xl="6"
                lg="6"
                md="12"
              >
                <p class="transportation-text">
                  Наличие водителей, с лицензией
                  медицинских поездок позволит Вам оказать заботу о родных и близких и при
                  необходимости отвезти их в лечебное учреждение.
                </p>
                <p class="transportation-text">
                  Современные технологии позволят отслеживать перемещение водителя,
                  благодаря чему Вы сможете заказать поездку в школу своим детям и знать, что
                  они в безопасности.
                </p>
                <p class="transportation-text">
                  Вне зависимости от поездки, вы сможете не думать о
                  вождении, а готовиться к действительно важным событиям.
                </p>
                <p class="transportation-text">
                  За годы работы в Taxi Aktiv Koeln сформировалось чёткое представление о
                  том, чем является качественная услуга перевозки.
                </p>
              </b-col>
            </b-row>
          </div>
        </div>
      </header>
      <div class="container">
        <div class="transportation-title text-center mx-5 mt-5">
          В центре нашей философии
          находится КЛИЕНТ, внимание к которому — на самом высоком уровне.
        </div>
      </div>
      <div class="transportation-about mt-4 ">
        <div class="container">
          <div class="transportation-about__title text-center py-3">
            Предлагаем познакомиться с нашей компанией
          </div>
          <div class="transportation-about__subtitle transportation-about__title text-center pb-4">
            Узнайте больше об истории компании и наших целях и стремлениях.
          </div>
          <b-row class="text-center ">
            <b-col class="p-3">
              <button
                type="button"
                class="shuttle-guarantor__btn"
                :onClick="`location.href=&quot;/${$i18n.locale}/about-company&quot;`"
              >
                О компании >
              </button>
            </b-col>
            <b-col class="p-3">
              <button
                type="button"
                class="shuttle-guarantor__btn"
                :onClick="`location.href=&quot;/${$i18n.locale}/driver-training&quot;`"
              >
                Шофер-тренинг >
              </button>
            </b-col>
            <b-col class="p-3">
              <button
                type="button"
                class="shuttle-guarantor__btn mb-5"
                :onClick="`location.href=&quot;/${$i18n.locale}/software&quot;`"
              >
                Прог. обеспечение >
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
// @ is an alias to /src
import Footer from "@/components/Footer.vue";
export default {
    name: "AboutUs",
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

</style>