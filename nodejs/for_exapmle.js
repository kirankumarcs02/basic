for(let i = 0; i< 5; i++){
    setTimeout(()=> {
        console.log('I = ',i);
    },1000)
    console.log('I outside', i)
}

for(var i = 0; i< 5; i++){
    setTimeout(function () {
        console.log('function = ',i);
    },1000)
}

for(var i = 0; i< 5; i++){
    (function (index) {
        setTimeout(function () {
            console.log('closure = ',index);
        },1000)
    })(i)
    
}