//Mon Nov 28 2022
class UtilClass {
    totalCount(numArr) {
        let sum = 0;
        for (let i = 0; i < numArr.length; i++) {
            sum += numArr[i]
        }
        return sum
    }

    printMessages(msgArr) {
        for (let i = 0; i < msgArr.length; i++) {
            console.log(msgArr[i])
        }
    }
}

var messagesPerDay = [5, 8, 6]
var messages = ["Please call back!", "Make sure you install jdk", "DO NOT INSTALL VS CODE EXTENSION!"]

var newBot = new UtilClass()

console.log(newBot.totalCount(messagesPerDay));
newBot.printMessages(messages);
  //node warmup.js