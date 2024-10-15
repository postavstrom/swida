<template>
  <div class="container mt-3">
    <table class="table table-striped">
      <thead>
      <tr>
        <th scope="col" class="min-width-50">#</th>
        <th scope="col" class="min-width-150">Order Name</th>
        <th scope="col" class="min-width-150">Customer Name</th>
        <th scope="col" class="min-width-100">Date</th>
        <th scope="col" class="min-width-150">Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(order, index) in orders" :key="order.id">
        <th scope="row">{{ index + 1 }}</th>
        <td>{{ order.order_number }}</td>
        <td>{{ order.customer_name }}</td>
        <td>{{ order.date }}</td>
        <td>
          <button class="btn btn-secondary me-2" @click="editOrder(order.id)">Edit</button>
          <button class="btn btn-danger" @click="deleteOrder(order.id)">Delete</button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const orders = ref([]);
const apiUrl = import.meta.env.VITE_API_URL;


const fetchOrders = async () => {
  const response = await axios.get(`${apiUrl}/orders/`);
  orders.value = response.data;
};

const editOrder = (orderId) => {
  window.location.href = `/orders/${orderId}/edit/`;
};

const deleteOrder = async (orderId) => {
  const confirmDelete = confirm('Are you sure you want to delete this order?');
  if (confirmDelete) {
    try {
      await axios.delete(`${apiUrl}/orders/${orderId}/delete/`);
      fetchOrders();
      alert('Order deleted successfully.');
    } catch (error) {
      console.error('Error deleting order:', error);
      alert('There was an error deleting the order. Please try again.');
    }
  }
};

onMounted(fetchOrders);
</script>

<style scoped>
.min-width-50 {
  min-width: 50px;
}

.min-width-100 {
  min-width: 100px;
}

.min-width-150 {
  min-width: 150px;
}

.container {
  margin-bottom: 1rem;
}
</style>
