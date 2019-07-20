console.log("1");
setTimeout(function () {
    console.log('2');
},0)
console.log('3')
console.log('4')

function count(){
    var n = 0;
    return{
        count: function() {
            return n++;
        },
        reset: function(){
            n=0;
        }
    }
}

var c = count();
var d = count();

console.log(c.count());
console.log(d.count());
console.log(c.reset());
console.log(c.count());
console.log('D',d.count());
console.log(this)
let array = [1,2,3];
let arr = new Array()

console.log('prototype',Object.getOwnPropertyNames(array))

console.log('prototype',Object.getPrototypeOf(arr))