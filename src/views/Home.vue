<template
  :isShown="isShown"
  :isProgressing="isProgressing"
  :myToggler="myToggler"
>
  <div
    class="home "
  >
    <div class="content">
      <div class="banner">
        <video
          style=" background: linear-gradient(0deg, rgba(196, 196, 196, 0.5), rgba(196, 196, 196, 0.5));opacity:0.5"
          autoplay
          muted
          loop
        >
          <source
            src="../img/home/bg-video.mp4"
            type="video/mp4"
          >
          
        </video>
        <div class="contents">
          <div class="contents-block">
            <h1>Taxi Aktiv Koeln</h1>
            <h2>24/7/365</h2>
          </div>


          <div class="modal-video">
            <a
              v-b-modal.modal-center
              class="modalBtn"
              href="#"
            ><svg
              width="61"
              height="44"
              viewBox="0 0 61 44"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M52.5 23C52.5 34.2704 42.2569 43.5 29.5 43.5C16.7431 43.5 6.5 34.2704 6.5 23C6.5 11.7296 16.7431 2.5 29.5 2.5C42.2569 2.5 52.5 11.7296 52.5 23Z"
                stroke="white"
              />
              <path
                class="q"
                d="M41 23.5L24.5 33.4593V13.5407L41 23.5Z"
                fill="white"
              />
            </svg>
            </a> 

            <b-modal
              id="modal-center"
              class="p-0"
              hide-footer
              hide-header
              centered
              size="lg"
            >
              <iframe
                class="youtube-video"
                src="https://www.youtube-nocookie.com/embed/j2RDQTcx_eY?autoplay=1;controls=0"
                frameborder="0"
                allow="accelerometer; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
              />
            </b-modal>
          </div>
        </div>
      </div>
      
      <!-- /.home-request -->
      <p>
        {{ $t('message') }}
      </p>
      <h1 class="wow shake">
        Example
      </h1>
      <div
        v-wow="{ 'animation-name': 'jello','animation-duration': '4s'}"
        class="container about holder jello"
      >
        <b-row>
          <div class="about-title text-center mt-3 wow shake">
            <h1>Chauffeur — und Limousinenservic </h1>
          </div>
          <b-col xl="7">
            <div class="about-subtitle ml-4">
              Taxi Aktiv Koeln
            </div>
            <p
              class=" about-text mt-2 wow fadeIn"
            >
              Наша фирма специализируется на перевозках людей.
              <span>Более 25 лет мы</span>  безупречно работаем в Кёльне. Профессиональные
              сертифицированные водители, с большим опытом работы и <span>первоклассным сервисом</span>
              предоставляют услуги шофёра и лимузина. <br>
            </p>
            <p class="about-text mb-4">
              Мы готовы встретить и доставить вас в нужное место <span>24/7/365</span>.
            </p>
            <div class="ml-3 mb-5 about-detailed">
              <a
                :href="`/${$i18n.locale}/limousine-service`"
              >
                Подробнее о лимузин сервисе и водительских услугах >
              </a>
            </div>
          
            <img
              class=" img-fluid mt-5"
              src="../img/home/about-car.jpg"
              alt="машина"
            >
          </b-col>
          <b-col
            xl="5"
            class="text-center mb-5 "
          >
            <div class="trees">
              <div
                class="trees-title"
              >
                {{ tree.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") }} km
              </div>
              <div class="trees-subtitle mt-4">
                c Jan 1, 2019. {{ eyro.toFixed(1).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") }} € потрачено на посадку новых
                деревьев.
              </div>
              <div
                class="trees-detailed text-left d-flex justify-content-between align-items-center  mt-3"
              >
                <a
                  class="trees-a"
                  :href="`/${$i18n.locale}/ecology`"
                >Узнайте больше об экологической программе</a> <button
                  :onClick="`location.href=&quot;/${$i18n.locale}/ecology&quot;`"
                  class="home-request-block-btn trees-btn"
                >
                  >
                </button>
              </div>
            </div>
          </b-col>
        </b-row>
      </div>
      <!-- /.about -->

      <div class="home-services text-center container mt-2 mb-5">
        <div class="home-services-title mb-5">
          Все наши услуги для Вас
        </div> 
        <b-row>
          <b-col
            xl="6"
            lg="6"
            class="mb-2"
          >
            <div class="img-wrap ">		
              <img
                src="../img/home/home-services/11.jpg"
                class=" img-responsive img-fluid "
              >
              <a
                class="pt-xl-3 pt-md-1"
                :href="`/${$i18n.locale}/limousine-service`"
              >Шофер - лимузин сервис</a>
            </div>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <div
              class="img-wrap "
            >		
              <img
                
                src="../img/home/home-services/22.jpg"
                class="img-responsive img-fluid shuttle"
              >
              <a
                class="pt-xl-3 pt-md-1"
                :href="`/${$i18n.locale}/shuttle-service`"
              >Шаттл-сервис</a>
            </div>
          </b-col>
        </b-row>
      </div>
      <!-- /.home-services -->

      <div class="city mb-5 ">
        <div class="container text-center">
          <b-row
            align-v="center"
            align-h="center"
          >
            <b-col
              xl="6"
              lg="6"
              md="6"
              align-self="center"
            >
              <div class="city-statistics-block">
                <p class="statistics-text pt-4 p-2 mt-4">
                  {{ qtClients.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") }} довольных клиентов <br>
                  из региона и других стран
                </p>
              </div>
            </b-col>
            <b-col
              xl="6"
              lg="6"
              md="6"
            >
              <div class="city-statistics-block">
                <p class="statistics-text pt-4 p-2 mt-4">
                  {{ qtKilometers.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") }} km мы проехали <br> с 1997 года
                </p>
              </div>
            </b-col>
          </b-row>
        </div>
      </div>
      <!-- /.city -->
      <div>
        <div class="flot mb-3">
          <div
            v-wow="{ 'animation-name': 'fadeInUp','animation-duration': '5s'}"
            class="holder fadeInUp container-fluid text-center"
          >
            <div class="home-services-title mb-4">
              Наш современный и комфортный флот
            </div> 
            <b-row>
              <b-col
                xl="3"
                lg="3"
                md="6"
                sm="6"
              >
                <img
                  class="img-fluid m-2"
                  src="../img/home/flot/1.jpg"
                  alt="машины"
                >
              </b-col>
              <b-col
                xl="3"
                lg="3"
                md="6"
                sm="6"
              >
                <img
                  class="img-fluid m-2"
                  src="../img/home/flot/2.jpg"
                  alt="машины"
                >
              </b-col>
              <b-col
                xl="3"
                lg="3"
                md="6"
                sm="6"
              >
                <img
                  class="img-fluid m-2"
                  src="../img/home/flot/3.jpg"
                  alt="машины"
                >
              </b-col>
              <b-col
                xl="3"
                lg="3"
                md="6"
                sm="6"
              >
                <img
                  class="img-fluid mt-2 mb-2 ml-2"
                  src="../img/home/flot/4.jpg"
                  alt="машины"
                >
              </b-col>
            </b-row>
            <button
              :onClick="`location.href=&quot;/${$i18n.locale}/flot&quot;`"
              class="flot-btn mt-3"
            >
              Посетите флот Taxi Aktiv >
            </button>
          </div>
        </div>
        <!-- /.flot -->

        <div class="forus container text-left  mb-5">
          <b-row>
            <b-col>
              <div class="forus-first-text mt-5 wow shake">
                <span class="about-subtitle ">
                  Taxi Aktiv Koeln
                </span>— это лидер в городе Кёльне, с историей успеха
                более 25 лет.<br>
              </div>
              <div
                class="forus-first-text"
              >
                Мы специализируемся на перевозках и предоставляем услуги
                класса Chauffer&amp;
                Limousineservice, а также — трансферы из центра Кёльна
                в аэропорт и обратно.
                Независимо от того где находится наш клиент, мы предлагаем
                первоклассный сервис.
              </div>
              <div class="forus-first-text">
                В режиме 24/7/365 и независимо от
                метеорологических условий мы заберём клиента из любой точки Кёльна и
                доставим в точку, куда он направляется.
                <br>Начните знакомство с Кёльном вместе с нами!
              </div>
            </b-col>
            <b-col
              xl="1"
              lg="1"
              align-self="center"
            >
              <div class="text-center lines" />
            </b-col>
            <b-col>
              <div class="forus-second-text mt-5">
                Мы любим наших
                клиентов и предлагаем вам комфортные поездки и премиум сервис.<br>
                Taxi Aktiv Koeln — ваш надежный партнёр и друг в Кёльне.<br>
              </div>
              <div class="forus-second-text ">
                Особое внимание мы уделяем вопросам экологической безопасности
                и добропорядочности. Наш парк состоит из автомобилей марки Mersedez-
                Benz. Мы обновляем свой парк моделями, собранными с учётом самых
                актуальных экологических требований и директив.
                <br>
                <br>Наш метод — первоклассный сервис.
                <br>Наша цель — довольный клиент.
              </div>
            </b-col>
          </b-row>
        </div>
      </div>
      <div
        v-wow="{ 'animation-name': 'fadeInUp','animation-duration': '1s'}"
        class="holder fadeInUp"
      >
        asdasdasd
      </div>
      <Footer />
    </div>
  </div>
</template>

<script>

// @ is an alias to /src
import Footer from "@/components/Footer.vue";
export default {
    name: "Home",
    components: {
        Footer,
        
    },
    props: ["isShown", "isProgressing", "myToggler", "test"],
    data() {
        return {
            showWithDelay: false,
            z: 0,
            eyro: 1725,
            tree: 1500000,
            qtClients:68000,
            qtKilometers:37000000,
            num: 999999,
            value: 1000,
            show: true
        }
    },
    mounted() {
        
        this.startInterval() 
        setTimeout(()=>{
            this.showWithDelay = true
        },2000)
    },
    methods: {
        startInterval: function () {
            setInterval(() => {
                this.tree += 1
                this.eyro += 0.1
                this.qtKilometers +=1
            }, 30000);
            setInterval(() => {
                this.qtClients +=1
            }, 60000);        
        },
    }
};

</script>
<style>
</style>