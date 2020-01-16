<template>
  <div class="software">
    <div class="content mb-5">
      <header class="training-bg pb-3">
        <div class="container-fluid">
          <div class="training-block text-center">
            <div class="training-block__title">
              Программное обеспечение
            </div>
          </div>
          <div class="software-subtitle ">
            Программное обеспечение, которое используется нами поможет вам в
            несколько кликов и абсолютно безопасно заказать поездку у нас
          </div>
        </div>
      </header>
      <div class="container mt-5">
        <b-row>
          <b-col xl="6">
            <p class="training-text">
              Для того, чтобы Вы могли легко и быстро заказать подачу машины, у нас
              работает экосистема программ.           Развитая многофункциональная программа
              диспонента позволит обработать Ваш заказ в считанные секунды.                 Мощный
              модуль картографии позволит расчитать наиболее оптимальный маршрут
              поездки, чтобы избежать пробок и других дорожных препятствий. 
            </p> 
            <p class="training-text">
              Удобное
              приложение клиента позволит Вам заказать и оплатить поездку, указать особые
              пожелания (например для медицинской поездки). Последующие заказы будут ещё
              легче и быстрее, а также принесут Вам бонусы, которые можно использовать в
              призовых поездках.
            </p>
          </b-col>
          <b-col xl="6">
            <p class="training-text">
              Кроме того программа позволит Вам отследить перемещение автомобиля в
              реальном времени, даже если у Вас не установлен клиентский App. Когда машина
              прибывает в точку А, вы получите SMS с ссылкой на карту, по которой вы
              сможете посмотреть где находится автомобиль.
            </p> 
            <p class="training-text">
              <b>
                Вы отправили ребёнка в школу на
                машине? 
              </b>
            </p>
            <p class="training-text">
              Можете быть спокойны и уверены в безопасности поездки, убедившись,
              что водитель следует правильному маршруту.
            </p>
          </b-col>
        </b-row>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Footer from "@/components/Footer.vue";
export default {
    name: "AboutSoftware",
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