const carouselimg = document.getElementById("carousel-img");

let carouselimage = [
    '/public/src/AdobeStock_517876305_Preview.jpeg',
    '/public/src/AdobeStock_380696746_Preview.jpeg',
    '/public/src/1000_F_548477704_fYSpo7TRTtKlIq9C2QZ0KczwJWSSMJgl.jpg',
    '/public/src/1000_F_1055339745_yReUufviE4zl4Vtr4thcgzkbeqMWOZkq.jpg',
];



let currentindex = 0;
let anim = 0;

function moveimg(){
    
    if (currentindex<carouselimage.length-1){
        currentindex += 1;
        anim  += 1;
}
    else{currentindex=0};
    carouselimg.src = carouselimage[currentindex];
};


setInterval (
    moveimg,3000
);
