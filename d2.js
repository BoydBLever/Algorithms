var isSunny = true;
// var temp = 55;
// var isRaining = false;
// var whatToBring = "I should bring: ";

// if(isSunny){
//     whatToBring += "sunglasses, ";
// }

// if(temp < 60){
//     whatToBring += "a light jacket, ";
// }

// if(isRaining){
//     whatToBring += "an umbrella, "
// }

// whatToBring += "and a smile!";

// console.log(whatToBring);

// for(var i = 0; i<11; i++){
//     console.log(i);
// }

// for(var i = 10; i>=0; i--){
//     if(i !== 2){
//         console.log(i);
//     }
//     else{
//         console.log("Ignition!");
//     }
// }

// console.log("Liftoff!");

var countPositives = 0;
var numbers = [6, 2, -9, 1, -4, 0, 100,-83, 6, 2, 12];

for (var i = 0; i < numbers.length; i++){
    if (numbers[i] > 0){
        countPositives++;
    }
}

console.log("There are " + countPositives + " positive number(s) in the array");