<template>
  <div class="jobs">
    <div class="content">
      <header class="jobs-bg pb-3">
        <div class="container">
          <div class="aboutus-block text-center">
            <div class="aboutus-block__title">
              Jobs
            </div>
          </div>
          <div class="jobs-subtitle text-center mb-3">
            Zur Unterstützung unseres Teams suchen wir zum nächstmöglichen Zeitpunkt
          </div>
        </div>
        <div class="container">
          <b-row>
            <b-col
              xl="6"
              lg="6"
              md="12"
              sm="12"
              class="mb-4"
            >
              <div class="jobs-textbg px-3 pt-3 pb-1 mb-4">
                <p class="jobs-text">
                  Fahrer / Chauffeure (w/m)
                  für den Chaufeutservice Aushilfe.
                </p>
              </div>
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
              xl="6"
              lg="6"
              md="12"
              class="mb-4"
            >
              <div class="jobs-textbg p-3">
                <p class="jobs-text">
                  Voraussetzungen:
                </p>
                <p class="jobs-text">
                  <ul>
                    <li>Qualifikation Fahrerlaubnis min. Klasse B</li>
                    <li> Gepflegtes Erscheinungsbild</li>
                    <li> Personenbeförderungsschein von Vorteil.</li>
                  </ul>
                </p>
                <p class="jobs-text">
                  Wenn Sie zudem Freude am Umgang mit Menschen haben, zuverlässig, pünktlich und teamfähig sind, freuen wir
                  uns auf Ihre aussagekräftige Bewerbung.
                </p>
              </div>
            </b-col>
          </b-row>
        </div>
      </header>
      <main>
        <div class="container">
          <b-row> 
            <b-col
              class="my-4"
              xl="12"
              lg="12"
              md="12"
              sm="12"
            >
              <div class="jobs-title text-center mb-4">
                füllen Sie unsere
              </div>
              <div class="jobs-form">
                <b-form
                  class="px-5"
                  @submit="onSubmit"
                >
                  <label
                    for="inp"
                    class="inp my-2 mt-4"
                  >
                    <input
                      id="inp"
                      v-model="form.name"
                      type="text"
                      required
                      placeholder="   "
                    >
                    <span class="label">Имя</span>
                    <span class="border1" />
                  </label>
                  <label
                    for="inp2"
                    class="inp my-2"
                  >
                    <input
                      id="inp2"
                      v-model="form.lastname"
                      type="text"
                      required
                      placeholder="   "
                    >
                    <span class="label">Фамилия</span>
                    <span class="border1" />
                  </label>
                  <label
                    for="inp3"
                    class="inp my-2"
                  >
                    <input
                      id="inp3"
                      v-model="form.email"
                      type="email"
                      required
                      placeholder="   "
                    >
                    <span class="label"> E-Mail-Adresse</span>
                    <span class="border1" />
                  </label>
                  <label
                    for="inp4"
                    class="inp my-2"
                  >
                    <input
                      id="in4"
                      v-model="form.phone"
                      type="tel"
                      required
                      placeholder="   "
                    >
                    <span class="label">Телефон</span>
                    <span class="border1" />
                  </label>
                  <label
                    for="inp5"
                    class="inp my-2"
                  >
                    <input
                      id="inp5"
                      v-model="form.birthday"
                      type="date"
                      required
                      placeholder="   "
                    >
                    <span class="label">Дата рождения</span>
                    <span class="border1" />
                  </label>

                  <!-- Выбор -->
                  <div class="checkbox-container my-3">
                    <div class="input-title">
                      Geschlecht:
                    </div>
                    <label class="checkbox-label">
                      <input
                        v-model="form.gender"
                        class="jobs-form__checkbox"
                        type="checkbox"
                        value="true"
                        :true-value="form.weiblich"
                        :false-value="form.manlich"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      weiblich
                    </div>
                    <label class="checkbox-label">
                      <input
                        v-model="form.gender"
                        type="checkbox"
                        value="true"
                        :true-value="form.manlich"
                        :false-value="form.weiblich"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      männlich
                    </div>
                  </div>

                  <div class="text-left">
                    <div class="d-inline-block mr-3">
                      Berufserfahrung:
                    </div>
                    
                    <div
                      class="custom-dropdown "
                    >
                      <select
                        v-model="form.state"
                        class="form-control"
                      >
                        <option
                          disabled
                          value=""
                        >
                          State
                        </option>
                        <option
                          v-for="(state, key) in states"
                          :key="key"
                          :value="state"
                        >
                          {{ key }}
                        </option>
                      </select>
                    </div>
                  </div>
                  <!-- Выбор -->
                  <div class="checkbox-container my-3">
                    <div class="input-title">
                      Führerschein Kl.B:
                    </div>
                    <label class="checkbox-label">
                      <input
                        v-model="form.drivingLicense"
                        class="jobs-form__checkbox"
                        type="checkbox"
                        value="true"
                        :true-value="form.yes"
                        :false-value="form.no"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      Ja
                    </div>
                    <label class="checkbox-label">
                      <input
                        v-model="form.drivingLicense"
                        type="checkbox"
                        value="true"
                        :true-value="form.no"
                        :false-value="form.yes"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      Nein
                    </div>
                  </div>
                  <!-- Выбор -->
                  <div class="checkbox-container my-3">
                    <div class="input-title">
                      Personenbeförderungsschein:
                    </div>
                    <label class="checkbox-label">
                      <input
                        v-model="form.passengerTransport"
                        class="jobs-form__checkbox"
                        type="checkbox"
                        value="true"
                        :true-value="form.yes"
                        :false-value="form.no"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      Ja
                    </div>
                    <label class="checkbox-label">
                      <input
                        v-model="form.passengerTransport"
                        type="checkbox"
                        value="true"
                        :true-value="form.no"
                        :false-value="form.yes"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      Nein
                    </div>
                  </div>
                  <label
                    for="inp6"
                    class="inp my-2"
                  >
                    <textarea
                      id="inp6"
                      v-model="form.otherQualifications"
                      placeholder="   "
                    />
                    <span class="label">Zusatzqualifikation:</span>
                    <span class="border1" />
                  </label>
                  


                  <div class="checkbox-container my-3">
                    <div class="input-title">
                      Gewünschter Vertrag: 
                    </div>
                    <label class="checkbox-label">
                      <input
                        v-model="form.contract"
                        :true-value="form.fullTime"
                        class="jobs-form__checkbox"
                        type="checkbox"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      Vollzeit
                    </div>
                    <label class="checkbox-label">
                      <input 
                        v-model="form.contract"
                        :true-value="form.partTime"
                        type="checkbox"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      Teilzeit
                    </div>
                    <label class="checkbox-label">
                      <input
                        v-model="form.contract"
                        :true-value="form.temporaryHelp"
                        type="checkbox"
                      >
                      <span class="checkbox-custom rectangular" />
                    </label>
                    <div class="input-subtitle">
                      Aushilfe
                    </div>
                  </div>
                  <label
                    for="inp7"
                    class="inp my-2"
                  >
                    <textarea
                      id="inp7"
                      v-model="form.remarks"
                      placeholder="   "
                    />
                    <span class="label">Anmerkungen::</span>
                    <span class="border1" />
                  </label>
                  <!-- файл -->
                  <div class="jobs-form__filetext">
                    Hier können Sie Ihre Bewerbungsunterlagen im PDF oder Word Format anhängen.(max 5 mb)
                  </div>
                  <!-- <b-form-file
                    v-model="file"
                    class="mt-3"
                    plain
                  /> -->

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
      </main>
    </div>
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import Footer from "@/components/Footer.vue";
export default {
    name: "Jobs",
    components: {
        Footer
    },
    data() {
        return {
            states: {
                AL: 'Alabama',
                AK: 'Alaska',
                AR: 'Arizona',
                CA: 'California',
                NV: 'Nevada'
            },
            form: {
                name: '',
                lastname:'',
                email: '',
                birthday:'',
                phone: '',
                otherQualifications: '',
                remarks: '',
                state: '',
                file: '',
                gender: '',
                weiblich: 'female',
                manlich: 'male',
                drivingLicense: '',
                passengerTransport: '',
                yes: 'yes',
                no: 'no',
                contract: '', 
                fullTime: "Vollzeit",
                partTime: "Teilzeit",
                temporaryHelp: "Aushilfe" 
            },            
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault();
            console.log(JSON.stringify(this.form))
            axios
                .post("http://192.168.1.123:8000/api/vacancy/", {
                    name: this.form.name + " " + this.form.lastname,
                    email: this.form.email,
                    birth_date: this.birthday,
                    sex: this.gender,
                    driver_license_id: this.form.drivingLicense,
                    passenger_transport_license: this.form,
                    additional_qualification: this.form,
                    contact_info: this.form,
                    comment: this.form,
                    resume: this.form,
                    tel: this.form,
                })
                .then(response => {
                    console.log(response);
                })
        },
    },
};

