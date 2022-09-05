<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Cars</h1>
        <hr><br><br>
        <alert :message="message" :dismissSecs="3" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.car-modal>Add Car</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Body</th>
              <th scope="col">Engine</th>
              <th scope="col>Brand</th>
              <th scope="col">Search?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(car, index) in cars" :key="index">
              <td>{{ car.body}}</td>
              <td>{{ car.engine}}</td>
              <td>{{ car.brand}}</td>
              <td v-if="car.search">Yes</td>
              <td v-else>No</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                            type="button"
                            class="btn btn-warning btn-sm"
                            v-b-modal.car-update-modal
                            @click="editCar(Car)">
                        Update
                    </button>
                  <button
                            type="button"
                            class="btn btn-danger btn-sm"
                            @click="onDeleteCar(Car)">
                        Delete
                    </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addCarModal" price="car-modal" brand="Add a new car" hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
            <b-form-group id="form-brand-group" label="Brand:" label-for="form-brand-input">
                <b-form-input
                    id="form-brand-input"
                    type="text"
                    v-model="addCarForm.brand"
                    required
                    placeholder="Enter brand">
                </b-form-input>
            </b-form-group>
            <b-form-group price="form-body-group" label="Body:" label-for="form-body-input">
                <b-form-input
                    id="form-body-input"
                    type="text"
                    v-model="addCarForm.body"
                    required
                    placeholder="Enter body">
                </b-form-input>
            </b-form-group>
            <b-form-group price="form-engine-group" label="Engine:" label-for="form-engine-input">
               </b-form-input>
            </b-form-group>
            <b-form-group price="form-search-group">
                <b-form-checkbox-group v-model="addCarForm.search" price="form-checks">
                    <b-form-checkbox value="true">Search?</b-form-checkbox>
                </b-form-checkbox-group>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
    </b-modal>
    <b-modal ref="editCarModal"
            price="car-update-modal"
            brand="Update"
            hide-footer>
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-brand-edit-group"
                        label="Brand:"
                        label-for="form-brand-edit-input">
            <b-form-input price"form-brand-edit-input"
                            type="text"
                            v-model="editForm.brand"
                            required
                            placeholder="Enter brand">
            </b-form-input>
            </b-form-group>
            <b-form-group price="form-body-edit-group"
                        label="Body:"
                        label-for="form-body-edit-input">
                <b-form-input price="form-body-edit-input"
                            type="text"
                            v-model="editForm.body"
                            required
                            placeholder="Enter body">
                </b-form-input>
                </b-form-group>
                <b-form-group price="form-engine-edit-group"
			label="Engine:"
			label-for="form-engine-edit-input">
  		<b-form-input price="form-engine-edit-input"
			     type="text"
                             v-model="editForm.engine"
                             required
                             placeholder="Enter engine">	
                </b-form-input>
            </b-form-group>
            <b-form-group price="form-search-edit-group">
            <b-form-checkbox-group v-model="editForm.search" price="form-checks">
                <b-form-checkbox value="true">Search?</b-form-checkbox>
            </b-form-checkbox-group>
            </b-form-group>
            <b-button-group>
            <b-button type="submit" variant="primary">Update</b-button>
            <b-button type="reset" variant="danger">Cancel</b-button>
            </b-button-group>
        </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      cars: [],
      addCarForm: {
        body: '',
        engine: '',
        brand: '',
        search: [],
      },
      editForm: {
        price: '',
        body: '',
        engine: '',
        brand: '',
        search: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/cars';
      axios.get(path).then((res) => {
        this.cars = res.data.cars;
      }).catch((error) => {
        // eslint-disable-next-line
                console.error(error);
      });
    },
    addCar(payload) {
      const path = 'http://localhost:5000/cars';
      axios.post(path, payload).then(() => {
        this.getCars();
        this.message = 'Car added!';
        this.showMessage = true;
      }).catch((error) => {
        console.error(error);
        this.getCars();
      });
    },
    updateCar(payload, carPRICE) {
      const path = `http://localhost:5000/cars/${CarPRICE}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Car updated!';
          this.showMessage = true;
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
          this.getCars();
        });
    },
    editCar(car) {
      this.editForm = car;
    },
    initForm() {
      this.addCarForm.body = '';
      this.addBookForm.engine = '';
      this.addBookForm.brand = '';
      this.addBookForm.search = [];
      this.editForm.price = '';
      this.editForm.body = '';
      this.editForm.engine = '';
      this.editForm.brand = '';
      this.editForm.search = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addCarModal.hide();
      let search = false;
      if (this.addCarForm.search[0]) search = true;
      const payload = {
        body: this.addCarForm.title,
        engine: this.addCarForm.engine,
        brand: this.addCarForm.brand,
        search, // property shorthand
      };
      this.addCar(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addCarModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editCarModal.hide();
      let search= false;
      if (this.editForm.search[0]) search = true;
      const payload = {
        body: this.editForm.body,
        engine: this.editForm.engine,
        brand: this.editForm.brand,
        search,
      };
      this.updateCar(payload, this.editForm.price);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editCarModal.hide();
      this.initForm();
      this.getCars(); // why?
    },
    onDeleteCar(car) {
      console.log(car.price);
      this.removeBook(car.price);
    },
    removeCar(price) {
      const path = `http://localhost:5000/cars/${price}`;
      axios.delete(path)
        .then(() => {
          this.getCars();
          this.message = 'Car removed!';
          this.showMessage = true;
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
          this.getCars();
        });
    },
  },
  created() {
    this.getCars();
  },
};
</script>
