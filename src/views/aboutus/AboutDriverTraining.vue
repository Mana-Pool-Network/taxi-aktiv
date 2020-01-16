<template>
  <div class="training">
    <div class="content mb-5">
      <header class="training-bg pb-3">
        <div class="container-fluid">
          <div class="training-block text-center">
            <div class="training-block__title">
              Программа профессионального роста водителей по системе Kick Down
            </div>
          </div>
        </div>
      </header>
      <div class="container mt-5">
        <b-row>
          <b-col xl="6">
            <p class="training-text">
              Taxi Aktiv Koeln уделяет большое внимание профессиональному росту наших
              водителей. 
            </p> 
            <p class="training-text">
              Это соответствует нашей цели к самосовершенствованию и
              стремлению быть лучше.
            </p>
            <p class="training-text">
              Для реализации системы профессионального роста наших водителей мы
              внедрили систему Kick Down.
            </p>
          </b-col>
          <b-col xl="6">
            <p class="training-text">
              Эта программа от нашего диджитального партнёра
              подразумевает цикл семинаров, где водители, диспетчеры и владельцы сервисов
              могут обмениваться знаниями друг с другом, для совместного роста и развития.
            </p> 
            <p class="training-text">
              Фактически мы принимаем участие в полноценной образовательной платформе,
              которая очень хорошо отвечает духу диджитальной среды.
            </p>
          </b-col>
          <b-col
            class="training-textbg p-4"
            xl="6"
          >
            <h4>КАК РАБОТАЕТ ЭТА СИСТЕМА?</h4>
            <p class="training-text">
              С периодичностью в 6-12 месяцев происходит семинар, на котором
              собираются представители рынка транспортных перевозок.
            </p> 
            <p class="training-text">
              В рамках площадки
              есть отдельная секция по работе с водителями. Она содержит несколько типов
              работы, и, с одной стороны, предполагает проверку знания водителем правил
              дорожного движения, а с другой — тренинги, посвященные развитию
              личностного общения с клиентом, пониманию его психологии, правильному
              взаимодействию во время поездки.
            </p>
            <p class="training-text">
              Доклады, панельные дискуссии обеспечивают
              не только сухую теоретическую подготовку, но и возможность обсуждения
              практических кейсов в работе водителей.
            </p>
          </b-col>
          <b-col
          
            class="training-textbg p-4"
            xl="6"
          >
            <p class="training-text">
              Кроме теоретических обсуждений, для водителя предусмотрена и
              практическая часть, связанная с проверкой правильной езды на дороге.
            </p> 
            <p class="training-text">
              Верная езда — это не только соблюдение правил дорожного движения. Это искусство
              управления возможностями автомобиля так, чтобы клиенту было комфортно
              добираться. 
            </p> 
            <p class="training-text">
              Тренировка плавности разгона и торможения, корректной постановке
              таких вопросов, как музыка, климат-контроль и т.д.
            </p> 
          </b-col>
        </b-row>
        <div class="training-title mt-4 text-center">
          Taxi Aktiv Koeln ежедневно работает для Вашего комфорта
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
    name: "AboutDriverTraining",
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