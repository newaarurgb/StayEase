const images = [
    "/static/images/hotel1.jpg",
    "/static/images/hotel2.jpg",
    "/static/images/hotel3.jpg",
    "/static/images/hotel4.jpg",
    "/static/images/hotel5.jpg"
];

let current = 0;

const hero = document.querySelector(".hero");

function showImage(){

    hero.style.backgroundImage =
        `url('${images[current]}')`;

}

function nextImage(){

    current++;

    if(current >= images.length){

        current = 0;

    }

    showImage();

}

function prevImage(){

    current--;

    if(current < 0){

        current = images.length-1;

    }

    showImage();

}

// Auto change every 5 seconds
setInterval(nextImage,5000);

// Click anywhere on hero to go next
hero.addEventListener("click",function(e){

    if(!e.target.closest(".hero-arrow")){

        nextImage();

    }

});