<template>
  <div class="contacts">
    <div class="content">
      <div class="container">
        <div class="contacts-block text-center mt-5 mb-3">
          <div class="contacts-block__title">
            Контакты
          </div>
        </div>
        <b-row> 
          <b-col
            align-self="center"
            xl="6"
            lg="6"
          >
            <p class="contacts-text">
              Если вы хотите узнать больше о работе Taxi Aktiv Koeln или имеете
              предложение о сотрудничестве, то вы можете обратиться к нам, позвонив по
              телефону или написав письмо на электронную почту.
            </p>
            <div class="contacts-adress text-center">
              <div class="contacts-adress__title mb-3">
                Наш адрес:
              </div>
              <div class="contacts-adress__text">
                FIRMA AKTIV TAXI
                Olpener Str. 690
                51109 Köln
              </div>
            </div>
          </b-col>
          <b-col
            class="my-4"
            xl="6"
            lg="6"
          >
            <div class="contacts-form">
              <div class="contacts-form__title text-center py-3">
                Отправте нам сообщение
              </div>
              <b-form
                class="px-4"
                @submit="onSubmit"
              >
                <div class="text-center pb-3">
                  <div
                    class="custom-dropdown "
                  >
                    <select
                      v-model="form.state"
                      required
                      class="form-control"
                    >
                      <option
                        
                        disabled
                        value=""
                      >
                        Betreff (Pflichtfeld)
                      </option>
                      <option
                        v-for="(state, key) in states"
                        :key="key"
                        :value="state"
                      >
                        {{ state }}
                      </option>
                    </select>
                  </div>
                </div>
                
                <label
                  for="inp"
                  class="inp my-2"
                >
                  <input
                    id="inp"
                    v-model="form.name"
                    type="text"
                    required
                    placeholder="   "
                  >
                  <span class="label">Ihr Name (Pflichtfeld)</span>
                  <span class="border1" />
                </label>
                
                <label
                  for="inp2"
                  class="inp my-2"
                >
                  <input
                    id="inp2"
                    v-model="form.email"
                    type="email"
                    required
                    placeholder="   "
                  >
                  <span class="label">Ihre E-Mail-Adresse (Pflichtfeld)</span>
                  <span class="border1" />
                </label>
                <label
                  for="inp3"
                  class="inp my-2"
                >
                  <textarea
                    id="inp3"
                    v-model="form.text"
                    placeholder="   "
                  />
                  <span class="label">Ihre Nachricht</span>
                  <span class="border1" />
                </label>
                <div>
                  <vue-recaptcha
                    ref="recaptcha"
                    class="captcha"
                    :sitekey="sitekey"
                    @verify="onVerify"
                  />
                </div>
                <div class="text-center py-3">
                  <b-button
                    type="submit"
                    variant="contacts"
                    size="sm"
                  >
                    Отправить
                  </b-button>
                </div>
              </b-form>
            </div>
          </b-col>
        </b-row>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import Footer from "@/components/Footer.vue";
import VueRecaptcha from "vue-recaptcha";
export default {
    name: "Contacts",
    components: {
        Footer,
        VueRecaptcha,
    },
    data() {
        return {
            sitekey: '6Ldrp84UAAAAAETWXfam5GoCdEVYktGcCVei4iGe',
            states: {
                A: 'Angebot',
                B: 'Autfrag',
                C: 'Anfragen',
                D: 'Sonstiges',
            },
            form: { 
                state: '',
                name: '',
                email: '',
                text: '',
                captcha: ''
            },
        }
    },
    methods: {
        onSubmit() {
            axios
                .post("http://192.168.1.123:8000/api/contact/", {
                    title: this.form.state,
                    name: this.form.name,
                    email: this.form.email,
                    message: this.form.text,
                    captcha: this.captcha
                })
        },
        onVerify: function (response) {
            this.captcha = response
        },

    },

};

</script>

<style>

</style>