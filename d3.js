//boolean -> true false
//var isSunny =true
//var temp = 55;
//var isRaining = false;
//var whatToBring = "I should bring: ";

//if(isSunny){
// whatToBring += "sunglasses, ";
//}

//if(temp < 50){
// whatToBring += "a light jacket, "
//}

//if(isRaining){
//whatToBring += "an umbrella, ";
//}

//whatToBring += "and a smile!";

//console.log(whatToBring);

//downcount
//loop goes from 10 to 0
//for (var i = 10; i>0; i--){
// if(i !== 2) {
//    console.log(i)
// }
// else{
//  console.log("ignition!")
//}
//}

//console.log("liftoff!")

var countPositives = 0;
var numbers = [6, 2, -9, 1, -4, 0, 100, 83, 8];
for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] > 0) {
        countPositives++;
    }
}

console.log("There are " + countPositives + " positives in the array");