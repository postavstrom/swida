<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="d-flex flex-column">
    <nav class="navbar bg-body-tertiary fixed-top">
      <div class="container-fluid">
        <div class="d-flex">
          <RouterLink class="navbar-brand" to="/">Home</RouterLink>
          <RouterLink class="navbar-brand" to="/orders/create">Create Order</RouterLink>
          <RouterLink class="navbar-brand" to="/orders">Orders</RouterLink>
        </div>
      </div>
    </nav>
    <div style="padding-top: 60px;">
      <RouterView />
    </div>
  </div>
</template>
