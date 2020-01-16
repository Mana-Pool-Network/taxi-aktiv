<template>
  <div class="services">
    <section class="container mt-5">
      <div class="services-block text-center px-2">
        <div class="services-block__title">
          Servise
        </div>
        <div class="services-block__subtitle text-right">
          Taxi Aktiv Koeln
        </div>
      </div>
      <b-row class="mt-5">
        <b-col xl="6">
          <p class="services-block__text">
            На сегодняшний день Taxi Aktiv Koeln осуществляет транспортные
            перевозки пассажиров для широкого спектра различных ситуаций.
          </p> 
          <p class="services-block__text">
            Вы можете заказать место в шаттле, курсирующем между аэропортом Кёльн-Бонн и
            центром города, или вызвать машину для медицинской поездки к врачу.
          </p>
        </b-col>
        <b-col xl="6">
          <p class="services-block__text">
            Мы заботимся о том, чтобы подача машины была своевременной, а поездка— комфортной.
          </p> <p class="services-block__text">
            Наш парк представлен современными моделями Mersedes-Benz E-Klass.
            А новый шаттл-сервис от Taxi Aktiv Koeln - прекрасная альтернатива
            добраться до аэропорта и успеть на свой рейс.
          </p>
        </b-col>
      </b-row>
    </section>
    <section class="container services-more">
      <div class="services-more__title text-center mt-5">
        Узнайте больше о нашем сервисе
      </div>
      <b-row>
        <b-col xl="12">
          <div class="services-more__subtitle text-center my-4">
            Шофер - лимузин сервис 
          </div>
          <b-row>
            <b-col xl="7">
              <div class="img-wrap">		
                <img
                  src="../img/services/limousine.jpg"
                  class="img-responsive img-fluid"
                >
                <a :href="`/${$i18n.locale}/limousine-service`">Шофер - лимузин сервис</a>
              </div>
            </b-col>
            <b-col align-self="center">
              <ul class="services-more__list">
                <li>Бизнес-поездки</li> 
                <li>Медицинские поездки</li> 
                <li>Корпоративные поездки</li>
                <li>Трансфер в школу и обратно домой</li>
                <li>Экскурсионные поездки</li>
              </ul>
            </b-col>
          </b-row>
        </b-col>
        <b-col xl="12">
          <div class="services-more__subtitle text-center my-4">
            Шаттл-сервис 
          </div>
          <b-row>
            <b-col xl="7">
              <div class="img-wrap">		
                <img
                  src="../img/services/airport.jpg"
                  class="img-responsive img-fluid"
                >
                <a :href="`/${$i18n.locale}/shuttle-service`">Шаттл-сервис</a>
              </div>
            </b-col>
            <b-col align-self="center">
              <ul class="services-more__list">
                <li>Доставим в аэропорт вовремя</li> 
                <li>Подберём подходящую машину</li> 
                <li>Поможем вам с планированием времени и дадим рекомендации</li>
              </ul>
            </b-col>
          </b-row>
        </b-col>
        <b-col xl="12">
          <div class="services-more__subtitle text-center my-4">
            Женское такси
          </div>
          <b-row>
            <b-col xl="7">
              <div class="img-wrap">		
                <img
                  src="../img/services/female_taxi.jpg"
                  class="img-responsive img-fluid"
                >
                <a :href="`/${$i18n.locale}/female-service`">Женское такси </a>
              </div>
            </b-col>
            <b-col align-self="center">
              <ul class="services-more__list">
                <li>
                  У нас вы можете заказать «женское такси» в любое время - так, чтобы
                  каждая женщина могла быть забрана водителем по запросу.
                </li> 
                <li>
                  Сервис «женщина водит женщину» полностью интегрирован в другие
                  сервисы.
                </li> 
                <li>
                  Местные поездки, трансферы из аэропорта, транспортировка
                  пациентов на кассе - клиент королева!
                </li>
              </ul>
            </b-col>
          </b-row>
        </b-col>
        <b-col xl="12">
          <div class="services-more__subtitle text-center my-4">
            Медицинские поездки
          </div>
          <b-row class="mb-5">
            <b-col xl="7">
              <div class="img-wrap">		
                <img
                  src="../img/services/hospital.jpg"
                  class="img-responsive img-fluid"
                >
                <a :href="`/${$i18n.locale}/medical-service`">Медицинские поездки</a>
              </div>
            </b-col>
            <b-col align-self="center">
              <ul class="services-more__list">
                <li>Поездки на прием к врачу</li> 
                <li>Бесплатные транспортные услуги  для пациентов</li> 
                <li>У нас есть радио-коляска</li>
                <li>Оздоровительные поездки</li>
                <li>Наши сотрудники проходят регулярную медицинскую подготовку.</li>
              </ul>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </section>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Footer from "@/components/Footer.vue";
export default {
    name: "Services",
    components: {
        Footer
    }
};

</script>
