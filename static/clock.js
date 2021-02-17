const htmlClock = document.getElementById('clock')
const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

function makeClock(){
    const date = new Date();

    const year = date.getFullYear();
    const monthText = monthNames[date.getMonth()];
    const day = date.getDate();
    const hours = date.getHours();

    htmlClock.innerHTML = `${monthText} ${day}th, ${year}`;
    console.log(htmlClock.innerHTML)    
}

function init(){
    makeClock()
}
init();