const profitText = document.querySelectorAll('.status__profit');
const profitPlus = document.querySelector('.status__plus'),
        plusText = profitPlus.querySelector('.status__profit');
const profitMinus = document.querySelector('.status__minus'),
        minusText = profitMinus.querySelector('.status__profit');

profitText.forEach(e => {
    const parsedProfit = Number(e.innerText);
    if(parsedProfit < 0){
        plusText.innerHTML = '';
    }
    if(parsedProfit > 0){
        minusText.innerHTML = '';
    }
});
