const carouselimg = document.getElementById("carousel-img");

let carouselimage = [
    '/public/src/AdobeStock_517876305_Preview.jpeg',
    '/public/src/AdobeStock_380696746_Preview.jpeg'
];

let currentindex = 0;


function moveimg(){
    if (currentidex<2){
        currentindex += 1;
}
    else{currentidex=0};
    carouselimg.src = carouselimage[currentindex];
};

/*
setInterval (
    moveimg(),3000
);*/