</script>

<style>
.input-title, .input-subtitle {
  display: inline-block;
}
.input-subtitle {
  position: relative;
  left: 50px;
  margin-right: 40px;
}
.checkbox-label {
    display: inline-block;
    position: relative;
    cursor: pointer;
    width: 5px;
}
.checkbox-label input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
}

.checkbox-label .checkbox-custom {
    position: absolute;
    left: 20px;
    bottom: -13px;
    height: 24px;
    width: 24px;
    background-color: transparent;
    border-radius: 5px;
  	transition: all 0.3s ease-out;
  	-webkit-transition: all 0.3s ease-out;
  	-moz-transition: all 0.3s ease-out;
  	-ms-transition: all 0.3s ease-out;
  	-o-transition: all 0.3s ease-out;
    border: 2px solid #110239;
}


.checkbox-label input:checked ~ .checkbox-custom {
    background-color: #E8E7E1;
    border-radius: 5px;
    -webkit-transform: rotate(0deg) scale(1);
    -ms-transform: rotate(0deg) scale(1);
    transform: rotate(0deg) scale(1);
    opacity:1;
    border: 2px solid #110239;
}


.checkbox-label .checkbox-custom::after {
    position: absolute;
    content: "";
    left: 12px;
    top: 12px;
    height: 0px;
    width: 0px;
    border-radius: 5px;
    border: solid #110239;
    border-width: 0 3px 3px 0;
    -webkit-transform: rotate(0deg) scale(0);
    -ms-transform: rotate(0deg) scale(0);
    transform: rotate(0deg) scale(0);
    opacity:1;
  	transition: all 0.3s ease-out;
  	-webkit-transition: all 0.3s ease-out;
  	-moz-transition: all 0.3s ease-out;
  	-ms-transition: all 0.3s ease-out;
  	-o-transition: all 0.3s ease-out;
}


