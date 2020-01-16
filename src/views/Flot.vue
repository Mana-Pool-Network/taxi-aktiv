<template>
  <div class="flot">
    <div class="content">
      <header class="flot-bg pb-3">
        <div class="container-fluid">
          <div class="flot-block text-center">
            <div class="flot-block__title">
              КОМФОРТ В МЕЛОЧАХ
            </div>
          </div>
        </div>
      </header>
      <main class="container mt-5">
        <b-row>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="flot-text">
              Пассажирский флот Taxi Aktiv Koeln состоит из Mersedes Benz E Klass
              новейшей сборки. Мы обновляем его каждые 2 года.
            </p>
            <p class="flot-text">
              Это — первоклассная модель автомобиля, разработанная немецкими инженерами, собранная на
              заводах в Германии и соответствующая последним экологическим директивам
              по нормативам выбросов выхлопных газов.
            </p>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="flot-text">
              Каждая из машин имеет просторный кожаный салон, оснащённый
              различными дополнениями, которые призваны сделать ваше путешествие
              комфортным.
            </p>
            <p class="flot-text">
              Отличная аэродинамика, плавный ход позволят расслабиться вам
              во время дороги и думать о важном.
            </p>
            <p class="flot-text">
              Мы полагаем, что настоящий комфорт достигается только в том случае,
              если думать о мелких деталях и воплощать их в сервисе.
            </p>
          </b-col>
          <b-col xl="12">
            <div class="limousine-block text-center py-3 my-4">
              <div class="services-block__title">
                Наш флот
              </div>
            </div>
          </b-col>
          <b-col
            class="text-center p-2"
            xl="6"
            lg="6"
          >
            <img
              src=""
              alt="тут должна быть картинка"
              class="img-fluid"
            >
          </b-col>
          <b-col
            class="text-center p-2"
            xl="6"
            lg="6"
          >
            <img
              src=""
              alt="тут должна быть картинка"
              class="img-fluid"
            >
          </b-col>
          <b-col
            class="text-center p-2"
            xl="6"
            lg="6"
          >
            <img
              src=""
              alt="тут должна быть картинка"
              class="img-fluid"
            >
          </b-col>
          <b-col
            class="text-center p-2"
            xl="6"
            lg="6"
          >
            <img
              src=""
              alt="тут должна быть картинка"
              class="img-fluid"
            >
          </b-col>
        </b-row>
      </main>
      <div class="flot-about my-5">
        <div class="container text-center">
          <div class="flot-about__text p-5">
            TAXI AKTIV KOELN НА СТРАЖЕ ЗАБОТЫ ОБ ОКРУЖАЮЩЕЙ ПРИРОДЕ
          </div>
        </div>
      </div>
      <div class="container">
        <b-row>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="flot-text">
              Мы стараемся уменьшить количество пустых километров, ограничить
              расход топлива и снизить выбросы выхлопных газов. 
            </p>
            <p class="flot-text">
              Мы делаем это в двух
              направлениях и реализуем две программы.
            </p>
            <p class="flot-text">
              Первая программа связана с дигитализацией. На фирме мы внедрили
              новейшие разработки в области программ, которые выполняют очень большое
              количество задач. Наша бухгалтерия, алгоритмы формирования электронных
              отчётов позволяют меньше печатать на бумаге.
            </p>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="flot-text">
              Больше 54 математических формул определяют какому водителю стоит
              ехать в точку А и как проехать по самому короткому и оптимальному
              маршруту, с избежанием пробок и других препятствий.
            </p> <p class="flot-text">
              Благодаря
              дигитализации мы сократили количество пустых километров и снизили
              выбросы вредных выхлопных газов.
            </p> <p class="flot-text">
              Вторая программа — озеленение. Используя часть своего дохода, мы
              высаживаем новые деревья, которые помогают бороться с углекислым газом.
            </p>
          </b-col>
          <b-col
            xl="12"
            lg="12"
          >
            <div class="flot-title text-center my-5">
              Пользуясь нашим сервисом, вы можете быть спокойны за экологию!
            </div>
          </b-col>
        </b-row>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
export default {
    name: "Flot",
    components: {
        Footer
    }
};

</script>

<style>

</style>