<template>
  <div class="main medical">
    <div class="content ">
      <div class="container">
        <div class="shuttle-block limousine-whyus__block text-center py-3 my-4 mb-5">
          <div class="shuttle-block__title">
            Медицинские поездки
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
              <p class="medical-text">
                Если вам нужен транспорт на такси, потому что вы должны быть
                доставлены к врачу (например, серии
                поездок на облучение, диализ и т. Д.);
              </p>
              <p class="medical-title">
                Как вы получаете бесплатные транспортные
                услуги для пациентов?
              </p>
              <p class="medical-text">
                Для этого вы подаете заявление на получение разрешения от вашей
                медицинской страховой компании на один или несколько поездок. Отправьте
                нам это разрешение и договоритесь о приеме на прием, если известно о
                посещении вашего врача или больницы.
              </p>
              <p class="medical-title">
                Вам нужна радиоуправляемая инвалидная коляска и вам нужно добраться от
                пункта А в пункт Б?
              </p>
              <p class="medical-text">
                Теперь у нас есть радио-коляска. Закажите это и пусть наши дружелюбные и
                обученные сотрудники доставят вас к месту назначения.
              </p>
            </b-col>
            <b-col
              xl="6"
              lg="6"
              md="12"
              sm="12"
            >
              <p class="medical-title">
                Мы также можем предложить оздоровительные поездки.
              </p>
              <p class="medical-text">
                Просто отправьте нам свое разрешение и, если применимо, вашу карту освобождения /
                сертификат об освобождении, и мы немедленно выставим счет на вашу
                медицинскую страховку.<br>
                <a
                  href="#"
                  class="medical-a"
                >Позвоните нам</a> 
              </p>
              <p class="medical-text">
                Даже при кратковременных встречах мы своевременно и безопасно
                доставляем вас на прием к врачу. В конце поездки вы только подтверждаете
                выполненную поездку без оплаты. Затем один раз в месяц мы отправляем
                дорожные расходы в вашу медицинскую страховку.
              </p>
              <p class="medical-text">
                Мы используем современные машины скорой помощи для перевозки всех
                пациентов. 
              </p>
              <p class="medical-text">
                Наши сотрудники проходят регулярную медицинскую подготовку.
              </p>
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
    name: "MedicalService",
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
.medical {
   background: linear-gradient( rgba(255, 255, 255, 0.7)), url("../../img/services/hospital.jpg") no-repeat center center fixed !important;
   background-color: white !important;
   background-size: cover;
}
</style>