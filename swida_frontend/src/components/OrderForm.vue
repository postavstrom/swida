<template>
  <form class="container text-center" @submit.prevent="submitOrder">
    <div class="row mb-3">
      <h2 v-if="isEditMode">Edit Order</h2>
      <h2 v-else>Create Order</h2>
      <div class="col">
        <input v-model="order.order_number" type="text" class="form-control min-width-input" placeholder="Order number" required />
      </div>
      <div class="col">
        <input v-model="order.customer_name" type="text" class="form-control min-width-input" placeholder="Customer Name" required />
      </div>
      <div class="col">
        <input v-model="order.date" type="date" class="form-control min-width-input" required />
      </div>
    </div>
    <div class="row mb-3">
      <waypoint-form v-if="waypoints.length" v-for="(waypoint, index) in waypoints" :key="index" :waypoint="waypoint" :removeWaypoint="() => removeWaypoint(index)" />
    </div>
    <div class="row">
      <div class="col mb-2">
        <button class="btn btn-secondary w-100" @click="addWaypoint">Add Waypoint</button>
      </div>
      <div class="col">
        <button class="btn btn-primary w-100" type="submit">{{ isEditMode ? 'Update Order' : 'Create Order' }}</button>
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import WaypointForm from './WaypointForm.vue';

const apiUrl = import.meta.env.VITE_API_URL;
const props = defineProps({
  isEditMode: {
    type: Boolean,
    default: false
  },
  orderId: {
    type: Number,
    required: false
  }
});

const order = ref({
  order_number: '',
  customer_name: '',
  date: '',
});

const waypoints = ref([]);

const submitOrder = () => {  const url = props.isEditMode
    ? `${apiUrl}/orders/${props.orderId}/edit/`
    : `${apiUrl}/orders/create/`;

  const method = props.isEditMode ? 'put' : 'post';


  axios[method](url, order.value)
    .then(response => {
      console.log('resp', response.data);

      const orderId = response.data.id || props.orderId;

      if (!orderId) {
        throw new Error('Order ID is undefined. Check the API response.');
      }

      const waypointPromises = waypoints.value.map(waypoint => {
        return axios.post(`${apiUrl}/orders/${orderId}/waypoints/`, waypoint);
      });

      return Promise.all(waypointPromises);
    })
    .then(() => {
      console.log('Order and waypoints created/updated successfully.');
    })
    .catch(error => {
      console.error('Error creating/updating order:', error);
      alert('There was an error creating/updating the order. Please try again.');
    });
};

const addWaypoint = () => {
  waypoints.value.push({
    location_name: '',
    waypoint_type: 'pickup',
  });
};

const removeWaypoint = (index) => {
  waypoints.value.splice(index, 1);
};

if (props.isEditMode && props.orderId) {
  onMounted(() => {
    axios.get(`${apiUrl}/orders/${props.orderId}/`)
      .then(response => {
        order.value = {
          order_number: response.data.order_number || '',
          customer_name: response.data.customer_name || '',
          date: response.data.date || ''
        };

        if (response.data.waypoints && response.data.waypoints.length) {
          waypoints.value = response.data.waypoints;
        } else {
          waypoints.value = [];
        }
      })
      .catch(error => {
        console.error('Error fetching order:', error);
        alert('There was an error fetching the order. Please try again.');
      });
  });
}
</script>

<style scoped>
.min-width-input {
  min-width: 200px;
}
</style>
