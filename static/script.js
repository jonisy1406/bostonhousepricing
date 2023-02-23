const inputs = document.querySelectorAll('input');

inputs.forEach(function(input){
    let isClicked = false;

    input.addEventListener('click', function(){
        if (isClicked) {
            this.value = '';
            isClicked = false;
        } else {
            isClicked = true;
        }
    });
});