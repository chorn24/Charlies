"use strict";
const slides = document.querySelectorAll(".slide");


slides.forEach((slide, indx) => {
  slide.style.transform = `translateX(${indx * 100}%)`;
});


const nextSlide = document.querySelector(".btn-next");


let CurrentSlide = 0;
let MaximumSlide = slides.length - 1;


nextSlide.addEventListener("click", function () {
  if (CurrentSlide === MaximumSlide) {
    CurrentSlide = 0;
  } else {
    CurrentSlide++;
  }
  slides.forEach((slide, indx) => {
    slide.style.transform = `translateX(${100 * (indx - CurrentSlide)}%)`;
  });
});


const prevSlide = document.querySelector(".btn-prev");


prevSlide.addEventListener("click", function () {
  if (CurrentSlide === 0) {
    CurrentSlide = MaximumSlide;
  } else {
    CurrentSlide--;
  }
  slides.forEach((slide, indx) => {
    slide.style.transform = `translateX(${100 * (indx - CurrentSlide)}%)`;
  });
});