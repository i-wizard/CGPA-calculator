$("#acc").accordion({
    collapsible:true,
    event:"click",
    animate:300,
    active:1,
    heightStyle:true,
    icons:{header:"ui-icon-circle-arrow-s",activeHeader:"ui-icon-circle-close"}
})

$( "#tabs" ).tabs({
    // active: 1
})
$(".card").
   //mouse toggling
function old(){
    //document.getElementById("old").src="images/intro.png"
  tim=  document.getElementsByClass(".old");
  tim.style.opacity="0.7"
}
function newi(){
    document.getElementsByClass(".old").style.opacity="1"
    //document.getElementById("old").src="images/home_slider.jpg"
}