import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const useWaypointStore = defineStore('waypoints', () => {
  const waypoints = ref([]);

  const fetchWaypoints = async (orderId) => {
    const response = await axios.get(`${apiUrl}/orders/${orderId}/waypoints/`);
    waypoints.value = response.data;
  };

  const addWaypoint = async (orderId, waypoint) => {
    await axios.post(`${apiUrl}/orders/${orderId}/waypoints/`, waypoint);
    await fetchWaypoints(orderId);
  };

  return { waypoints, fetchWaypoints, addWaypoint };
});
