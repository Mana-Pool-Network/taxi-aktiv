<template>
  <div class="ecology">
    <div class="content">
      <header class="ecology-bg pb-3">
        <div class="container">
          <div class="ecology-head__title text-center pt-5 pb-3">
            Экология во имя будущего
          </div>
          <div class="ecology-head__subtitle pt-3 pb-3">
            <p>
              Руководство и сотрудники фирмы Taxi Aktiv Koeln стремятся быть
              лидерами не только на рынке шофер-лимузин-сервисов.
            </p>
            <p>
              Мы ощущаем ответственность перед будущими поколениями и поэтому
              вносим вклад в борьбу с углекислым газом.
            </p>
          </div>
        </div>
      </header>
      <main class="container mt-5 mb-5">
        <div class="ecology-program text-center mb-5">
          Программа «Экологическая доброчестность»
        </div>
        <b-row>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="ecology-text">
              Благодаря дигитализации мы сократили количество пустых километров и
              выбросов CO 2 в атмосферу. Но это недостаточно для уплаты долга природе,
              ведь углекислый газ нужно обратно превратить в кислород.
            </p>
            <p class="ecology-text">
              Поэтому в Taxi Aktiv Koeln была запущена программа «Экологическая добропорядочность»
            </p>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="ecology-text">
              Часть нашего дохода используется для покупки и высадки новых деревьев в
              регионе Кёльн. Мы тратим 2 цента с каждого километра, который проехали
              наши машины, покупаем саженцы деревьев и два раза в год высаживаем их в
              землю.
            </p>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <div class="ecology-why mt-5">
              <div class="ecology-why__text text-center">
                Зачем нам это нужно
              </div>
              <img
                src="../img/question.svg"
                alt=""
                class="ecology-why__img"
              >
            </div>
            <p class="ecology-text">
              Нашей командой движет понимание, что комфорт в мелочах — история не
              только про качество поездок. Это — понимание того, что комфорт состоит в
              том числе из того, чем мы дышим, где гуляем мы и наши дети? А также —
              какое будущее у нашей планеты и как правильно реагировать на изменение
              климата.
            </p>
            <p class="ecology-text">
              Taxi Aktiv Koeln — региональная фирма, но готовы делать вклад в развитие
              нашего социума. Мы верим, что небольшие усилия со стороны каждого
              способны кардинально изменить мир к лучшему.
            </p>
          </b-col>
          <b-col
            align-self="center"
            xl="6"
            lg="6"
          >
            <div class="cooperation">
              <div class="cooperation-title text-center pt-3">
                Предложения о сотрудничестве
              </div>
              <div class="cooperation-text px-4 py-4">
                <p class="ecology-text">
                  Мы открыты к сотрудничеству с другими фирмами, которые разделяют
                  наши идеи.
                </p>
                <p class="ecology-text">
                  У вас есть идеи и предложения по сотрудничеству?
                </p>
                <p class="ecology-text">
                  Свяжитесь с нами через 
                  <a
                    href="/contacts"
                    class="ecology-a"
                  >KONTAKT </a>   или напишите письмо.
                </p>
                <p class="ecology-text">
                  И пусть это станет началом хорошей истории.
                </p>
              </div>
            </div>
          </b-col>
        </b-row>
      </main>
    </div>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Footer from "@/components/Footer.vue";
export default {
    name: "Ecology",
    components: {
        Footer
    }
};

</script>

<style>

</style>