.checkbox-label input:checked ~ .checkbox-custom::after {
  -webkit-transform: rotate(45deg) scale(1);
  -ms-transform: rotate(45deg) scale(1);
  transform: rotate(45deg) scale(1);
  opacity:1;
  left: 8px;
  top: 3px;
  width: 6px;
  height: 12px;
  border: solid #110239;
  border-width: 0 2px 2px 0;
  background-color: transparent;
  border-radius: 0;
}



/* For Ripple Effect */
.checkbox-label .checkbox-custom::before {
    position: absolute;
    content: "";
    left: 10px;
    top: 10px;
    width: 0px;
    height: 0px;
    border-radius: 5px;
    border: 2px solid #FFFFFF;
    -webkit-transform: scale(0);
    -ms-transform: scale(0);
    transform: scale(0);	
}

.checkbox-label input:checked ~ .checkbox-custom::before {
    left: -3px;
    top: -3px;
    width: 24px;
    height: 24px;
    border-radius: 5px;
    -webkit-transform: scale(3);
    -ms-transform: scale(3);
    transform: scale(3);
    opacity:0;
    z-index: 999;
    transition: all 0.3s ease-out;
  	-webkit-transition: all 0.3s ease-out;
  	-moz-transition: all 0.3s ease-out;
  	-ms-transition: all 0.3s ease-out;
  	-o-transition: all 0.3s ease-out;
}



</style>