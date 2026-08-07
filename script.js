console.log(typeof NaN); // number
console.log(typeof null); // object ,because in js objects are represented as 000 and null as 00000.. so js consider null as object
console.log([] == false); // true , [].toString() -> "" -> 0 then 0 == 0 
console.log([] === false); //false,  strict equality  checks array(object) is not equal to boolean

console.log('5' - 2); //3 , The - operator only performs numeric subtraction so '5' -> 5
console.log('5' + 2); // 52 , If either operand is a string, JavaScript converts the other operand to a string and concatenates them.
console.log('5' + '5'); //55 simple concatenation

console.log([] + []);// "" i.e, empty string ,. [].toString(); "" + ""

console.log([] + {});  // [object Object] because "" + [object Object]

console.log({} + {});//[object Object][object Object]

console.log(true + true);   //2    When the + operator is used with booleans, JavaScript converts them to numbers. true - 1 and false - 0
console.log(true + false); //1

console.log('2' > '12');   //true lexicographic comparison

// foo();

// var foo = function () {
//     console.log("Hello");
// }

// for (var i = 0; i < 3; i++) {
//     setTimeout(() => console.log(i), 100);     // 3 3 3 it doesnt run it at last i becomes 3 then all settimeout will run together from
// }                                              //callback queue to call stack


// for (let i = 0; i < 3; i++) {
//     setTimeout(() => console.log(i), 100);
// }

console.log(0.1 + 0.2 == 0.3);          //because in js 0.1 + 0.2 == 0.300000000004

console.log(NaN == NaN); //false NaN is not equal to anything
console.log(NaN === NaN); //false same as above
console.log(typeof undefined);  //undefined

console.log(1 < 2 < 3); // true goes from left to right 1 < 2 -> true now true < 3 means 1 < 3 true
console.log(3 > 2 > 1);// false  3 > 2 -> true now true > 1 means 1 > 1 it gives false

