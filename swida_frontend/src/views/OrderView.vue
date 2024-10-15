<template>
  <OrderForm :isEditMode="isEditMode" :orderId="Number(orderId)" />
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import OrderForm from '../components/OrderForm.vue';

const route = useRoute();
const isEditMode = computed(() => route.params.id !== undefined);
const orderId = computed(() => route.params.id);
</script>
