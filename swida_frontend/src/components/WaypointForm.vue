<template>
  <div class="container text-center mb-3">
    <div class="row">
      <div class="col">
        <input
          v-model="waypoint.location_name"
          type="text"
          class="form-control min-width-input"
          placeholder="Location Name"
          required
        />
      </div>
      <div class="col">
        <select
          v-model="waypoint.waypoint_type"
          class="form-select min-width-input"
          required
        >
          <option value="pickup">Pickup</option>
          <option value="delivery">Delivery</option>
        </select>
      </div>
      <div class="col">
        <button class="btn btn-secondary w-100" @click="removeWaypoint">Remove Waypoint</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  waypoint: Object,
  removeWaypoint: Function,
});
</script>

<style scoped>
.min-width-input {
  min-width: 200px;
}
</style>
