<template>
  <router-view />
</template>

<style>
body {
  margin: 0;
}
@media screen and (min-width: 1201px) {
  ::-webkit-scrollbar-thumb {
    /* Укажи цвет скроллбара */
    background: #7d33ff;
    /* Укажи радиус скругления скроллбара */
    border-radius: 10px;
  }
  ::-webkit-scrollbar {
    /* Укажи ширину вертикального скроллбара */
    width: 0px;
    /* Укажи высоту горизонтального скроллбара */
    height: 5px;
    /* Укажи цвет фона под скроллбаром */
    background: black;
  }
}
</style>
