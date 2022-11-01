// var floor = Math.floor(1.8);
// //floor rounds down to the lower integer
// var ceil = Math.ceil(3.7);
// //ceil rounds up to the higher integer
// var random = Math.random();
// //generates random number between 0 (inclusive) and 1 (exclusive)
// console.log(random);

// function d6() {
//     var roll = Math.ceil(Math.random() * 6);
    
//     return roll;
// }
    
// var playerRoll = d6();
// console.log("The player rolled: " + playerRoll);

function magicEightBall(){
var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];

var index;
index = Math.floor(Math.random()*lifesAnswers.length);
return lifesAnswers[index];
}

console.log(magicEightBall());