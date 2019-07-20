var test = function() {

     return function(){
         console.log(this.a);
     }
}
console.log(test()())