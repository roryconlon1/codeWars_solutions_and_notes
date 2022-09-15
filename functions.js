// function disemvowel(str) {
//     return str.replace(/[aeiou]/gi, '')
//   }

// module.exports = disemvowel;

// function squareDigits(num) {
//     return Number(('' + num).split('').map(function (val) { return val * val; }).join(''));
// }


// module.exports = squareDigits

// function areYouPlayingBanjo(name) {
//     newName = name.toLowerCase()
//     if (newName.startsWith('r')) { return `${name} plays banjo` };
//     return `${name} does not play banjo`;
// }
// console.log(areYouPlayingBanjo('Gory'));

// function lovefunc(flower1, flower2) {
//     valueOfFlower1 = (flower1 % 2 == 0)
//     valueOfFlower2 = (flower2 % 2 == 0)
//     if (valueOfFlower1 != valueOfFlower2) { return true }
//     return false
// }


// function opposite(number) {
//     return number * -1
// }
// console.log(opposite(-4.25));

// function simpleMultiplication(number) {
//     if (number %2 ==0 ){return number * 8}
//     return number * 9
// }
// console.log(simpleMultiplication(2));

function solution(str) {
    return (str+"_").match(/../g)||[]

    // will only work for 2 places, same with .{2}, however {1,2} will work fro minimum of one and max 2.
    //g is global, can add i for upper and lower case.  || [] gives an empty array if an empty string rather than returning null
    //so _ is added every time and will only be added on if it is odd, as it needs 2 elements so will be omitted if even.
    
    //function solution(str) {
//     if (str.length == 0) {
//         return []
//     };

//     return (str.length % 2 == 0? str: str + '_' ).match(/../gi);
// }

//same thing, setting if 0 to an empty string.
//checking if its even, if so saying str calling match function to 2 places
//otherwise calling string + _ and calling same function which will add _ after last 
//character of string and work correctly.
}

console.log(solution('hellos'));

