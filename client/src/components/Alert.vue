<template>
  <b-alert
    :show="dismissSecs"
    variant="success"
    fade>
    {{message}}
</b-alert>
</template>

<script>
export default {
  props: ['message', 'dismissSecs'],
};
</script>
