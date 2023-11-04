//BURGER + MENU
const $BURGER = document.querySelector('.burger')

$BURGER.addEventListener('click', function(){
    document.querySelector('.main__menu').classList.toggle('main__menu_closed')
    for (let i = 0; i < this.children.length; i++) this.children[i].classList.toggle(`burger_active_b${i}`)
   
    })


//Клон продуктов
const $product = document.querySelectorAll('.product') 
const $review = document.querySelectorAll('.review') 
const $productList = document.querySelectorAll('.product__list')


function cloneBlock(params, num) {
    for (let i = 0; i < params.length; i++) {
        const e = params[i];
        for (let j = 0; j < num; j++) {
            const cloneProduct = e.cloneNode(true)
            e.parentElement.appendChild(cloneProduct)   
        }   
    }
}
cloneBlock($product, 5)
cloneBlock($review, 2)

//cloneBlock($productList, 16)




/*
//Цена без скидки
const $price = document.querySelectorAll('.price')
$price.forEach(e => {
    let a = + e.textContent.slice(0, -3)
    let b = +e.parentElement.parentElement.children[0].textContent.slice(0, -1)
    let price = (a/100) * b
    e.parentElement.textContent = price.toFixed(2)
    e.textContent = a
    
    
    console.dir(a);
   
});

*/


const $slider = document.querySelector('.slider');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');
const slides = Array.from($slider.querySelectorAll('img'));


let slideIndex = 0;

// Устанавливаем обработчики событий для кнопок
prevButton.addEventListener('click', showPreviousSlide);
nextButton.addEventListener('click', showNextSlide);

// Функция для показа предыдущего слайда
function showPreviousSlide() {
  slideIndex = (slideIndex - 1 + slides.length) % slides.length;
  updateSlider();
}


// Функция для показа следующего слайда
function showNextSlide() {
  slideIndex = (slideIndex + 1) % slides.length;
  updateSlider();
}

setInterval(() => {
    showNextSlide()
}, 5000);

// Функция для обновления отображения слайдера
function updateSlider() {
  slides.forEach((e, i) => {
    if (i === slideIndex) e.style.display = 'block'
    else e.style.display = 'none';
  });
}

// Инициализация слайдера
updateSlider();

//SLider effect
const $effect = document.querySelectorAll('.slider__button') 
console.log($effect);

$slider.addEventListener('mouseover', ()=>{
    $effect.forEach(e =>{
        e.classList.add('slider__button_opacity')
    })
    
})
$slider.addEventListener('mouseout', ()=>{
    $effect.forEach(e =>{
        e.classList.remove('slider__button_opacity')
    })
   
})